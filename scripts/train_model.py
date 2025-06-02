# CLI script to train the model
from src.data.load_amazon import load_amazon_data
from src.features.build_features import build_features
from src.models.train import train_model

if __name__ == "__main__":
    df = load_amazon_data("data/raw/amazon.csv")
    df = build_features(df)
    X = df.drop("success", axis=1)
    y = df["success"]
    train_model(X, y)
