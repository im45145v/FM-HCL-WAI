\thispagestyle{empty}

\begin{center}

\vspace*{2.5cm}

{\Large \textbf{Firm-Level and Project-Level Financial Analysis of HCL Technologies Limited Using Artificial Intelligence}}

\vspace{1.2cm}

{\large \textbf{Financial Management – Working With Artificial Intelligence}}

\vspace{2cm}

\textbf{Submitted by}

\vspace{0.5cm}

{\large Malla Venkata Sai Ashish}  

{\large Roll Number: B31-25}

\vspace{2cm}

\textbf{Institutional Term Project Submission}

\vfill

\textbf{Academic Year: 2024–25}

\end{center}

\newpage


## 1. Problem Identification

Large publicly listed firms operate in an environment characterised by market volatility, regulatory oversight, technological disruption, and evolving investor expectations. In such conditions, managerial decisions regarding **corporate governance, risk management, cost of capital, and capital investment** play a decisive role in value creation.

**For HCL Technologies Limited, a globally operating IT services firm, these challenges are amplified due to:** exposure to global economic cycles, reliance on knowledge-intensive human capital, rapid technological change,and increasing importance of digital and AI-led transformation.

**Traditional corporate finance analysis faces limitations in:** assessing governance quality quantitatively, capturing risk variation across time horizons, evaluating capital structure trade-offs, and appraising future-oriented investment projects under uncertainty.

**Artificial Intelligence offers tools to enhance financial analysis through:** efficient data processing, multi-frequency risk–return estimation, Scenario-based cost of capital analysis,and structured modelling of investment projects.

**Core Research Problem**

> How can Artificial Intelligence be responsibly and effectively used to support corporate finance decisions covering governance evaluation, risk–return analysis, cost of capital estimation, and capital investment appraisal while preserving managerial judgment, transparency, and ethical accountability?

## 2. Literature Review

Corporate finance theory provides the analytical foundation for understanding how firms create value through governance mechanisms, risk management, capital structure decisions, and capital investment choices. This section reviews the key theoretical concepts relevant to the study and justifies the analytical framework adopted.

**Corporate Governance and Firm Value**

The separation of ownership and control in modern corporations gives rise to agency problems between managers and shareholders (Jensen & Meckling, 1976). Corporate governance mechanisms such as board independence, specialised board committees, and transparent disclosures are designed to mitigate these agency conflicts.

Prior research indicates that strong governance structures are associated with: reduced agency costs, improved monitoring and accountability, lower information asymmetry,and reduced cost of capital.

Board-level committees, including audit, nomination and remuneration, and risk management committees, enhance governance quality by providing focused oversight in complex organisational environments. Effective governance is particularly critical for globally operating, knowledge-intensive firms such as IT services companies.

**Risk, Return, and Asset Pricing**

The risk–return trade-off is central to corporate finance and investment analysis. Modern Portfolio Theory (Markowitz, 1952) establishes that investors are compensated only for systematic risk, leading to equilibrium asset pricing models.

The Capital Asset Pricing Model (CAPM) (Sharpe, 1964; Lintner, 1965) links expected returns to systematic risk (beta) and remains widely used in practice for: estimating the cost of equity, evaluating investment projects, and benchmarking risk-adjusted performance.

However, empirical studies document limitations of CAPM, including:  instability of beta estimates across time horizons, low explanatory power, and inability to capture firm-specific and structural risks.

As a result, CAPM is best interpreted as a benchmark rather than a complete description of return behaviour.

**Capital Structure and Cost of Capital**

Modigliani and Miller (1958, 1963) demonstrate that in the presence of taxes, debt financing provides a tax shield that can enhance firm value. Subsequent trade-off theory suggests firms balance the tax benefits of debt against financial distress and agency costs to minimise WACC.

Empirical evidence shows that financially stable firms with predictable cash flows often operate with conservative leverage, prioritising flexibility and risk management over theoretical optimal leverage.

**Capital Investment and Project Evaluation**

Capital budgeting decisions rely on discounted cash flow (DCF) techniques, particularly Free Cash Flow to Firm (FCFF) valuation. The discount rate applied must reflect the systematic risk of the project rather than the firm’s existing capital structure.

When project-specific market data is unavailable, peer-based asset beta estimation is commonly used to assess business risk and derive an appropriate cost of equity.

**Role of Artificial Intelligence in Corporate Finance:** automated data processing, predictive modelling, scenario and sensitivity analysis, and decision-support systems.

**Justification of Analytical Framework**

