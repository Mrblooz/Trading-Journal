
# 📘 **Trading Journal**

An advanced Python-based trading journal designed to analyze and visualize trading data using concepts inspired by the **Wyckoff Method** and **Volume Spread Analysis (VSA)**. This application helps traders track their trades, detect market phases, and gain valuable insights into their performance.

---

## 🚀 **Features**

✅ **Data Management**  
- Load trading data from CSV files.  
- Save updated trading data with error handling and logging.  
- Fetch historical data via the Yahoo Finance API (*yfinance*).  

✅ **Wyckoff Phase Detection**  
- Identify market phases such as:  
  - *Accumulation*  
  - *Distribution*  
  - *Markup*  
  - *Markdown*  
- Utilize rolling averages and price action for detection.

✅ **Volume Spread Analysis (VSA)**  
- Calculate price spreads for each trade.  
- Detect critical VSA signals such as:  
  - "High Volume Wide Spread"  
  - "Low Volume Narrow Spread"  

✅ **Visualization**  
- Plot entry and exit prices with:  
  - Annotations for Wyckoff phases.  
  - VSA signals directly displayed on the chart.  
  - Dynamic and interactive visualizations.  

✅ **Modular Design**  
- Structured and clean codebase:  
  - **`app.py`**: Main application.  
  - **`data_manager.py`**: Data loading, saving, and fetching.  
  - **`phases.py`**: Wyckoff phase detection.  
  - **`vsa.py`**: Volume Spread Analysis logic.  
  - **`visualizations.py`**: Plotting and visualizations.

---

## 🗂 **Folder Structure**

```plaintext
trading-journal/
├── README.md                # Project documentation
├── app.py                   # Main application
├── data/                    # Local storage for data
│   └── example_trades.csv   # Example trading file
├── tools/                   # Core logic and utilities
│   ├── __init__.py          # Module initializer
│   ├── data_manager.py      # Data management
│   ├── phases.py            # Wyckoff phase detection
│   ├── vsa.py               # VSA logic
│   └── visualizations.py    # Visualizations
├── tests/                   # Unit tests
│   ├── test_data_manager.py
│   ├── test_phases.py
│   ├── test_vsa.py
│   └── test_visualizations.py
├── notebooks/               # Optional Jupyter notebooks
└── docs/                    # Documentation and guides
```

---

## 🛠 **Installation**

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourUsername/trading-journal.git
   cd trading-journal
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests**  
   ```bash
   pytest ./tests/
   ```

---

## ⚙️ **How to Use**

1. **Set up the environment**  
   Install dependencies as described above.

2. **Run the application**  
   Start the app:  
   ```bash
   python app.py
   ```

3. **Provide your data**  
   Place your trading data CSV in the `/data` folder.  
   Ensure it follows the correct structure (see sample below).

4. **View results**  
   Processed data and visualizations will be saved in the output folder.

---

## 📊 **Sample CSV Structure**

| Date       | Asset   | High  | Low   | Entry Price | Exit Price | Volume  | Phase     |
|------------|---------|-------|-------|-------------|------------|---------|-----------|
| 2023-01-01 | EUR/USD | 1.25  | 1.20  | 1.2000      | 1.2500     | 100000  | Undefined |
| 2023-01-02 | EUR/USD | 1.26  | 1.25  | 1.2500      | 1.2600     | 120000  | Undefined |
| 2023-01-03 | EUR/USD | 1.24  | 1.23  | 1.2400      | 1.2300     | 130000  | Undefined |

---

## 📈 **Sample Workflow**

1. **Load data**  
   Reads trading data from `/data/example_trades.csv`.

2. **Analyze data**  
   - Detects Wyckoff phases (e.g., *Accumulation*, *Markup*).  
   - Identifies VSA signals (e.g., *High Volume Wide Spread*).

3. **Visualize data**  
   Generates a chart showing:  
   - Entry and exit prices.  
   - Annotated phases.  
   - VSA signals.

---

## 🛣️ **Roadmap**

### **Phase 1: Foundation**  
✅ Load and manage CSV data  
✅ Perform Wyckoff analysis  
✅ Visualize results  

### **Phase 2: Advanced Analytics**  
⬜ Expand Volume Spread Analysis (VSA)  
⬜ Improve interactivity in visualizations  

### **Phase 3: Real-Time Data**  
⬜ Integrate APIs for live market data  
⬜ Provide AI-driven trading insights  

---

## 📸 **Screenshots**

Coming soon! Stay tuned for visual examples of the application's capabilities.

---

## 🤝 **Contributing**

We welcome contributions!  

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## 📝 **License**

This project is licensed under the MIT License. Feel free to use and modify it as you see fit!

---

📬 **Contact**

For any questions or suggestions, feel free to reach out at **goliathnm@gmail.com**.

---

Enjoy exploring and enhancing the Trading Journal! 🚀
