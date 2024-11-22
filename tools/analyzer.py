
class Analyzer:
    def detect_phases(self, data):
        """
        Detect Wyckoff phases based on price trends.
        """
        print("Detecting Wyckoff phases...")
        data["Phase"] = "Undefined"
        rolling_mean = data["Entry Price"].rolling(window=2).mean()

        # Fill NaN values in rolling mean
        rolling_mean = rolling_mean.fillna(data["Entry Price"])

        data.loc[data["Entry Price"] < rolling_mean, "Phase"] = "Accumulation"
        data.loc[data["Entry Price"] > rolling_mean, "Phase"] = "Markup"
    
        return data
