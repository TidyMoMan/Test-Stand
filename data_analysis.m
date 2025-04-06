data = readmatrix("C:\Users\moses\Documents\Test-Stand\test_stand_data_2025_04_05__18_44_24.csv");
data = data(2:size(data, 1), 1:size(data, 2)); %get rid of HIGHLY suspect first datapoint

OGdata = data;

data(:, 1) = data(:, 1) - data(1, 1); %convert to seconds since logging started

convert = [-2.5823e+05, 190; -2.5473e+05, 384; -2.5756e+05, 255;];
p = polyfit(convert(:, 1), convert(:, 2), 1);

scaledData = data;

offset = mean(scaledData(1:150)); %subtract initial load cell offset
scaledData = scaledData - offset;

grams = scaledData(:, 2) * p(1) + p(2); %convert to grams

scaledData = grams .* 0.0098066500286389; %convert to newtons

subplot(4, 1, 1);
title("Load Cell Readings, Grams")
plot(data(:, 1), scaledData)
xlabel("seconds");
ylabel("grams");
grid on;

subplot(4, 1, 2);
title("Load Cell Readings, SI")
plot(data(:, 1), scaledData)
xlabel("seconds");
ylabel("newtons");
grid on;

subplot(4, 1, 3);
title("Load Cell Readings, Imperial")
plot(data(:, 1), scaledData.*0.224809)
xlabel("seconds")
ylabel("pounds force");
grid on;

subplot(4, 1, 4);
title("raw data");
plot(1:numel(OGdata(:,1)), OGdata(:,2))
xlabel("sample number")
ylabel("raw load cell reading");
grid on;