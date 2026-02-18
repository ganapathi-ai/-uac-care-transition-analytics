import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="UAC Care Transition Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/uac_metrics_processed.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar
st.sidebar.title("🏥 UAC Care Transition Analytics")
st.sidebar.markdown("---")

# Date range selector
min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filter data
if len(date_range) == 2:
    mask = (df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))
    filtered_df = df[mask]
else:
    filtered_df = df

# Metric toggles
st.sidebar.markdown("### 📊 Metric Selection")
show_transfer = st.sidebar.checkbox("Transfer Efficiency", value=True)
show_discharge = st.sidebar.checkbox("Discharge Effectiveness", value=True)
show_throughput = st.sidebar.checkbox("Pipeline Throughput", value=True)

# Threshold alerts
st.sidebar.markdown("### ⚠️ Alert Thresholds")
transfer_threshold = st.sidebar.slider("Transfer Efficiency Alert", 0.0, 1.0, 0.5)
discharge_threshold = st.sidebar.slider("Discharge Effectiveness Alert", 0.0, 0.1, 0.03)

# Main content
st.title("🏥 Care Transition Efficiency & Placement Outcome Analytics")
st.markdown("### U.S. Department of Health and Human Services - UAC Program")
st.markdown("---")

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    avg_transfer = filtered_df['Transfer_Efficiency_Ratio'].mean()
    st.metric(
        "Avg Transfer Efficiency",
        f"{avg_transfer:.2%}",
        delta=f"{(avg_transfer - df['Transfer_Efficiency_Ratio'].mean()):.2%}"
    )

with col2:
    avg_discharge = filtered_df['Discharge_Effectiveness'].mean()
    st.metric(
        "Avg Discharge Effectiveness",
        f"{avg_discharge:.2%}",
        delta=f"{(avg_discharge - df['Discharge_Effectiveness'].mean()):.2%}"
    )

with col3:
    avg_throughput = filtered_df['Pipeline_Throughput'].mean()
    st.metric(
        "Avg Pipeline Throughput",
        f"{avg_throughput:.2f}",
        delta=f"{(avg_throughput - df['Pipeline_Throughput'].mean()):.2f}"
    )

with col4:
    avg_backlog = filtered_df['CBP_Bottleneck_Score'].mean()
    st.metric(
        "CBP Bottleneck Score",
        f"{avg_backlog:.3f}",
        delta=f"{(avg_backlog - df['CBP_Bottleneck_Score'].mean()):.3f}",
        delta_color="inverse"
    )

with col5:
    avg_stability = filtered_df['Outcome_Stability_Score'].mean()
    st.metric(
        "Outcome Stability",
        f"{avg_stability:.3f}",
        delta=f"{(avg_stability - df['Outcome_Stability_Score'].mean()):.3f}"
    )

st.markdown("---")

# Care Pipeline Flow Visualization
st.header("📊 Care Pipeline Flow Visualization")
col1, col2 = st.columns(2)

with col1:
    fig_pipeline = go.Figure()
    fig_pipeline.add_trace(go.Scatter(
        x=filtered_df['Date'], y=filtered_df['CBP_Custody'],
        name='CBP Custody', mode='lines', fill='tonexty',
        line=dict(color='#FF6B6B', width=2)
    ))
    fig_pipeline.add_trace(go.Scatter(
        x=filtered_df['Date'], y=filtered_df['HHS_Care'],
        name='HHS Care', mode='lines', fill='tonexty',
        line=dict(color='#4ECDC4', width=2)
    ))
    fig_pipeline.update_layout(
        title="Care Load Over Time",
        xaxis_title="Date",
        yaxis_title="Number of Children",
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig_pipeline, width='stretch')

with col2:
    fig_flow = go.Figure()
    fig_flow.add_trace(go.Scatter(
        x=filtered_df['Date'], y=filtered_df['Transferred_Out'],
        name='Transferred Out', mode='lines',
        line=dict(color='#95E1D3', width=2)
    ))
    fig_flow.add_trace(go.Scatter(
        x=filtered_df['Date'], y=filtered_df['Discharged'],
        name='Discharged', mode='lines',
        line=dict(color='#F38181', width=2)
    ))
    fig_flow.update_layout(
        title="Daily Transfers & Discharges",
        xaxis_title="Date",
        yaxis_title="Number of Children",
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig_flow, width='stretch')

# Transfer & Discharge Efficiency Panels
st.header("⚡ Transfer & Discharge Efficiency Analysis")
col1, col2 = st.columns(2)

with col1:
    if show_transfer:
        fig_transfer = go.Figure()
        fig_transfer.add_trace(go.Scatter(
            x=filtered_df['Date'],
            y=filtered_df['Transfer_Efficiency_Ratio'],
            mode='lines+markers',
            name='Transfer Efficiency',
            line=dict(color='#667EEA', width=2),
            marker=dict(size=4)
        ))
        fig_transfer.add_hline(
            y=transfer_threshold,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Alert Threshold ({transfer_threshold:.0%})"
        )
        fig_transfer.update_layout(
            title="Transfer Efficiency Ratio (CBP → HHS)",
            xaxis_title="Date",
            yaxis_title="Efficiency Ratio",
            yaxis_tickformat='.0%',
            height=400
        )
        st.plotly_chart(fig_transfer, width='stretch')

