from tools.data_manager import DataMananger  # Data loading/saving logic
from tools.analyzer import Analyzer        # Wyckoff phase detection logic
from tools.vsa import VolumeSpreadAnalyzer
from tools.visualization import Visualizer  # Data visualization logic

class TradingJournalApp:
    """
    Main application class for the trading journal.
    Orchestrates data loading, analysis, and visualization.
    """
    def __init__(self):
        self.data_manager = DataMananger()  # Handles loading/saving trade data
        self.analyzer = Analyzer()  # Detects Wyckoff phases
        self.vsa_analyzer = VolumeSpreadAnalyzer()
        self.visualizer = Visualizer()  # Plots trade data

    def run(self):
        """
        Executes the application's main workflow:
        1. Load data
        2. Analyze phases
        3. Visualize the results
        """
        # Load example trade data
        data = self.data_manager.load_data("data/example_trades.csv")

        # Analyze phases in the trade data
        analyzed_data = self.analyzer.detect_phases(data)

        # Apply Volume Spread Analysis (VSA)
        data = self.vsa_analyzer.calculate_spread(data)
        data = self.vsa_analyzer.detect_vsa_signals(data)


        # Visualize the results
        self.visualizer.plot_data(analyzed_data)


if __name__ == "__main__":
    # Initialize and run the app
    app = TradingJournalApp()
    app.run()


