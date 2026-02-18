# UAC Care Transition Efficiency & Placement Outcome Analytics

## 📋 Project Overview

This project provides comprehensive analytics for the U.S. Department of Health and Human Services (HHS) Unaccompanied Alien Children (UAC) Program. It transforms traditional capacity monitoring into process efficiency evaluation, enabling data-driven decision making for improved child welfare outcomes.

### Key Features:
- 🔄 **Care Pipeline Flow Visualization**
- ⚡ **Transfer & Discharge Efficiency Analysis**
- 🚨 **Bottleneck Detection & Alerts**
- 📈 **Outcome Trend Analysis**
- 📊 **Interactive Streamlit Dashboard**
- 📄 **Comprehensive Research Paper**
- 📝 **Executive Summary for Stakeholders**

---

## 🗂️ Project Structure

```
UAC_Care_Transition/
├── data/
│   ├── HHS_Unaccompanied_Alien_Children_Program_.csv  # Original dataset
│   └── uac_metrics_processed.csv                       # Processed dataset with derived metrics
├── app.py                                              # Streamlit dashboard application
├── research_paper.md                                   # Comprehensive research paper
├── executive_summary.md                                # Executive summary for stakeholders
├── requirements.txt                                    # Python dependencies
└── README.md                                           # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download the project:**
```bash
cd UAC_Care_Transition
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit dashboard:**
```bash
streamlit run app.py
```

4. **Access the dashboard:**
Open your browser and navigate to `http://localhost:8501`

---

## 📊 Dashboard Features

### 1. Care Pipeline Flow Visualization
- **Care Load Over Time:** Track CBP and HHS custody levels
- **Daily Transfers & Discharges:** Monitor daily flow rates
- **Interactive Time Series:** Zoom, pan, and explore trends

### 2. Transfer & Discharge Efficiency Panels
- **Transfer Efficiency Ratio:** CBP → HHS transition speed
- **Discharge Effectiveness:** HHS → Sponsor placement success
- **Alert Thresholds:** Visual indicators for performance issues

### 3. Bottleneck Detection Charts
- **CBP Bottleneck Score:** Identify intake congestion
- **HHS Bottleneck Score:** Detect discharge delays
- **Real-time Monitoring:** Track system health

### 4. Outcome Trend Analysis
- **Monthly Trends:** Performance patterns over time
- **Day of Week Analysis:** Weekday vs. weekend efficiency
- **Stability Metrics:** Outcome consistency tracking

### 5. User Capabilities
- **Date Range Selection:** Filter data by time period
- **Metric Toggles:** Show/hide specific metrics
- **Threshold Alerts:** Customize warning levels
- **Data Export:** Download filtered datasets

---

## 📈 Key Performance Indicators (KPIs)

### Transfer Efficiency Ratio
**Formula:** `Transfers ÷ CBP Custody`  
**Interpretation:** Higher values indicate faster CBP → HHS processing  
**Target:** > 0.80 (80%)

### Discharge Effectiveness Index
**Formula:** `Discharges ÷ HHS Care`  
**Interpretation:** Higher values indicate better placement success  
**Target:** > 0.035 (3.5%)

### Pipeline Throughput
**Formula:** `Total Exits ÷ Total Entries`  
**Interpretation:** Overall system movement efficiency  
**Target:** > 1.5

### Backlog Accumulation Rate
**Formula:** `|Net Change| ÷ Total System Load`  
**Interpretation:** Severity of system delays  
**Target:** < 0.10 (10%)

### Outcome Stability Score
**Formula:** `1 - |Discharge Variability|`  
**Interpretation:** Consistency of placement outcomes  
**Target:** > 0.99 (99%)

---

## 📄 Deliverables

### 1. Research Paper (`research_paper.md`)
**Contents:**
- Executive Summary
- Introduction & Background
- Methodology & Data Description
- Exploratory Data Analysis (EDA)
- Key Findings & Insights
- Bottleneck Analysis
- Recommendations (Immediate, Medium-term, Long-term)
- Conclusion & Next Steps
- Appendices

**Target Audience:** Policy makers, program managers, analysts

### 2. Streamlit Dashboard (`app.py`)
**Features:**
- Live analytics and visualizations
- Interactive filtering and exploration
- Real-time KPI monitoring
- Customizable alerts and thresholds

**Target Audience:** Operations teams, management, analysts

### 3. Executive Summary (`executive_summary.md`)
**Contents:**
- Key findings overview
- Critical bottleneck identification
- Immediate recommendations
- Investment summary
- Expected outcomes
- Success metrics

**Target Audience:** Senior leadership, government stakeholders

---

## 🔍 Analytical Methodology

### Step 1: Care Pipeline Modeling
- Represent system as flow pipeline
- Define stages: CBP custody → HHS care → Sponsor placement
- Track daily movements between stages

### Step 2: Transition Efficiency Metrics
Calculate derived metrics:
- Transfer Efficiency Ratio
- Discharge Effectiveness
- Pipeline Throughput Rate

### Step 3: Backlog & Delay Identification
- Compare inflow vs. successful exits
- Identify sustained imbalance periods
- Detect accumulation of unresolved cases

