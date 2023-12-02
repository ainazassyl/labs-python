# Task1.1
import requests

post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'

response = requests.get(url)

print(response.json())

if 400 <= response.status_code <= 499:
    print(f"Client Error: {response.status_code}")
elif 500 <= response.status_code <= 599:
    print(f"Server Error: {response.status_code}")

# Task1.2
class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# Task1.3
new_todo_object = ToDo(userId=2, id=201, title="Example Task", completed=False)

# Task1.4
new_todo_item = {
    "userId": new_todo_object.userId,
    "title": new_todo_object.title,
    "completed": new_todo_object.completed
}

response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_todo_item)

if response.status_code >= 400:
    print(f'Error: {response.status_code} - {response.reason}')
else:
    print("Response Content:")
    print(response.json())

# Task1.5
new_todo_object.completed = True

# Task1.6
new_todo_item["title"] = "Updated Title"

chosen_id = 1
put_url = f"https://jsonplaceholder.typicode.com/todos/{chosen_id}"
put_response = requests.put(put_url, json=new_todo_item)

if put_response.status_code >= 400:
    print(f'Error: {put_response.status_code} - {put_response.reason}')
else:
    print("Response Content:")
    print(put_response.json())

# Task2.1
import requests
import random

character_id = random.randint(1, 826)

url = f"https://rickandmortyapi.com/api/character/{character_id}"
response = requests.get(url)

if response.status_code == 200:
    character_data = response.json()
    print("JSON Response:")
    print(character_data)
else:
    print(f"Error: {response.status_code} - {response.reason}")

# Task2.2
if character_data:
    print("JSON Response:")
    print(character_data)

    print("\nKeys of the JSON structure:")
    for key in character_data.keys():
        print(key)

# Task2.3
if character_data:
    filename = f"info_character_{character_id}.json"
    with open(filename, 'w') as file:
        json.dump(character_data, file)
    print(f"JSON data saved to '{filename}'")

# Task2.4
if character_data:
    episode_urls = character_data['episode']

    episode_ids = [int(url.split('/')[-1]) for url in episode_urls]

    filename_episodes = f"all_episodes_with_character_{character_id}.txt"
    with open(filename_episodes, 'a') as file:
        for url in episode_urls:
            file.write(url + '\n')
    print(f"Episode URLs saved to '{filename_episodes}'")

# Task2.5
episode_response = requests.get("https://rickandmortyapi.com/api/episode/1")
print(episode_response.json())

# Task2.6
class Episode:
    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

    def __str__(self):
        return f"Episode ID: {self.id}, Name: {self.name}, Air Date: {self.air_date}"
    
# Task2.7
episode_objects = []

for episode_id in episode_ids:
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = requests.get(url)

    if response.status_code == 200:
        episode_data = response.json()
        episode = Episode(**episode_data)
        episode_objects.append(episode)
    else:
        print(f"Error fetching episode {episode_id}: {response.status_code} - {response.reason}")

# Task2.8
class Episode:

    def display_info(self):
        print(f"Episode ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Air Date: {self.air_date}")

# Task2.10
class Character:
    def __init__(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

    def __str__(self):
        return f"Character ID: {self.id}, Name: {self.name}, Status: {self.status}"


