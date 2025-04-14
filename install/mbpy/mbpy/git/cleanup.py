import asyncio
from check import quick_merge, arun


async def main():
    # First ensure we're on main
    await arun(["git", "checkout", "main"])

    tmp_branch = "None-tmp-20250218051452"
    await quick_merge(tmp_branch)


if __name__ == "__main__":
    asyncio.run(main())
