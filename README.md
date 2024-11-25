# Trading Journal Project

An advanced Python-based trading journal designed to analyze and visualize trading data using concepts inspired by the **Wyckoff Method** and **Volume Spread Analysis (VSA)**. This app helps traders track their trades, detect market phases, and gain valuable insights into their performance.

---

## 🚀 Features

### 📊 Data Management
- Load trade data from CSV files.
- Save updated trade data to CSV files with error handling and logging.
- Fetch historical data via Yahoo Finance API using `yfinance`.

### 🧮 Wyckoff Phase Detection
- Detect trading phases such as **Accumulation**, **Distribution**, **Markup**, and **Markdown** using rolling averages.

### 📈 Volume Spread Analysis (VSA)
- Calculate price spreads for each trade.
- Detect potential VSA signals such as **High Volume Wide Spread** or **Low Volume Narrow Spread**.

### 📋 Performance Metrics (NEW 🚀)
- Calculate and display key trading performance metrics:
  - **Total Trades**
  - **Profitable Trades**
  - **Losing Trades**
  - **Win Rate (%)**
  - **Profit/Loss Ratio**
  - **Average Trade Duration (days)**

### 📊 Visualization
- Plot Entry and Exit Prices with:
  - Wyckoff phases annotated.
  - VSA signals displayed directly on the chart.
  - Dynamic and interactive visualizations.

### 🛠 Modular Design
- Simplified codebase with clear separation of concerns:
  - `app.py`: Main application runner.
  - `data_manager.py`: Data loading, saving, and fetching logic.
  - `phases.py`: Wyckoff phase detection logic.
  - `vsa.py`: Volume Spread Analysis logic.
  - `performance_metrics.py`: Metrics calculation logic (NEW 🚀).
  - `visualizations.py`: Plotting and visualization logic.

---

## 🧩 Folder Structure

```plaintext
trading-journal/
├── README.md                # Project documentation
├── app.py                   # Main script for running the app
├── data/                    # Local storage for trade and market data
│   └── example_trades.csv   # Example trade data file
├── tools/                   # Core logic and utilities
│   ├── __init__.py          # Makes 'tools' a Python module
│   ├── data_manager.py      # Data loading, saving, and fetching logic
│   ├── phases.py            # Wyckoff phase detection logic
│   ├── vsa.py               # Volume Spread Analysis logic
│   ├── performance_metrics.py  # Performance metrics calculation logic
│   └── visualizations.py    # Plotting and visualization logic
├── logs/                    # Centralized logging system
│   └── app.log              # Log file for the application
├── tests/                   # Unit tests for modules
│   ├── test_data_manager.py
│   ├── test_phases.py
│   ├── test_vsa.py
│   ├── test_metrics.py      # Tests for performance metrics (NEW 🚀)
│   └── test_visualizations.py
├── notebooks/               # Optional Jupyter notebooks for research
└── docs/                    # Documentation and guides
```

---

## ⚙️ How to Use

### Set Up Environment
1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/trading-journal.git
    cd trading-journal
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run Tests:
    ```bash
    pytest ./tests/
    ```

---

## 📈 Phase 1 Progress

### **Completed Tasks**
- Modularized code into distinct files (e.g., `data_manager.py`, `phases.py`, `vsa.py`, and `visualizations.py`).
- Implemented Wyckoff phase detection with rolling averages.
- Added logging across all modules for robust error handling.
- Integrated historical data fetching with `yfinance`.
- Built core performance metrics calculation and tests (NEW 🚀).
- Verified functionality with unit tests for all modules.
- Established a clean and extensible project structure.

---

## 🛣️ Next Steps in Phase 1
To ensure a solid foundation for the dashboard:
1. **Advanced Error Handling**:
   - Validate inputs (e.g., trade data format, historical data fetching).
   - Gracefully handle missing or incomplete data during metrics calculations.

2. **Visualization Enhancements**:
   - Add dynamic subplots for metrics visualization (e.g., profit/loss distribution, win rate trends).
   - Highlight key VSA signals on charts.

3. **Integration of Testing Coverage**:
   - Generate a code coverage report to identify untested areas.
   - Expand unit tests for edge cases (e.g., missing columns, unusual price movements).

4. **Data Validation Rules**:
   - Ensure all loaded data conforms to expected types and ranges.
   - Highlight inconsistencies in trade data for user correction.

5. **Profit/Loss Analysis**:
   - Introduce cumulative profit/loss graphs over time.
   - Add a rolling PnL feature for enhanced trend detection.

---

## 🌟 Phase 2: Coming Soon!
Once Phase 1 is complete, we’ll focus on:
1. Interactive dashboards for real-time performance monitoring.
2. Advanced analytics with dynamic filters.
3. Integration with live market data APIs for real-time insights.
