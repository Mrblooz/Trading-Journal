import logging
from tools.data_manager import DataManager
from tools.analyzer import Analyzer
from tools.vsa import VolumeSpreadAnalyzer
from tools.visualization import Visualizer

# Configuration for the logging.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"    
)

class TradingJournalApp:
    """
    Main application class for the Trading Journal.
    This class orchestrates data loading,analysis, and visualization.
    """
    def __init__(self):
        # Initiliaze of components
        self.data_manager = DataManager()
        self.analyzer = Analyzer()        
        self.visualizer = Visualizer()
        self.vsa_analyzer = VolumeSpreadAnalyzer()

    def run(self):
        """ 
        Executes the core workflow of the trading journal application.
        """
        logging.info("Starting Trading Journal Application...")

        # Step 1 Load Data
        data_file = "data/example_trades.csv"
        logging.info(f"Loading data from: {data_file}")
        data = self.data_manager.load_data(data_file)

        # Step 2 Analyseer Fases
        logging.info("Analyzing Wyckoff phases...")
        data = self.analyzer.detect_phases(data)

        # Step 3 Execute Volume Spread Analysis (VSA)        
        logging.info("Performing Volume Spread Analysis (VSA)...")
        data = self.vsa_analyzer.calculate_spread(data)
        data = self.vsa_analyzer.detect_vsa_signals(data)

        # Step 4 Visualize the results
        logging.info("Visualizing results...")
        self.visualizer.plot_data(data) 

        # Step 5 Save Data(optional)
        output_file = "data/processed_trades.csv"
        logging.info(f"Saving processed data to: {output_file}...")
        self.data_manager.save_data(data, output_file)

        logging.info("Trading Journal Application has completed successfully!")

if __name__ == "__main__":
    app = TradingJournalApp()
    app.run()