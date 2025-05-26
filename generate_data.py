import pandas as pd
import random

# Set the seed for reproducibility
def generate_new_data(num_samples=1):
    """Generates new data for loanee with random values."""
    data = {
        'CreditScore': [random.randint(300, 850) for _ in range(num_samples)],
        'Income': [random.randint(20000, 100000) for _ in range(num_samples)],
        'LoanAmount': [random.randint(1000, 50000) for _ in range(num_samples)]
    }
    return data

def save_data_to_csv(data, file_path):
    """Saves the dataset to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Generate the data
    data_dict = generate_new_data(num_samples=1)
    
    # Save the data to a CSV file
    csv_file_path = 'new_loanee_data.csv'
    save_data_to_csv(data_dict, csv_file_path)
    print(f"Data has been generated and saved to {csv_file_path}")