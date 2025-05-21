data = readmatrix("C:\Users\moses\Documents\Test-Stand\test_stand_data_2025_05_16__14_58_22.csv");

data(:, 1) = data(:, 1) - data(1, 1); %convert to seconds since logging started

Y1 = -157500; %no load
Y2 = -144700; %937g load

X1 = 0;
X2 = 0.937; %kg

m = (X2 - X1) / (Y2 - Y1);

force = ((data(:, 2) - Y1)* m);

plot(data(:, 1), force);