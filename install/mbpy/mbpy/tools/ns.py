import argparse
import json
import os
from typing import Optional
from mbcore.display import safe_print
from mbcore.even._internal._cache_impl import render_table
import rich_click as click
import httpx
from mbpy.cli import base_args, get_help_config
from mbcore.config import config
from dataclasses import dataclass, asdict


class Secret(str):
    """A secret string that can be used to store sensitive information."""

    def __str__(self):
        return self[:4] + "*" * (len(self) - 8) + self[-4:]


@dataclass
class UserCreate:
    """Request model matching backend UserCreate"""

    email: str
    password: str
    user_name: str | None = None
    first_name: str | None = None
    last_name: str | None = None


@dataclass
class UserProfileResponse:
    """Response model matching backend UserProfileResponse"""

    email: str
    user_name: str
    first_name: str | None = None
    last_name: str | None = None
    raw_key: str | None = None


async def signup_user(
    email: str,
    password: str,
    user_name: str | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    base_url: str = "https://api.mbodi.ai/test",
) -> UserProfileResponse | None:
    """
    Sign up a new user to mbodi.ai

    Args:
        email: User's email address
        password: User's password
        user_name: Optional username (defaults to email prefix if not provided)
        first_name: Optional first name
        last_name: Optional last name
        base_url: Base URL of the API

    Returns:
        UserProfileResponse if successful, None if failed
    """
    async with httpx.AsyncClient() as client:
        try:
            # Create signup data
            signup_data = UserCreate(
                email=email,
                password=password,
                user_name=user_name or email.split("@")[0],
                first_name=first_name,
                last_name=last_name,
            )

            # Make the request
            response = await client.put(
                f"{base_url}/auth/add_user",
                json=asdict(signup_data),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()

            # Parse the response
            data = response.json()
            user_response = UserProfileResponse(**data)

            return user_response

        except httpx.HTTPStatusError as e:
            print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None


def save_credentials(response: UserProfileResponse, output_file: str):
    """Save credentials to a file."""
    with open(output_file, "w") as f:
        json.dump(
            {
                "user_name": response.user_name,
                "email": response.email,
                "api_key": response.raw_key,
            },
            f,
            indent=2,
        )
    print(f"Credentials saved to {output_file}")


def get_git_credentials():
    """Get email from git config."""
    from mbpy.cmd import run

    email = run(["git", "config", "user.email"], show=False).strip()
    if "test@example.com" in email:
        return ""
    return


def get_git_token():
    """Get token from git config."""
    from mbpy.cmd import run

    return os.getenv("GIT_TOKEN", os.getenv("GITHUB_TOKEN"))


_token = get_git_token()
if _token:
    display_token = _token[:4] + str(Secret(_token[4:-4])) + _token[-4:]
else:
    display_token = None


@click.command("login")
@click.option(
    "--email",
    help="Email address",
    prompt="Enter an email",
    default=get_git_credentials(),
)
@click.password_option(
    "--password",
    help="Password",
    prompt="Enter a password",
    default=display_token,
    confirmation_prompt=False,
)
@click.option("--username", help="Username (optional)")
@click.option("--firstname", help="First name (optional)")
@click.option("--lastname", help="Last name (optional)")
@click.option(
    "--output",
    default="mbodi_credentials.json",
    help="Output file for credentials (default: mbodi_credentials.json)",
)
@click.option("--url", default="https://api.mbodi.ai/test", help="Base URL of the API")
@click.rich_config(get_help_config())
async def main(
    email: str,
    password: str,
    username: str | None,
    firstname: str | None,
    lastname: str | None,
    output: str,
    url: str,
    **kwargs,
):
    """Sign up to mbodi.ai and get API key"""
    response = await signup_user(
        email=email,
        password=password,
        user_name=username,
        first_name=firstname,
        last_name=lastname,
        base_url=url,
    )

    if response:
        render_table(response)
    else:
        safe_print("Signup failed!")
        exit(1)


@click.command("whoami")
@click.rich_config(get_help_config())
async def whoami_command():
    """Sign up to mbodi.ai and get API key"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{config.get('base_url')}/auth/whoami")
        if response.status_code == 401:
            safe_print("Unauthorized")
            safe_print(f"Please run `mb login` to sign up or recieve an API key")
        else:
            print(response.json())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
