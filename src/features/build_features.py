# Feature engineering for e-commerce data
def build_features(df):
    """Create features from raw data."""
    # Example: Add a feature for product title length
    df["title_length"] = df["title"].str.len()
    return df
