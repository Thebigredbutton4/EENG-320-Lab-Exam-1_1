#Daniel Yermakov

import numpy as np
import matplotlib.pyplot as plt

#Problem 1
def signalx(x):
  y = []
  for xval in x:
    if xval < -2:
      f = 0
    elif xval >= -2 and xval < -1:
      f = 2*xval + 4
    elif xval >= -1 and xval < 0:
      f = 2*xval + 2
    elif xval >= 0 and xval < 1:
      f = 2
    else:
      f = 0
    y.append(f)
  return y

def evenprt(x,y):
  yt = [];
  y_inv = np.flip(y)
  for yval, yvali in zip(y,y_inv):
    y_temp = 0.5*(yval+yvali)
    yt.append(y_temp)
  t = x
  return t,yt;

def oddprt(x,y):
  yt = [];
  y_inv = np.flip(y)
  for yval, yvali in zip(y,y_inv):
    y_temp = 0.5*(yval-yvali)
    yt.append(y_temp)
  t = x
  return t,yt;

x = np.arange(-4,4,0.013)
signalfunc = signalx(x)
ev = evenprt(x,signalfunc)
od = oddprt(x,signalfunc)

plt.figure()
plt.subplot(311); plt.plot(x,signalfunc,'g-', linewidth=4)
plt.title('x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.subplot(312); plt.plot(ev[0],ev[1],'b--', linewidth=3)
plt.title('Even part of function')
plt.xlabel('t')
plt.ylabel('xe(t)')
plt.subplot(313); plt.plot(od[0],od[1],'r', linewidth=2)
plt.title('Odd part of function')
plt.xlabel('t')
plt.ylabel('xo(t)')

#Problem 2

def unit_conv(opt, val):
  if opt == 'FeetToCm':
    newval = val*30.48

  elif opt == 'CmToFee':
    newval = val/30.48

  return newval

while(1):
  opt = input('Choose and enter FeetToCm or CmToFee = \n')
  val = float(input('Enter a value to be converted = \n'))
  if opt == 'FeetToCm':
    print(f'The given {val} [ft] is corresponding to {unit_conv(opt, val)}[cm]')
  elif opt == 'CmToFee':
    print(f'The given {val} [cm] is corresponding to {unit_conv(opt,val)} [ft]')
  else:
    print("You need to select either FeetToCm or CmToFee")