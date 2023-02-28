import numpy as np
import matplotlib.pyplot as plt

# 区分求積法をゴリ押しする

r = np.pi/(10 ** 5)

x = np.arange(0, np.pi, r)
y = np.sin(x)

plt.figure(figsize=(16, 9))
plt.grid()
plt.plot(x, y, color="#0000ff")


s = 0
for i in range(len(x)):
    s += r * np.sin(r)

print(r)
