import time
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

fig = go.Figure()
file = r"C:\Users\moses\Documents\Test-Stand\DataLogging\data\temp_test_after_fire1.csv"

print("now plotting...")

while True:
    data = pd.read_csv(file, delimiter=',')
    fig.add_trace(go.Scatter(
        x = data
    ))
    fig.refresh

    time.sleep(0.25);

