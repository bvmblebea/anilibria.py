# AnilibriaAPI
Python library for Anilibria -  www.anilibria.tv
Библиотека для аниме вебсайта - www.anilibria.tv
![AnilibriaAPI](https://anilibria.app/res/images/og_image.jpg?1598792059)

### Example
```python3
# Login
import anilibria
client = anilibria.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
```
