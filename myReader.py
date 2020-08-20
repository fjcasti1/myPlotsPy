#!/usr/bin/env python
from numpy import *

def find_tokens(basename):
  bn_list = basename.split('_')
  token_list = []
  for item in bn_list:
    token = ''
    for char in item:
      if char.isdigit():
        if token is not '':
          token_list.append(token)
          break
      else:
        token += char
  return token_list

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

#### Knife Edge Finite Differences ####

def read_kedgeTop_restart(f):
  hdt = dtype('(4)i4, (4)f8, (2)i4, (7)f8, i4') # header data type
  pdt = dtype('i4') # padding data type
  with open(f,'rb') as fh:
    header= fromfile(fh,dtype=hdt,count=1)
    Nz    = header[0][0][1]  # M=Nz, N=Nr
    Nr    = header[0][0][2]  # M=Nz, N=Nr
    Gamma = header[0][3][5]
    eta   = header[0][3][6]
    t     = header[0][1][3]
    udt   = dtype('({:d},{:d}) f8'.format(Nz,Nr))
    s, x, g = read_FD_field(fh,udt,pdt)
  z = linspace(0, Gamma, Nz)
  r = linspace(0, 1, Nr)
  Z,R = meshgrid(z,r,indexing='ij')
  d = {
    'sf' : s,
    'wt' : x,
    'Lt' : g,
    't'  : t,
  }
  return R,Z,d

def read_kedgeTop_fields(fheader,udt,pdt,pcount=1):
  pad     = fromfile(fheader,dtype=pdt,count=1)
  field_s = fromfile(fheader,dtype=udt,count=1)
  field_x = fromfile(fheader,dtype=udt,count=1)
  field_g = fromfile(fheader,dtype=udt,count=1)
  pad     = fromfile(fheader,dtype=pdt,count=1)
  s = field_s[0].astype(double).T
  x = field_x[0].astype(double).T
  g = field_g[0].astype(double).T
  return (s,x,g)

#### Free Surface Finite Differences ####

def read_freeSurfTop_restart(f):
  hdt = dtype('(3)i4, (4)f8, (2)i4, (6)f8, i4') # header data type
  pdt = dtype('i4') # padding data type
  with open(f,'rb') as fh:
    header= fromfile(fh,dtype=hdt,count=1)
    Nz    = header[0][0][1]  # M=Nz, N=Nr
    Nr    = header[0][0][2]  # M=Nz, N=Nr
    t     = header[0][1][3]
    Gamma = header[0][3][5]
    udt   = dtype('({:d},{:d}) f8'.format(Nz,Nr)) # fields data type
    cdt   = dtype('({:d}) f8'.format(Nr)) # concentration data type
    s, x, g = read_freeSurfTop_fields(fh,udt,cdt,pdt)
  z = linspace(0, Gamma, Nz)
  r = linspace(0, 1, Nr)
  Z,R = meshgrid(z,r,indexing='ij')
  d = {
    'sf' : s,
    'wt' : x,
    'Lt' : g,
    'c'  : c,
    't'  : t,
  }
  return R,Z,d

def read_freeSurfTop_fields(fheader,udt,cdt,pdt):
  pad     = fromfile(fheader,dtype=pdt,count=1)
  field_s = fromfile(fheader,dtype=udt,count=1)
  field_x = fromfile(fheader,dtype=udt,count=1)
  field_g = fromfile(fheader,dtype=udt,count=1)
  field_c = fromfile(fheader,dtype=cdt,count=1)
  pad     = fromfile(fheader,dtype=pdt,count=1)
  s = field_s[0].astype(double).T
  x = field_x[0].astype(double).T
  g = field_g[0].astype(double).T
  c = field_c[0].astype(double)
  return (s,x,g,c)

#### Spectral vtk files ####

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

