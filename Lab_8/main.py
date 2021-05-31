import matplotlib.pyplot as plt
import math
import numpy as np


def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            remove_dirst_str = line.replace("[", "")
            remove_next_str = remove_dirst_str.replace("]", "")
            data.append(remove_next_str.split(", "))

    data_float_format = []
    for item in data:
        data_float_format.append([float(x) for x in item])

    new_data = np.asarray(data_float_format)
    data = np.reshape(new_data, (new_data.shape[1] // 1024, 1024))
    return data[8]

def draw_areas(signal_data, area_data, types, title):
    plt.title(title)
    plt.ylim([-0.5, 0])
    for i in range(len(area_data)):
        if types[i] == "фон":
            color_ = 'y'
        if types[i] == "сигнал":
            color_ = 'r'
        if types[i] == "переход":
            color_ = 'g'
        #print(types)
        plt.plot([num for num in range(area_data[i][0], area_data[i][1], 1)], signal_data[i], color=color_, label=types[i])
        plt.savefig('areas.jpg')
    plt.legend()
    plt.show()


def inter_Group(signal, k):
    sum_n = 0
    sum = 0
    for signal_i in signal:
        sum_n += len(signal_i)

    for signal_i in signal:
        mean_i = np.mean(signal_i)
        for signal_j in signal_i:
            sum += (signal_j - mean_i) ** 2 * len(signal_i)
    return sum / (sum_n - k)


def inta_Group(signal, k):
    sum_n = 0
    sum = 0
    means = list()
    for signal_i in signal:
        sum_n += len(signal_i)
        means.append(np.mean(signal_i))
    main_mean = np.mean(means)
    for signal_i in signal:
        sum += (np.mean(signal_i) - main_mean) ** 2 * len(signal_i)
    return sum / (k - 1)


def get_new_selection(signal, k):
    newSizeY = int(signal.size / k)
    newSizeX = k
    return np.reshape(signal, (newSizeX, newSizeY))


def get_F(signal, k):
    splitetd_signal = get_new_selection(signal, k)
    print("при k = " + str(k))
    inter_D = inter_Group(splitetd_signal, k)
    print("inter_group = " + str(inter_D))
    inta_D = inta_Group(splitetd_signal, k)
    print("intar_group = " + str(inta_D))
    print("F = " + str(inta_D / inter_D), '\n')
    return inter_D / inta_D


def get_K(num):
    i = 4
    while num % i != 0:
        i += 1
    return i


def get_Fisher(signal, area_data):
    fishers = []
    for i in range(len(area_data)):
        start = area_data[i][0]
        finish = area_data[i][1]
        k = get_K(finish - start)
        while k == finish - start:
            finish += 1
            k = get_K(finish - start)
        fishers.append(get_F(signal[start:finish], int(k)))
    return fishers


signal = read_file('wave_ampl.txt')

# Построение графика сигнала
plt.title('Сигнал ' + '8')
plt.plot(range(len(signal)), signal)
plt.show()

# Построение гистограммы сигнала
bin = int(math.log2(len(signal) + 1))
hist = plt.hist(signal, bins=bin)
plt.title("Гистограмма сигнала")
plt.show()

# Разделение сигналов на области
count = []
start = []
finish = []
types = [0] * bin

for i in range(bin):
    count.append(hist[0][i])
    start.append(hist[1][i])
    finish.append(hist[1][i + 1])

sortedHist = sorted(count)
repeat = 0
for i in range(bin):
    for j in range(bin):
        if sortedHist[len(sortedHist) - 1 - i] == count[j]:
            if repeat == 0:
                types[j] = "фон"
            elif repeat == 1:
                types[j] = "сигнал"
            else:
                types[j] = "переход"
            repeat += 1

signal_types = [0] * len(signal)
zones = []
zones_type = []

for i in range(len(signal)):
    for j in range(len(types)):
        if (signal[i] >= start[j]) and (signal[i] <= finish[j]):
            signal_types[i] = types[j]

currType = signal_types[0]
start = 0
for i in range(len(signal_types)):
    if currType != signal_types[i]:
        finish = i
        zones_type.append(currType)
        zones.append([start, finish])
        start = finish
        currType = signal_types[i]

if currType != zones_type[len(zones_type) - 1]:
    zones_type.append(currType)
    zones.append([finish, len(signal) - 1])

signal_data = list()
for borders in zones:
    data_part = list()
    for j in range(borders[0], borders[1]):
        data_part.append(signal[j])
    signal_data.append(data_part)

# Определение типа областей критерием Фишера
fishers = get_Fisher(signal, zones)
print(fishers)
types = ['фон', 'переход', 'сигнал', 'переход', 'фон']
draw_areas(signal_data, zones, types, "Разделенные области для сигнала без выбросов")
print(zones)
