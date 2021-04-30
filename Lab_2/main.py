import numpy as np
import scipy.stats as sts

n = [10, 100, 1000]
mean, median, z_R, z_Q, z_tr = [], [], [], [], []

def characters(distribution):
    mean.append(np.mean(distribution))
    median.append(np.median(distribution))
    distr = np.sort(distribution)
    z_R.append((distr[1]+distr[-1])/2)
    z_Q.append((np.percentile(distr, 0.25)+np.percentile(distr, 0.75))/2)
    z_tr.append(sts.trim_mean(distr, 0.25))

def printin(n):
    print("n = %i" % n)
    print("E:", end=" ")
    print(np.around(np.mean(mean), decimals=6), end=" ")
    print(np.around(np.mean(median), decimals=6), end=" ")
    print(np.around(np.mean(z_R), decimals=6), end=" ")
    print(np.around(np.mean(z_Q), decimals=6), end=" ")
    print(np.around(np.mean(z_tr), decimals=6), end="\n")

    print("D:", end=" ")
    print(np.around(np.std(mean) ** 2, decimals=6), end=" ")
    print(np.around(np.std(median) ** 2, decimals=6), end=" ")
    print(np.around(np.std(z_R) ** 2, decimals=6), end=" ")
    print(np.around(np.std(z_Q) ** 2, decimals=6), end=" ")
    print(np.around(np.std(z_tr) ** 2, decimals=6), end="\n")

    print("E-sqrt(D):", end=" ")
    print(np.around(np.mean(mean) - np.std(mean), decimals=6), end=" ")
    print(np.around(np.mean(median) - np.std(median), decimals=6), end=" ")
    print(np.around(np.mean(z_R) - np.std(z_R), decimals=6), end=" ")
    print(np.around(np.mean(z_Q) - np.std(z_Q), decimals=6), end=" ")
    print(np.around(np.mean(z_tr) - np.std(z_tr), decimals=6), end="\n")

    print("E+sqrt(D):", end=" ")
    print(np.around(np.mean(mean) + np.std(mean), decimals=6), end=" ")
    print(np.around(np.mean(median) + np.std(median), decimals=6), end=" ")
    print(np.around(np.mean(z_R) + np.std(z_R), decimals=6), end=" ")
    print(np.around(np.mean(z_Q) + np.std(z_Q), decimals=6), end=" ")
    print(np.around(np.mean(z_tr) + np.std(z_tr), decimals=6), end="\n")

    mean.clear()
    median.clear()
    z_R.clear()
    z_Q.clear()
    z_tr.clear()

print("Нормальное распределение:")
for i in range(len(n)):
    for j in range(1000):
        norm = np.random.normal(0, 1, n[i])
        characters(norm)
    printin(n[i])

print("\nРаспределение Коши:")
for i in range(len(n)):
    for j in range(1000):
        cauchy = np.random.standard_cauchy(n[i])
        characters(cauchy)
    printin(n[i])

print("\nРаспределение Лапласа:")
for i in range(len(n)):
    for j in range(1000):
        laplace = np.random.laplace(0, 2 ** (-0.5), n[i])
        characters(laplace)
    printin(n[i])

print("\nРаспределение Пуассона:")
for i in range(len(n)):
    for j in range(1000):
        poisson = np.random.poisson(10, n[i])
        characters(poisson)
    printin(n[i])

print("\nРавномерное распределение:")
for i in range(len(n)):
    for j in range(1000):
        uniform = np.random.uniform(-1 * (3 ** 0.5), 3 ** 0.5, n[i])
        characters(uniform)
    printin(n[i])
