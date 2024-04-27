import matplotlib.pyplot as plt
import numpy as np
give=np.array(['A','B','C','D','t','E','O'])
high=np.array([10,49,65,76,78,86,54])
plt.pie(high,labels=give,autopct="int",shadow='True')
plt.show()
plt.hist(give)
plt.show()
plt.bar(give,high,color="pink")
plt.show()
x=np.random.normal(180,10,50)
plt.hist(x)
plt.show()
