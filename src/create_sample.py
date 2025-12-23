import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/walmart_full.csv")
SAMPLE_DIR = Path("data/sample")
SAMPLE_PATH = SAMPLE_DIR / "walmart_sample.csv"


def create_sample(nrows=10_000):
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_PATH)
    df.sample(n=min(nrows, len(df)), random_state=42).to_csv(
        SAMPLE_PATH, index=False
    )

    print(f"Sample created at {SAMPLE_PATH}")


if __name__ == "__main__":
    create_sample()
