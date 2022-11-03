import numpy as np
isolevel = 0
cube = np.array([.5,.7,.2,1,-1,-1,2,0])
corner = np.where(cube < isolevel, 1, 0)
print(corner)
qq = np.random.rand(2,3,4)
x,y,z = qq.shape
print(x,y,z)
aaa = list(np.array([2,3,5]))
bbb = []
bbb.append(aaa)
ccc = list(np.array([6,7,8]))
bbb.append(ccc)
print((np.array(bbb)))