- governance analysis to assess agency mitigation,
- multi-frequency risk–return estimation,
- CAPM-based cost of equity estimation with managerial interpretation,
- WACC and asset beta analysis for capital structure evaluation,
- project-level FCFF analysis using peer-based risk assessment.

## 3. AI Tools, Methodology, and Data Preparation

This project employs Artificial Intelligence (AI) strictly as a **decision-support tool** to enhance the rigour and efficiency of corporate finance analysis. AI is used selectively for structuring analysis, processing data, and supporting modelling, while all assumptions, validations, and interpretations remain under **human oversight**.

**3.1 Role of AI in the Project**

AI is utilised to structure complex financial analysis workflows, automate data collection and computation, estimate risk and cost of capital across scenarios, and support financial modelling and dashboard-based insights. AI is not used as a substitute for financial theory or managerial judgment, and all AI-generated outputs are critically evaluated before inclusion.

**3.2 Tools and Techniques Used**

| Tool / Technique            | Application                                              |
|----------------------------|----------------------------------------------------------|
| Large Language Models       | Structuring analysis and drafting interpretations         |
| Python (AI-assisted coding)| Data extraction, return computation, regression analysis |
| Statistical Libraries      | CAPM regression and beta estimation                      |
| Visualisation Tools        | Price trends and return distributions                    |
| Scenario Modelling         | Capital structure and project cash flow analysis         |

**3.3 Data Sources**

**Market Data**  
Market data for HCL Technologies Limited and the NIFTY 50 index was sourced from Yahoo Finance (via the `yfinance` library). The analysis covers the period from **01 April 2022 to 28 March 2025**, comprising **739 daily observations**. Adjusted closing prices were used to account for dividends and corporate actions.

**Corporate Disclosures**  
Annual Reports, Corporate Governance Reports, Board and Committee disclosures, and Notes to Financial Statements of HCL Technologies Limited were used for governance assessment, capital structure inputs, cost of debt estimation, and tax rate determination.

**3.4 Data Preparation Process**

Data preparation followed a structured process. Price series were first cleaned by removing missing observations and aligning stock and market data by date, resulting in a dataset with no missing values. Returns were then computed at daily, weekly (Friday-to-Friday), and monthly frequencies to capture time-horizon effects. Returns and volatility were annualised using standard financial conventions (252 trading days, 52 weeks, and 12 months). Excess returns were calculated using frequency-adjusted risk-free rates, and Ordinary Least Squares (OLS) regression was applied for CAPM estimation.

**3.5 Validation and Controls**

To ensure reliability and responsible AI usage, date ranges and return magnitudes were manually verified, summary statistics were reviewed for economic plausibility, and regression diagnostics (beta stability and R² values) were examined. No AI-generated output was accepted without independent validation.

**3.6 Data and Methodological Limitations**

The analysis is subject to limitations inherent in historical market data, which may not fully capture future risk dynamics. Beta estimates are sensitive to the chosen time period and frequency, and CAPM is a single-factor model with limited explanatory power. Project-level financials are based on assumptions and depend on execution quality. These limitations are explicitly acknowledged in the interpretation of results.

## 4. Analysis – Part A: Firm-Level Analysis  

## 4.1 Corporate Governance and Board Structure

HCL Technologies Limited follows a formal corporate governance framework aligned with SEBI (LODR) regulations and global best practices. The governance structure consists of shareholders, a Board of Directors responsible for strategic oversight, executive management responsible for operations, and specialised board-level committees providing focused supervision.

**Governance Impact on Firm Value:** reduction of agency costs, improved strategic oversight, enhanced risk monitoring, and increased investor confidence.

## 4.2 Board-Level Committees and Governance Role

- **Audit Committee:** Enhances financial reporting quality and internal control effectiveness, reducing information asymmetry.
- **Nomination and Remuneration Committee:** Aligns executive compensation with performance and ensures leadership continuity.
- **Risk Management Committee:** Oversees financial, operational, cyber, and strategic risks, stabilising cash flows.
- **CSR and ESG Committees:** Support sustainability and stakeholder trust, reducing long-term reputational risk.

## 4.3 Risk and Return Characteristics of Equity

Equity returns were analysed using adjusted closing prices for the period 01 April 2022 to 28 March 2025.

**Unannualised Returns & Annualised Risk–Return Profile**

| Frequency | Mean Return | Standard Deviation | Annualised Return | Annualised Volatility |
| --------- | ----------- | ------------------ | ----------------- | --------------------- |
| Daily     | 0.0695%     | 1.45%              | 17.51%            | 23.02%                |
| Weekly    | 0.33%       | 3.17%              | 17.16%            | 22.85%                |
| Monthly   | 1.64%       | 6.51%              | 19.70%            | 22.54%                |

