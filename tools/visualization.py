import matplotlib.pyplot as plt

class Visualizer:
    def plot_data(self, data):
        """
        Plot trade data with Wyckoff phases and VSA signals.
        """
        print("Plotting data...")
        plt.figure(figsize=(12, 6))

        # Plot Entry and Exit Prices
        plt.plot(data["Date"], data["Entry Price"], label="Entry Price", marker="o", color="blue")
        plt.plot(data["Date"], data["Exit Price"], label="Exit Price", linestyle="--", color="orange")

        # Annotate phases
        for i, phase in enumerate(data["Phase"]):
            plt.text(data["Date"][i], data["Entry Price"][i] + 0.005, phase, fontsize=10, ha="center")

        plt.title("Wyckoff Analysis: Entry & Exit Prices with Phases and VSA")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
