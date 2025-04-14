TypeVar = str
Console = object

T = TypeVar("T")


def normalize(name: str) -> str:
    return (
        name.replace("/", ".")
        .replace("\\", ".")
        .replace("-", "_")
        .replace(" ", "_")
        .removesuffix(".py")
    )


async def main(
    path_or_module: "str| Path" = ".",
    dry_run: bool = False,
    console: "Console | None" = None,
) -> None:
    # Build dependency graph and adjacency list
    from importlib import import_module
    from inspect import getabsfile
    from itertools import chain, takewhile
    from pathlib import Path

    from mbcore.collect import equals, nonzero
    from mbcore.display import safe_print
    from mbcore.more import collapse, flatten, ilen, unique
    from mbcore.resolve import resolve_name as resolve

    from mbpy.pkg.graph import build_dependency_graph

    path = Path(path_or_module)
    if not path.exists():
        # Assume it's a module name
        try:
            path = Path(getabsfile(import_module(str(path_or_module)))).parent
        except ImportError:
            from mbcore.resolve import resolve_name as resolve

            path = resolve(
                getattr(
                    path_or_module,
                    "__name__",
                    normalize(getattr(path_or_module, "__name__", "")),
                )
            )
    gs = await build_dependency_graph([Path(str(path))])
    for g in gs:
        root = g.root
        if not root:
            raise ValueError("No root node found")
        broken = root.content.get("broken_imports", {})

        for broken_module, module_nodes in broken.copy().items():
            if broken_module in module_nodes and module_nodes[
                broken_module
            ].content.get("path"):
                safe_print(f"Removing {broken_module} from broken imports")
                del broken[broken_module]

        # Display broken imports with file paths
        remaining_broken = {
            k: ilen(takewhile(equals(k), collapse(broken.values())))
            for k in flatten(unique(chain(broken.values())))
        }
        if broken:
            safe_print("\n[bold red]Broken Imports:[/bold red]")
            for imp, file_paths in broken.items():
                if await walk_broken_options(imp, dry_run):
                    safe_print(
                        f"{', '.join(file_paths)} are no longer broken by {imp}.",
                        style="light_sea_green",
                    )
                    remaining_broken.update(
                        nonzero(
                            {
                                k: v - 1
                                for k, v in remaining_broken.items()
                                if k in file_paths
                            }
                            or {imp: 0}
                        ),
                    )


async def walk_broken_options(imp, dry_run) -> bool:
    from mbcore.display import safe_print

    from mbpy.cmd import AsyncSpawn
    from mbpy.git.check import GitContext

    try:
        modname = imp.split(".")[0] if len(imp.split(".")) > 1 else imp
        safe_print(f"\nModule: {modname}")
        from mbpy.cmd import arun
        from mbpy.pkg.dependency import PyPackageInfo as PackageInfo
        from mbpy.pkg.pypi import find_and_sort

        results: list[PackageInfo] = [
            x async for x in find_and_sort(modname, include="all", verbosity=2)
        ]
        github_urls = [
            result.get("github_url") for result in results if result.get("github_url")
        ]

        if not results:
            safe_print(f" - No results found for {modname}", style="red")
            return False
        result = results[0]
        if not result.get("releases"):
            safe_print(f" - No releases found for {modname}", style="red")

        for release in result.get("releases", []) or []:
            version = next(iter(release.keys()))
            if dry_run:
                safe_print(f" - Would install: {modname}=={version}")
                return True

            result = await arun(f"pip install {modname}=={version}", show=False)
            if "ERROR" in result:
                safe_print(
                    f" Failed to install {modname}=={version}. Trying next version down",
                    style="red",
                )
                continue
            safe_print(f" - Installed: {modname}=={version}!", style="light_sea_green")
            return True
        safe_print(" - Exhausted all versions.", style="red")
        for url in github_urls:
            async with GitContext():
                safe_print(f" - Found github url: {url}")
                async with AsyncSpawn(f"gh repo view {url}") as result:
                    await arun(f"gh repo clone {url}")
                    await arun(f"cd {url.split('/')[-1] if url else '.'}")
                    await arun("pip install -e .")
                    await arun("cd ..")
                    safe_print(
                        f" - Installed: {modname} from github to {url.split('/')[-1]}",
                        style="light_sea_green",
                    ) if url else safe_print(
                        f" - Installed: {modname} from github", style="light_sea_green"
                    )
                    return True

        safe_print("Exhausted all versions and no urls found.", style="red")
        return False
    except Exception as e:
        safe_print(f"Error processing {imp}: {str(e)}", style="red")
        return False


if __name__ == "__main__":
    import asyncio
    import sys
    from pathlib import Path

    sys.exit(all(asyncio.as_completed([main(f) for f in Path.cwd().rglob("*.py")])))
