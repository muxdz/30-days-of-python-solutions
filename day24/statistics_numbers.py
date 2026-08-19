import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

normal_array = np.random.normal(0, 1, 100)

print(normal_array)

sns.set_theme()
plt.hist(normal_array, color='green', bins=20)
plt.show()

# numpy arrange

evens = np.arange(0, 10, 2)
odds = np.arange(1, 10, 2)

print(evens)
print(odds)

# numpy linspace

evenly_spaced = np.linspace(0, 10, 5)
unevenly_spaced = np.linspace(0, 10, 5, endpoint=False)

print(evenly_spaced)
print(unevenly_spaced)

# numpy logspace

logarithmically_spaced = np.logspace(0, 10, 5)
print(logarithmically_spaced)

# numpy complex

complex_array = np.array([1+0j, 0+1j, 0-1j, -1+0j])
print(complex_array)
print(complex_array.dtype)
print(complex_array.size)
print(complex_array.shape)
print(complex_array.itemsize)


# numpy statistical functions

normal_dist = np.random.normal(0, 1, 100)

print('minimum:', normal_dist.min())
print('maximum:', normal_dist.max())
print('mean:', normal_dist.mean())
print('variance:', normal_dist.var())
print('standard deviation:', normal_dist.std())
print('minimum:', normal_dist.min())
print('maximum:', normal_dist.max())

two_dimensional_array = np.array([[0,1,2], [3,4,5], [6,7,8]])
print('column with min:', two_dimensional_array.min(axis=0))
print('row with min:', two_dimensional_array.min(axis=1))
print('column with max:', two_dimensional_array.max(axis=0))
print('row with max:', two_dimensional_array.max(axis=1))

# repeating sequence

a = [1,2,3]

tile = np.tile(a, 3)
print('Tiled:', tile)

repeated = np.repeat(a, 3)
print('Repeated:', repeated)

# numpy random

one_random = np.random.random()
one_random_in = np.random

print(one_random)
print(one_random_in)

random_array = np.random.random((3, 3))
print(random_array)

choice = np.random.choice([1,2,3,4,5], 3)
print(choice)

array = [1,2,3,4,5]
np.random.shuffle(array)
print(array)

# graphs

normal_dist = np.random.normal(5, 0.5, 100)
plt.hist(normal_array, color='green', bins=21)
plt.show()

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(temp, pressure)

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()