#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10,0.001)
y=np.sinc(x)
plt.xlim(-10,10)
plt.ylim(-0.4,1)
plt.plot(x,y)
plt.show()


# In[11]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import mpl_toolkits.axisartist as axisartist
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16,12))
ax=fig.add_subplot(projection='3d')

x=np.arange(-10,10,0.001)
y=0+0*x
ax.scatter(x,y,s=1,  zdir='z',color='black')

a=np.arange(-0.04,0.04,0.0001)
b=0+0*a
ax.scatter(a,b,s=1,  zdir='x',color='black')
r = 0.01
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z=6+0*x+0*y  
z1=-6+0*x+0*y
z2=4+0*x+0*y
z3=-4+0*x+0*y
z4=2+0*x+0*y
z5=-2+0*x+0*y
z6=0*x+0*y
plt.plot(z,x,y,color='black',linestyle='--')
plt.plot(z1,x,y,color='black',linestyle='--')
plt.plot(z2,x,y,color='black',linestyle='--')
plt.plot(z3,x,y,color='black',linestyle='--')
plt.plot(z4,x,y,color='black',linestyle='--')
plt.plot(z5,x,y,color='black',linestyle='--')
plt.plot(z6,x,y,color='black',linestyle='--')
ax.quiver(0,0,0,0,0.5,0,length=0.01,color='black',normalize=True)
ax.quiver(-2,0,0,0,0.5,-1,length=0.01,color='black',normalize=True)
ax.quiver(2,0,0,0,0.5,1,length=0.01,color='black',normalize=True)
ax.quiver(-4,0,0,0,-0.5,-1,length=0.01,color='black',normalize=True)
ax.quiver(4,0,0,0,-0.5,1,length=0.01,color='black',normalize=True)
ax.quiver(6,0,0,0,-0.5,-1,length=0.01,color='black',normalize=True)
ax.quiver(-6,0,0,0,-0.5,1,length=0.01,color='black',normalize=True)
c=np.arange(-0.04,0.04,0.0001)
d=0+0*c
ax.scatter(d,c,s=1,  zdir='x',color='black')
ax.text(0.5, -0.005, -0.001, "0", color='black')
ax.text(10.5, 0, 0, "w", color='black')
ax.text(0.1, 0.04, 0, "x", color='black')
ax.text(0.1, 0, 0.04, "y", color='black')
ax.text(2, -0.005, -0.001, "ω0", color='black')
ax.text(4, -0.005, -0.001, "2ω0", color='black')
ax.text(5.5, 0.005, -0.001, "3ω0", color='black')
ax.text(-2.5, 0.005, -0.001, "-ω0", color='black')
ax.text(-4.5, 0.005, -0.001, "-2ω0", color='black')
ax.text(-6, -0.005, -0.001, "-3ω0", color='black')
plt.xlim(-7,7)
plt.ylim(-0.05,0.05)
ax.set_zlim(-0.05,0.05)
plt.axis('off')
plt.show()


