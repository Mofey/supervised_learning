import pandas as pd

def load_data():
    """Generates a sample loan approval dataset."""
    data = {
        'CreditScore': [600, 650, 700, 750, 800, 850],
        'Income': [30000, 40000, 50000, 60000, 70000, 80000],
        'LoanAmount': [5000, 10000, 15000, 20000, 25000, 30000],
        'Approved': [0, 1, 1, 1, 1, 0]
    }
    return pd.DataFrame(data)