**Interpretation:** Annualised volatility remains stable across frequencies, indicating consistent systematic risk exposure. Monthly returns exhibit higher variability due to aggregation effects and fewer observations. Overall, the risk profile suggests predictable cash flows and operational resilience.

## 4.4 Expected Returns Using CAPM

CAPM regressions were estimated using the NIFTY 50 index as the market proxy and a 6% annual risk-free rate.

**CAPM Regression Results & Expected Returns (per period)**

| Frequency | Beta | R²   | Expected Return |
| --------- | ---- | ---- | --------------- |
| Daily     | 0.87 | 0.25 | 0.0397%         |
| Weekly    | 0.82 | 0.20 | 0.1830%         |
| Monthly   | 0.71 | 0.18 | 0.8411%         |

**Interpretation:** Equity beta for HCL Technologies remains below one across all frequencies, with values of 0.87 (daily), 0.82 (weekly), and 0.71 (monthly), indicating lower sensitivity to market movements compared to the overall market. The declining beta at lower frequencies reflects reduced short-term noise and a stronger influence of firm fundamentals. The relatively low R² values, ranging from 18% to 25%, highlight the limited explanatory power of CAPM and suggest that firm-specific factors such as governance quality, execution capability, and client diversification play a significant role in return behaviour.


## 4.5 Capital Structure and Cost of Capital

**Cost of Debt**

- Pre-tax cost of debt: **7.5%**
- After-tax cost of debt: **5.625%**
- This reflects a conservative borrowing assumption under prevailing interest rate conditions.

**Current WACC**
Using observed capital structure weights and CAPM-based cost of equity:

\[
WACC_{Current} = 10.04\%
\]

## 4.6 Asset Beta Estimation

To isolate business risk, equity beta was adjusted assuming a neutral baseline capital structure.

| Metric      | Daily | Weekly | Monthly |
| ----------- | ----- | ------ | ------- |
| Equity Beta | 0.87  | 0.82   | 0.71    |
| Asset Beta  | 0.84  | 0.79   | 0.68    |

## 4.7 Relevering and Target Capital Structure

Assuming a target capital structure of 25% debt and 75% equity, asset betas were relevered.

| Metric                | Daily | Weekly | Monthly |
|-----------------------|-------|--------|---------|
| Relevered Equity Beta | 1.05  | 0.99   | 0.85    |

**Revised WACC**

\[
WACC_{Target} = 8.93%
\]


**Strategic Implications:** Relevering the firm to a target capital structure of 25% debt and 75% equity increases equity beta but results in a lower overall cost of capital.The reduction in WACC from 10.04% to approximately 8.93% indicates potential value creation through moderate leverage, even under conservative borrowing cost assumptions. While higher leverage increases equity risk, the firm’s stable cash flows and strong governance framework suggest that this additional risk remains manageable. The analysis implies that HCL Technologies is conservatively financed and may be under-levered relative to its risk profile.


## 5. Analysis – Part B: Project-Level Analysis  

> Project: AI-Driven Autonomous Enterprise IT Operations (AIOps) Platform

## 5.1 Project Description and Economic Rationale

The proposed project involves developing an **AI-driven Autonomous IT Operations (AIOps) platform** for large enterprises managing complex hybrid and multi-cloud environments. The platform integrates infrastructure telemetry, application performance data, and system logs, applying machine learning and large language models (LLMs) for anomaly detection, predictive incident management, and automated root-cause analysis.

**Economic Rationale**
Enterprises increasingly face high IT complexity, operational downtime costs, and shortages of skilled DevOps and Site Reliability Engineers (SREs). The proposed platform addresses these challenges by reducing incident response time, improving system reliability, and lowering operating costs. The project follows a **subscription-based SaaS model**, enabling recurring revenues and scalability.

## 5.2 Investment and Operating Assumptions

| Dimension          | Assumption                        | Rationale                        |
| ------------------ | --------------------------------- | -------------------------------- |
| Revenue Model      | Enterprise SaaS subscriptions     | Industry standard                |
| Growth Profile     | Rapid early-stage adoption        | Driven by digital transformation |
| Cost Structure     | High fixed R&D, low marginal cost | AI software economics            |
| Capital Intensity  | Asset-light                       | Cloud-based delivery             |
| Operating Leverage | Increases with scale              | Fixed costs amortised            |

