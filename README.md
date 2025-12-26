# 📈 Quantum Portfolio Optimizer

An advanced financial engineering tool that uses **Quantum Approximate Optimization Algorithms (QAOA)** to solve the Markowitz Mean-Variance optimization problem. This application fetches real-time market data and uses quantum interference to identify the most efficient asset allocation based on a user's risk appetite.

## 🌟 Features
- **Real-Time Data:** Integrates with `yfinance` to pull live stock and crypto performance.
- **Quantum Optimization:** Uses Qiskit's QAOA to navigate complex risk-reward landscapes.
- **Adjustable Risk Aversion:** A custom "Risk Appetite" slider that modifies the mathematical Hamiltonian in real-time.
- **Interactive Visualizations:** Heatmaps for asset correlation and normalized growth charts using Plotly.



## 🧠 How the Quantum Logic Works
1. **The Problem:** Selecting $k$ stocks from a list of $n$ to minimize risk $\sigma$ and maximize return $\mu$.
2. **The Mapping:** We convert the financial data into a **QUBO** (Quadratic Unconstrained Binary Optimization) problem.
3. **The Algorithm:** The QAOA algorithm places the qubits into a state of superposition representing all possible stock combinations. Through a series of gates, it amplifies the "probability" of the combination that represents the lowest cost (lowest risk).



## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
  git clone https://github.com/ARJose-cyber/-Quantum-Portfolio-Optimizer.git
   cd quantum-portfolio-optimizer
