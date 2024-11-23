Trading Journal Project

An advanced Python-based trading journal designed to analyze and visualize trading data using concepts inspired by the Wyckoff Method and Volume Spread Analysis (VSA). The app helps traders track their trades, detect market phases, and gain insights into their performance.

---

🚀 Features

    📊 Data Management
        Load trade data from CSV files.
        Save updated trade data to CSV files with error handling and logging.
        Fetch historical data via Yahoo Finance API using yfinance.

    🧮 Wyckoff Phase Detection
        Detect trading phases such as "Accumulation," "Distribution," "Markup," and "Markdown" using rolling averages.

    📈 Volume Spread Analysis (VSA)
        Calculate price spreads for each trade.
        Detect potential VSA signals such as "High Volume Wide Spread" or "Low Volume Narrow Spread."

    📊 Visualization
        Plot Entry and Exit Prices with:
            Wyckoff phases annotated.
            VSA signals displayed directly on the chart.
            Dynamic and interactive visualizations.

    🛠 Modular Design
        Simplified codebase with clear separation of concerns:
            app.py: Main application runner.
            data_manager.py: Data loading, saving, and fetching logic.
            phases.py: Wyckoff phase detection logic.
            vsa.py: Volume Spread Analysis logic.
            visualizations.py: Plotting and visualization logic.

---

🧩 Folder Structure

Here’s how the project is organized:

```plain text
trading-journal/
├── README.md                # Project documentation
├── app.py                   # Main script for running the app
├── data/                    # Local storage for trade and market data
│   └── example_trades.csv   # Example trade data file
├── tools/                   # Core logic and utilities
│   ├── __init__.py          # Makes 'tools' a Python module
│   ├── data_manager.py      # Data loading, saving, and fetching logic
│   ├── phases.py            # Wyckoff phase detection logic
│   ├── vsa.py               # Volume Spread Analysis (VSA) logic
│   └── visualizations.py    # Plotting and visualization logic
├── tests/                   # Unit tests for modules
│   ├── test_data_manager.py
│   ├── test_phases.py
│   ├── test_vsa.py
│   └── test_visualizations.py
├── notebooks/               # Optional Jupyter notebooks for research
└── docs/                    # Documentation and guides
```

---

🛠 Installation

1. Clone the repository:
      ```bash   
         git clone https://github.com/YourUsername/trading-journal.git
         cd trading-journal
      ```
2. Install dependencies:
      ```bash
         pip install -r requirements.txt
      ```
3. Run Tests to ensure everything is working.
      ```bash
         pytest ./tests/
      ```

---

⚙️ How to Use

   1. Set Up Environment:
        Install dependencies as shown above.

   2. Run the Application:
         Execute the app:
         ```bash
         python app.py
         ```
   3. Provide Your Data:
         Place your trade data CSV in the /data folder.
         Ensure it follows the correct structure (see Sample CSV Structure below).

   4. View Results:
         Check the output folder for processed data and visualizations.

---

📊 Sample Workflow

   1. Load Data:
         Reads trade data from data/example_trades.csv or your provided file.

   2. Analyze Data:
         Detects Wyckoff phases (e.g., "Accumulation", "Markup").
         Identifies VSA signals (e.g., "High Volume Wide Spread").

   3. Visualize Data:
         Generates a chart showing:
            Entry and Exit Prices.
            Phases annotated near Entry Prices.
            VSA signals annotated directly on the chart.

---

🗂 Sample CSV Structure

```csv
Date,Asset,High,Low,Entry Price,Exit Price,Volume,Phase
2023-01-01,EUR/USD,1.25,1.20,1.2000,1.2500,100000,Undefined
2023-01-02,EUR/USD,1.26,1.25,1.2500,1.2600,120000,Undefined
2023-01-03,EUR/USD,1.24,1.23,1.2400,1.2300,130000,Undefined
2023-01-04,EUR/USD,1.21,1.20,1.1200,1.2000,140000,Undefined
2023-01-05,EUR/USD,1.19,1.18,1.1900,1.1000,150000,Undefined
```

---

📈 Project Progress

Completed Tasks

Modularized code into distinct files (data_manager.py, phases.py, vsa.py, visualizations.py, and app.py).
Implemented logging for robust debugging and error tracking.
Fully implemented and tested Wyckoff phase detection.
Created dynamic tests using pytest for all modules.
Established a clean and extensible project structure.

    Built foundational visualizations for trading data.

Upcoming Tasks

Enhance Visualization

    Add subplots for volume and profit/loss metrics.
    Highlight VSA signals visually on the chart.

Profit and Loss (PnL)

    Calculate and visualize PnL for each trade.

Expand VSA Logic

    Add detection for "Climactic Action" and "Stopping Volume."

Build Tests

    Write end-to-end tests for app.py.

Integrate Real-Time Data

    Incorporate APIs for live market data.
    Provide AI-driven trade insights.

---

🛣️ Roadmap
Phase 1: Foundation

    Load and manage CSV data.
    Perform Wyckoff analysis.
    Visualize results.

Phase 2: Advanced Analytics

    Add Volume Spread Analysis (VSA).
    Improve visualizations with interactivity.

Phase 3: Real-Time Data

    Integrate APIs for live market data.
    Provide AI-driven trade insights.

---

🛠 Technologies Used

    Python: Core programming language.
    Pandas: Data manipulation and analysis.
    Matplotlib: Data visualization.
    Yahoo Finance API via yfinance: Fetching historical market data.
    Pytest: Unit testing framework.

---

📸 Screenshots

Coming soon! Stay tuned for visual examples of the application's capabilities.

---

🤝 Contributing

We welcome contributions! Here's how you can help:

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

📝 License

This project is licensed under the MIT License. Feel free to use and modify it as you see fit!

---

📬 Contact

For any questions or suggestions, please feel free to contact me at goliathnm@gmail.com.

---

Enjoy exploring and enhancing the Trading Journal! 🚀