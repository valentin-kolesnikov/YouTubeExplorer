import os
import subprocess

def log(history, action, **data):
    history.add_session(action, **data)
    history.save()


def log_error(history, reason, error):
    history.add_session("ERROR", reason=reason, error=str(error))
    history.save()

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)