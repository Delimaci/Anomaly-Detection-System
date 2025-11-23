import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("logins.csv")

# === Machine Learning Anomaly Detection ===

# ML model only needs numeric features
X = df[["hour"]]

# Create the anomaly detection model
model = IsolationForest(contamination=0.1, random_state=42)

# Fit model + predict anomalies
df["ml_suspicious"] = model.fit_predict(X)

# Convert: model outputs -1 = anomaly, so convert to True/False
df["ml_suspicious"] = df["ml_suspicious"] == -1

# Count anomalies
ml_suspicious_count = df["ml_suspicious"].sum()

# Count per user
ml_offenders = df[df["ml_suspicious"]].groupby("username").size()

# Users with more than 1 anomaly
ml_repeat = ml_offenders[ml_offenders > 1]


# === PRINT RESULTS ===
print("ML suspicious logins per user:\n", ml_offenders)
print("ML repeat offenders:\n", ml_repeat)
print("Total ML suspicious logins:", ml_suspicious_count)