## 5.3 Pro-Forma Financial Performance

A five-year pro-forma model was developed to estimate operating performance and cash flows.

**Pro-Forma Summary (Crore)**

| Year | Revenue | EBITDA | EBIT   | NOPAT  | Capex | FCFF  |
| ---- | ------- | ------ | ------ | ------ | ----- | ----- |
| 1    | 150.00  | 30.00  | 22.50  | 16.88  | 12.00 | 12.38 |
| 2    | 195.00  | 48.75  | 39.00  | 29.25  | 15.60 | 23.40 |
| 3    | 253.50  | 76.05  | 63.38  | 47.53  | 20.28 | 39.93 |
| 4    | 329.55  | 115.34 | 98.86  | 74.15  | 26.36 | 64.26 |
| 5    | 428.42  | 171.37 | 149.95 | 112.46 | 34.27 | 99.61 |

**Interpretation:** The pro-forma financial projections indicate strong revenue growth from INR 150 crore in Year 1 to INR 428.42 crore in Year 5, reflecting increasing enterprise adoption of the AIOps platform. EBITDA and EBIT margins expand over time due to operating leverage inherent in scalable software businesses. Free Cash Flow to Firm (FCFF) increases from INR 12.38 crore in Year 1 to INR 99.61 crore in Year 5, demonstrating significant long-term value creation. Capital expenditure remains modest relative to revenue, confirming the asset-light nature of the project.


## 5.4 Peer Identification for Risk Assessment

Since the project is not independently listed, project risk is assessed using comparable firms operating in enterprise IT services, cloud platforms, and AI-enabled operations. These peers share similar exposure to enterprise demand cycles, technology risk, and innovation intensity.

## 5.5 Estimation of Project Asset Beta

**Methodology**

1. Peer equity betas were estimated using historical market data.
2. Equity betas were unlevered to remove capital structure effects.
3. A weighted average of peer asset betas was computed.

**Result**
\[
\boxed{\text{Project Asset Beta} = 0.849}
\]

**Interpretation of Project Risk:** The estimated project asset beta of 0.849 indicates moderate systematic business risk. This level of risk is lower than the overall market but higher than traditional IT outsourcing services, reflecting the project’s exposure to technology adoption cycles and innovation risk. At the same time, recurring enterprise subscriptions, high switching costs, and the asset-light operating model contribute to risk stability. The asset beta is therefore appropriate for evaluating the project’s cash flows using an unlevered cost of equity.


## 5.6 Cost of Equity and Capital Budgeting

The project’s cost of equity is estimated using CAPM with the asset beta, reflecting an all-equity financed project:

\[
K_e = R_f + \beta_A (R_m - R_f)
\]

where \( R_f \) denotes the risk-free rate (6%) and \( \beta_A \) represents the asset beta (0.849).


This unlevered cost of equity is used to discount **Free Cash Flow to Firm (FCFF)**, ensuring that project evaluation reflects intrinsic business risk rather than the firm’s existing financing structure.

## 6. Managerial Interpretation and Recommendations

**6.1 Managerial Interpretation – Firm Level**

The firm-level analysis of HCL Technologies Limited highlights the importance of governance quality, disciplined risk management, and capital structure decisions in value creation.

**Governance and Oversight**  
The presence of an independent board supported by specialised committees strengthens monitoring, reduces agency conflicts, and enhances investor confidence. For a globally operating IT services firm, strong governance mitigates regulatory, operational, and reputational risks, thereby supporting valuation stability.

**Risk Profile and Market Behaviour**  
HCL Technologies exhibits a defensive risk profile, with equity beta remaining below one across daily (0.87), weekly (0.82), and monthly (0.71) frequencies. Annualised volatility remains stable at approximately 22–23%, indicating predictable cash flows and operational resilience. The relatively low explanatory power of CAPM regressions (R² between 18% and 25%) suggests that firm-specific fundamentals play a significant role beyond market movements.

**Capital Structure Implications**  
The current WACC of 10.04% reflects a conservative financing strategy based on an effectively equity-financed structure. Simulation of a moderate leverage structure (25% debt) reduces WACC to approximately 8.93%, indicating that the firm may be under-levered. While leverage increases equity risk, the overall firm value improves due to the lower cost of capital.

**6.2 Managerial Interpretation – Project Level**

The proposed AI-driven AIOps platform represents a future-oriented investment aligned with enterprise digital transformation trends.

