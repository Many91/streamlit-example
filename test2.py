import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


imgs = [np.random.random((50,50)) for _ in range(4)]

#fig 1 et fig2 fonctionnel

fig1 = plt.figure(figsize = (3,3))
plt.subplot(2, 2, 1);
plt.imshow(imgs[0]);
plt.axis('off');
plt.subplot(2, 2, 2);
plt.imshow(imgs[1]);
plt.axis('off');
plt.subplot(2, 2, 3);
plt.imshow(imgs[2]);
plt.axis('off');
plt.subplot(2, 2, 4);
plt.imshow(imgs[3]);
plt.axis('off');
plt.subplots_adjust(wspace=.025, hspace=.025)
st.pyplot(fig1)



fig2 = plt.figure(figsize = (3,3))
plt.subplot(2, 2, 1);
plt.imshow(imgs[0]);
plt.axis('off');
st.pyplot(fig2)
