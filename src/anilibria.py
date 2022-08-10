import requests
from random import choices
from string import ascii_uppercase, ascii_lowercase

class Anilibria:
    def __init__(self):
        self.api = "https://api.anilibria.tv"
        self.api_v2 = "https://www.anilibria.tv/public"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }

    def generate_captcha(self):
        value = "".join(
            choices(
                ascii_uppercase +
                ascii_lowercase +
                "_-",
                k=462)).replace(
            "--",
            "-")
        return value

    def login(
            self,
            email: str,
            password: str,
            csrf: int = 1):
        data = {
            "csrf": csrf,
            "mail": email,
            "passwd": password
        }
        response = requests.post(
            f"{self.api_v2}/login.php",
            data=data,
            headers=self.headers)
        json = response.json()
        self.headers = response.headers
        self.session = self.headers["set-cookie"]
        if json.get("code") == 200:
            try:
                self.session = self.session[0: self.session.index(";")]
            except Exception as e:
                print(e)
        return json

    def register(self, login: str, email: str, password: str):
        data = {
            "g-recaptcha-response": self.generate_captcha(),
            "login": login,
            "mail": email,
            "passwd": password
        }
        return requests.post(
            f"{self.api_v2}/registration.php",
            data=data,
            headers=self.headers).json()

    def search_anime(self, search: str, small: int = 1):
        data = {
            "search": search,
            "small": small
        }
        return requests.post(
            f"{self.api_v2}/search.php",
            data=data,
            headers=self.headers).json()

    def report_a_error(self, message: str, url: str):
        data = {
            "mes": message,
            "url": url,
            "g-recaptcha-response": self.generate_captcha(),
            "recaptcha": 2
        }
        return requests.post(
            f"{self.api_v2}/error.php",
            data=data,
            headers=self.headers).json()

    def favorite_anime_list(
            self,
            year: int = None,
            genre: str = None,
            season: str = None,
            page: int = 1,
            sort: int = 2,
            finish: int = 1,
            xpage: str = "favorites"):
        data = {
            "page": page,
            "search": {
                 "year": year,
                 "genre": genre,
                 "season": season
            },
            "xpage": xpage,
            "sort": sort,
            "finish": finish
        }
        return requests.post(
            f"{self.api_v2}/catalog.php",
            data=data,
            headers=self.headers).json()

    def catalog(
            self,
            year: int = None,
            genre: str = None,
            season: str = None,
            page: int = 1,
            sort: int = 2,
            finish: int = 2,
            xpage: str = "catalog"):
        data = {
            "page": page,
            "search": {
                "year": year,
                "genre": genre, 
                "season": season
            },
            "xpage": xpage,
            "sort": sort,
            "finish": finish
        }
        return requests.post(
            f"{self.api_v2}/catalog.php",
            data=data,
            headers=self.headers).json()

    def random_anime(self):
        data = {"js": 1}
        return requests.post(
            f"{self.api_v2}/random.php",
            data=data,
            headers=self.headers).json()

    def get_title(self, code: str):
        return requests.get(
            f"{self.api}/v2/getTitle?code={code}",
            headers=self.headers).json()

    def get_updates(self, filter: str, limit: int = 5):
        return requests.get(
            f"{self.api}/v2/getUpdates?filter={filter},type,status&limit={limit}",
            headers=self.headers).json()

    def get_changes(self, filter: str = "type,status", limit: int = 5):
        return requests.get(
            f"{self.api}/v2/getChanges?filter={filter}&limit={limit}",
            headers=self.headers).json()

    def get_schedule(self, days: int):
        return requests.get(
            f"{self.api}/v2/getSchedule?days={days}",
            headers=self.headers).json()

    def get_caching_nodes(self):
        return requests.get(
            f"{self.api}/v2/getCachingNodes",
            headers=self.headers).json()

    def get_random_title(self):
        return requests.get(
            f"{self.api}/v2/getRandomTitle",
            headers=self.headers).json()

    def get_youtube_videos(self, limit: int = 10):
        return requests.get(
            f"{self.api}/v2/getYouTube?limit={limit}",
            headers=self.headers).json()

    def get_feed(self, limit: int = 10):
        return requests.get(
            f"{self.api}/v2/getFeed?limit={limit}",
            headers=self.headers).json()

    def get_years(self):
        return requests.get(
            f"{self.api}/v2/getYears",
            headers=self.headers).json()

    def get_genres(self, sorting_type: int = 0):
        return requests.get(
            f"{self.api}/v2/getGenres?sorting_type={sorting_type}",
            headers=self.headers).json()

    def search_titles(self, search: str, limit: int = 10):
        return requests.get(
            f"{self.api}/v2/searchTitles?search={search}&limit={limit}",
            headers=self.headers).json()

    def get_team(self):
        return requests.get(
            f"{self.api}/v2/getTeam",
            headers=self.headers).json()

    def get_seed_stats(self, users: str = None, limit: int = 10):
        url = f"{self.api}/v2/getSeedStats?limit={limit}"
        if users:
            url = f"{self.api}/v2/getSeedStats?users={users}"
        return requests.get(url, headers=self.headers).json()

    def get_rss(self, rss_type: str, limit: int = 5):
        return requests.get(
            f"{self.api}/v2/getRSS?rss_type={rss_type}&limit={limit}",
            headers=self.headers).json()

    def get_favorite_titles(self, session: str):
        return requests.get(
            f"{self.api}/v2/getFavorites?session={session}",
            headers=self.headers).json()

    def add_title_to_favorites(self, session: str, title_id: int):
        return requests.put(
            f"{self.api}/v2/addFavorite?session={session}&title_id={title_id}",
            headers=self.headers).json()

    def delete_title_from_favorites(self, session: str, title_id: int):
        return requests.delete(
            f"{self.api}/v2/delFavorite?session={session}&title_id={title_id}",
            headers=self.headers).json()
