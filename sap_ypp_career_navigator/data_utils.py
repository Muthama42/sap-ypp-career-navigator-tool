import pandas as pd
from pathlib import Path

def load_certificates(csv_path=None):
    if csv_path is None:
        csv_path = Path(__file__).parent.parent / 'data' / 'sap_certificates.csv'
    return pd.read_csv(csv_path) 