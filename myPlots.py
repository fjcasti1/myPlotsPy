#!/usr/bin/env python
import pylab
import ctypes
from myColors import *

try:
  mkl_rt = ctypes.CDLL('libmkl_rt.so')
  mkl_max_threads = mkl_rt.mkl_get_max_threads()

  def mkl_set_num_threads(threads):
    th = threads
    if th > mkl_max_threads:
      print('Threads: {:d} > {:d} Max Threads'.format(threads,mkl_max_threads))
      th = 1
    mkl_rt.mkl_set_num_threads(ctypes.byref(ctypes.c_int(th)))
    print('MKL THREADS SET: {:d}'.format(th))
    return None
except Exception as ex:
  print('MKL ERROR -- ',ex)

def no_ax_fig(k=1,figBaseSize=6,Gamma=1):
    """
    Generates a figure of size (figBaseSize,Gamma*figBaseSize) with 1 axes.
    The axes and the box around the figure are not visible

    Parameters
    ----------
    k: integer, expected
        Figure number.
    figBaseSize: integer, optional
        Horizontal size of the figure.
        Default value is 6.
    Gamma: real, optional
        Aspect ratio H/L, where H is the height of the figure and L is its horizontal length.
        Useful when a non-square figure is desired.
        Default value is 1 (squared figure).

    Returns
    -------
        fig: 'Figure'
        ax:  'matplotlib.axes._axes.Axes'
    """
    fig = pylab.figure(k,figsize=(figBaseSize,Gamma*figBaseSize))
    ax  = pylab.Axes(fig,[0,0,1,1]) # Size of canvas compared to figure
    ax.set_axis_off() # No Box around
    fig.clf()
    fig.add_axes(ax)
    for a in fig.axes:
        a.get_xaxis().set_visible(False)
        a.get_yaxis().set_visible(False)
    return fig,ax

def mycontourf(*args,lc='face',lw=0,**kwargs):
    cf = pylab.contourf(*args,**kwargs)
    for c in cf.collections:
        c.set_edgecolor(lc)
        c.set_linewidth(lw)
    return None
