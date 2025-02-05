import pandas as pd
from sklearn.preprocessing import LabelEncoder
from models.model_accuracy import simple_model_accuracy  # Ensure this import works
from models.hyper_tuning import hyperparameter_tuning     # Ensure this import works

def preprocess_data(data):
    # Encode any non-numeric (categorical) columns
    for column in data.columns:
        if data[column].dtype == 'object':
            encoder = LabelEncoder()
            data[column] = encoder.fit_transform(data[column])
    return data

def process_file(file, target_column=None):
    import pandas as pd
    # Load and preprocess the data...
    data = pd.read_csv(file)
    data = preprocess_data(data)

    # Determine target column
    if target_column is None:
        target_column = data.columns[-1]
    elif target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' not found in the dataset.")

    # Split the data into features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Calculate accuracy for simple and tuned models
    simple_acc = simple_model_accuracy(X, y)
    tuned_acc = hyperparameter_tuning(X, y)

    return {
        "simple_accuracy": simple_acc * 100,
        "tuned_accuracy": tuned_acc * 100
    }