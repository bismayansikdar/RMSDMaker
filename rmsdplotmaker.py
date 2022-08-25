import numpy as np
from matplotlib import pyplot as plt
opath='/home/oem/Simulations/4ZT0_RNA/Sim1/RMSD_4TZ0.dat'
npath='/home/oem/Simulations/4ZT0_RNA/Sim1/RMSD_4TZ0NEW.dat'
with open(opath, 'r') as f:
    data=f.read()
data=data.replace('mol0','0')
data=data.replace('NA','0')
data=data.replace('frame','0')
with open(npath,'w') as file:
    file.write(data)
with open(npath, 'r') as f:
    data=f.read()
data=np.loadtxt(path)
frames= data[:,0]
rmsd= data[:,1]
plt.figure()
plt.plot(frames, rmsd)
plt.xlabel('Frames')
plt.ylabel('RMSD')
plt.title('RMSD of 4ZT0')
plt.show()


