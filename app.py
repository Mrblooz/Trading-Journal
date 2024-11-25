from tools.data_manager import DataManager
from tools.performance_metrics import Metrics
from tools.phases import PhaseAnalyzer
from tools.vsa import VolumeSpreadAnalyzer
from tools.visualization import Visualizer
from logs.setup_logging import setup_logger

# Initialize centralized logger
logger = setup_logger("TradingJournalApp")

class TradingJournalApp:
    """
    Main application class for the trading journal workflow.
    """
    def __init__(self):
        # Initialize components
        self.data_manager = DataManager()
        self.metrics = Metrics()
        self.phase_analyzer = PhaseAnalyzer()  # Correctly instantiate PhaseAnalyzer
        self.vsa_analyzer = VolumeSpreadAnalyzer()
        self.visualizer = Visualizer()

    def run(self):
        """
        Executes the main workflow of the application.
        """
        logger.info("Starting Trading Journal Application...")
        try:
            # Step 1: Load data
            data_file = "data/example_trades.csv"
            logger.info(f"Loading data from {data_file}...")
            data = self.data_manager.load_data(data_file)

            # Step 2: Detect phases
            logger.info("Analyzing Wyckoff phases...")
            data = self.phase_analyzer.detect_phases(data)  # Use PhaseAnalyzer instead of Analyzer

            # Step 3: Perform VSA
            logger.info("Performing Volume Spread Analysis (VSA)...")
            data = self.vsa_analyzer.calculate_spread(data)
            data = self.vsa_analyzer.detect_vsa_signals(data)

            # Step 4: Calculate Metrics
            logger.info("Calculating perfomance metrics...")
            metrics = self.metrics.calculate_metrics(data)

            # Step 5: Visualize results
            logger.info("Visualizing results...")
            self.visualizer.plot_data(data)

            # Step 6: Save processed data
            output_file = "data/processed_trades.csv"
            logger.info(f"Saving processed data to {output_file}...")
            self.data_manager.save_data(data, output_file)

            logger.info("Trading Journal Application completed successfully!")
        except Exception as e:
            logger.error("Critical error in application execution.", exc_info=True)

if __name__ == "__main__":
    app = TradingJournalApp()
    app.run()
