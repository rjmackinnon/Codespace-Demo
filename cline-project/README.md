# Drug Approval Analysis

This project analyzes drug approval trends in the United States using data from the OpenFDA API.

## Description

This project fetches drug approval records, counts new drug approvals by year, identifies the most common approved drug products, and visualizes the results. It is designed as a simple, reproducible example for pharmacists and data curators.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the analysis:**
    ```bash
    python main.py
    ```

## Output

The script will generate the following files:

*   `drug_data.json`: Raw data fetched from the OpenFDA API.
*   `approvals_by_year.png`: A bar chart showing the number of drug approvals per year.
*   `common_drug_products.png`: A bar chart showing the most commonly approved drug products.
