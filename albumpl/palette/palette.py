import matplotlib
from matplotlib.colors import LinearSegmentedColormap
# from albumpl.cmap import register_all
from albumpl import cmap

class Vividict(dict):
	## with thanks to https://stackoverflow.com/a/24089632
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

covers = Vividict() #not the most loc efficient, but neat and easy to update
covers['LondonCalling']['cycle'] = ['#343530', '#d67892', '#c0b7b0', '#018c51']
covers['LondonCalling']['cmap'] = ['#343530', '#d8d4cb']
covers['LondonCalling']['ncolors'] = 4
covers['LondonCalling']['maptype'] = "sequential"

covers['Antisocialites']['cycle'] = ['#1b201c', '#d44f2c', '#f6d339', '#4855a4', '#5d7661', '#d4e0ec']
covers['Antisocialites']['cmap'] = ['#b9d0e0', '#faf0e6', '#ef9d6d']
covers['Antisocialites']['ncolors'] = 6
covers['Antisocialites']['maptype'] = "diverging"

covers['RhumbLine']['cycle'] = ['#31343b', '#579eb2', '#8f8C7b', '#e7a834', '#256c82', '#e9ddb7']
covers['RhumbLine']['cmap'] = ['#579eb2', '#e9ddb7', '#e7a834']
covers['RhumbLine']['ncolors'] = 6
covers['RhumbLine']['maptype'] = "diverging"

covers['Matangi']['cycle'] = ['#1f3a45', '#e72526', '#01aaa4', '#76233a']
covers['Matangi']['cmap'] = ['#01aaa4', '#764935', '#e72526']
covers['Matangi']['ncolors'] = 4
covers['Matangi']['maptype'] = "diverging"

covers['MellonCollie']['cycle'] = ['#1e312d', '#CC2f3a', '#215175', '#9ca23e', '#f69769', '#646675']
covers['MellonCollie']['cmap'] = ['#275f82', '#5b6f8a', '#fefcc3']
covers['MellonCollie']['ncolors'] = 6
covers['MellonCollie']['maptype'] = "sequential"

covers['MellonCollie2012']['cycle'] = ['#0c2021', '#e49e25', '#6f5733', '#e3553f', '#3a7549', '#24352b']
covers['MellonCollie2012']['cmap'] = ['#1b0f00', '#174542', '#e49e25']
covers['MellonCollie2012']['ncolors'] = 6
covers['MellonCollie2012']['maptype'] = "sequential"

covers['Yoshimi']['cycle'] = ['#242321', '#C50036', '#4c8981', '#cd4f02', '#d4d180', '#d57867']
covers['Yoshimi']['cmap'] = ['#ecd7a2', '#d28d56', '#ca4f01', '#c50036']
covers['Yoshimi']['ncolors'] = 6
covers['Yoshimi']['maptype'] = "sequential"

covers['Figure8']['cycle'] = ['#01000a', '#938082', '#af0100', '#a7b1ca']
covers['Figure8']['cmap'] = ['#dde6ef', '#a7b1ca', '#01000a']
covers['Figure8']['ncolors'] = 4
covers['Figure8']['maptype'] = "sequential"

covers['LiveThroughThis']['cycle'] = ['#0b1333', '#b54327', '#4f305d', '#fcd192', '#c3ac56', '#c78bbe']
covers['LiveThroughThis']['cmap'] = ['#050725', '#4f305d', '#c78bbe', '#fdfdfd']
covers['LiveThroughThis']['ncolors'] = 6
covers['LiveThroughThis']['maptype'] = "sequential"

covers['Post']['cycle'] = ['#030303', '#d41380', '#94ccb3', '#d8550f', '#2a367e', '#c99114']
covers['Post']['cmap'] = ['#d41380', '#d8550f', '#c99114', '#94ccb3']
covers['Post']['ncolors'] = 6
covers['Post']['maptype'] = "sequential"

covers['VampireWeekend']['cycle'] = ['#411c0c', '#f9a02a', '#c9772d', '#f79d85']
covers['VampireWeekend']['cmap'] = ['#d87929', '#f99a24', '#fde6de', '#f79d85', '#c9772d']
covers['VampireWeekend']['ncolors'] = 4
covers['VampireWeekend']['maptype'] = "diverging"

covers['CopperBlue']['cycle'] = ['#0b0708', '#5881c3', '#cc8432', '#618169', '#eedb96', '#364876']
covers['CopperBlue']['cmap'] = ['#4d2a0a', '#cc8432', '#eec460', '#f3eec6', '#94c1ac', '#158495', '#364876']
covers['CopperBlue']['ncolors'] = 6
covers['CopperBlue']['maptype'] = "diverging"