**Financial Viability**  
Pro-forma financials indicate strong revenue growth, expanding margins, and rapidly increasing Free Cash Flow to Firm (FCFF), rising from INR 12.38 crore in Year 1 to INR 99.61 crore in Year 5. The asset-light nature of the project enables high operating leverage and scalability.

**Risk Assessment and Capital Budgeting**  
The estimated project asset beta of 0.849 indicates moderate systematic risk—lower than the market but higher than traditional IT services. Using the unlevered cost of equity derived from this asset beta ensures that capital budgeting decisions reflect intrinsic project risk rather than the firm’s existing financing structure.

**6.3 Recommendations and Implementation**

**Recommendation 1: Strengthen Governance Framework**  
HCL Technologies should continue regular board and committee evaluations, with increased focus on oversight of technology, cyber, and AI-related risks. This will sustain investor confidence, improve monitoring effectiveness, and lower governance-related risk premiums.

**Recommendation 2: Optimise Capital Structure Through Moderate Leverage**  
The firm should consider introducing moderate levels of low-cost, long-term debt aligned with its stable cash flows. This can reduce WACC from 10.04% to approximately 8.93%, thereby enhancing shareholder value without materially increasing financial risk.

**Recommendation 3: Adopt Multi-Dimensional Risk Assessment**  
Management should complement market-based risk measures such as CAPM beta with project-specific and qualitative risk analysis. AI-enabled dashboards can be used to monitor risk across time horizons, improving the quality of strategic decision-making.

**Recommendation 4: Implement the AIOps Project in Phases**  
The AI-driven AIOps platform should be deployed in a phased manner, beginning with pilot implementations for select enterprise clients. Scaling should be linked to clearly defined performance milestones, limiting downside risk while capturing long-term upside.

**Recommendation 5: Institutionalise Responsible AI Use**  
The firm should formalise guidelines for AI usage in financial analysis, ensuring transparency, validation of AI-generated outputs, and human-in-the-loop oversight. This will enhance analytical efficiency while mitigating ethical, legal, and reputational risks.

## 7. Ethical and Responsible AI Considerations

**Data Privacy and Confidentiality**

All data used in this project was sourced exclusively from publicly available market databases and corporate disclosures. No personal, confidential, or proprietary information was accessed at any stage. Project-level financial data was model-generated and clearly disclosed as such. This approach ensures compliance with data privacy norms, institutional guidelines, and academic integrity requirements.

**Bias and Model Limitations**

Market-based financial models such as the Capital Asset Pricing Model (CAPM) rely on historical data and may reflect structural biases present in financial markets. Beta estimates are sensitive to the chosen time horizon and estimation window, while peer-based asset beta estimation involves an element of subjective judgment. These risks were mitigated by analysing risk across multiple frequencies, using asset beta rather than raw equity beta for project evaluation, and explicitly acknowledging model limitations in interpretation and conclusions.

**Risk of AI Hallucination and Over-Reliance**

AI tools can generate outputs that appear plausible but may be incorrect if accepted without scrutiny. To address this risk, all AI-generated outputs were manually verified, numerical results were cross-checked against established financial theory, and AI was used strictly as a decision-support tool rather than a decision-maker.

**Transparency and Accountability**

Transparency and accountability were ensured by documenting all AI usage in a dedicated Prompt Logbook. Assumptions, modelling choices, and limitations are explicitly disclosed throughout the report. Final responsibility for analysis, interpretation, and conclusions rests entirely with the student, ensuring clear human accountability in AI-assisted work.

## 8. Conclusion

This project demonstrates how Artificial Intelligence can be responsibly integrated into corporate finance analysis to support decision-making at both the firm and project levels.

The firm-level analysis of HCL Technologies Limited highlights the role of strong governance, defensive risk characteristics, and disciplined capital structure decisions in value creation. The project-level evaluation of an AI-driven AIOps platform illustrates how future-oriented investments can be appraised using AI-assisted financial modelling while maintaining managerial judgment.

By combining financial theory, empirical data, and AI-enabled analytics within a transparent and ethical framework the study provides a structured approach to value-oriented, responsible financial decision-making in an increasingly AI-driven business environment.

\newpage
## 9. Annexures

- **Annexure A:** Prompt Logbook and AI Justification
- **Annexure B:** Python Code Files and Computational Outputs
- **Annexure C:** Financial Model Tables and Cash Flow Outputs
- **Annexure D:** [Streamlit Dashboard for Insights](https://hcl-tech.streamlit.app/): https://hcl-tech.streamlit.app/
- **Annexure E:** Visualisations and Screenshots
- **Annexure F:** Presentation Deck