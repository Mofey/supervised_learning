# Loan Approval Prediction using Decision Tree (Supervised Learning)

"""
This project applies a Decision Tree Classifier to predict loan approval based on customer financial history.
It follows a modular structure to ensure separation of concerns.

Modules:
- data_loader.py: Load dataset
- model.py: Train Random Forest model
- predict.py: Make predictions
- main.py: Run the full pipeline
"""
import sys
sys.dont_write_bytecode = True

from data_loader import load_data, load_csv_data, load_new_data
from model import train_model
from predict import predict_loan

if __name__ == "__main__":
    # Load the data
    df = load_data()
    
    # Train the model
    X = df[['CreditScore', 'Income', 'LoanAmount']]
    y = df['Approved']
    model = train_model(X, y)

    # Load new data for prediction
    try:
        new_data = load_csv_data()
    except:
        print("CSV file not found. Loaded sample data.")
        new_data = load_new_data()
    
    # Make predictions
    prediction = predict_loan(model, new_data)
    print(f'Predicted Approval: {prediction[0]}')