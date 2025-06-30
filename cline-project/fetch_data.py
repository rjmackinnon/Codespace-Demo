import requests
import json

def fetch_drug_data(limit=100):
    """
    Fetches drug approval data from the OpenFDA API.
    
    Args:
        limit (int): The number of records to fetch.
        
    Returns:
        list: A list of drug approval records.
    """
    url = f"https://api.fda.gov/drug/drugsfda.json?limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return []

if __name__ == "__main__":
    drug_data = fetch_drug_data()
    with open("cline-project/drug_data.json", "w") as f:
        json.dump(drug_data, f, indent=4)
    print(f"Successfully fetched and saved {len(drug_data)} drug approval records.")
