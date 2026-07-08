from HistoryFunctions.output import open_history_json

from pathlib import Path

import sys










def launcherHistory():
    
    try:
        if getattr(sys, "frozen", False):
            app_folder = Path(sys.executable).resolve().parents[1]
            json_path = app_folder / "HistoryLogs"

        else:
            app_folder = Path(__file__).resolve().parents[1]
            json_path = app_folder / "HistoryLogs"

        while True:
        
            year_folders = sorted(json_path.iterdir(), key=lambda x: x.name)

            indexed = {}

            relative_display = json_path.resolve().relative_to(app_folder.resolve())
            print(f"====== {relative_display} ======\n")

            for index, folder in enumerate(year_folders, start=1):

                indexed[str(index)] = folder
                
                if folder.is_dir():
                    print(f"{index}. {folder.name}")

                else:
                    print(f"{index}. {folder.stem}")

            number = input("\nEnter the number of the year (Press Enter to return): ")

            if number == "":
                if json_path.name == "HistoryLogs":
                    raise Exception

                json_path = json_path.parent
                print("\033[H\033[J", end="")
                continue
            
            selected = indexed.get(number)

            if not selected:
                print("\033[H\033[J", end="")
                continue

            if selected.is_dir():
                print("\033[H\033[J", end="")
                json_path = selected
                continue

            else:
                print("\033[H\033[J", end="")
                exc = open_history_json(relative_display, selected)
                
                if exc:
                    raise Exception
                elif not exc:
                    print("\033[H\033[J", end="")
                    continue
                
            return selected, False

    except Exception:
        if not json_path.exists():
            print("\033[H\033[J", end="")
            print("No history found.")

            input("\nPress Enter to return...")
            return
        
        print("\033[H\033[J", end="")

        return