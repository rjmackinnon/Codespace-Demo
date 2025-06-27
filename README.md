# Drug Approval Data Analysis with OpenFDA

## Project Goals

This project demonstrates how to use publicly-accessible data from the OpenFDA API to analyze drug approval trends in the United States. The primary objectives are:

1. **Fetch Drug Approval Data:**
   - Retrieve drug approval records from the OpenFDA API.

2. **Analyze Trends:**
   - Count the number of new drug approvals by year.
   - Identify the most common drug products approved.

3. **Visualize Results:**
   - Present findings in a clear, easy-to-understand format (tables or charts).

4. **Educational Purpose:**
   - Provide a simple, reproducible example for pharmacists and data curators to explore pharmaceutical data using Python and Codespaces.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the analysis script:
   ```bash
   python fda_scraper.py
   ```

## Data Source
- [OpenFDA Drug API](https://open.fda.gov/apis/drug/)

## Requirements
- Python 3.8+
- Internet connection

## Next Steps
- Expand analysis to include adverse event data or drug labeling information.
- Integrate data visualization for deeper insights.
