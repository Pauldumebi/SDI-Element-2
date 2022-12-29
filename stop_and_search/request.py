from cached_data import store
import requests

def police_force():
    target_key = "all_police_force"

    # we need to check if the data is available in the cache
    if target_key in store:
        return store[target_key]
    else:
        response = requests.get("https://data.police.uk/api/forces")
        if response.status_code == 200:
            data = response.json()
            all_police_force = {item["name"] : item["id"] for item in data}
            store[target_key] = all_police_force
        else:
            all_police_force = {}
        return all_police_force
    
def crime_categories():
    target_key = "all_crime_categories"

    # we need to check if the data is available in the cache
    if target_key in store:
        return store[target_key]
    else:
        response = requests.get("https://data.police.uk/api/crime-categories")
        if response.status_code == 200:
            data = response.json()
            all_crime_categories = { item["url"] : item["name"] for item in data}
            store[target_key] = all_crime_categories
        else:
            all_crime_categories = {}
        return all_crime_categories
    
def get_cases(selected_police_force, date):
    # print(police_force, 'police_force')
    # print(date, 'date')
    all_police_force_cache = police_force()
    # cache request of police force cases by date
    target_key = selected_police_force + "-" + date
    if target_key in store:
        return store[target_key]
    else:
        response = requests.get(
            "https://data.police.uk/api/stops-force?force="
            + all_police_force_cache[selected_police_force]
            + "&date="
            + date
        )
        if response.status_code == 200:
            data = response.json()
            store[target_key] = [len(data), data]
            return len(data), data
        else:
            return []