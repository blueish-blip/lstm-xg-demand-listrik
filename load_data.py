import pandas as pd

file_path = r"C:\Users\hhfzsn\Downloads\Panama_beban_listrik_per_jam_2015-2020_.xlsx"
try:
    df = pd.read_excel(file_path)
    print(df.head())
    print(df.info())
except Exception as e:
    print(f"Error: {e}")
