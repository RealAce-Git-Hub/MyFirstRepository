import matplotlib.pyplot as plt
x = [80, 20, 40, 60]
mylabels = ["Math","English","Sports","History"]
myexplode = [0.2, 0, 0, 0]
plt.pie(x, labels = mylabels, explode = myexplode)
plt.legend()
plt.show()