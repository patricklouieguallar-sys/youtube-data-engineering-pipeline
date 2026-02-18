import pandas as pd
import json

# read the csv raw data from the vaariable path
def extract_csv(path):
    return pd.read_csv(path)

# extract the category from the the variable path
def extract_categories(path):
    with open(path) as f:
        data = json.load(f)


    categories = []
    for item in data["items"]:
        categories.append({
            "category_id": int(item["id"]),
            "category_name": item["snippet"]["title"]
        })

    return pd.DataFrame(categories)