from sklearn.ensemble import RandomForestClassifier  # Assuming you're using this model

def simple_model_accuracy(X, y):
    from sklearn.model_selection import train_test_split
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Ensure data is numeric
    X_train = X_train.astype(float)
    y_train = y_train.astype(float)
    
    # Initialize the model
    model = RandomForestClassifier(random_state=42)
    
    try:
        # Train the model
        model.fit(X_train, y_train)
    except ValueError as e:
        print(f"Error during model training: {e}")
        raise

    # Return the accuracy
    return model.score(X_test, y_test)
