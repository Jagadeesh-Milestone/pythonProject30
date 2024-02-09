#line style,color,markersize:
import matplotlib.pyplot as plt
import numpy as np

x=np.array([3,8,1,10])
#plt.plot(x,'o:r')
#plt.plot(x,'o-b')
#plt.plot(x,'o--g')
#plt.plot(x,'o-.c')
#plt.plot(x,'o:y')
#plt.plot(x,'o:',ms=20)
plt.plot(x,'s:g',ms=10,mec='b',mfc='c')
plt.show()
#mfc--marker face color(cyan)
#mec--marker edge color(blue)
#ms--marker size(10 pixel)
#g--line color(green)
#:--line size(dotted)
#s--marker style(square).