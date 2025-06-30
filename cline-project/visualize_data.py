import matplotlib.pyplot as plt
from analyze_data import analyze_drug_data

def visualize_data(approval_years, common_products):
    """
    Visualizes the analyzed drug approval data.
    
    Args:
        approval_years (dict): A dictionary of drug approvals by year.
        common_products (dict): A dictionary of the most common drug products.
    """
    # Plot drug approvals by year
    years = sorted(approval_years.keys())
    counts = [approval_years[year] for year in years]
    
    plt.figure(figsize=(10, 5))
    plt.bar(years, counts)
    plt.xlabel("Year")
    plt.ylabel("Number of Approvals")
    plt.title("New Drug Approvals by Year")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("cline-project/approvals_by_year.png")
    
    # Plot most common drug products
    products = [item[0] for item in common_products.most_common(5)]
    product_counts = [item[1] for item in common_products.most_common(5)]
    
    plt.figure(figsize=(10, 5))
    plt.bar(products, product_counts)
    plt.xlabel("Drug Product")
    plt.ylabel("Number of Approvals")
    plt.title("Most Common Approved Drug Products")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("cline-project/common_drug_products.png")

if __name__ == "__main__":
    years, products = analyze_drug_data()
    visualize_data(years, products)
    print("Data visualization charts saved as PNG files.")
