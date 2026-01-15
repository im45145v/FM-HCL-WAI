# 🚀 Quick Start Guide

## Launch the Dashboard (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Dashboard
```bash
streamlit run app.py
```

### Step 3: Open in Browser
The dashboard will automatically open at: `http://localhost:8501`

---

## 📱 Using the Dashboard

### Navigation
Use the **sidebar radio buttons** to navigate between pages:
- 🏠 Executive Summary → Overview & key metrics
- 📈 Market Analysis → Price trends & returns
- ⚖️ Risk & Return → CAPM & beta analysis
- 💰 Capital Structure → WACC & leverage
- 🚀 Project Valuation → NPV & investment decision

### Interactive Controls

#### Return Frequency
Switch between **Daily**, **Weekly**, or **Monthly** analysis using the sidebar dropdown.

#### What-If Scenarios
Adjust these sliders to see real-time impacts:
- **Target Debt %**: Change capital structure (0-40%)
- **Cost of Debt**: Modify borrowing assumptions (4-12%)

Watch the WACC, NPV, and capital structure charts update automatically!

---

## 💡 Key Features to Showcase

### 1. Executive Summary (🏠)
- **5 KPI Metrics** at the top
- **Risk Gauge** showing defensive beta
- **Strategic Insights** cards (color-coded)
- **Mini price chart** for context

### 2. Market Analysis (📈)
- **Dual-axis chart**: HCL vs NIFTY 50
- **Return distributions**: Histogram & box plots
- **Cumulative performance**: Track over time

### 3. Risk & Return (⚖️)
- **Multi-frequency comparison**: Daily/Weekly/Monthly
- **CAPM scatter plot** with regression line
- **Beta stability** across time horizons

### 4. Capital Structure (💰)
- **WACC comparison**: Current vs Target
- **Capital structure pies**: Visual breakdown
- **Beta transformation**: Equity → Asset → Relevered
- **Sensitivity chart**: WACC vs Debt %

### 5. Project Valuation (🚀)
- **Revenue & FCFF projections**: 5-year trajectory
- **Margin analysis**: EBITDA/EBIT/NOPAT trends
- **NPV waterfall**: Value buildup visualization
- **Investment recommendation**: Accept/Reject

---

## 🎯 Tips for Presentation

### For Impact:
1. **Start Big**: Open with Executive Summary KPIs
2. **Show Interactivity**: Adjust what-if sliders live
3. **Explain Visuals**: Hover over charts to show tooltips
4. **Tell Story**: Flow from firm → risk → structure → project

### For Viva/Defense:
1. **CAPM Deep-Dive**: Go to Risk & Return page, explain beta
2. **Capital Structure**: Show WACC optimization logic
3. **Project NPV**: Walk through waterfall chart
4. **Sensitivity**: Demonstrate discount rate impact

### Pro Tips:
- Use **fullscreen mode** (F11) for presentations
- Keep sidebar expanded to show controls
- Hover over charts to highlight interactivity
- Switch frequencies to show consistency

---

## ⚙️ Troubleshooting

### Dashboard won't start?
```bash
# Install/update dependencies
pip install --upgrade -r requirements.txt
```

### Missing data error?
Ensure `FMWAI_Analysis.xlsx` is in the same folder as `app.py`

### Charts not showing?
- Check console for errors
- Verify all required sheets exist in Excel file
- Restart the dashboard

### Slow performance?
- First load is slower (data caching)
- Subsequent page changes are fast
- Reduce data size if needed

---

## 📊 Data Requirements

The Excel file must contain these sheets:
- ✅ Data
- ✅ Returns_Daily
- ✅ Returns_Weekly  
- ✅ Returns_Monthly
- ✅ Risk_Return_Summary
- ✅ CAPM_Regression
- ✅ CAPM_Expected_Returns
- ✅ Capital_Structure_WACC
- ✅ Beta_Adjustments
- ✅ Project_Financials
- ✅ Project_Risk

---

## 🎨 Customization Ideas

### Change Colors
Edit the custom CSS in `app.py` (lines 20-45):
```python
background: linear-gradient(90deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
```

### Add Your Logo
Replace the placeholder image URL in sidebar:
```python
st.sidebar.image("YOUR_LOGO_URL", use_container_width=True)
```

### Modify What-If Ranges
Adjust slider parameters:
```python
debt_pct = st.sidebar.slider("Target Debt %", MIN, MAX, DEFAULT, step=STEP)
```

---

## 📚 Learning Resources

### Understanding the Analysis:
- Read `FMWAI.md` for theoretical background
- Review `IMPROVEMENTS.md` for enhancement details
- Check `README.md` for full documentation

### Streamlit Documentation:
- [Official Docs](https://docs.streamlit.io)
- [Gallery](https://streamlit.io/gallery)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

---

## 🆘 Getting Help

### Common Questions:

**Q: How do I export charts?**  
A: Hover over any Plotly chart → Click camera icon → Save as PNG

**Q: Can I change the date range?**  
A: Update the Excel file with new data, dashboard auto-refreshes

**Q: How do I share this?**  
A: Deploy to Streamlit Cloud (free) or run on local network

**Q: Where are calculations done?**  
A: In Python/pandas → Excel → Dashboard (separation of concerns)

---

## ✅ Pre-Presentation Checklist

- [ ] Dashboard launches without errors
- [ ] All 5 pages load correctly
- [ ] What-if sliders work smoothly
- [ ] Charts are interactive (hover works)
- [ ] Data is up-to-date
- [ ] Internet connection (for fonts/icons)
- [ ] Backup plan (screenshots/video)
- [ ] Practiced navigation flow

---

## 🎓 Academic Integrity Note

This dashboard uses **AI-assisted analysis** responsibly:
- All insights grounded in financial theory
- Transparent assumptions documented
- Human oversight on all interpretations
- Ethical accountability maintained

**Remember**: The dashboard is a **decision-support tool**, not a replacement for professional judgment.

---

**Status**: Ready for Production ✅  
**Version**: 2.0 (Enhanced)  
**Last Updated**: 2025  

Good luck with your presentation! 🚀
