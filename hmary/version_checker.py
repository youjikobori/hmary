import requests
import webbrowser
import tomllib  # Python 3.11+

def check_version():
    # pyproject.toml
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
        current = data["project"]["version"]
    
    print(f" Welcome!\n Current version of the project: {current}")
    
    # GitHub-Api Checker
    try:
        r = requests.get("https://api.github.com/repos/youjikobori/hmary/releases/latest", timeout=5)
        if r.status_code == 200:
            latest = r.json()["tag_name"]
            if latest != current:
                print(f" Update to version {latest} is available.")
                if input(" Would you like to update? (Y/n): ").lower() == 'y':
                    webbrowser.open(r.json()["html_url"])
            else:
                input(" You have the latest version of the program\n\n Press [ENTER] to continue")
        else:
            input(" Unable to check for updates\n\n Press [ENTER] to continue")
    except:
        input(" Unable to check for updates\n\n Press [ENTER] to continue")
