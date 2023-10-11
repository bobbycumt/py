# 版权所有：许志晗
import numpy as np
import matplotlib.pyplot as plt

def func():
    x2 = np.linspace(0, 1000, 1000)  # 1000 points
    y2 = 0.995**x2
    z2 = 1.005**x2

    plt.plot(x2, z2, label="$1.005^n$", color="red", linewidth=2)
    plt.plot(x2, y2, "b--", label="$0.995^n$", linewidth=1.5)
    plt.xlabel("Days")
    plt.ylabel("Result")
    plt.title("The Story of $0.995^n$ and $1.005^n$")
    plt.xlim(0, 1000)
    plt.ylim(-1, 150)
    plt.legend()
    plt.show()

def main():
    n = 0
    y1 = 0.995**n
    z1 = 1.005**n
    x = []
    y = []
    z = []
    plt.figure('许志晗作品',figsize=(8, 8))
    while n < 1000:
        y1 = 0.995**n
        z1 = 1.005**n
        plt.clf()
        plt.xlabel("Days")
        plt.ylabel("Result")
        plt.title("The Story of $0.995^n$ and $1.005^n$")
        x.append(n)
        y.append(y1)
        z.append(z1)
        plt.xlim(0, 1000)
        plt.ylim(-1, 150)
        plt.plot(x, z, color='red')
        plt.plot(x, y, "b--")
        n += 1
        plt.pause(0.01)
        plt.ioff()
    plt.clf()
    func()

if __name__ == "__main__":
    main()
