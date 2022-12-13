from cache.store import store
import requests

def fetchPoliceForce():
    targetKey = "forceList"

    # Check if data has been previously cached
    if targetKey in store:
        return store[targetKey]
    else:
        response = requests.get("https://data.police.uk/api/forces")
        if response.status_code == 200:
            data = response.json()
            forceList = {item["name"]: item["id"] for item in data}
            store[targetKey] = forceList
        else:
            forceList = {}
        return forceList
    
def fetchCasesRequest(policeForce, date):
    policeForceStore = fetchPoliceForce()
    targetKey = policeForce + "-" + date      #cache request by date
    if targetKey in store:
        return store[targetKey]
    else:
        response = requests.get(
            "https://data.police.uk/api/stops-force?force="
            + policeForceStore[policeForce]
            + "&date="
            + date
        )
        if response.status_code == 200:
            data = response.json()
            store[targetKey] = [len(data), data]
            return len(data), data
        else:
            return []