from sklearn.tree import DecisionTreeClassifier

def train_model(X, y):
    """Trains a Decision Tree Classifier model."""
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model