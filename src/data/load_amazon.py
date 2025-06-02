# Data loading for Amazon e-commerce dataset
import pandas as pd

def load_amazon_data(filepath: str) -> pd.DataFrame:
    """Load Amazon e-commerce data from a CSV file."""
    return pd.read_csv(filepath)
