"""
from matplotlib import pyplot as plt
plt.figure(1)
plt.subplot(211)
plt.plot([1,0. 2,0. 3,0. 4],0. [4,0. 7,0. 8,0. 9])
#plt.figure(2)
plt.subplot(212)
plt.hist([1,0. 3,0. 7,0. 4,0. 2])
plt.show()
"""
"""
import matplotlib.pyplot as plt

scores = [0.82, 0.88, 0.96, 0.90, 0.87, 0.88, 0.81, 0.90, 0.90, 0.74, 0.82, 0.73, 0.92, 0.76, 0.87, 0.90, 0.90, 0.74, 0.72, 0.88, 0.62, 0.70, 0.82, 0.82, 0.90, 0.74, 0.65, 0.86, 0.89, 0.97, 0.46, 0.89, 0.82, 0.87, 0.90, 0.96, 0.92, 0.60, 0.91, 0.26, 0.92, 0.91, 0.60, 0.94, 0.87, 0.91, 0.92, 0.98, 0.96, 0.96, 0.96, 0.81, 0.67, 0.81, 0.91, 0.94, 0.94, 0.96, 0.95, 0.90]
bins = [0.6, 0.7, 0.73, 0.77, 0.8, 0.83, 0.87, 0.9, 0.93, 1]
plt.hist(scores, bins)
plt.xticks(bins, ['F', 'D', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A'])
plt.show()
"""

class Fraction:
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator);



a = Fraction(1, 2)
print(a)
     













