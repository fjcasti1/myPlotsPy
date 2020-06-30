#!/usr/bin/env python
import pylab
from myColors import *

def parse_token(bn,token):
    """
    Obtains the value associated with the given within the basename.

    Parameters
    ----------
    bn: string, expected.
        The basename fo the file.
    token: string, expected.
        The token to be parsed.

    Returns
    -------
        The value associated with the token.

    Example
    -------
        bn = str1val1_str2val2_str3val3.ext
        tokens = [str1,str2,str3]
        values = [parse_token(bn,token) for token in tokens]
        values will be [val1,val2,val3]
    """
    return bn.split(token)[1].split('_')[0]

def read_vtk(f):
    import pyvista as pv
    """
    Reads a vtk file
    It requires PyVista.
    """
    mesh = pv.read(f)
    pts  = mesh.points
    M,N  = [ mesh.dimensions[k] for k in [0,-1] ]
    R,Z  = [ x.reshape(M,N).T for x in pts[:,[0,-1]].T ]
    d    = { k:mesh[k].reshape(M,N).T for k in mesh.array_names }
    return R,Z,d

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
