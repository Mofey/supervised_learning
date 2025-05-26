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

def load_new_data():
    """Generates new data for prediction."""
    new_data = {
        'CreditScore': [720],
        'Income': [55000],
        'LoanAmount': [18000]
    }
    return pd.DataFrame(new_data)

def load_csv_data(file_path='new_loanee_data.csv'):
    """Loads new data for prediction from a CSV file."""
    return pd.read_csv(file_path)