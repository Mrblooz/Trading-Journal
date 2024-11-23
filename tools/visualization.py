import matplotlib.pyplot as plt
import logging

# Configure logging for the visualizer
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class Visualizer:
    """
    A class responsible for visualizing trading data with various types of charts.
    """
    def __init__(self):
        """
        Initialize the Visualizer class.
        """
        logging.debug("Visualizer initialized.")

    def plot_data(self, data):
        """
        Plot trading data, including Entry and Exit Prices, with annotations for phases.

        Args:
            data (pd.Dataframe): The trading data to visualize. It should have colummns:
                - 'Date'
                - 'Entry Price'
                - 'Exit Price'
                - 'Phase'
        """
        logging.debug("Starting to plot data...")

        try:
            # Configure plot size
            plt.figure(figsize=(12,6))

            # Plot Entry and Exit prices
            plt.plot(data["Date"], data["Entry Price"], label = "Entry Price", marker="o", color="blue")
            plt.plot(data["Date"], data["Exit Price"], label = "Exit Price", linestyle = "--", color="orange")

            # annotate phases  
            for  i, phase in enumerate(data["Phase"]):
                plt.text(data["Date"][i], data["Entry Price"][i] + 0.005, phase, fontsize=10, ha="center")

            # Add Labels, title, and Legend
            plt.title("Trading Data Visualization")
            plt.xlabel("Date", fontsize=12)
            plt.ylabel("Price", fontsize=12)
            plt.legend()

            # Enable grid and adjust layout
            plt.grid(True)
            plt.tight_layout()

            # Display the plot
            logging.debug("Displaying the plot...")
            plt.show()
        except Exception as e:
            logging.error(f"An error occurred while plotting date: {e}")
            raise




        
