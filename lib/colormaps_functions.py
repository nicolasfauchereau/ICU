import os

def gmtColormap(palette):
      from matplotlib.colors import LinearSegmentedColormap,Normalize
      import colorsys
      import numpy as N
      try:
          f = open(os.path.join(os.environ['HOME']), 'pythonlibs/GMTcolormaps/', palette,'.cpt' )
      except:
          print "file " + palette + ".cpt not found"
          return None

      lines = f.readlines()
      f.close()

      x = []
      r = []
      g = []
      b = []
      colorModel = "RGB"
      for l in lines:
          ls = l.split()
          if l[0] == "#":
             if ls[-1] == "HSV":
                 colorModel = "HSV"
                 continue
             else:
                 continue
          if ls[0] == "B" or ls[0] == "F" or ls[0] == "N":
             pass
          else:
              x.append(float(ls[0]))
              r.append(float(ls[1]))
              g.append(float(ls[2]))
              b.append(float(ls[3]))
              xtemp = float(ls[4])
              rtemp = float(ls[5])
              gtemp = float(ls[6])
              btemp = float(ls[7])

      x.append(xtemp)
      r.append(rtemp)
      g.append(gtemp)
      b.append(btemp)

      nTable = len(r)
      x = N.array( x , N.float32)
      r = N.array( r , N.float32)
      g = N.array( g , N.float32)
      b = N.array( b , N.float32)
      if colorModel == "HSV":
         for i in range(r.shape[0]):
             rr,gg,bb = colorsys.hsv_to_rgb(r[i]/360.,g[i],b[i])
             r[i] = rr ; g[i] = gg ; b[i] = bb
      if colorModel == "HSV":
         for i in range(r.shape[0]):
             rr,gg,bb = colorsys.hsv_to_rgb(r[i]/360.,g[i],b[i])
             r[i] = rr ; g[i] = gg ; b[i] = bb
      if colorModel == "RGB":
          r = r/255.
          g = g/255.
          b = b/255.
      xNorm = (x - x[0])/(x[-1] - x[0])

      red = []
      blue = []
      green = []
      for i in range(len(x)):
          red.append([xNorm[i],r[i],r[i]])
          green.append([xNorm[i],g[i],g[i]])
          blue.append([xNorm[i],b[i],b[i]])
      colorDict = {"red":red, "green":green, "blue":blue}
      matcmap = LinearSegmentedColormap('my_colormap',colorDict)
      return matcmap

def cmap_map(function,cmap):
    from numpy import array
    import matplotlib
    """ Applies function (which should operate on vectors of shape 3:
    [r, g, b], on colormap cmap. This routine will break any discontinuous     points in a colormap.
    """
    cdict = cmap._segmentdata
    step_dict = {}
    # Firt get the list of points where the segments start or end
    for key in ('red','green','blue'):         step_dict[key] = map(lambda x: x[0], cdict[key])
    step_list = sum(step_dict.values(), [])
    step_list = array(list(set(step_list)))
    # Then compute the LUT, and apply the function to the LUT
    reduced_cmap = lambda step : array(cmap(step)[0:3])
    old_LUT = array(map( reduced_cmap, step_list))
    new_LUT = array(map( function, old_LUT))
    # Now try to make a minimal segment definition of the new LUT
    cdict = {}
    for i,key in enumerate(('red','green','blue')):
        this_cdict = {}
        for j,step in enumerate(step_list):
            if step in step_dict[key]:
                this_cdict[step] = new_LUT[j,i]
            elif new_LUT[j,i]!=old_LUT[j,i]:
                this_cdict[step] = new_LUT[j,i]
        colorvector=  map(lambda x: x + (x[1], ), this_cdict.items())
        colorvector.sort()
        cdict[key] = colorvector

    return matplotlib.colors.LinearSegmentedColormap('colormap',cdict,1024)

def reverse(cmap):
    from colormaps_functions import cmap_map
    cmap_r = cmap_map(lambda x: x[::-1], cmap)
    return(cmap_r)

def cmap_discretize(cmap, N):
	"""
	Return a discrete colormap from the continuous colormap cmap.

	cmap: colormap instance, eg. cm.jet.
	N: Number of colors.

	Example
	x = resize(arange(100), (5,100))
	djet = cmap_discretize(cm.jet, 5)
	imshow(x, cmap=djet)
	"""
	import numpy as np
	from pylab import interp
	import pylab as pl
	import pylab as plt

	cdict = cmap._segmentdata.copy()
	# N colors
	colors_i = np.linspace(0,1.,N)
	# N+1 indices
	indices = np.linspace(0,1.,N+1)
	for key in ('red','green','blue'):
		# Find the N colors
		D = np.array(cdict[key])
		#I = interpolate.interp1d(D[:,0], D[:,1])
		#I = interpolate.interp1d(D[:,0],D[:,1])
		colors = interp(colors_i,D[:,0],D[:,1])
		# Place these colors at the correct indices.
		A = np.zeros((N+1,3), float)
		A[:,0] = indices
		A[1:,1] = colors
		A[:-1,2] = colors
		# Create a tuple for the dictionary.
		L = []
		for l in A:
			L.append(tuple(l))
		cdict[key] = tuple(L)
	# Return colormap object.
	return plt.matplotlib.colors.LinearSegmentedColormap('colormap',cdict,1024)