with col2:
    if show_discharge:
        fig_discharge = go.Figure()
        fig_discharge.add_trace(go.Scatter(
            x=filtered_df['Date'],
            y=filtered_df['Discharge_Effectiveness'],
            mode='lines+markers',
            name='Discharge Effectiveness',
            line=dict(color='#F093FB', width=2),
            marker=dict(size=4)
        ))
        fig_discharge.add_hline(
            y=discharge_threshold,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Alert Threshold ({discharge_threshold:.1%})"
        )
        fig_discharge.update_layout(
            title="Discharge Effectiveness (HHS → Sponsor)",
            xaxis_title="Date",
            yaxis_title="Effectiveness Ratio",
            yaxis_tickformat='.1%',
            height=400
        )
        st.plotly_chart(fig_discharge, width='stretch')

# Bottleneck Detection
st.header("🚨 Bottleneck Detection & Analysis")
col1, col2 = st.columns(2)

with col1:
    fig_cbp = px.area(
        filtered_df,
        x='Date',
        y='CBP_Bottleneck_Score',
        title='CBP Bottleneck Score (Higher = More Congestion)',
        color_discrete_sequence=['#FF6B6B']
    )
    fig_cbp.update_layout(height=400)
    st.plotly_chart(fig_cbp, width='stretch')

with col2:
    fig_hhs = px.area(
        filtered_df,
        x='Date',
        y='HHS_Bottleneck_Score',
        title='HHS Bottleneck Score (Higher = More Congestion)',
        color_discrete_sequence=['#4ECDC4']
    )
    fig_hhs.update_layout(height=400)
    st.plotly_chart(fig_hhs, width='stretch')

# Outcome Trend Analysis
st.header("📈 Outcome Trend Analysis")

tab1, tab2, tab3 = st.tabs(["Monthly Trends", "Day of Week Analysis", "Stability Metrics"])

with tab1:
    monthly_avg = filtered_df.groupby('Month_Name').agg({
        'Transfer_Efficiency_Ratio': 'mean',
        'Discharge_Effectiveness': 'mean',
        'Pipeline_Throughput': 'mean'
    }).reset_index()
    
    fig_monthly = go.Figure()
    fig_monthly.add_trace(go.Bar(
        x=monthly_avg['Month_Name'],
        y=monthly_avg['Transfer_Efficiency_Ratio'],
        name='Transfer Efficiency',
        marker_color='#667EEA'
    ))
    fig_monthly.add_trace(go.Bar(
        x=monthly_avg['Month_Name'],
        y=monthly_avg['Discharge_Effectiveness'],
        name='Discharge Effectiveness',
        marker_color='#F093FB'
    ))
    fig_monthly.update_layout(
        title="Monthly Average Performance Metrics",
        xaxis_title="Month",
        yaxis_title="Ratio",
        barmode='group',
        height=400
    )
    st.plotly_chart(fig_monthly, width='stretch')

with tab2:
    weekday_avg = filtered_df.groupby('Day_Name').agg({
        'Transfer_Efficiency_Ratio': 'mean',
        'Discharge_Effectiveness': 'mean',
        'Discharged': 'mean'
    }).reset_index()
    
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_avg['Day_Name'] = pd.Categorical(weekday_avg['Day_Name'], categories=day_order, ordered=True)
    weekday_avg = weekday_avg.sort_values('Day_Name')
    
    fig_weekday = px.line(
        weekday_avg,
        x='Day_Name',
        y=['Transfer_Efficiency_Ratio', 'Discharge_Effectiveness'],
        title='Weekday vs Weekend Performance',
        markers=True
    )
    fig_weekday.update_layout(height=400)
    st.plotly_chart(fig_weekday, width='stretch')

with tab3:
    fig_stability = go.Figure()
    fig_stability.add_trace(go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['Outcome_Stability_Score'],
        mode='lines',
        name='Outcome Stability',
        line=dict(color='#38B2AC', width=2),
        fill='tonexty'
    ))
    fig_stability.update_layout(
        title="Outcome Stability Score Over Time",
        xaxis_title="Date",
        yaxis_title="Stability Score",
        height=400
    )
    st.plotly_chart(fig_stability, width='stretch')

# Data Table
st.header("📋 Detailed Data View")
st.dataframe(
    filtered_df[['Date', 'CBP_Custody', 'HHS_Care', 'Transferred_Out', 'Discharged',
                 'Transfer_Efficiency_Ratio', 'Discharge_Effectiveness', 'Pipeline_Throughput']].tail(20),
    width='stretch'
)

# Footer
st.markdown("---")
st.markdown("""
**Data Source:** U.S. Department of Health and Human Services - UAC Program  
**Analysis Period:** {} to {}  
**Total Records:** {}
""".format(
    filtered_df['Date'].min().strftime('%Y-%m-%d'),
    filtered_df['Date'].max().strftime('%Y-%m-%d'),
    len(filtered_df)
))
