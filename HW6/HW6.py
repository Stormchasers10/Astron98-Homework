import numpy as np
import matplotlib.pyplot as plt
import random

#1
def sine_wave(A,w,x):
    return A * np.sin(w * x)

plt.figure(figsize=(10, 6))
A_w_array = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])

for A, w in A_w_array:
    x = np.linspace(0,2*np.pi,1000)
    y = sine_wave(A,w,x)
    plt.plot(x, y, label=f"Sine Function A={A}, w={w}")

plt.xlabel('x')
plt.ylabel('y')
plt.title('5 Different Sine Functions')
plt.legend()
plt.grid(True)
plt.show()

#2
list_1 = []
list_2 = []

x_1 = []
x_2 = []

i = 0
plt.figure(figsize=(10, 6))

while i < 40:
    random_integer1 = random.randint(1, 100)
    random_integer2 = random.randint(1, 100)
    i = i + 1
    list_1.append(random_integer1)
    list_2.append(random_integer2)

final_list_1 = list_1
final_list_2 = list_2

for index, _ in enumerate(final_list_1):
    x_1.append(index)

plt.plot(x_1, final_list_1, linewidth = 10, color = 'orange', label=f"Line 1")

for index, _ in enumerate(final_list_2):
    x_2.append(index)

plt.plot(x_2, final_list_2, linestyle = '--', color = 'red', label=f"Line 2")

plt.xlabel('x (index)')
plt.ylabel('y (rand num list)')
plt.title('2 Lines')
plt.legend()
plt.grid(True)
plt.show()