# In[10]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import mpl_toolkits.axisartist as axisartist
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(16,12))
ax=fig.add_subplot(projection='3d')
x=np.arange(-15,15,0.001)
y=0+0*x
ax.scatter(x,y,s=0.01,  zdir='z',color='black')
ax.quiver(0,0,0,0,0.5,0,length=0.5,color='black',normalize=True)
ax.quiver(-6,0,0,0,-0.5,0,length=0.106,color='black',normalize=True)
ax.quiver(6,0,0,0,-0.5,0,length=0.106,color='black',normalize=True)
ax.quiver(2,0,0,0,0.5,0,length=0.318,color='black',normalize=True)
ax.quiver(-2,0,0,0,0.5,0,length=0.318,color='black',normalize=True)
ax.quiver(10,0,0,0,0.5,0,length=0.063,color='black',normalize=True)
ax.quiver(-10,0,0,0,0.5,0,length=0.063,color='black',normalize=True)
ax.text(0, -0.05, -0.05, "0", color='black')
ax.text(2, -0.05, -0.05, "1", color='black')
ax.text(5.7, 0.05, 0.01, "3", color='black')
ax.text(10.2, -0.1, -0.01, "5", color='black')
ax.text(-2.5, -0.05, -0.05, "-1", color='black')
ax.text(-6.3, 0.05, 0.01, "-3", color='black')
ax.text(-9.8, -0.1, -0.01, "-5", color='black')
ax.text(0, 0.5, 0.01, "0.5", color='black')
ax.text(2, 0.3, 0.05, "0.318", color='black')
ax.text(5.3, -0.05, -0.15, "-0.106", color='black')
ax.text(10, 0.05, 0.05,"0.063", color='black')
ax.text(-2, 0.3,0.05, "0.318", color='black')
ax.text(-6.8, -0.1,-0.15, "-0.106", color='black')
ax.text(-10, 0.05,0.05, "0.063", color='black')
ax.text(14, 0,0.001, "f", color='black')
r = 0.3
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z=2+0*x+0*y  
z1=-2+0*x+0*y
plt.plot(z,x,y,color='black',linestyle='--')
plt.plot(z1,x,y,color='black',linestyle='--')
r = 0.1
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z=6+0*x+0*y  
z1=-6+0*x+0*y
plt.plot(z,x,y,color='black',linestyle='--')
plt.plot(z1,x,y,color='black',linestyle='--')
r = 0.08
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z=10+0*x+0*y  
z1=-10+0*x+0*y
plt.plot(z,x,y,color='black',linestyle='--')
plt.plot(z1,x,y,color='black',linestyle='--')

plt.xlim(-7,7)
plt.ylim(-1,1)
ax.set_zlim(-0.8,0.8)
plt.axis('off')
plt.show()


# In[2]:


from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
fig=plt.figure()
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
x_f = np.arange(-6,7,1)
y_f = np.sinc(x_f/2)/2
plt.xlim(-5.8,5.8)
plt.stem(x_f,y_f,use_line_collection=True,linefmt="black", markerfmt="C5o", basefmt="black")
for i in range(0,7,1):
    a=[-5.5,-3.5,-1.5,-0.2,0.5,2.5,4.5]
    a1=[-5.2,-3.2,-1.2,-0.1,0.8,2.8,4.8]
    b=[0.1,-0.18,0.35,0.53,0.35,-0.18,0.1]
    b1=[-0.04,0.03,-0.04,-0.04,-0.04,0.03,-0.04]
    c=[0.063,-0.106,0.318,0.5,0.318,-0.106,0.063]
    d=[-5,-3,-1,0,1,3,5]
    plt.text(a[i], b[i], c[i], weight="bold", color="black")
    plt.text(a1[i], b1[i], d[i], weight="bold", color="black")
plt.text(6.3, 0, 'f', weight="bold", color="black")
plt.show()


# In[4]:


from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
fig=plt.figure()
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
x_f = np.arange(-6,7,1)
y_f = abs(np.sinc(x_f/2)/2)
plt.xlim(-5.8,5.8)
plt.stem(x_f,y_f,use_line_collection=True,linefmt="black", markerfmt="C5o", basefmt="black")
for i in range(0,7,1):
    a=[-5.5,-3.5,-1.5,-0.2,0.5,2.5,4.5]
    a1=[-5.2,-3.2,-1.2,-0.1,0.8,2.8,4.8]
    b=[0.1,0.13,0.35,0.53,0.35,0.13,0.1]
    b1=[-0.03,-0.03,-0.03,-0.03,-0.03,-0.03,-0.03]
    c=[0.063,0.106,0.318,0.5,0.318,0.106,0.063]
    d=[-5,-3,-1,0,1,3,5]
    plt.text(a[i], b[i], c[i], weight="bold", color="black")
    plt.text(a1[i], b1[i], d[i], weight="bold", color="black")
plt.text(6.3, 0, 'f', weight="bold", color="black")
plt.show()


# In[3]:


from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
fig=plt.figure()
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>")
x_f = np.arange(-5,7,2)
y_f = np.sinc(x_f/2)/2
y2=np.angle(y_f)
plt.stem(x_f,y2,use_line_collection=True,linefmt="black", markerfmt="bo", basefmt="black")
plt.text(6, 0, 'f', weight="bold", color="black")
plt.xticks([-5,-3,-1,0,1,3,5])
plt.ylim(-1,4)
for i in range(0,7,1):
    a=[-5,-3,-1,0,1,3,5]
    b=[0.35,3.6,0.35,0.35,0.35,3.6,0.35]
    c=[0,'π',0,0,0,'π',0]
    plt.text(a[i], b[i], c[i], fontsize=12,verticalalignment='top',horizontalalignment='center', weight="bold", color="black")
plt.plot(0,0,'bo')
plt.show()


# In[12]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import mpl_toolkits.axisartist as axisartist
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16,12))
ax=fig.add_subplot(projection='3d')

x=np.arange(-10,10,0.001)
y=0+0*x
ax.scatter(x,y,s=1,  zdir='z',color='black')

a=np.arange(-0.02,0.02,0.0001)
b=0+0*a
ax.scatter(a,b,s=1,  zdir='x',color='black')
x,y,z=([0,0],
        [0,0],
       [-5,5])
u,v,w=([0,0],
      [0.5,0.5],
      [0,0])
ax.quiver(z,x,y,u,v,w,length=0.01,color='black',normalize=True)
c=np.arange(-0.02,0.02,0.0001)
d=0+0*c
ax.scatter(d,c,s=1,  zdir='x',color='black')
ax.text(1, -0.005, 0, "0", color='black')
ax.text(10.5, 0, 0, "w", color='black')
ax.text(0.1, 0.02, 0, "x", color='black')
ax.text(0.1, 0, 0.02, "y", color='black')
ax.text(4, 0.015, -0.001, "0.5", color='black')
ax.text(-8, 0.025, -0.006, "0.5", color='black')
r = 0.01
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z=5+0*x+0*y  
z1=-5+0*x+0*y
plt.plot(z,x,y,color='black',linestyle='--')
plt.plot(z1,x,y,color='black',linestyle='--')
plt.xlim(-10,10)
plt.ylim(-0.03,0.03)
ax.set_zlim(-0.02,0.02)
plt.axis('off')
plt.show()


# In[5]:


from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
from matplotlib import font_manager as fm, rcParams
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure()
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
x=np.arange(-6,6,4)
y=5+0*x
plt.stem(x,y,use_line_collection=True,linefmt="black", markerfmt="C5o", basefmt="black")
plt.text(4.5, 0, 'ω', fontsize=20,weight="bold", color="black")
plt.text(-0.5, 11,"幅度",fontsize=20, weight="bold", color="black")
plt.text(1.5, -0.8, 'ω0', fontsize=20,weight="bold", color="black")
plt.text(-2.5, -0.8, '-ω0', fontsize=20,weight="bold", color="black")
plt.text(1.5, 5.5, '0.5', fontsize=20,weight="bold", color="black")
plt.text(-2.5, 5.5, '0.5', fontsize=20,weight="bold", color="black")
plt.text(-0.1, -0.7, '0', fontsize=20,weight="bold", color="black")
plt.xlim(-4,4)
plt.ylim(0,10)
plt.xticks([])
plt.yticks([])
plt.show()


# In[6]:


from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
from matplotlib import font_manager as fm, rcParams
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure()
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
x=np.arange(-6,6,4)
y=0+0*x
plt.stem(x,y,use_line_collection=True,linefmt="black", markerfmt="ro")
plt.text(4.5, 0, 'ω', fontsize=20,weight="bold", color="black")
plt.text(-0.5, 11,"相位",fontsize=20, weight="bold", color="black")
plt.text(1.5, -0.8, 'ω0', fontsize=20,weight="bold", color="black")
plt.text(-2.5, -0.8, '-ω0', fontsize=20,weight="bold", color="black")
plt.text(1.9, 0.5, '0', fontsize=20,weight="bold", color="black")
plt.text(-2.1, 0.5, '0', fontsize=20,weight="bold", color="black")
plt.text(-0.1, -0.7, '0', fontsize=20,weight="bold", color="black")
plt.xlim(-4,4)
plt.ylim(0,10)
plt.xticks([])
plt.yticks([])
plt.show()