covers['Dreamland']['cycle'] = ['#6b56f3', '#ff7c53', '#4eb5e0', '#f64bab', '#da50fe', '#b4d5f8']
covers['Dreamland']['cmap'] = ['#4eb5e0', '#b4d5f8', '#da50fe']
covers['Dreamland']['ncolors'] = 6
covers['Dreamland']['maptype'] = "diverging"

covers['Garbage']['cycle'] = ['#091c1a', '#dc1c72', '#7b6568', '#f396b1']
covers['Garbage']['cmap'] = ['#dc1c72', '#f396b1', '#eeeee4']
covers['Garbage']['ncolors'] = 4
covers['Garbage']['maptype'] = "sequential"

covers['BlameItOnGravity']['cycle'] = ['#050706', '#0a756f', '#bb141b', '#a8a838', '#ecb830', '#bfe3f3']
covers['BlameItOnGravity']['cmap'] = ['#fce341', '#f3d235', '#ecb830', '#ef9729']
covers['BlameItOnGravity']['ncolors'] = 6
covers['BlameItOnGravity']['maptype'] = "sequential"

covers['ChutesTooNarrow']['cycle'] = ['#000000', '#f9a823', '#8dcfdf', '#819f55', '#f23742', '#887169']
covers['ChutesTooNarrow']['cmap'] = ['#aada77', '#fffffd', '#8dcfdf']
covers['ChutesTooNarrow']['ncolors'] = 6
covers['ChutesTooNarrow']['maptype'] = "diverging"

# register_all()

##########
# * * * *
##########

def list_palettes(mincolors = False, maptype = False, verbose = False):
	"""
	List all available palettes by name. Optionally filter for color cycle and colormap properties.

	Parameters:
		mincolors (int): Minimum number of colors in color cycle. Use this to filter the available palettes. Default is no minimum.
		maptype (str): Either "sequential" or "diverging". Use this to filter the available palettes. Default is no preference for colormap type.
		verbose (bool): Default is False. Enables printing of additional information.

	Returns:
		The list of available palettes (that match search criteria).
	"""
	
	for k in covers.keys():
		if not mincolors and not maptype:
			if verbose:
				print(k, covers[k]['cycle'], covers[k]['maptype'] + 'colormap')
			if not verbose:
				print(k)
		if mincolors and not maptype:
			if covers[k]['ncolors'] >= mincolors:
				if verbose:
					print(k, covers[k]['cycle'], covers[k]['maptype'] + 'colormap')
				if not verbose:
					print(k)
		if maptype and not mincolors:
			if covers[k]['maptype'] == maptype:
				if verbose:
					print(k, covers[k]['cycle'], covers[k]['maptype'] + 'colormap')
				if not verbose:
					print(k)
		if mincolors and maptype:
			if (covers[k]['ncolors'] >= mincolors) & (covers[k]['maptype'] == maptype):
				if verbose:
					print(k, covers[k]['cycle'], covers[k]['maptype'] + 'colormap')
				if not verbose:
					print(k)




def set_default(palette, verbose = False, reverse_cmap = False):
	"""
	Set palette as default colormap and color cycle.

	Parameters:
		palette (str): Name of palette to set as default.
		verbose (bool): Default is False. Enables printing of additional information about the color cycle.
		reverse_cmap (bool/str): Default is False. To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., set_default('LondonCalling', 'reverse').
	"""

	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=covers[palette]['cycle']) 
	if not reverse_cmap:
		matplotlib.rcParams['image.cmap'] = palette
	if reverse_cmap:
		matplotlib.rcParams['image.cmap'] = palette+"_r"
	if verbose:
		print("Cycled colors in %s are: "%(palette) + covers[palette]['cycle'].values)



def set_default_cmap(palette, reverse_cmap = False):
	"""
	Set palette as default colormap.

	Parameters:
			palette (str): Name of palette to set as default.
			reverse_cmap (bool/str): Default is False. To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., set_default('LondonCalling', 'reverse').
	"""

	if not reverse_cmap:
		matplotlib.rcParams['image.cmap'] = palette
	if reverse_cmap:
		matplotlib.rcParams['image.cmap'] = palette+"_r"


def set_default_ccycle(palette, verbose = False):
	"""
	Set palette as default color cycle.

	Parameters:
		palette (str): Name of palette to set as default.
		verbose (bool): Default is False. Enables printing of additional information about the color cycle.
	"""

	# matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=palettes['palette'][palettes['name'] == palette]['cycle']) 
	# if verbose:
	# 	print("Cycled colors in %s are: "%(palette) + palettes['palette'][palettes['name'] == palette]['cycle'].values)

	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=covers[palette]['cycle'])
	if verbose:
		print("Cycled colors in %s are: "%(palette) + covers[palette]['cycle'].values)


def return_colors(palette):
	"""
	Return colors in a particular palette's color cycle.

	Parameters:
			palette (str): Name of palette.
	"""

	return covers[palette]['cycle']


