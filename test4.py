import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

model = svm.SVC(C=1.5, kernel='poly')
x = np.random.random(size=(1000, 3))
y = np.random.randint(low=0, high=2, size=(1000,))
model.fit(x, y)
res = model.predict(np.array([[0.2, 0.1, 0.5]]))
print(res)