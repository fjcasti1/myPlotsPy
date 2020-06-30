#!/usr/bin/env python
from matplotlib import colors

myBlues = colors.LinearSegmentedColormap.from_list('myBlues',[
   ( 0.   ,'#0000AF'),
   ( 0.5  ,'#0000CC'),
   ( 1.   ,'#0000FF'),
])

myReds  = colors.LinearSegmentedColormap.from_list('myReds',[
  ( 0.   ,'#FF0000'),
  ( 0.5  ,'#CD0000'),
  ( 1.   ,'#AF0000'),
])

myBlWh = colors.LinearSegmentedColormap.from_list('myBlWh',[
  (  0./14,'#0000FF'),
  (  2./14,'#0E62F2'),
  (  4./14,'#0099FF'),
  (  6./14,'#00B7FF'),
  (  8./14,'#00DBFF'),
  ( 10./14,'#5AE8FF'),
  ( 12./14,'#AFF4FF'),
  ( 14./14,'#FFFFFF'),
])

myWhRd = colors.LinearSegmentedColormap.from_list('myWhRd',[
  ( 0./14,'#FFFFFF'),
  ( 2./14,'#FFFF00'),
  ( 4./14,'#FFE300'),
  ( 6./14,'#FFC500'),
  ( 8./14,'#FFAD00'),
  (10./14,'#F98B04'),
  (12./14,'#F94F04'),
  (14./14,'#FF0000'),
])

myKWh = colors.LinearSegmentedColormap.from_list('myKWh',[
  (  0./14,'#000000'),
  (  2./14,'#0E62F2'),
  (  4./14,'#0099FF'),
  (  6./14,'#00B7FF'),
  (  8./14,'#00DBFF'),
  ( 10./14,'#5AE8FF'),
  ( 12./14,'#AFF4FF'),
  ( 14./14,'#FFFFFF'),
])

mycm15 = colors.LinearSegmentedColormap.from_list('mycm15',[
  ( 0./14,'#0000FF'),
  ( 1./14,'#0E62F2'),
  ( 2./14,'#0099FF'),
  ( 3./14,'#00B7FF'),
  ( 4./14,'#00DBFF'),
  ( 5./14,'#5AE8FF'),
  ( 6./14,'#AFF4FF'),
  ( 7./14,'#FFFFFF'),
  ( 8./14,'#FFFF00'),
  ( 9./14,'#FFE300'),
  (10./14,'#FFC500'),
  (11./14,'#FFAD00'),
  (12./14,'#F98B04'),
  (13./14,'#F94F04'),
  (14./14,'#FF0000'),
])

mycm19 = colors.LinearSegmentedColormap.from_list('mycm19',[
 ( 0.   ,'#0000AF'),
 ( 1./18,'#0000CC'),
 ( 2./18,'#0000FF'),
 ( 3./18,'#0E62F2'),
 ( 4./18,'#0099FF'),
 ( 5./18,'#00B7FF'),
 ( 6./18,'#00DBFF'),
 ( 7./18,'#5AE8FF'),
 ( 8./18,'#AFF4FF'),
 ( .5   ,'#FFFFFF'),
 (10./18,'#FFFF00'),
 (11./18,'#FFE300'),
 (12./18,'#FFC500'),
 (13./18,'#FFAD00'),
 (14./18,'#F98B04'),
 (15./18,'#F94F04'),
 (16./18,'#FF0000'),
 (17./18,'#CD0000'),
 ( 1    ,'#AF0000')
])
