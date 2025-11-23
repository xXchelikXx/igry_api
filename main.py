import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("api_key")


def get_best_games():
    games_url = f"https://api.rawg.io/api/games"

    params = {"key": api_key, "page": 1, "page_size": 10, "genres": "strategy", "metacritic": "70,100", "tags": "multiplayer"}
    response = requests.get(games_url, params=params)
    response.raise_for_status()

    response_results = response.json()["results"]

    for best_game in response_results:
        print(f"""    
Название: {best_game["name"]}
Дата: {best_game["released"]}
Ссылка: https://rawg.io/games/{best_game["slug"]}""")

        screenshots_url = f"https://api.rawg.io/api/games/{best_game['slug']}/screenshots"
        params = {"key": api_key}
        response = requests.get(screenshots_url, params=params)
        response.raise_for_status()
        screenshots = response.json()["results"]
        print("Скринщоты: ")
        for screenshot in screenshots:
            print(screenshot["image"])

        stores_url = f"https://api.rawg.io/api/games/{best_game['slug']}/stores"
        params = {"key": api_key}
        response = requests.get(stores_url, params=params)
        response.raise_for_status()
        stores = response.json()["results"]
        print("Магазины для покупки:")
        for store in stores:
            print(store["url"])


def main():
    get_best_games()


if __name__=="__main__":
    main()
