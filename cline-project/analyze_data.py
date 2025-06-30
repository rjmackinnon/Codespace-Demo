import json
from collections import Counter

def analyze_drug_data(file_path="cline-project/drug_data.json"):
    """
    Analyzes the fetched drug approval data.
    
    Args:
        file_path (str): The path to the drug data JSON file.
        
    Returns:
        tuple: A tuple containing two dictionaries:
               - approval_years: A Counter of drug approvals by year.
               - common_products: A Counter of the most common drug products.
    """
    with open(file_path, "r") as f:
        drug_data = json.load(f)
    
    approval_years = Counter()
    common_products = Counter()
    
    for record in drug_data:
        if "submissions" in record and record["submissions"]:
            for submission in record["submissions"]:
                if submission["submission_status_date"]:
                    year = submission["submission_status_date"][:4]
                    approval_years[year] += 1
        
        if "products" in record and record["products"]:
            for product in record["products"]:
                if "brand_name" in product:
                    common_products[product["brand_name"]] += 1
                    
    return approval_years, common_products

if __name__ == "__main__":
    years, products = analyze_drug_data()
    print("Drug Approvals by Year:")
    for year, count in sorted(years.items()):
        print(f"- {year}: {count}")
        
    print("\nMost Common Drug Products:")
    for product, count in products.most_common(5):
        print(f"- {product}: {count}")
