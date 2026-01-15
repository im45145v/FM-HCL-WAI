# AI-Assisted Financial Dashboard for HCL Technologies

## 🎯 Overview

This is a comprehensive, interactive financial dashboard for analyzing HCL Technologies Limited using AI-assisted decision support tools. The dashboard covers firm-level and project-level financial analysis with professional-grade visualizations and insights.

## ✨ Key Features

### Multi-Page Navigation
The dashboard is organized into 5 main sections:

1. **🏠 Executive Summary**
   - Key Performance Indicators (KPIs)
   - Corporate Governance Overview
   - Risk-Return Profile Gauge
   - Strategic Insights Cards
   - Market Context

2. **📈 Market Analysis**
   - Interactive dual-axis price trends (HCL vs NIFTY 50)
   - Return distribution analysis
   - Box plots and histograms
   - Cumulative performance comparison

3. **⚖️ Risk & Return**
   - Multi-frequency risk-return analysis
   - CAPM regression with enhanced scatter plots
   - Beta stability across time horizons
   - R² and explanatory power metrics

4. **💰 Capital Structure**
   - Current vs Target WACC comparison
   - Capital structure visualization (pie charts)
   - Asset beta and relevering analysis
   - WACC sensitivity analysis
   - Interactive what-if scenarios

5. **🚀 Project Valuation**
   - Pro-forma financial projections
   - Revenue and FCFF growth visualization
   - Margin analysis and profitability trends
   - NPV calculation with waterfall chart
   - Risk considerations and sensitivity analysis

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Data Files
Ensure `FMWAI_Analysis.xlsx` is in the same directory with these sheets:
- Data
- Returns_Daily, Returns_Weekly, Returns_Monthly
- Risk_Return_Summary
- CAPM_Regression
- CAPM_Expected_Returns
- Capital_Structure_WACC
- Beta_Adjustments
- Project_Financials
- Project_Risk

## 🚀 Running the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

## 📊 Dashboard Features

### Interactive Controls (Sidebar)

- **Return Frequency Selector**: Switch between Daily, Weekly, and Monthly analysis
- **What-If Scenarios**: 
  - Adjust target debt percentage (0-40%)
  - Modify cost of debt assumptions (4-12%)
  - See real-time WACC impact

### Advanced Visualizations

- **Plotly Interactive Charts**: Hover, zoom, and pan capabilities
- **Multi-axis Plots**: Compare different metrics simultaneously
- **Gradient Tables**: Color-coded financial data
- **Waterfall Charts**: NPV buildup visualization
- **Gauge Charts**: Risk metrics visualization

### Key Metrics Displayed

#### Firm-Level
- Equity Beta (Daily/Weekly/Monthly)
- Annualized Returns & Volatility
- CAPM Parameters (Alpha, Beta, R²)
- Cost of Equity & WACC
- Asset Beta Adjustments

#### Project-Level
- 5-Year Revenue Projections
- EBITDA, EBIT, NOPAT Margins
- Free Cash Flow to Firm (FCFF)
- Capital Expenditure Profile
- Net Present Value (NPV)

## 🎨 Design Enhancements

### Visual Design
- Custom CSS styling with gradient headers
- Color-coded insights (success/info/warning)
- Professional color palette
- Responsive layout

### User Experience
- Multi-page navigation
- Contextual help text
- Real-time what-if analysis
- Clear metric interpretation
- Academic disclaimers

## 📈 Analytical Framework

The dashboard implements a comprehensive corporate finance framework:

1. **Governance Analysis**: Board structure and committee effectiveness
2. **Risk Assessment**: Multi-frequency beta estimation
3. **Asset Pricing**: CAPM-based expected returns
4. **Capital Structure**: WACC optimization and leverage analysis
5. **Project Valuation**: DCF with sensitivity analysis

## 🔍 AI Integration

All AI-assisted analysis follows responsible practices:
- ✅ Theory-grounded interpretations
- ✅ Transparent assumptions
- ✅ Human oversight and validation
- ✅ Clear documentation
- ✅ Ethical accountability

## 📝 Data Sources

- **Market Data**: Yahoo Finance (via yfinance)
- **Corporate Data**: HCL Technologies Annual Reports
- **Analysis Period**: April 1, 2022 - March 28, 2025
- **Observations**: 739 daily data points

## 🎓 Academic Context

This dashboard was developed as part of the **Financial Management – Working With Artificial Intelligence** course project for analyzing HCL Technologies Limited.

**Project Focus Areas:**
- Corporate governance evaluation
- Risk-return trade-offs
- Cost of capital estimation
- Capital structure optimization
- Project-level investment appraisal

## ⚠️ Disclaimer

This dashboard employs AI-assisted analysis as a **decision-support tool**. All insights are grounded in financial theory and validated assumptions. Users should exercise professional judgment and consider qualitative factors beyond quantitative analysis.

## 📧 Support

For questions or issues, please refer to the project documentation in `FMWAI.md`.

---

**Academic Project** • HCL Technologies Limited • FY 2024-25
