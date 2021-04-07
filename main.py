python -m pip freeze > requirements.txtimport requests
from settings import USERNAME

if USERNAME != '':
    pass
else:
    USERNAME = str(input("Username: "))

url = f'https://api.github.com/users/{USERNAME}'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
user_dict = r.json()


print(f"Login: {user_dict['login']}")
print(f"URL: {user_dict['html_url']}")
print(f"Avatar link: {user_dict['avatar_url']}")
print(f"Created: {user_dict['created_at'][0:10]}")
print(f"Updated: {user_dict['updated_at'][0:10]}")
print(f"Following: {user_dict['following']}")
print(f"Followers: {user_dict['followers']}")
print(f"Location: {user_dict['location']}")



url = f'https://api.github.com/users/{USERNAME}/repos'
r = requests.get(url, headers=headers)
user_dict = r.json()
for n in user_dict:
    print(f"Repository name: {n['name'].title()}")
    print(f"Description: {n['description']}")
    print(f"Link: https://github.com/{n['full_name']}")
