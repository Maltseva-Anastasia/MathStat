import numpy as np
import matplotlib.pyplot as plt
n = [20, 100]

def boxplot():
    plt.figure()
    norm20 = np.random.normal(0, 1, 20)
    norm100 = np.random.normal(0, 1, 100)
    plt.boxplot(x=(norm20, norm100), vert=False, labels=[20, 100])
    plt.title("Нормальное распределение")
    plt.xlabel("x")
    plt.ylabel("size")
    plt.show()

    plt.figure()
    cauchy20 = np.random.standard_cauchy(20)
    cauchy100 = np.random.standard_cauchy(100)
    plt.boxplot(x=(cauchy20 , cauchy100), vert=False, labels=[20, 100])
    plt.title("Распределение Коши")
    plt.xlabel("x")
    plt.ylabel("size")
    plt.show()

    plt.figure()
    laplace20 = np.random.laplace(0, 2 ** (-0.5), 20)
    laplace100 = np.random.laplace(0, 2 ** (-0.5), 100)
    plt.boxplot(x=(laplace20, laplace100), vert=False, labels=[20, 100])
    plt.title("Распределение Лапласа")
    plt.xlabel("x")
    plt.ylabel("size")
    plt.show()

    plt.figure()
    poisson20 = np.random.poisson(10, 20)
    poisson100 = np.random.poisson(10, 100)
    plt.boxplot(x=(poisson20, poisson100), vert=False, labels=[20, 100])
    plt.title("Распределение Пуассона")
    plt.xlabel("x")
    plt.ylabel("size")
    plt.show()

    plt.figure()
    uniform20 = np.random.uniform(-1 * (3 ** 0.5), 3 ** 0.5, 20)
    uniform100 = np.random.uniform(-1 * (3 ** 0.5), 3 ** 0.5, 100)
    plt.boxplot(x=(uniform20, uniform100), vert=False, labels=[20, 100])
    plt.title("Равномерное распределение")
    plt.xlabel("x")
    plt.ylabel("size")
    plt.show()

def emissions():
    for i in range(len(n)):
        ejection = 0
        for j in range(1000):
            norm = np.random.normal(0, 1, n[i])
            IQR = np.quantile(norm, 0.75) - np.quantile(norm, 0.25)
            min = np.quantile(norm, 0.25) - 1.5*IQR
            max = np.quantile(norm, 0.75) + 1.5*IQR
            for elem in norm:
                if elem < min or elem > max:
                    ejection += 1
        print("Нормальное распределение: n=%i " % n[i], np.around(ejection/1000/n[i], decimals=2), end='\n')

    for i in range(len(n)):
        ejection = 0
        for j in range(1000):
            cauchy = np.random.standard_cauchy(n[i])
            IQR = np.quantile(cauchy, 0.75) - np.quantile(cauchy, 0.25)
            min = np.quantile(cauchy, 0.25) - 1.5*IQR
            max = np.quantile(cauchy, 0.75) + 1.5*IQR
            for elem in cauchy:
                if elem < min or elem > max:
                    ejection += 1
        print("Распределение Коши: n=%i " % n[i], np.around(ejection/1000/n[i], decimals=2), end='\n')

    for i in range(len(n)):
        ejection = 0
        for j in range(1000):
            laplace = np.random.laplace(0, 2 ** (-0.5), n[i])
            IQR = np.quantile(laplace, 0.75) - np.quantile(laplace, 0.25)
            min = np.quantile(laplace, 0.25) - 1.5*IQR
            max = np.quantile(laplace, 0.75) + 1.5*IQR
            for elem in laplace:
                if elem < min or elem > max:
                    ejection += 1
        print("Распределение Лапласа: n=%i " % n[i], np.around(ejection/1000/n[i], decimals=2), end='\n')

    for i in range(len(n)):
        ejection = 0
        for j in range(1000):
            poisson = np.random.poisson(10, n[i])
            IQR = np.quantile(poisson, 0.75) - np.quantile(poisson, 0.25)
            min = np.quantile(poisson, 0.25) - 1.5*IQR
            max = np.quantile(poisson, 0.75) + 1.5*IQR
            for elem in poisson:
                if elem < min or elem > max:
                    ejection += 1
        print("Распределение Пуассона: n=%i " % n[i], np.around(ejection/1000/n[i], decimals=2), end='\n')

    for i in range(len(n)):
        ejection = 0
        for j in range(1000):
            uniform = np.random.uniform(-1 * (3 ** 0.5), 3 ** 0.5, n[i])
            IQR = np.quantile(uniform, 0.75) - np.quantile(uniform, 0.25)
            min = np.quantile(uniform, 0.25) - 1.5*IQR
            max = np.quantile(uniform, 0.75) + 1.5*IQR
            for elem in uniform:
                if elem < min or elem > max:
                    ejection += 1
        print("Равномерное распределение: n=%i " % n[i], np.around(ejection/1000/n[i], decimals=2), end='\n')

boxplot()
emissions()
