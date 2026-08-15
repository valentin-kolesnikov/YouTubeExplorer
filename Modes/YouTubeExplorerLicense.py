import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    dir = Path(sys.executable).resolve().parents[1]
else:
    dir = Path(__file__).resolve().parents[1]


def launcherLICENSE():
    license = Path(dir, "LICENSE")

    if license.is_file():
        with open(license, "r", encoding="utf-8") as f:
            license_text = f.read()

    else:
        input("The LICENSE file was not found.\n" \
        "This software is distributed under GNU GPL-3.0\n" \
        "Original project repository: https://github.com/valentin-kolesnikov/YouTube_Explorer\n\n" \
        "Original project: YouTube Explorer by Valentin Kolesnikov\n\n" \
        "Press Enter to return...")

        return

    print("\033[H\033[J", end="")

    print(license_text)

    input("\nPress Enter to return...")




def launcherABOUT():
    about = Path(dir, "ABOUT")

    if about.is_file():
        with open(about, "r", encoding="utf-8") as f:
            about_text = f.read()

    else:
        input("The ABOUT file was not found.\n" \
        "This software is distributed under GNU GPL-3.0\n" \
        "Original project repository: https://github.com/valentin-kolesnikov/YouTube_Explorer\n\n" \
        "Original project: YouTube Explorer by Valentin Kolesnikov\n\n" \
        "Press Enter to return...")

        return
    
    print("\033[H\033[J", end="")

    print(about_text)

    input("\nPress Enter to return...")