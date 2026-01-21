import pandas as pd
import numpy as np
import os

def load_and_clean_data(data_dir):
    """
    Standardized data loader.
    Expects data_dir to point to the folder containing train.csv
    """
    # 1. Construct Paths
    train_path = os.path.join(data_dir, "train.csv")
    test_path = os.path.join(data_dir, "test.csv")

    # 2. Check existence
    if not os.path.exists(train_path):
        raise FileNotFoundError(f"❌ Cannot find train.csv at: {os.path.abspath(train_path)}")

    # 3. Load
    print(f"Loading data from {data_dir}...")
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    # 4. Clean (Drop ID and Target)
    y = train['y']
    X = train.drop(['y', 'ID'], axis=1)
    X_test = test.drop(['ID'], axis=1)

    # 5. Drop Zero Variance (Feasibility Check)
    numeric_cols = X.select_dtypes(include=[np.number]).columns
    var_check = X[numeric_cols].var()
    zero_var_cols = var_check[var_check == 0].index.tolist()
    
    if zero_var_cols:
        print(f"⚠️  Dropped {len(zero_var_cols)} constant columns.")
        X = X.drop(zero_var_cols, axis=1)
        X_test = X_test.drop(zero_var_cols, axis=1)

    return X, y, X_test