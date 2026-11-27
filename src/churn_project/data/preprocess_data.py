import pandas as pd

def preprocess_data(df:pd.DataFrame, target_col:str = "Churn") -> pd.DataFrame:

    # remove whitespace from leading and trailing 
    df.columns = df.columns.str.strip()

    # drop id column
    df = df.drop(columns=['customerID'])

    # mapping the target column (No -> 0 and Yes -> 1)
    if target_col in df.columns and df[target_col].dtype == 'object':
        df[target_col] = df[target_col].str.strip().map({'No':0, 'Yes':1})

    # convert the type of this column to numeric
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    if 'SeniorCitizen' in df.columns:
        df['SeniorCitizen'] = df['SeniorCitizen'].fillna(0).astype(int)

    # Handling NaN value of numeric columns
    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].fillna(0)

    return df