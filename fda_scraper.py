import requests
import pandas as pd
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt

# Fetch drug approval data from OpenFDA
API_URL = "https://api.fda.gov/drug/drugsfda.json"
PARAMS = {
    "limit": 100,
    "skip": 0
}

def fetch_approvals(limit=100):
    """Fetch drug approval data from OpenFDA."""
    all_results = []
    skip = 0
    while len(all_results) < limit:
        params = PARAMS.copy()
        params["limit"] = min(100, limit - len(all_results))
        params["skip"] = skip
        response = requests.get(API_URL, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        data = response.json()
        results = data.get("results", [])
        if not results:
            break
        all_results.extend(results)
        skip += len(results)
    return all_results

def analyze_approvals(approvals):
    """Analyze approval years and product names."""
    years = []
    products = []
    for entry in approvals:
        # Extract all years from submission_status_date in submissions
        for sub in entry.get('submissions', []):
            date = sub.get('submission_status_date')
            if date and len(date) >= 4:
                years.append(date[:4])
        for product in entry.get('products', []):
            name = product.get('brand_name')
            if name:
                products.append(name)
    return years, products

def main():
    print("Fetching drug approval data from OpenFDA...")
    approvals = fetch_approvals(limit=200)
    print(f"Fetched {len(approvals)} records.")
    # Debug: print first 2 entries to inspect structure
    import json
    print("Sample entry:")
    print(json.dumps(approvals[0], indent=2))
    if len(approvals) > 1:
        print(json.dumps(approvals[1], indent=2))
    years, products = analyze_approvals(approvals)
    # Count approvals by year
    year_counts = Counter(years)
    print("\nDrug Approvals by Year:")
    for year, count in sorted(year_counts.items()):
        print(f"{year}: {count}")
    # Most common products
    product_counts = Counter(products)
    print("\nMost Common Approved Drug Products:")
    for name, count in product_counts.most_common(10):
        print(f"{name}: {count}")
    # --- Chart: Drug Approvals by Year ---
    if year_counts:
        years_sorted = sorted(year_counts.items())
        x, y = zip(*years_sorted)
        print(f"Years for chart: {x}")
        print(f"Counts for chart: {y}")
        plt.figure(figsize=(8, 5))
        plt.bar(x, y, color='skyblue')
        plt.xlabel('Year')
        plt.ylabel('Number of Approvals')
        plt.title('Drug Approvals by Year (OpenFDA Sample)')
        plt.tight_layout()
        plt.savefig('approvals_by_year.png')
        print("\nChart saved as approvals_by_year.png in directory:")
        import os
        print(os.getcwd())

if __name__ == "__main__":
    main()
