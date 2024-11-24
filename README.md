
# Trading Journal Project

An advanced Python-based trading journal designed to analyze and visualize trading data using concepts inspired by the Wyckoff Method and Volume Spread Analysis (VSA). The app helps traders track their trades, detect market phases, and gain insights into their performance.

---

## 🚀 Features

### 📊 Data Management
- Load trade data from CSV files with validation and error handling.
- Save processed trade data to CSV files with logging for operations.
- Fetch historical data via Yahoo Finance API using `yfinance`.

### 🧮 Wyckoff Phase Detection
- Detect trading phases such as **Accumulation**, **Distribution**, **Markup**, and **Markdown** using rolling averages.

### 📈 Volume Spread Analysis (VSA)
- Calculate price spreads for each trade.
- Detect VSA signals such as **High Volume Wide Spread** and **Low Volume Narrow Spread**.

### 📊 Visualization
- Plot Entry and Exit Prices with:
  - Wyckoff phases annotated.
  - VSA signals displayed directly on the chart.
- Generate clear and dynamic visualizations for insights.

### 📋 Performance Metrics
- **Coming Soon**: Calculate and visualize:
  - Profit and Loss (PnL) per trade.
  - Cumulative PnL over time.
  - Key performance metrics like Win Rate and Risk/Reward Ratio.

### 🛠 Modular Design
- Simplified, scalable codebase with a clear separation of concerns:
  - `app.py`: Main application runner.
  - `data_manager.py`: Handles data loading, saving, and validation.
  - `phases.py`: Wyckoff phase detection logic.
  - `vsa.py`: Volume Spread Analysis logic.
  - `visualizations.py`: Plotting and visualization logic.

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/trading-journal.git
   cd trading-journal
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests to ensure everything is working:
   ```bash
   pytest ./tests/
   ```

---

## ⚙️ Logging System

### Key Features:
- Centralized logging for the entire application.
- Logs written to both the console and a file (`logs/app.log`).
- Supports `INFO`, `DEBUG`, `WARNING`, `ERROR`, and `CRITICAL` levels.
- Exception stack traces are logged for debugging.

### Example Log Output:
```
INFO - Starting Trading Journal Application...
INFO - Loading data from: data/example_trades.csv
ERROR - Failed to load data. File not found: data/example_trades.csv
```

### How to Use:
- Set up a logger in any module:
  ```python
  from logs.setup_logging import setup_logger
  logger = setup_logger("ModuleName")
  logger.info("Message here")
  ```

---

## 🧩 Folder Structure

```plaintext
trading-journal/
├── README.md                # Project documentation
├── app.py                   # Main script for running the app
├── data/                    # Local storage for trade and market data
│   └── example_trades.csv   # Example trade data file
├── logs/                    # Centralized logging
│   ├── setup_logging.py     # Logger setup
│   └── app.log              # Application logs
├── tools/                   # Core logic and utilities
│   ├── __init__.py          # Makes 'tools' a Python module
│   ├── data_manager.py      # Data loading, saving, and validation
│   ├── phases.py            # Wyckoff phase detection logic
│   ├── vsa.py               # Volume Spread Analysis logic
│   └── visualizations.py    # Visualization and plotting logic
├── tests/                   # Unit tests for modules
│   ├── test_data_manager.py
│   ├── test_phases.py
│   ├── test_vsa.py
│   └── test_visualizations.py
├── notebooks/               # Optional Jupyter notebooks for research
└── docs/                    # Documentation and guides
```

---

## ⚡ Roadmap

### **Phase 1: Foundation (Completed)**
- Implement data management, Wyckoff phase detection, VSA logic, and visualizations.
- Build a centralized logging system.

### **Phase 2: Advanced Analytics**
- Implement performance metrics:
  - Profit and Loss (PnL).
  - Win Rate and Risk/Reward Ratios.
  - Cumulative PnL over time.
- Add interactive and dynamic visualizations.

### **Phase 3: Interactive Dashboard**
- Integrate `Dash` or `Streamlit` for a web-based trading journal dashboard.
- Enable real-time updates and interactivity.

---

## 🛠 Technologies Used

- **Python**: Core programming language.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Data visualization.
- **Logging**: Centralized logging for debugging and monitoring.
- **Yahoo Finance API**: Fetching historical market data.
- **Pytest**: Unit testing framework.

---

## 📬 Contact

For any questions or suggestions, feel free to contact me at **goliathnm@gmail.com**.

---

Enjoy using and improving the Trading Journal! 🚀
