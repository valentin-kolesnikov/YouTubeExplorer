import sys
from datetime import datetime
from json import dump
from pathlib import Path


class HistorySessions:
    def __init__(self, tool):

        self.tool = tool

        now = datetime.now().astimezone()

        self.timestamp = now.strftime("%H-%M-%S")

        self.created_at = now.strftime("%Y-%m-%d %H:%M:%S")

        if getattr(sys, "frozen", False):
            app_folder = Path(sys.executable).resolve().parents[1]
        else:
            app_folder = Path(__file__).resolve().parents[1]

        self.folder = Path(app_folder, "HistoryLogs",
                            now.strftime("%Y"),
                            now.strftime("%m"),
                            now.strftime("%d"))
        
        self.folder.mkdir(parents=True, exist_ok=True)

        self.file = f"{self.timestamp}_{tool}.json"

        self.path = self.folder / self.file

        self.data = {
            "time": self.now(),
            "tool": tool,
            "sessions": []
        }
    
    def now(self):
        now = datetime.now().astimezone()
        set = now.strftime("%z")
        return now.strftime("%H:%M:%S") + f" (UTC{set[:3]}:{set[3:]})"

    def add_session(self, action, **data):

        self.data["sessions"].append({
            "time_action": self.now(),
            "action": action,
            "data": data
        })
        
    def save(self):
        with open(self.path, "w", encoding="utf-8") as files:
            dump(self.data, files, ensure_ascii=False, indent=4)