import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

m = 1 #kg
f_b = 176.58 #newtons (assume constant force)
t_b = 0.21 #burn time in seconds

d_coef = 0.138
p = 1.225 #kg/m^3
a = 0.002397 #square meters
d_coef = d_coef * 0.6 * p * a

f_g = m * 9.81

pos = 0 #start on the ground
v = 0
a = 0

time = 0
dt = 0.01

aLog = [0]
velLog = [0]
heightLog = [0]

while pos >= 0:

    #f = ma, a = f/m

    if time < t_b:
        f_m = f_b
    else:
        f_m = 0

    f_d = d_coef * v**2

    a = (f_m - f_d - f_g) / m
    v += a * dt
    pos += v * dt

    time += dt
    
    aLog.append(a)
    velLog.append(v)
    heightLog.append(pos)

fig = go.Figure()

fig.add_trace(go.Scatter(
    y = heightLog,
    name = "height (m)"
))

fig.add_trace(go.Scatter(
    y = aLog,
    name = "acceleration (m/s^2)"
))

fig.add_trace(go.Scatter(
    y = velLog,
    name = "velocity (m/s)"
))

fig.add_annotation(x = heightLog.index(max(heightLog)), y = max(heightLog),
    text=("apogee at " + str(round(max(heightLog), 2)) + "m"),
    showarrow=True,
    arrowhead=1
)

fig.add_annotation(x = aLog.index(max(aLog)), y = max(aLog),
    text=("top speed of " + str(round(max(velLog), 2)) + "m/s"),
    showarrow=True,
    arrowhead=1
)

fig.add_annotation(x = velLog.index(max(velLog)), y = max(velLog),
    text=("peak acceleration of " + str(round(max(aLog), 2)) + "m/s^2"),
    showarrow=True,
    arrowhead=1
)

fig.show()
