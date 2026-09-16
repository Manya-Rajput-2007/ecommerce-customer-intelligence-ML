
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="E-Commerce Customer Intelligence",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    .main {
        padding-top: 1rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .dashboard-title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .dashboard-subtitle {
        color: #777;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        background-color: #f8f9fa;
        border: 1px solid #e5e7eb;
        text-align: center;
    }

    .section-title {
        font-size: 24px;
        font-weight: 650;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .recommendation-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        background-color: #000000;
        margin-bottom: 12px;
    }

    .recommendation-title {
        font-size: 18px;
        font-weight: 650;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid #e5e7eb;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    customer_df = pd.read_csv(
        "./data/processed/customer_intelligence.csv"
    )

    pca_df = pd.read_csv(
        "./data/processed/pca_data.csv"
    )

    cluster_profile = pd.read_csv(
        "./data/processed/cluster_profiles.csv"
    )

    return customer_df, pca_df, cluster_profile


df, pca_df, cluster_profile = load_data()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🛒 Customer Intelligence")

st.sidebar.markdown("---")

st.sidebar.subheader("Dashboard Filters")

segments = sorted(
    df["Segment_Name"].dropna().unique()
)

selected_segment = st.sidebar.multiselect(
    "Customer Segment",
    options=segments,
    placeholder="Select segments..."
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "E-Commerce Customer Intelligence System"
)

st.sidebar.caption(
    "Customer segmentation • Behavioral analytics • Business insights"
)


# =========================================================
# FILTER DATA
# =========================================================

if selected_segment:

    filtered_df = df[
        df["Segment_Name"].isin(selected_segment)
    ]

else:

    filtered_df = df.copy()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="dashboard-title">🛒 E-Commerce Customer Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Customer segmentation, behavioral analytics and actionable business insights'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# KPI SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📊 Business Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        label="Total Customers",
        value=f"{filtered_df['customer_id'].nunique():,}"
    )


with col2:

    st.metric(
        label="Customer Segments",
        value=f"{filtered_df['Segment_Name'].nunique():,}"
    )


with col3:

    st.metric(
        label="Avg Monthly Spend",
        value=f"₹{filtered_df['avg_monthly_spend'].mean():,.2f}"
    )


with col4:

    st.metric(
        label="Avg Purchase Frequency",
        value=f"{filtered_df['purchase_frequency'].mean():.2f}"
    )


# =========================================================
# SEGMENT ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">👥 Customer Segment Distribution</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


# -----------------------------
# Bar Chart
# -----------------------------

with col1:

    segment_counts = (
        filtered_df["Segment_Name"]
        .value_counts()
        .sort_values(ascending=True)
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    segment_counts.plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel("Number of Customers")
    ax.set_ylabel("Customer Segment")
    ax.set_title("Customers by Segment")

    plt.tight_layout()

    st.pyplot(fig)


# -----------------------------
# Pie Chart
# -----------------------------

with col2:

    segment_pie = filtered_df["Segment_Name"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))

    wedges, texts, autotexts = ax.pie(
        segment_pie.values,
        labels=segment_pie.index,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"linewidth": 1, "edgecolor": "white"}
    )

    ax.set_title("Segment Share")
    ax.axis("equal")

    st.pyplot(fig)




# =========================================================
# CLUSTER PROFILES
# =========================================================

st.markdown(
    '<div class="section-title">📋 Customer Cluster Profiles</div>',
    unsafe_allow_html=True
)

st.dataframe(
    cluster_profile,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# CUSTOMER SEARCH
# =========================================================

st.markdown(
    '<div class="section-title">🔎 Customer Lookup</div>',
    unsafe_allow_html=True
)

customer_id = st.number_input(
    "Enter Customer ID",
    min_value=int(df["customer_id"].min()),
    max_value=int(df["customer_id"].max()),
    value=int(df["customer_id"].min()),
    step=1
)

customer_info = df[
    df["customer_id"] == customer_id
]


if not customer_info.empty:

    st.success("Customer found")

    customer_row = customer_info.iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Customer Segment",
            customer_row["Segment_Name"]
        )

    with col2:
        st.metric(
            "Monthly Spend",
            f"₹{customer_row['avg_monthly_spend']:,.2f}"
        )

    with col3:
        st.metric(
            "Purchase Frequency",
            f"{customer_row['purchase_frequency']:.2f}"
        )

    with col4:
        st.metric(
            "Customer ID",
            str(int(customer_row["customer_id"]))
        )

    st.markdown("#### Customer Details")

    st.dataframe(
        customer_info,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("Customer not found.")


# =========================================================
# FILTERED CUSTOMER DATA
# =========================================================

st.markdown(
    '<div class="section-title">📁 Customer Dataset</div>',
    unsafe_allow_html=True
)

st.caption(
    f"Showing {len(filtered_df):,} customers"
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# BUSINESS RECOMMENDATIONS
# =========================================================

st.markdown(
    '<div class="section-title">💡 Business Recommendations</div>',
    unsafe_allow_html=True
)


recommendations = {

    "Premium Loyal Customers":
        "Launch loyalty rewards, exclusive offers and premium product recommendations.",

    "Budget-Conscious Customers":
        "Provide personalized discounts, affordable bundles and price-sensitive promotions.",

    "At-Risk Customers":
        "Run targeted re-engagement campaigns, personalized offers and retention strategies.",

    "Return-Prone Customers":
        "Improve product descriptions, sizing information, product quality and customer support."
}


for segment, recommendation in recommendations.items():

    if segment in segments:

        st.markdown(
            f"""
            <div class="recommendation-card">
                <div class="recommendation-title">
                    {segment}
                </div>
                <div>
                    {recommendation}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "E-Commerce Customer Intelligence System • "
    "Built with Python, Pandas, Scikit-learn, Matplotlib, Seaborn & Streamlit"
)

