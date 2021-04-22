import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
 
name = ['体能','失误','反应','速度',]   
theta = np.linspace(0,2*np.pi,len(name),endpoint=False)   
value = np.random.randint(50,100,size=4)   
theta = np.concatenate((theta,[theta[0]])) 
value = np.concatenate((value,[value[0]]))  
 
ax = plt.subplot(1,1,1,projection = 'polar')
ax.plot(theta,value,'m-',lw=1,alpha = 0.75)    
ax.fill(theta,value,'m',alpha = 0.75)           
ax.set_thetagrids(theta*180/np.pi,name)        
ax.set_ylim(0,110)                        
ax.set_theta_zero_location('N')        
ax.set_title('中国乒乓球选手分析',fontsize = 15)
plt.show()
