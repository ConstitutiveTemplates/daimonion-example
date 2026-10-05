import subprocess
import sys

from daimonion_example import __version__


def test_cli_version() -> None:
    cmd = [sys.executable, "-m", "daimonion_example", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
