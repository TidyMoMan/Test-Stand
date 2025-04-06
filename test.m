data = readmatrix("C:\Users\moses\Documents\Test-Stand\test_stand_data_2025_04_05__17_21_27.csv");

avgWt = mean(data(:, 2))

plot(data(:, 1), data(:, 2))
hold on;