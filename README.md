# E-Commerce Customer Intelligence

A data-driven customer segmentation and business intelligence dashboard for an e-commerce platform. This project analyzes customer behavior and groups customers into meaningful segments using clustering and dimensionality reduction techniques, then visualizes the results in an interactive Streamlit app.

## Project Objective

The goal is to help e-commerce businesses understand:

- Which customer groups exist in the customer base
- How spending and purchase behavior differ across segments
- Which customers are most valuable or at risk
- How to create business strategies based on customer behavior

This project combines machine learning, exploratory data analysis, and business reporting into a single dashboard.

---

## What This Project Does

The app provides a dashboard for:

- Customer segmentation by cluster/segment name
- Business overview KPIs
- Distribution of customer segments
- PCA-based cluster visualization
- Customer lookup by ID
- Dataset exploration
- Business recommendations for each customer segment

The dashboard is built using Python and Streamlit and reads processed customer data stored in the `data/processed` folder.

---

## Core Features

### 1. Business Overview
The dashboard displays:

- Total customers
- Number of distinct segments
- Average monthly spend
- Average purchase frequency

This helps quickly understand the health and structure of the customer base.

### 2. Customer Segment Distribution
The app visualizes:

- Horizontal bar chart of segment counts
- Pie chart showing contribution of each segment

This helps identify which customer groups are most prominent.

### 3. Customer Cluster Analysis
Using PCA reduced features, the project creates a scatter plot of clusters in 2D space to reveal natural customer groupings.

### 4. Customer Lookup
Users can search for a specific customer ID and view:

- Segment name
- Monthly spend
- Purchase frequency
- Customer details

### 5. Cluster Profiles
The dashboard shows a profile table with cluster-level summary statistics to interpret what each segment represents.

### 6. Business Recommendations
The system offers targeted recommendations for each segment, such as:

- Premium loyal customers: loyalty rewards and premium offers
- Budget-conscious customers: discounts and affordable bundles
- At-risk customers: re-engagement campaigns
- Return-prone customers: product and support improvements

---

## Data Workflow

This project follows a structured customer analytics workflow:

1. Data understanding
2. Cleaning and preprocessing
3. Exploratory data analysis
4. Feature engineering
5. Clustering (K-Means, DBSCAN, Hierarchical Clustering)
6. PCA visualization
7. Customer profiling and dashboard generation

The processed output files are stored in the `data` directory, especially in `data/processed`, where the dashboard reads from:

- `customer_intelligence.csv`
- `pca_data.csv`
- `cluster_profiles.csv`

---

## Project Structure

```text
E-Commerce-Customer-Intelligence/
│
├── app.py                          # Streamlit dashboard application
├── Requirements.txt                # Python dependencies
├── data/
│   ├── analysed_data03.csv
│   ├── cleaned_data02.csv
│   ├── db_scaned_data06.csv
│   ├── db_scanned_data06.csv
│   ├── FinalFeatureDataset04.csv
│   ├── kmean_cluster_data05.csv
│   ├── pca_data07.csv
│   ├── processed_data01.csv
│   └── processed/
│       ├── cluster_profiles.csv
│       ├── customer_intelligence.csv
│       └── pca_data.csv
├── models/
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_kmeans_clustering.ipynb
│   ├── 06_dbscan_clustering.ipynb
│   ├── 07_hierarchical_clustering.ipynb
│   └── 08_pca_visualization.ipynb
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- OpenPyXL
- Joblib

---

## Setup Instructions

### 1. Clone the project

```bash
git clone <repository-url>
cd ecommerce-customer-intelligence
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r Requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal (usually `http://localhost:8501`).

---

## How to Use the Dashboard

1. Open the app in the browser.
2. Use the sidebar to filter customer segments.
3. Review the KPIs and visual charts.
4. Inspect clusters and profiles.
5. Search for a customer by ID.
6. Review dataset tables and segment-specific recommendations.

---

## Business Value

This project helps business teams:

- Identify high-value customer groups
- Understand purchase behavior patterns
- Detect customers needing retention campaigns
- Build personalized marketing strategies
- Improve segmentation-driven decision making

It is particularly useful for e-commerce teams, digital marketing teams, customer success teams, and product managers.

---

## Sample Insights the Dashboard Can Reveal

- Some segments may represent premium, high-frequency buyers.
- Others may be price-sensitive or low-engagement customers.
- The cluster profiles can highlight spend patterns and purchase intensity.
- At-risk segments can be targeted with retention offers.
- Return-prone customers can be improved through better support and product transparency.

---

## Summary

This project is a full customer intelligence solution that transforms raw e-commerce data into actionable business insights through segmentation, analysis, and visualization. The final output is a professional interactive dashboard that helps businesses understand their customers and make smarter, data-driven decisions.

---

## License

This project is intended for educational and business analytics use. Add your preferred license if you plan to share or publish it.
