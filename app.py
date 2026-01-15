import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="HCL Financial Analysis Dashboard",
    layout="wide"
)

st.title("AI-Assisted Financial Analysis Dashboard")
st.subheader("HCL Technologies Limited | Firm-Level & Project-Level Insights")

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data
def load_data():
    prices = pd.read_excel("FMWAI_Analysis.xlsx", sheet_name="Data", index_col=0)
    returns_daily = pd.read_excel("FMWAI_Analysis.xlsx", sheet_name="Returns_Daily", index_col=0)
    returns_weekly = pd.read_excel("FMWAI_Analysis.xlsx", sheet_name="Returns_Weekly", index_col=0)
    returns_monthly = pd.read_excel("FMWAI_Analysis.xlsx", sheet_name="Returns_Monthly", index_col=0)
    capm = pd.read_excel("FMWAI_Analysis.xlsx", sheet_name="CAPM_Regression", index_col=0)
    wacc = pd.read_excel("FMWAI_Analysis.xlsx", sheet_name="Capital_Structure_WACC")
    project = pd.read_excel("FMWAI_Analysis.xlsx", sheet_name="Project_Financials", index_col=0)
    return prices, returns_daily, returns_weekly, returns_monthly, capm, wacc, project

prices, rd, rw, rm, capm, wacc, project = load_data()

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.header("Dashboard Controls")
freq = st.sidebar.selectbox(
    "Select Return Frequency",
    ["Daily", "Weekly", "Monthly"]
)

# -----------------------
# SECTION 1: PRICE TRENDS
# -----------------------
st.header("1. Stock and Market Price Trends")

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(prices.index, prices["Stock_Close"], label="HCL Technologies")
ax.plot(prices.index, prices["Market_Close"], label="NIFTY 50")
ax.set_title("Price Trends (2022–2025)")
ax.legend()
st.pyplot(fig)

# -----------------------
# SECTION 2: RETURN DISTRIBUTION
# -----------------------
st.header("2. Return Distribution Analysis")

returns_map = {
    "Daily": rd,
    "Weekly": rw,
    "Monthly": rm
}

fig, ax = plt.subplots(figsize=(8,4))
ax.hist(
    returns_map[freq]["Stock_Close"],
    bins=40,
    alpha=0.7
)
ax.set_title(f"{freq} Return Distribution – HCL Technologies")
st.pyplot(fig)

# -----------------------
# SECTION 3: CAPM BETA
# -----------------------
st.header("3. CAPM Risk Exposure")

beta = capm.loc[freq, "Beta"]
r2 = capm.loc[freq, "R_squared"]

col1, col2 = st.columns(2)
col1.metric("Equity Beta", f"{beta:.2f}")
col2.metric("R² (Market Explanatory Power)", f"{r2:.2f}")

st.caption(
    "Beta below 1 indicates defensive market behaviour. "
    "Lower R² highlights the importance of firm-specific fundamentals."
)

# -----------------------
# SECTION 4: WACC COMPARISON
# -----------------------
st.header("4. Cost of Capital Comparison")

wacc_current = float(wacc.loc[wacc["Unnamed: 0"] == "WACC (Current)", "Value"])
wacc_target = float(wacc.loc[wacc["Unnamed: 0"] == "WACC (25%D / 75%E)", "Value"])

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(
    ["Current WACC", "Target WACC (25%D)"],
    [wacc_current*100, wacc_target*100]
)
ax.set_ylabel("WACC (%)")
ax.set_title("Impact of Capital Structure on WACC")
st.pyplot(fig)

# -----------------------
# SECTION 5: PROJECT FCFF
# -----------------------
st.header("5. Project Free Cash Flow to Firm (FCFF)")

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(project.index, project["FCFF"], marker="o")
ax.set_title("Projected FCFF Growth")
ax.set_ylabel("INR Crore")
st.pyplot(fig)

# -----------------------
# SECTION 6: AI-DRIVEN INSIGHTS
# -----------------------
st.header("6. Key AI-Driven Insights")

st.markdown("""
- HCL Technologies exhibits **defensive risk characteristics** with beta consistently below 1.
- Market movements explain only **18–25% of return variation**, highlighting the role of firm fundamentals.
- Introducing **moderate leverage (25%)** reduces WACC even under conservative debt cost assumptions.
- The proposed AIOps project shows **strong scalability**, with FCFF growing nearly eightfold over five years.
- AI-assisted analysis enables faster scenario evaluation while retaining human oversight.
""")

st.success("Dashboard insights support both firm-level strategy and project-level investment decisions.")
