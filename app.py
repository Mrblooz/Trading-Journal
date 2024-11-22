import pandas as pd
import matplotlib.pyplot as plt

# Data Manager
class DataManager:
    def load_data(self, filepath):
        """Load trade data from a CSV file."""
        print(f"Loading data from {filepath}...")
        return pd.read_csv(filepath, parse_dates=["Date"])

# Analyzer
class Analyzer:
    def detect_phases(self, data):
        """Detect Wyckoff phases based on price trends."""
        print("Detecting Wyckoff phases...")
        data["Phase"] = "Undefined"
        rolling_mean = data["Entry Price"].rolling(window=2).mean()
        data.loc[data["Entry Price"] < rolling_mean, "Phase"] = "Accumulation"
        data.loc[data["Entry Price"] > rolling_mean, "Phase"] = "Markup"
        return data

# Visualizer
class Visualizer:
    def plot_data(self, data):
        """Plot trade data."""
        print("Plotting data...")
        plt.plot(data["Date"], data["Entry Price"], label="Entry Price")
        plt.plot(data["Date"], data["Exit Price"], label="Exit Price")
        plt.legend()
        plt.show()

# Main Application
class TradingJournalApp:
    def __init__(self):
        self.data_manager = DataManager()
        self.analyzer = Analyzer()
        self.visualizer = Visualizer()

    def run(self):
        # Load example data
        data = self.data_manager.load_data("data/example_trades.csv")

        # Apply the Wyckoff method
        data = self.analyzer.detect_phases(data)

        # Visualize the results
        self.visualizer.plot_data(data)

if __name__ == "__main__":
    app = TradingJournalApp()
    app.run()
