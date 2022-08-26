import numpy as np
from matplotlib import pyplot as plt
opath='/home/oem/Simulations/4ZT0_RNA/Sim1/RMSD_4TZ0.dat'
npath='/home/oem/Simulations/4ZT0_RNA/Sim1/RMSD_4TZ0NEW.dat'
opath1='/home/oem/Simulations/4CMP_WithoutIons/4cmprmsdwithoutIons.dat'
npath1='/home/oem/Simulations/4CMP_WithoutIons/4cmprmsdwithoutIonsNEW.dat'
opath2='/home/oem/Simulations/4Cmp_Mg/trajrmsd_4cmp.dat'
npath2='/home/oem/Simulations/4Cmp_Mg/trajrmsd_4cmpNew.dat'
opath3='/home/oem/Simulations/4CMQWithIons/4cmq.dat'
npath3='/home/oem/Simulations/4CMQWithIons/4cmqNEW.dat'
opath4='/home/oem/Simulations/5F9RWithIons/trajrmsd_5f9r.dat'
npath4='/home/oem/Simulations/5F9RWithIons/trajrmsd_5f9rNEW.dat'
with open(opath, 'r') as f:
    data=f.read()
data=data.replace('mol0','0')
data=data.replace('NA','0')
data=data.replace('frame','0')
with open(npath,'w') as file:
    file.write(data)
with open(npath, 'r') as f:
    data=f.read()
with open(opath1, 'r') as f1:
    data1=f1.read()
data1=data1.replace('mol0','0')
data1=data1.replace('NA','0')
data1=data1.replace('frame','0')
with open(npath1,'w') as file1:
   file1.write(data1)
with open(npath1, 'r') as f1:
   data1=f1.read()
with open(opath2, 'r') as f2:
    data2=f2.read()
data2=data2.replace('mol0','0')
data2=data2.replace('NA','0')
data2=data2.replace('time','0')
with open(npath2,'w') as file2:
   file2.write(data2)
with open(npath2, 'r') as f2:
   data2=f2.read()
with open(opath3, 'r') as f3:
    data3=f3.read()
data3=data3.replace('mol0','0')
data3=data3.replace('NA','0')
data3=data3.replace('time','0')
with open(npath3,'w') as file3:
   file3.write(data3)
with open(npath3, 'r') as f3:
   data3=f3.read()
with open(opath4, 'r') as f4:
    data4=f4.read()
data4=data4.replace('mol0','0')
data4=data4.replace('NA','0')
data4=data4.replace('Time','0')
data4=data4.replace('RMSD','0')
with open(npath4,'w') as file4:
   file4.write(data4)
with open(npath4, 'r') as f4:
   data4=f4.read()
data=np.loadtxt(npath)
frames= data[:,0]
time=frames*0.04
rmsd= data[:,1]
data1=np.loadtxt(npath1)
frames1=data1[:,0]
time1=frames1*0.08
rmsd1=data1[:,1]
data2=np.loadtxt(npath2)
time2=data2[:,0]
rmsd2=data2[:,1]
data3=np.loadtxt(npath3)
time3=data3[:,0]
rmsd3=data3[:,1]
data4=np.loadtxt(npath4)
time4=data4[:,0]
rmsd4=data4[:,1]
plt.figure()
plt.plot(time, rmsd, label='4ZT0WithIons')
plt.plot(time1,rmsd1, label='4CMPWithouIons')
plt.plot(time2,rmsd2, label='4CMPWithIons')
plt.plot(time3,rmsd3, label='4CMQWithIons')
plt.plot(time4,rmsd4, label='45F9RwithIons')
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (Å)')
plt.title('RMSD of 4ZT0 and 4CMP')
plt.legend()
plt.show()


