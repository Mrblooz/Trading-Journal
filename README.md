# **Trading Journal**

An advanced Python-based trading journal application focused on the **Wyckoff Method**. This tool allows traders to analyze performance, detect Wyckoff phases, and visualize their trading data with ease. Built to provide clarity and insights for both beginner and advanced traders.

---

# Trading Journal Application

An advanced Python-based trading journal designed to analyze and visualize trading data using concepts inspired by the Wyckoff Method and Volume Spread Analysis (VSA). The app helps traders track their trades, detect market phases, and gain insights into their performance.

---

## 🚀 Current Features

### 🛠 Core Features
1. **Data Management**:
   - Load trade data from CSV files.
   - Save updated trade data to CSV files.
   - Fetch historical data from Yahoo Finance.

2. **Analysis**:
   - Wyckoff Phase Detection:
     - Detects "Accumulation" and "Markup" phases using rolling averages.
   - Volume Spread Analysis (VSA):
     - Detects "High Volume Wide Spread" and "Low Volume Narrow Spread" signals.
     - Calculates price spreads for each trade.

3. **Visualization**:
   - Plots Entry and Exit Prices with:
     - Wyckoff phases annotated.
     - VSA signals displayed directly on the chart.

---

## 🧩 Folder Structure


Here’s how the project is organized:

```bash
trading-journal/ 
├── README.md # Project documentation 
├── app.py # Main script for running the app 
├── data/ # Local storage for trade and market data 
│ └── example_trades.csv # Example trade data file 
├── tools/ # Core logic and utilities 
│ ├── init.py # Makes 'tools' a Python module 
│ ├── data_manager.py # Data loading, saving, and fetching logic 
│ ├── analyzer.py # Wyckoff phase detection logic 
│ ├── vsa.py # Volume Spread Analysis (VSA) logic 
│ └── visualizations.py # Plotting and visualization logic 
├── tests/ # Unit tests for modules 
│ ├── test_data_manager.py 
│ ├── test_analyzer.py 
│ ├── test_vsa.py 
│ └── test_visualizations.py 
├── notebooks/ # Optional Jupyter notebooks for research 
└── docs/ # Documentation and guides
```

---

## **Roadmap**

### Phase 1: Foundation
- Load and manage CSV data.
- Perform Wyckoff analysis.
- Visualize results.

### Phase 2: Advanced Analytics
- Add Volume Spread Analysis (VSA).
- Improve visualizations with interactivity.

### Phase 3: Real-Time Data
- Integrate APIs for live market data.
- Provide AI-driven trade insights.

---


---

## 📋 What’s Next?

1. **Enhance Visualization**:
   - Add subplots for volume and profit/loss metrics.
   - Highlight VSA signals visually on the chart.

2. **Profit and Loss (PnL)**:
   - Calculate and visualize PnL for each trade.

3. **Expand VSA Logic**:
   - Add detection for "Climactic Action" and "Stopping Volume".

4. **Build Tests**:
   - Write unit tests for each module.

---

## 🛠 Technologies Used
- **Python** for core logic and data handling.
- **Matplotlib** for visualizations.
- **Pandas** for data processing.
- **Yahoo Finance API** via `yfinance` for fetching historical market data.
- **Pytest** for unit testing.

---

## 📖 Documentation
For detailed instructions and guides, check the `docs/` folder.
**Under Construction**

---

## ⚙️ How to Use

1. **Set Up Environment**:
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Application**:
   - Execute the app:
     ```bash
     python app.py
     ```

3. **Test the Modules**:
   - Run unit tests:
     ```bash
     pytest
     ```

---

## 📊 Sample Workflow

1. **Load Data**:
   - Reads trade data from `data/example_trades.csv`.

2. **Analyze Data**:
   - Detects Wyckoff phases (e.g., "Accumulation", "Markup").
   - Identifies VSA signals (e.g., "High Volume Wide Spread").

3. **Visualize Data**:
   - Generates a chart showing:
     - Entry and Exit Prices.
     - Phases annotated near Entry Prices.
     - VSA signals annotated directly on the chart.

---

## 🗂 Example CSV Structure
```csv
Date,Asset,High,Low,Entry Price,Exit Price,Volume,Phase 
2023-01-01,EUR/USD,1.25,1.20,1.2000,1.2500,100000,Undefined 
2023-01-02,EUR/USD,1.26,1.25,1.2500,1.2600,120000,Undefined 
2023-01-03,EUR/USD,1.24,1.23,1.2400,1.2300,130000,Undefined 
2023-01-04,EUR/USD,1.21,1.20,1.1200,1.2000,140000,Undefined 
2023-01-05,EUR/USD,1.19,1.18,1.1900,1.1000,150000,Undefined
```
---

## **Contributing**

We welcome contributions! Here’s how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Added feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## **License**

This project is licensed under the MIT License.

---

## **Contact**

For any questions or suggestions, please feel free to contact me at goliathnm@gmail.com*.

---
