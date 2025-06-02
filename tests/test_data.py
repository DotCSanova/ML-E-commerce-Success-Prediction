# Test for data loading
from src.data.load_amazon import load_amazon_data

def test_load_amazon_data(tmp_path):
    # Create a dummy CSV
    d = tmp_path / "dummy.csv"
    d.write_text("col1,col2\n1,2\n3,4")
    import pandas as pd
    df = load_amazon_data(str(d))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
