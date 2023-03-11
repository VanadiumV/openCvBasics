#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install opencv-python


# In[3]:


import cv2
import matplotlib.pyplot as plt


# In[7]:


#Read Images

img=cv2.imread("atcoder.png")
print(img.shape)

newImg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #CONVERT BGR TO RGB


# In[4]:


print(img[0][0])  #RGB


# In[6]:


#Show this image
plt.imshow(img)    #this will appear a little blue because of bgr format..so convert it into rgb


# In[8]:


plt.imshow(newImg)
plt.axis("off")  #say NO to nos along axis 
plt.show()  #tho it has downgraded quality here in my case xD


# In[ ]:




