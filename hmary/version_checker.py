import requests
import webbrowser
import tomllib  # для Python 3.11+

def check_version():
    # Текущая версия из pyproject.toml
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
        current = data["project"]["version"]
    
    print(f"Добро пожаловать, версия текущего проекта: {current}")
    
    # Проверка GitHub
    try:
        r = requests.get("https://api.github.com/repos/VLRZZ/hmary/releases/latest", timeout=5)
        if r.status_code == 200:
            latest = r.json()["tag_name"]
            if latest != current:
                print(f"Доступно обновление на версию {latest}")
                if input("Хотите обновится (Y/n): ").lower() == 'y':
                    webbrowser.open(r.json()["html_url"])
            else:
                input("У вас самая последняя версия программы\nнажмите [ENTER] чтобы продолжить")
        else:
            input("Не удалось проверить обновления\nнажмите [ENTER] чтобы продолжить")
    except:
        input("Не удалось проверить обновления\nнажмите [ENTER] чтобы продолжить")