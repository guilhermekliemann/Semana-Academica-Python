from requests import get 

def get_followers(user_name: str):
    url = f"https://api.github.com/users/{user_name}"
    response = get(url)
    if response.status_code == 200:
        return {"followers": response.json()["followers"]}
    else:
        return {"followers": None}

print(get_followers("guilhermekliemann"))