import os
import pandas as pd

RAW_DATA_DIR = "../../data/raw"
PICKUP_COL = "tpep_pickup_datetime"
DROPOFF_COL = "tpep_dropoff_datetime"


def load_raw_taxi_data(raw_data_dir=RAW_DATA_DIR):
    """
    Load and concatenate all NYC TLC CSV files from the raw data directory.
    Returns concatenated pandas DataFrame containing all raw trip records.
    """

    # Get .csv data files in the correct order aaaaa
    csv_files = sorted(
        f for f in os.listdir(raw_data_dir)
        if f.endswith(".csv")
    )

    if not csv_files:
        raise FileNotFoundError("No CSV files found in data/raw/")

    # Load files and create dataframes
    dataframes = []
    for file in csv_files:
        file_path = os.path.join(raw_data_dir, file)
        print(f"Loading {file_path}...")

        df = pd.read_csv(
            file_path,
            parse_dates=[PICKUP_COL, DROPOFF_COL],
            low_memory=False
        )

        df["source_file"] = file
        dataframes.append(df)

    # Concatenate dataframes
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df


def inspect_schema(df):
    """
    Print basic schema information.
    """

    print("\n--- Schema Info ---")
    df.info()

    print("\n--- Head ---")
    print(df.head())

    print("\n--- Missing Values ---")
    print(df.isna().sum())


if __name__ == "__main__":
    df = load_raw_taxi_data()
    inspect_schema(df)
