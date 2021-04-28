import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts

n = [10, 50, 1000]

# Нормальное распределение
for i in range(len(n)):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(sts.norm.ppf(0.0001), sts.norm.ppf(0.9999), n[i])
    ax.plot(x, sts.norm.pdf(x), linewidth=3, color='maroon')
    ax.hist(sts.norm.rvs(size=n[i]), color='peachpuff', density=True)
    ax.set_title('n=%i' % n[i])
    plt.grid()
    plt.show()

# Распределение Коши
for i in range(len(n)):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(sts.cauchy.ppf(0.001), sts.cauchy.ppf(0.999), n[i])
    ax.plot(x, sts.cauchy.pdf(x), linewidth=3, color='maroon')
    ax.hist(sts.cauchy.rvs(size=n[i]), color='peachpuff', density=True)
    ax.set_title('n=%i' % n[i])
    plt.grid()
    plt.show()

# Распределение Лапласа
for i in range(len(n)):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(sts.laplace.ppf(0.001), sts.laplace.ppf(0.999), n[i])
    ax.plot(x, sts.laplace.pdf(x), linewidth=3, color='maroon')
    ax.hist(sts.laplace.rvs(size=n[i]), color='peachpuff', density=True)
    ax.set_title('n=%i' % n[i])
    plt.grid()
    plt.show()

# Распределение Пуассона
for i in range(len(n)):
    fig, ax = plt.subplots(1, 1)
    x = sorted(np.random.poisson(10, size=n[i]))
    ax.plot(x, sts.poisson.pmf(x, 10), linewidth=3, color='maroon', ms=8)
    ax.hist(sts.poisson.rvs(10, size=n[i]), color='peachpuff', density=True)
    ax.set_title('n=%i' % n[i])
    plt.grid()
    plt.show()

# Равномерное распределение
for i in range(len(n)):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(sts.uniform.ppf(0.001), sts.uniform.ppf(0.999), n[i])
    ax.plot(x, sts.uniform.pdf(x), linewidth=3, color='maroon')
    ax.hist(sts.uniform.rvs(size=n[i]), color='peachpuff', density=True)
    ax.set_title('n=%i' % n[i])
    plt.grid()
    plt.show()