# In[15]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import mpl_toolkits.axisartist as axisartist
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16,12))
ax=fig.add_subplot(projection='3d')

x=np.arange(-5,5,0.001)
y=0+0*x
ax.scatter(x,y,s=1,  zdir='z',color='black')

a=np.arange(-0.03,0.03,0.0001)
b=0+0*a
ax.scatter(a,b,s=1,  zdir='x',color='black')
x,y,z=([0,0],
        [0,0],
       [-3,3])
u,v,w=([0,0],
      [0,0],
      [0.5,-0.5])
ax.quiver(z,x,y,u,v,w,length=0.01,color='black',normalize=True)
c=np.arange(-0.02,0.02,0.0001)
d=0+0*c
ax.scatter(d,c,s=1,  zdir='x',color='black')
ax.text(0.5, -0.005, 0, "0", color='black')
ax.text(5.2, 0, 0, "w", color='black')
ax.text(0.1, 0.03, 0, "x", color='black')
ax.text(0.1, 0, 0.02, "y", color='black')
ax.text(5.5, -0.03, 0, "-0.5j", color='black')
ax.text(-7, 0.038, -0.004, "0.5j", color='black')
r = 0.01
a, b = (0., 0.)
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z=3+0*x+0*y  
z1=-3+0*x+0*y
plt.plot(z,x,y,color='black',linestyle='--')
plt.plot(z1,x,y,color='black',linestyle='--')
plt.xlim(-5,5)
plt.ylim(-0.03,0.03)
ax.set_zlim(-0.02,0.02)
plt.axis('off')
plt.show()


# In[16]:


from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
from matplotlib import font_manager as fm, rcParams
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure()
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
x=np.arange(-6,6,4)
y=5+0*x
plt.stem(x,y,use_line_collection=True,linefmt="black", markerfmt="C5o", basefmt="black")
plt.text(4.5, 0, 'ω', fontsize=20,weight="bold", color="black")
plt.text(-0.5, 11,"幅度",fontsize=20, weight="bold", color="black")
plt.text(1.5, -0.8, 'ω0', fontsize=20,weight="bold", color="black")
plt.text(-2.5, -0.8, '-ω0', fontsize=20,weight="bold", color="black")
plt.text(1.5, 5.5, '0.5', fontsize=20,weight="bold", color="black")
plt.text(-2.5, 5.5, '0.5', fontsize=20,weight="bold", color="black")
plt.text(-0.1, -0.7, '0', fontsize=20,weight="bold", color="black")
plt.xlim(-4,4)
plt.ylim(0,10)
plt.xticks([])
plt.yticks([])
plt.show()


# In[7]:


from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
from matplotlib import font_manager as fm, rcParams
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure()
ax = axisartist.Subplot(fig, 111) 
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
x=np.arange(-6,6,4)
inte= [1 if (i<0) else 0 for i in x]
inte1 = [1 if (i>=0) else 0 for i in x]
y=(5+0*x)*inte+(-5+0*x)*inte1
plt.stem(x,y,use_line_collection=True,linefmt="black", markerfmt="C5o", basefmt="black")
plt.text(4.5, 0, 'ω', fontsize=20,weight="bold", color="black")
plt.text(-0.5, 12,"相位",fontsize=20, weight="bold", color="black")
plt.text(1.5, 1, 'ω0', fontsize=20,weight="bold", color="black")
plt.text(-2.5, -1.5, '-ω0', fontsize=20,weight="bold", color="black")
plt.text(1.5, -6.5, '-π/2', fontsize=20,weight="bold", color="black")
plt.text(-2.5, 5.5, 'π/2', fontsize=20,weight="bold", color="black")
plt.text(0.2, -1.5, '0', fontsize=20,weight="bold", color="black")
plt.xlim(-4,4)
plt.ylim(-10,10)
plt.xticks([])
plt.yticks([])
plt.show()


# In[ ]:




