import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def show_insights():
    st.subheader("Dataset Info:")
    health_df = pd.read_csv('healthcare_data.csv')
    
    # Display info
    buffer = io.StringIO()
    health_df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    # Show stats
    st.subheader("Statistical Summary:")
    st.write(health_df.describe())

    st.subheader("Missing Values:")
    st.write(health_df.isnull().sum())

    # Histogram plot and save
    st.subheader("Distribution of Numeric Features:")
    fig1, ax = plt.subplots(figsize=(14, 10))
    health_df.hist(ax=ax, bins=25, color='skyblue', edgecolor='black')
    plt.tight_layout()
    fig1.savefig("histogram_plot.png")
    st.pyplot(fig1)

    # Correlation heatmap and save
    st.subheader("Correlation Heatmap:")
    fig2 = plt.figure(figsize=(12, 7))
    sns.heatmap(health_df.corr(), annot=True, cmap='coolwarm')
    plt.tight_layout()
    fig2.savefig("correlation_heatmap.png")
    st.pyplot(fig2)
