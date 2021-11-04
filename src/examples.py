# Login without input
import anilibria
client = anilibria.Client()
client.auth(email="email", password="password")

# Login with input
import anilibria
client = anilibria.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)

# search anime
import anilibria
client = anilibria.Client()
anime = client.search_anime(search="название аниме)
print(anime)

# get random anime
import anilibria
client = anilibria.Client()
random_anime = client.random_anime()
print(random_anime)
