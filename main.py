import requests
import os
from dotenv import load_dotenv


def get_screenshots(api_key, best_game):
    screenshots_url = f"https://api.rawg.io/api/games/{best_game['slug']}/screenshots"
    params = {
        "key": api_key
    }
    response = requests.get(screenshots_url, params=params)
    response.raise_for_status()
    screenshots = response.json()["results"]
    return screenshots


def get_stores(api_key, best_game):
    stores_url = f"https://api.rawg.io/api/games/{best_game['slug']}/stores"
    params = {
        "key": api_key
    }
    response = requests.get(stores_url, params=params)
    response.raise_for_status()
    stores = response.json()["results"]
    return stores


def get_best_games(api_key):
    games_url = f"https://api.rawg.io/api/games"
    pages_amount = 1
    page_size = 10
    params = {
        "key": api_key,
        "page": pages_amount,
        "page_size": page_size,
        "genres": "strategy",
        "metacritic": "70,100",
        "tags": "multiplayer"
    }
    response = requests.get(games_url, params=params)
    response.raise_for_status()
    response_results = response.json()["results"]

    for best_game in response_results:
        print(f"""    
Название: {best_game["name"]}
Дата: {best_game["released"]}
Ссылка: https://rawg.io/games/{best_game["slug"]}""")

        screenshots = get_screenshots(api_key, best_game)
        print("Скринщоты: ")
        for screenshot in screenshots:
            print(screenshot["image"])

        stores = get_stores(api_key, best_game)
        print("Магазины для покупки:")
        for store in stores:
            print(store["url"])


def main():
    load_dotenv()
    api_key = os.getenv("api_key")
    get_best_games(api_key)


if __name__=="__main__":
    main()
