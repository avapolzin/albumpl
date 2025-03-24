import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

maps = {}

maps['LondonCalling'] = ['#343530', '#d8d4cb']
maps['Clampdown'] = ['#4da57c', '#d8d4cb', '#d67892']
maps['Antisocialites'] = ['#b9d0e0', '#faf0e6', '#ef9d6d']
maps['PlimsollPunks'] = ['#fad6b2', '#d44f2c', '#2c281f']
maps['RhumbLine'] = ['#579eb2', '#e9ddb7', '#e7a834']
maps['Winter05'] = ['#fef9f3', '#579EB2', '#31343B']
maps['Matangi'] = ['#01aaa4', '#764935', '#e72526']
maps['MellonCollie'] = ['#275f82', '#5b6f8a', '#fefcc3']
maps['MellonCollie2012'] = ['#1b0f00', '#174542', '#e49e25']
maps['Yoshimi'] = ['#ecd7a2', '#d28d56', '#ca4f01', '#c50036']
maps['Figure8'] = ['#dde6ef', '#a7b1ca', '#01000a']
maps['LiveThroughThis'] = ['#050725', '#4f305d', '#c78bbe', '#fdfdfd']
maps['MissWorld'] = ['#050725', '#4f305d', '#c78bbe', '#fdfdfd', '#fcd192', '#b54327', '#1d0806']
maps['Post'] = ['#d41380', '#d8550f', '#c99114', '#94ccb3']
maps['VampireWeekend'] = ['#d87929', '#f99a24', '#fde6de', '#f79d85', '#c9772d']
maps['CopperBlue'] = ['#4d2a0a', '#cc8432', '#eec460', '#f3eec6', '#94c1ac', '#158495', '#364876']
maps['Dreamland'] = ['#4eb5e0', '#b4d5f8', '#da50fe']
maps['HeatWaves'] = ['#d01cc6', '#f64bab', '#d2aef4']
maps['Garbage'] = ['#dc1c72', '#f396b1', '#eeeee4']
maps['Vow'] = ['#7b6568', '#eeeee4', '#dc1c72']
maps['BlameItOnGravity'] = ['#fce341', '#f3d235', '#ecb830', '#ef9729']
maps['ChutesTooNarrow'] = ['#aada77', '#fffffd', '#8dcfdf']
maps['YoungPilgrims'] = ['#ece6c2', '#73625b']


##########
# * * * *
##########


def get_map(palette, reverse_cmap):
	"""
	Access colormaps for each album cover.

	Parameters:
		palette (str): Name of album cover.
		reverse_cmap (str): Default is False.
	"""

	if not reverse_cmap:
		cmap = LinearSegmentedColormap.from_list(palette, maps[palette])
	if reverse_cmap:
		cmap = LinearSegmentedColormap.from_list(palette+"_r", maps[palette][::-1])
	return cmap

def register_all():
	"""
	Register all of the colormaps.
	"""
	for k in maps.keys():
		cmap = LinearSegmentedColormap.from_list(k, maps[k])
		cmap_r = LinearSegmentedColormap.from_list(k+"_r", maps[k][::-1])
		matplotlib.colormaps.register(cmap=cmap)
		matplotlib.colormaps.register(cmap = cmap_r)

register_all()


def list_maps(maptype = False, verbose = False):
	"""
	List all available colormaps by name. Optionally filter for colormap properties.

	Parameters:
		maptype (str): Either "sequential" or "diverging". Use this to filter the available palettes. Default is no preference for colormap type.
		verbose (bool): Default is False. Enables printing of additional information.

	Returns:
		The list of available colormaps (that match search criteria).
	"""
	
	for k in maps.keys():
		if not maptype:
			if verbose:
				print(k, maps[k]['cycle'], maps[k]['maptype'] + 'colormap')
			if not verbose:
				print(k)
		if maptype:
			if maps[k]['maptype'] == maptype:
				if verbose:
					print(k, maps[k]['cycle'], maps[k]['maptype'] + 'colormap')
				if not verbose:
					print(k)
