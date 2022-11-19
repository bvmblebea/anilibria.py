import requests
from random import choices

class Anilibria:
	def __init__(self) -> None:
		self.first_api = "https://api.anilibria.tv"
		self.second_api = "https://www.anilibria.tv/public"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
			"x-requested-with": "XMLHttpRequest"
		}
		self.session_id = None

	def generate_captcha(self) -> str:
		return "".join(
			choices(
				"ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
				"abcdefghijklmnopqrstuvwxyz" +
				"_-",
				k=462)).replace(
					"--",
					"-")

	def login(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"csrf": 1,
			"mail": email,
			"passwd": password
		}
		response = requests.post(
			f"{self.second_api}/login.php",
			data=data,
			headers=self.headers).json()
		if "sessionId" in response:
			self.session_id = response["sessionId"]
			self.headers["cookie"] = f"PHPSESSID={self.session_id}"
		return response

	def register(
			self,
			login: str,
			email: str,
			password: str) -> dict:
		data = {
			"g-recaptcha-response": self.generate_captcha(),
			"login": login,
			"mail": email,
			"passwd": password
		}
		return requests.post(
			f"{self.second_api}/registration.php",
			data=data,
			headers=self.headers).json()

	def search_anime(
			self,
			search: str,
			small: int = 1) -> dict: 
		data = {
			"search": search,
			"small": small
		}
		return requests.post(
			f"{self.second_api}/search.php",
			data=data,
			headers=self.headers).json()

	def report_error(
			self,
			message: str,
			url: str) -> dict:
		data = {
			"mes": message,
			"url": url,
			"g-recaptcha-response": self.generate_captcha(),
			"recaptcha": 2
		}
		return requests.post(
			f"{self.second_api}/error.php",
			data=data,
			headers=self.headers).json()

	def get_catalog(
			self,
			year: int = None,
			genre: str = None, 
			season: str = None,
			page: int = 1,
			sort: int = 2,
			finish: int = 2,
			x_page: str = "catalog") -> dict:
		data = {
			"page": page,
			"search": {
				"year": year,
				"genre": genre,
				"season": season
			},
			"xpage": x_page,
			"sort": sort,
			"finish": finish
		}
		return requests.post(
			f"{self.second_api}/catalog.php",
			data=data,
			headers=self.headers).json()

	def get_random_anime(self) -> dict:
		data = {
			"js": 1
		}
		return requests.post(
			f"{self.second_api}/random.php",
			data=data,
			headers=self.headers).json()

	def get_title(self, code: str) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getTitle?code={code}",
			headers=self.headers).json()

	def get_updates(
			self,
			filter: str,
			limit: int = 5) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getUpdates?filter={filter},type,status&limit={limit}",
			headers=self.headers).json()

	def get_changes(
			self,
			filter: str = "type,status",
			limit: int = 5) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getChanges?filter={filter}&limit={limit}",
			headers=self.headers).json()

	def get_schedule(self, days: int) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getSchedule?days={days}",
			headers=self.headers).json()

	def get_caching_nodes(self) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getCachingNodes",
			headers=self.headers).json()

	def get_random_title(self) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getRandomTitle",
			headers=self.headers).json()

	def get_youtube_videos(self, limit: int = 10) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getYouTube?limit={limit}",
			headers=self.headers).json()

	def get_feed(self, limit: int = 10) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getFeed?limit={limit}",
			headers=self.headers).json()

	def get_years(self) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getYears",
			headers=self.headers).json()

	def get_genres(self, sorting_type: int = 0) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getGenres?sorting_type={sorting_type}",
			headers=self.headers).json()

	def search_titles(
			self,
			search: str,
			limit: int = 10) -> dict:
		return requests.get(
			f"{self.first_api}/v2/searchTitles?search={search}&limit={limit}",
			headers=self.headers).json()

	def get_team(self) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getTeam",
			headers=self.headers).json()

	def get_seed_stats(
			self,
			users: str = None,
			limit: int = 10) -> dict:
		url = f"{self.first_api}/v2/getSeedStats?limit={limit}"
		if users:
			url = f"{self.first_api}/v2/getSeedStats?users={users}"
		return requests.get(url, headers=self.headers).json()

	def get_rss(
			self,
			rss_type: str,
			limit: int = 5) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getRSS?rss_type={rss_type}&limit={limit}",
			headers=self.headers).json()

	def get_favorite_titles(self, session: str) -> dict:
		return requests.get(
			f"{self.first_api}/v2/getFavorites?session={session}",
			headers=self.headers).json()

	def add_title_to_favorites(
			self,
			session: str,
			title_id: int) -> dict:
		return requests.put(
			f"{self.first_api}/v2/addFavorite?session={session}&title_id={title_id}",
			headers=self.headers).json()

	def delete_title_from_favorites(
			self, 
			session: str,
			title_id: int) -> dict:
		return requests.delete(
			f"{self.first_api}/v2/delFavorite?session={session}&title_id={title_id}",
			headers=self.headers).json()