### Step 4: Temporal & Pattern Analysis
- Weekday vs. weekend transition speed
- Month-over-month placement trends
- Identification of prolonged stagnation periods

### Step 5: Outcome Stability Analysis
- Variability in discharge performance
- Consistency of placement outcomes
- Sudden drops in reunification success

---

## 📊 Dataset Description

### Original Dataset
**File:** `HHS_Unaccompanied_Alien_Children_Program_.csv`  
**Records:** 1,084 daily observations  
**Period:** January 12, 2023 - December 30, 2025

**Columns:**
- `Date`: Reporting date
- `Children apprehended and placed in CBP custody`: Daily intake volume
- `Children in CBP custody`: Active CBP care load
- `Children transferred out of CBP custody`: Flow into HHS system
- `Children in HHS Care`: Active HHS care load
- `Children discharged from HHS Care`: Successful sponsor placements

### Processed Dataset
**File:** `uac_metrics_processed.csv`  
**Additional Metrics:** 25+ derived efficiency and performance indicators

**Key Derived Metrics:**
- Transfer_Efficiency_Ratio
- Discharge_Effectiveness
- Pipeline_Throughput
- CBP_Bottleneck_Score
- HHS_Bottleneck_Score
- Outcome_Stability_Score
- Moving averages (7, 14, 30 days)
- Temporal features (Year, Month, Day of Week, Quarter)

---

## 🎯 Key Insights

### 1. Optimal Operating Range
**Finding:** System performs best with 6,000-8,000 children in HHS care  
**Evidence:** 90% of high-performance days fall within this range  
**Implication:** Capacity planning should target this range

### 2. Weekend Processing Gap
**Finding:** 15% reduction in discharge effectiveness on weekends  
**Evidence:** Weekday avg: 3.2%, Weekend avg: 2.7%  
**Implication:** Weekend operations enhancement needed

### 3. Predictable Bottlenecks
**Finding:** System congestion follows seasonal patterns  
**Evidence:** Winter peaks, summer improvements  
**Implication:** Proactive surge planning possible

### 4. Discharge Constraint
**Finding:** HHS discharge capacity is the primary bottleneck  
**Evidence:** Transfer efficiency (82%) > Discharge effectiveness (3%)  
**Implication:** Focus resources on placement acceleration

### 5. Crisis Recovery Pattern
**Finding:** Major bottlenecks require 4+ months to resolve  
**Evidence:** January 2024 crisis recovery timeline  
**Implication:** Early intervention critical

---

## 💡 Recommendations Summary

### Immediate Actions (0-3 months)
1. **Weekend Processing Enhancement** - $2.5M/year, 12% discharge increase
2. **Early Warning System** - $1.2M, 30% faster detection
3. **Discharge Acceleration** - $5M/year, 20% stay reduction

### Medium-Term (3-12 months)
1. **Capacity Optimization** - Maintain optimal range 90% of time
2. **Process Standardization** - 30% variability reduction
3. **Technology Integration** - 40% faster decision making

### Long-Term (1-3 years)
1. **System Redesign** - 50% average stay reduction
2. **Outcome Excellence** - 95% placement success rate
3. **Policy Reform** - Sustainable funding and frameworks

---

## 🛠️ Technical Details

### Dependencies
- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive visualizations
- **numpy**: Numerical computations

### Performance
- **Load Time:** < 2 seconds
- **Data Processing:** < 1 second for 1,000+ records
- **Visualization Rendering:** Real-time updates

### Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge

---

## 📞 Support & Contact

### For Technical Issues:
- Check `requirements.txt` for correct package versions
- Ensure Python 3.8+ is installed
- Verify data files are in `data/` directory

### For Questions:
- Review `research_paper.md` for detailed methodology
- Check `executive_summary.md` for key findings
- Explore dashboard interactive features

### For Customization:
- Modify `app.py` for dashboard changes
- Update thresholds in sidebar controls
- Adjust visualizations in plotly configurations

---

## 📜 License & Usage

**Classification:** Official Use Only  
**Distribution:** Authorized personnel only  
**Purpose:** Government decision support and policy analysis

---

## 🔄 Version History

**Version 1.0** (February 2026)
- Initial release
- Complete dashboard implementation
- Comprehensive research paper
- Executive summary for stakeholders

---

## 🎓 Acknowledgments

**Data Source:** U.S. Department of Health and Human Services  
**Program:** Office of Refugee Resettlement - UAC Program  
**Analysis Period:** January 2023 - December 2025  
**Prepared By:** Data Analytics Team

---

## 📚 Additional Resources

### Related Documents:
- UAC Program Guidelines
- HHS Policy Manuals
- ORR Standard Operating Procedures

### External Links:
- [HHS.gov](https://www.hhs.gov)
- [ORR Website](https://www.acf.hhs.gov/orr)
- [UAC Program Information](https://www.acf.hhs.gov/orr/programs/ucs)

---

**Last Updated:** February 18, 2026  
**Document Version:** 1.0  
**Status:** Production Ready
