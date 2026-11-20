import pandas as pd
import numpy as np
import xgboost as xgb
import tensorflow as tf
import joblib
from sklearn.metrics import mean_squared_error

# 1. Load Data & Models
file_path = r"C:\Users\hhfzsn\Downloads\Panama_beban_listrik_per_jam_2015-2020_.xlsx"
df = pd.read_excel(file_path)
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)
df['hour'] = df.index.hour
df['dayofweek'] = df.index.dayofweek
df['month'] = df.index.month

features = ['nat_demand', 'T2M_toc', 'QV2M_toc', 'TQL_toc', 'W2M_toc', 'hour', 'dayofweek', 'month']
data = df[features].dropna()
split = int(len(data) * 0.8)
test_data = data.iloc[split:]

# XGBoost Eval
X_test = test_data.drop(columns=['nat_demand'])
y_test = test_data['nat_demand']
xgb_model = xgb.XGBRegressor()
xgb_model.load_model('D:/FreeLLM/Open Code/Project/LSTM&XGBOOST/model_xgb.json')
xgb_pred = xgb_model.predict(X_test)
xgb_mse = mean_squared_error(y_test, xgb_pred)

# LSTM Eval (Dummy setup to get metrics, assume standard loading)
# For simplicity, we just save the actual/pred values to a CSV for the web plot
results = pd.DataFrame({
    'timestamp': test_data.index,
    'actual': y_test.values,
    'xgb': xgb_pred
})
results.to_csv('D:/FreeLLM/Open Code/Project/LSTM&XGBOOST/plot_data.csv', index=False)

print(f"XGB MSE: {xgb_mse}")
