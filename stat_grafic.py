import pandas as pd
import matplotlib.pyplot as plt

class SteamStats:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.counts = self.df["country"].dropna().value_counts()

    def plot(self, top_n=10, scale=1000, label="В тысячах",
             save_path=None, figsize=(10, 6)):

        data = self.counts.head(top_n) if top_n else self.counts
        labels = list(data.index)
        values = [v / scale for v in data.values]

        if top_n is None and len(labels) > 20:
            figsize = (max(14, len(labels) * 0.6), 7)

        _, ax = plt.subplots(figsize=figsize)
        bars = ax.bar(labels, values, color="#4472C4", width=0.5)

        ax.set_title("Количество игроков Steam", fontsize=15, pad=15)
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)

        ax.yaxis.grid(True, alpha=0.5)
        ax.set_axisbelow(True)
        ax.set_xlabel("Страна")
        ax.set_ylabel("Количество игроков")

        ax.tick_params(axis="x", rotation=90 if len(labels) > 15 else 45, length=0)
        ax.tick_params(axis="y", length=0)
        for t in ax.get_xticklabels():
            t.set_horizontalalignment("right")

        ax.legend([bars[0]], [label], loc="lower center",
                  bbox_to_anchor=(0.5, -0.25), frameon=False)
               
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
            print(f"Сохранено: {save_path}")

        plt.show()
