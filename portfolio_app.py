import streamlit as st
import plotly.express as px
from optimizer import solve_portfolio_quantum

st.set_page_config(page_title="Quantum Portfolio Pro", page_icon="📈", layout="wide")

st.title("📈 Quantum Portfolio Optimizer")
st.markdown("---")

# --- Sidebar Configuration ---
st.sidebar.header("User Settings")
tickers_input = st.sidebar.text_input("Stocks (comma separated)", "AAPL, MSFT, NVDA, TSLA, BTC-USD, GOLD")
tickers = [t.strip().upper() for t in tickers_input.split(",")]

budget = st.sidebar.number_input("Stocks to Select", min_value=1, max_value=len(tickers), value=2)

risk_appetite = st.sidebar.select_slider(
    "Risk Tolerance", 
    options=["Aggressive", "Moderate", "Conservative"],
    value="Moderate"
)

# Mapping UI to Math
risk_map = {"Aggressive": 0.1, "Moderate": 0.5, "Conservative": 2.0}
q_factor = risk_map[risk_appetite]

# --- Main Dashboard ---
if st.button("🚀 Run Quantum Optimization"):
    with st.spinner("Executing QAOA on Quantum Simulator..."):
        try:
            # Run the engine
            result, price_data = solve_portfolio_quantum(tickers, budget, q_factor)
            
            # Display Recommendations
            st.subheader("🎯 Optimal Selection")
            selected_stocks = [tickers[i] for i, val in enumerate(result.x) if val > 0.5]
            
            cols = st.columns(len(selected_stocks))
            for idx, stock in enumerate(selected_stocks):
                cols[idx].metric(f"Asset {idx+1}", stock)

            # --- Visualizations ---
            st.markdown("---")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("### Normalized Price Growth")
                # Normalize to 100 for better comparison
                normalized_df = (price_data / price_data.iloc[0] * 100)
                fig_line = px.line(normalized_df, title="1-Year Growth Comparison")
                st.plotly_chart(fig_line, use_container_width=True)

            with col2:
                st.write("### Risk Heatmap (Covariance)")
                corr = price_data.pct_change().corr()
                fig_heat = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r')
                st.plotly_chart(fig_heat, use_container_width=True)

        except Exception as e:
            st.error(f"Error during optimization: {e}")

else:
    st.info("Adjust the sidebar settings and click 'Run' to see the quantum selection.")
