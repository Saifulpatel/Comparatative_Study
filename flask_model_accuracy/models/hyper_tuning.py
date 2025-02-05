from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def hyperparameter_tuning(X, y):
    """
    Performs hyperparameter tuning on a RandomForestClassifier and returns the accuracy.
    
    Parameters:
        X (DataFrame or array-like): Features.
        y (Series or array-like): Target variable.
    
    Returns:
        float: The accuracy score of the best estimator.
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Define the parameter grid for hyperparameter tuning
    param_grid = {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    }

    # Create a GridSearchCV object with a RandomForestClassifier
    grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    # Get the best model and evaluate it
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    return accuracy_score(y_test, y_pred)
