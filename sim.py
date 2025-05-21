import plotly.express as px
import pandas as pd

m = 1 #kg
f_b = 176.58 #newtons (assume constant force)
t_b = 0.75 #burn time in seconds

d_coef = 0.138
p = 1.225 #kg/m^3
a = 0.002397 #square meters
d_coef = d_coef * 0.5 * p * a

f_g = m * 9.81

pos = 0 #start on the ground
v = 0
a = 0

time = 0
dt = 0.01

data = [0]

while pos >= 0:

    #f = ma, a = f/m
    f_d = d_coef * v**2

    if time < t_b:
        f_m = f_b
    else:
        f_m = 0
    
    a = (f_m - f_d - f_g) / m
    v += a * dt
    pos += v * dt

    time += dt
    print(pos, '\n')
    data.append(pos)

fig = px.line(data)
fig.show()
