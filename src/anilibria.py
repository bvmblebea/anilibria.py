# Library made by DeLuvSushi
# P.S I didn't tested many functions!
import requests
import random
import string
import json

class Client():
    def __init__(self):
        self.api = "https://api.anilibria.tv"
        self.api_v2 = "https://www.anilibria.tv/public"
        self.session = None
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"}

    def generate_captcha(self):
        value = "".join(
            random.choices(
                string.ascii_uppercase +
                string.ascii_lowercase +
                "_-",
                k=462)).replace(
            "--",
            "-")
        return value

    def auth(self, email: str, password: str, csrf: int = 1):
        data = {"csrf": csrf, "mail": email, "passwd": password}
        request = requests.post(f"{self.api_v2}/login.php", data=data)
        json = request.json()
        self.headers = request.headers
        self.session = request.headers["set-cookie"]
        if json.get("code") == 200:
            try:
                self.session = self.session[0: self.session.index(";")]
            except Exception as e:
                print(e)
        else:
            print(f"Authorization in {email} was sucessful!")
        return request.json()

    def logout(self):
        request = requests.get(f"{self.api_v2}/logout.php")
        return request.json()

    def register(self, login: str, email: str, password: str):
        data = {
            "g-recaptcha-response": self.generate_captcha(),
            "login": login,
            "mail": email,
            "passwd": password}
        request = requests.post(
            f"{self.api_v2}/registration.php",
            data=data,
            headers=self.headers)
        return request.json()

    def search_anime(self, search: str, small: int = 1):
        data = {"search": search, "small": small}
        request = requests.post(
            f"{self.api_v2}/search.php",
            data=data,
            headers=self.headers)
        return request.json()

    def report_a_error(self, message: str, url: str):
        data = {
            "mes": message,
            "url": url,
            "g-recaptcha-response": self.generate_captcha(),
            "recaptcha": 2}
        request = requests.post(
            f"{self.api_v2}/error.php",
            data=data,
            headers=self.headers)
        return request.json()

    def favorite_anime_list(
            self,
            year: int = None,
            genre: str = None,
            season: str = None,
            page: int = 1,
            sort: int = 2,
            finish: int = 1,
            xpage: str = "favorites"):
        data = {"page": page,
                "search": {"year": year, "genre": genre, "season": season},
                "xpage": xpage,
                "sort": sort,
                "finish": finish
                }
        request = requests.post(
            f"{self.api_v2}/catalog.php",
            data=data,
            headers=self.headers)
        return request.json()

    def catalog(
            self,
            year: int = None,
            genre: str = None,
            season: str = None,
            page: int = 1,
            sort: int = 2,
            finish: int = 2,
            xpage: str = "catalog"):
        data = {"page": page,
                "search": {"year": year, "genre": genre, "season": season},
                "xpage": xpage,
                "sort": sort,
                "finish": finish
                }
        request = requests.post(
            f"{self.api_v2}/catalog.php",
            data=data,
            headers=self.headers)
        return request.json()

    def random_anime(self):
        data = {"js": 1}
        request = requests.post(
            f"{self.api_v2}/random.php",
            data=data,
            headers=self.headers)
        return request.json()

    def get_title(self, code: str):
        request = requests.get(f"{self.api}/v2/getTitle?code={code}")
        return request.json()

    def get_updates(self, filter: str, limit: int = 5):
        request = requests.get(
            f"{self.api}/v2/getUpdates?filter={filter},type,status&limit={limit}")
        return request.json()

    def get_changes(self, filter: str, limit: int = 5):
        request = requests.get(
            f"{self.api}/v2/getChanges?filter={filter},type,status&limit={limit}")
        return request.json()

    def get_schedule(self, days: int):
        request = requests.get(f"{self.api}/v2/getSchedule?days={days}")
        return request.json()

    def get_caching_nodes(self):
        request = requests.get(f"{self.api}/v2/getCachingNodes")
        return request.json()

    def get_random_title(self):
        request = requests.get(f"{self.api}/v2/getRandomTitle")
        return request.json()

    def get_youtube_videos(self, limit: int = 10):
        request = requests.get(f"{self.api}/v2/getYouTube?limit={limit}")
        return request.json()

    def get_feed(self, limit: int = 10):
        request = requests.get(f"{self.api}/v2/getFeed?limit={limit}")
        return request.json()

    def get_years(self):
        request = requests.get(f"{self.api}/v2/getYears")
        return request.json()

    def get_genres(self, sorting_type: int = 0):
        request = requests.get(
            f"{self.api}/v2/getGenres?sorting_type={sorting_type}")
        return request.json()

    def search_titles(self, search: str, limit: int = 10):
        request = requests.get(
            f"{self.api}/v2/searchTitles?search={search}&limit={limit}")
        return request.json()

    def get_team(self):
        request = requests.get(f"{self.api}/v2/getTeam")
        return request.json()

    def get_seed_stats(self, users: str = None, limit: int = 10):
        get_seed_stats_link = f"{self.api}/v2/getSeedStats?limit={limit}"
        if users:
            get_seed_stats_link = f"{self.api}/v2/getSeedStats?users={users}"
        request = requests.get(get_seed_stats_link)
        return request.json()

    def get_rss(self, rss_type: str, limit: int = 5):
        request = requests.get(
            f"{self.api}/v2/getRSS?rss_type={rss_type}&limit={limit}")
        return request.json()

    def get_favorite_titles(self, session: str):
        request = requests.get(f"{self.api}/v2/getFavorites?session={session}")
        return request.json()

    def add_title_to_favorites(self, session: str, title_Id: int):
        request = requests.put(
            f"{self.api}/v2/addFavorite?session={session}&title_id={title_Id}")
        return request.json()

    def delete_title_from_favorites(self, session: str, title_Id: int):
        request = requests.delete(
            f"{self.api}/v2/delFavorite?session={session}&title_id={title_Id}")
        return request.json()
