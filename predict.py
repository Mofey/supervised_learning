def predict_loan(model, X_new):
    """Predicts loan approval for new applicants."""
    return model.predict(X_new)
