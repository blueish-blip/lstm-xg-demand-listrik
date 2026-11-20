import pandas as pd
import numpy as np
import xgboost as xgb
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import joblib

# 1. Load Data
file_path = r"C:\Users\hhfzsn\Downloads\Panama_beban_listrik_per_jam_2015-2020_.xlsx"
df = pd.read_excel(file_path)
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

# 2. Feature Engineering
df['hour'] = df.index.hour
df['dayofweek'] = df.index.dayofweek
df['month'] = df.index.month

features = ['nat_demand', 'T2M_toc', 'QV2M_toc', 'TQL_toc', 'W2M_toc', 'hour', 'dayofweek', 'month']
data = df[features].dropna()

# 3. XGBoost Training
X = data.drop(columns=['nat_demand'])
y = data['nat_demand']
split = int(len(data) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

xgb_model = xgb.XGBRegressor(n_estimators=100)
xgb_model.fit(X_train, y_train)
xgb_model.save_model('D:/FreeLLM/Open Code/Project/LSTM&XGBOOST/model_xgb.json')

# 4. LSTM Training
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)
joblib.dump(scaler, 'D:/FreeLLM/Open Code/Project/LSTM&XGBOOST/scaler.pkl')

def create_sequences(data, seq_length=24):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length, 1:]) # Using all features except target
        y.append(data[i+seq_length, 0])    # Target is nat_demand
    return np.array(X), np.array(y)

seq_len = 24
X_lstm, y_lstm = create_sequences(data_scaled, seq_len)
split_lstm = int(len(X_lstm) * 0.8)
X_train_l, X_test_l = X_lstm[:split_lstm], X_lstm[split_lstm:]
y_train_l, y_test_l = y_lstm[:split_lstm], y_lstm[split_lstm:]

lstm_model = tf.keras.Sequential([
    tf.keras.layers.LSTM(50, activation='relu', input_shape=(seq_len, X_lstm.shape[2])),
    tf.keras.layers.Dense(1)
])
lstm_model.compile(optimizer='adam', loss='mse')
lstm_model.fit(X_train_l, y_train_l, epochs=5, batch_size=32, verbose=0)
lstm_model.save('D:/FreeLLM/Open Code/Project/LSTM&XGBOOST/model_lstm.h5')

print("Models saved successfully.")
