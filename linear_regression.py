"""Linear Regression"""
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt


veri_x = np.array(range(100)).reshape(-1, 1)  
veri_y = np.array([3*x + np.random.normal(0, 20) for x in range(100)]).reshape(-1, 1)  # 2D yapıldı


x_train, x_test, y_train, y_test = train_test_split(veri_x, veri_y, test_size = 0.2, random_state = 42)


lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)


m = lin_reg.coef_[0][0]  
b = lin_reg.intercept_[0]


plt.scatter(veri_x, veri_y,color = "b")
plt.plot(veri_x, m * veri_x + b, color = "r")
plt.xlabel("X Değeri")
plt.ylabel("Y Değeri")
plt.title("Linear Regression")
plt.show()
