data = readmatrix("C:\Users\moses\Desktop\TestStand\TestStandController\test_stand_data_2025_03_21__19_53_16.csv");
OGdata = data;

plot(data(:, 1), data(:, 2))

data(:, 1) = data(:, 1) - data(1, 1); %convert to seconds since logging started

convert = [-2000, 180; 2700, 402; 42500, 2285;];
p = polyfit(convert(:, 1), convert(:, 2), 1);

scaledData = data(:, 2) * p(1) + p(2); %convert to grams
scaledData = scaledData .* 0.0098066500286389; %convert to newtons

offset = mean(scaledData(1:150)); %subtract initial load cell offset
scaledData = scaledData - offset;

subplot(3, 1, 1);
title("Load Cell Readings, SI")
plot(data(:, 1), scaledData)
xlabel("seconds");
ylabel("newtons");
grid on;

subplot(3, 1, 2);
title("Load Cell Readings, Imperial")
plot(data(:, 1), scaledData.*0.224809)
xlabel("seconds")
ylabel("pounds force");
grid on;

subplot(3, 1, 3);
title("raw data");
plot(1:numel(OGdata(:,1)), OGdata(:,2))
xlabel("sample number")
ylabel("raw load cell reading");
grid on;