def clisttomapdict(clist,name='myColorMap', number=256):
      from matplotlib import colors
      nColors = len(clist)
      red = []
      blue = []
      green = []
      delta = 1.0/(nColors-1)
      for n in range(nColors):
          red.append([n*delta, clist[n][0],clist[n][0]])
          green.append([n*delta, clist[n][1],clist[n][1]])
          blue.append([n*delta, clist[n][2],clist[n][2]])
      cmDict = {'red':red,'green':green,'blue':blue}
      return (colors.LinearSegmentedColormap(name,cmDict,number))

def textfiletoarray(file_name,numberOfHeaderLines=0):
     import numpy
     import string
     try:
        f = open(file_name,'r')
     except:
        print ' file not opened ',file_name
        return(None)
     lines = f.readlines()
     i = len(lines)
     j = len(string.split(lines[numberOfHeaderLines]))
     array = numpy.zeros((i-numberOfHeaderLines,j), float)
     xx = 0
     e = None
     for x in range(numberOfHeaderLines,i):
         for y in range(0,j):
                try:
                   array[xx:xx+1, y:y+1] = string.atof(string.split(lines[x])[y])
                except ValueError:
                   new = array[:xx,:]
                   f.close()
                   return new
         xx = xx + 1
     f.close()
     return(array)

def readnclcolormaps(fileName,returnAs='colorMap',alpha=1.):
      from os.path import exists
      from glob import glob
      from colormaps_functions import clisttomapdict, textfiletoarray
      filePath = os.path.join(os.environ['HOME'], 'pythonlibs/NCLcolormaps', fileName, '.rgb')
      if not exists(filePath):
          print 'file not found ',filePath
          print 'Possible  ones are '
          flist = glob(Path+'/*.rgb')
          for l in flist:
              print l
          return None
      a = textfiletoarray(filePath,numberOfHeaderLines=2)
      clist = []
      for i in range(a.shape[0]):
          c = (a[i,0]/255,a[i,1]/255,a[i,2]/255,alpha)
          clist.append(c)
      if returnAs == 'listOfTuples':
          return clist
      elif returnAs == 'colorMap':
          cmap = clisttomapdict(clist,fileName)
          return cmap
      else:
          print 'return type not recognized'
          return None

def loadCCPLOTcolormap(filename):
    import os
    import numpy as np
    import matplotlib as mpl
    """"Returns a tuple of matplotlib colormap, matplotlib norm,
    and a list of ticks loaded from the file filename in format:

    BOUNDS
    from1 to1 step1
    from2 to2 step2
    ...

    TICKS
    from1 to1 step1
    from2 to2 step2

    COLORS
    r1 g1 b1
    r2 g2 b2
    ...

    UNDER_OVER_BAD_COLORS
    ro go bo
    ru gu bu
    rb gb bb

    Where fromn, ton, stepn are floating point numbers as would be supplied
    to numpy.arange, and rn, gn, bn are the color components the n-th color
    stripe. Components are expected to be in base10 format (0-255).
    UNDER_OVER_BAD_COLORS section specifies colors to be used for
    over, under and bad (masked) values in that order.

    Arguments:
        filename    -- name of the colormap file
        name        -- name for the matplotlib colormap object

    Returns:
        A tuple of: instance of ListedColormap, instance of BoundaryNorm, ticks.
    """
    path = os.path.join(os.environ['HOME'], 'pythonlibs/CCPLOTcolormaps')

    bounds = []
    ticks = []
    rgbarray = []
    specials = []
    mode = "COLORS"

    fp = None
    try:
        fp = open(os.path.join(path, filename), "r")
    except IOError:
        print "File not found"
    lines = fp.readlines()
    for n, s in enumerate(lines):
        s = s.strip()
        if len(s) == 0: continue
        if s in ("BOUNDS", "TICKS", "COLORS", "UNDER_OVER_BAD_COLORS"):
            mode = s
            continue

        a = s.split()
        if len(a) not in (3, 4):
            raise ValueError("Invalid number of fields")

        if mode == "BOUNDS":
            bounds += list(np.arange(float(a[0]), float(a[1]), float(a[2])))
        elif mode == "TICKS":
            ticks += list(np.arange(float(a[0]), float(a[1]), float(a[2])))
        elif mode == "COLORS":
            rgba = [int(c)/256.0 for c in a]
            if len(rgba) == 3: rgba.append(1)
            rgbarray.append(rgba)
        elif mode == "UNDER_OVER_BAD_COLORS":
            rgba = [int(c)/256.0 for c in a]
            if len(rgba) == 3: rgba.append(1)
            specials.append(rgba)
    if (len(rgbarray) > 0):
        colormap = mpl.colors.ListedColormap(rgbarray)
        try:
            colormap.set_under(specials[0][:3], specials[0][3])
            colormap.set_over(specials[1][:3], specials[1][3])
            colormap.set_bad(specials[2][:3], specials[2][3])
        except IndexError: pass
    else:
        colormap = None

    if len(bounds) == 0:
        norm = None
    else:
        norm = mpl.colors.BoundaryNorm(bounds, colormap.N)
    if len(ticks) == 0: ticks = None
    return (colormap, norm, ticks)
