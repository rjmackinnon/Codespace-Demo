from fetch_data import fetch_drug_data
from analyze_data import analyze_drug_data
from visualize_data import visualize_data
import json

def main():
    """
    Main function to run the drug approval analysis project.
    """
    # Step 1: Fetch data
    print("Fetching drug data...")
    drug_data = fetch_drug_data()
    with open("cline-project/drug_data.json", "w") as f:
        json.dump(drug_data, f, indent=4)
    print(f"Successfully fetched and saved {len(drug_data)} drug approval records.")
    
    # Step 2: Analyze data
    print("\nAnalyzing drug data...")
    years, products = analyze_drug_data()
    print("Drug Approvals by Year:")
    for year, count in sorted(years.items()):
        print(f"- {year}: {count}")
    print("\nMost Common Drug Products:")
    for product, count in products.most_common(5):
        print(f"- {product}: {count}")
        
    # Step 3: Visualize data
    print("\nGenerating visualizations...")
    visualize_data(years, products)
    print("Data visualization charts saved as PNG files.")

if __name__ == "__main__":
    main()
