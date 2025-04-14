from click.testing import CliRunner

from mbcore.display import prompt_ask


def test_prompt_ask_with_table():
    # Test data for table display
    display_rows = [
        ["Package", "Version", "Status"],
        ["CairoSVG", "2.7.1", "Installed"],
        ["Pillow", "10.0.0", "Installed"],
        ["numpy", "1.24.0", "Installed"],
    ]

    runner = CliRunner()
    with runner.isolation():
        # Simulate user input '1' for the first option
        with runner.isolation(input="1\n"):
            result = prompt_ask(
                "Select a package to uninstall:",
                display_rows=display_rows,
                choices=["CairoSVG", "Pillow", "numpy"],
                enumerate=True,
            )
            assert result == 1, f"Expected result to be 1, got {result}"


if __name__ == "__main__":
    test_prompt_ask_with_table()
