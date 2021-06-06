# python3 dataGenerator.py

import numpy as np

for i in range(1000):
    rnd1 = np.random.choice([2, 4])
    rnd2 = np.random.uniform(0, 0.33)
    rnd3 = np.random.choice([2, 3])
    rnd4 = np.random.uniform(0.67, 1)
    rnd5 = np.random.choice([1, 3])
    rnd6 = np.random.uniform(0.34, 0.66)
    f = open('data.csv', 'a')
    f.write('1;' + '2;' + '%d;' % rnd1 + '%f;' % rnd2 + '2;' + '2;' + '\n')  # audial
    f.write('0;' + '3;' + '%d;' % rnd3 + '%f;' % rnd4 + '3;' + '3;' + '\n')  # visual
    f.write('1;' + '1;' + '%d;' % rnd5 + '%f;' % rnd6 + '1;' + '1;' + '\n')  # discrete
print(f)
f.close()
