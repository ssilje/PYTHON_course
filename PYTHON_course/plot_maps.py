import numpy as np
import matplotlib.pyplot as plt




x = np.arange(0, 10, 0.1)

f, ax = plt.subplots()
ax.plot(x, np.sin(x));
plt.show()
# adjusting the resolution 
f.savefig('figure_300.png', dpi=300)


f, ax = plt.subplots()

print('Default size:', f.get_size_inches() * 2.54)

f.set_size_inches(10 / 2.54, 5 / 2.54)

ax.plot(x, np.sin(x));

print('Manually set size:', f.get_size_inches() * 2.54)


