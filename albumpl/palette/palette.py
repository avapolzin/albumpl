import matplotlib
from matplotlib.colors import LinearSegmentedColormap


LondonCalling_ = {'cycle':["#343530", "#d67892", "#c0b7b0", "#018c51"], 'cmap':['#343530', '#d8d4cb']}
Antisocialites_ = {'cycle':["#1b201c", "#d44f2c", "#f6d339", "#4855a4", "#5d7661", "#d4e0ec"], 'cmap':['#d4e0ec', '#faf0e6', '#d44f2c']}
RhumbLine_ = {'cycle':["#31343b", "#579eb2", "#8f8c7b", "#e7a834", "#256c82", "#e9ddb7"], 'cmap':['#579eb2', '#e9ddb7', '#e7a834']}
Matangi_ = {'cycle':["#491d32", "#e72526", "#01aaa4", "#76233a"], 'cmap':["#01aaa4", "#505e47", "#e72526"]}

palettes = {'name':['LondonCalling', 'Antisocialites', 'Rhumbline', 'Matangi'], 'palette':[LondonCalling_, Antisocialites_, RhumbLine_, Matangi_], 'ncolors': [4, 6, 6, 4], 'maptype':['sequential', 'diverging', 'diverging', 'diverging']}

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
	
	if (not mincolors) & (not maptype):
		if verbose:
			print('Available color palettes are:')
			for i in range(len(palettes['name'])):
				print ('    %s has %i colors and a %s colormap.'%(palettes['name'][i], palettes['ncolors'][i], palettes['maptype'][i]))

		else:
			print(palettes['name'])

	if (not mincolors) & maptype:
		N_ = len(palettes['name'][palettes['maptype'] == maptype])

		if verbose:
			print('Available color palettes with %s colormaps are:'%(maptype))
			if N_ >= 1:
				for i in range(N_):
					print ('    %s has %i colors.'%(palettes['name'][palettes['maptype'] == maptype][i], palettes['ncolors'][palettes['maptype'] == maptype][i]))
			else:
				print('    None')
		else:
			if N_ >= 1:
				print(palettes['name'][palettes['maptype'] == maptype])
			else:
				print('None')


	if mincolors & (not maptype):
		N_ = len(palettes['name'][palettes['ncolors'] >= mincolors])

		if verbose:
			print('Available color palettes with a minimum of %i colors are:'%(mincolors))
			if N_ >= 1:
				for i in range(N_):
					print ('    %s has %i colors and a %s colormap.'%(palettes['name'][palettes['ncolors'] >= mincolors][i], palettes['ncolors'][palettes['ncolors'] >= mincolors][i], palettes['maptype'][palettes['ncolors'] >= mincolors][i]))

			else:
				print('    None')

		else:
			if N_ >= 1:
				print(palettes['name'][palettes['ncolors'] >= mincolors])
			else:
				print('None')


	if mincolors & maptype:
		N_ = len(palettes['name'][(palettes['ncolors'] >= mincolors) & palettes['maptype'] == maptype])

		if verbose:
			print('Available color palettes with a minimum of %i colors and %s colormaps are:'%(mincolors, maptype))
			if N_ >= 1:
				for i in range(N_):
					print ('    %s has %i colors.'%(palettes['name'][(palettes['ncolors'] >= mincolors) & palettes['maptype'] == maptype][i], palettes['ncolors'][(palettes['ncolors'] >= mincolors) & palettes['maptype'] == maptype][i]))
			else:
				print('    None')

		else:
			if N_ >= 1:
				print(palettes['name'][(palettes['ncolors'] >= mincolors) & palettes['maptype'] == maptype])
			else:
				print('None')



def set_default(palette, verbose = False, reverse_cmap = False):
	"""
	Set palette as default colormap and color cycle.

	Parameters:
		palette (str): Name of palette to set as default.
		verbose (bool): Default is False. Enables printing of additional information about the color cycle.
		reverse_cmap (bool/str): Default is False. To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., set_default('LondonCalling', 'reverse').
	"""

	if palette == 'LondonCalling':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=LondonCalling_['cycle']) 
		LondonCalling = LinearSegmentedColormap.from_list("LondonCalling", LondonCalling_['cmap'])
		LondonCalling_r = LinearSegmentedColormap.from_list("LondonCalling_r", LondonCalling_['cmap'][::-1])
		if not reverse_cmap:
			matplotlib.rcParams['image.cmap'] = LondonCalling
		if reverse_cmap:
			matplotlib.rcParams['image.cmap'] = LondonCalling_r
		if verbose:
			print("Cycled colors in %s are: "%(palette) + LondonCalling_['cycle'].values)

	if palette == 'Antisocialites':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=Antisocialites_['cycle']) 
		Antisocialites = LinearSegmentedColormap.from_list("Antisocialites", Antisocialites_['cmap'])
		Antisocialites_r = LinearSegmentedColormap.from_list("Antisocialites_r", Antisocialites_['cmap'][::-1])
		if not reverse_cmap:
			matplotlib.rcParams['image.cmap'] = Antisocialites
		if reverse_cmap:
			matplotlib.rcParams['image.cmap'] = Antisocialites_r
		if verbose:
			print("Cycled colors in %s are: "%(palette) + Antisocialites_['cycle'].values)

	if palette == 'RhumbLine':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=RhumbLine_['cycle'])
		RhumbLine = LinearSegmentedColormap.from_list("RhumbLine", RhumbLine_['cmap'])
		RhumbLine_r = LinearSegmentedColormap.from_list("RhumbLine_r", RhumbLine_['cmap'][::-1])
		if not reverse_cmap:
			matplotlib.rcParams['image.cmap'] = RhumbLine
		if reverse_cmap:
			matplotlib.rcParams['image.cmap'] = RhumbLine_r
		if verbose:
			print("Cycled colors in %s are: "%(palette) + RhumbLine_['cycle'].values)

	if palette == 'Matangi':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=Matangi_['cycle'])
		Matangi = LinearSegmentedColormap.from_list("Matangi", Matangi_['cmap'])
		Matangi_r = LinearSegmentedColormap.from_list("Matangi_r", Matangi_['cmap'][::-1])
		matplotlib.rcParams['image.cmap'] = Matangi
		if verbose:
			print("Cycled colors in %s are: "%(palette) + Matangi_['cycle'].values)


def set_default_cmap(palette, reverse_cmap = False):
	"""
	Set palette as default colormap.

	Parameters:
			palette (str): Name of palette to set as default.
			reverse_cmap (bool/str): Default is False. To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., set_default('LondonCalling', 'reverse').
	"""

	if palette == 'LondonCalling':
		LondonCalling = LinearSegmentedColormap.from_list("LondonCalling", LondonCalling_['cmap'])
		LondonCalling_r = LinearSegmentedColormap.from_list("LondonCalling_r", LondonCalling_['cmap'][::-1])
		if not reverse_cmap:
			matplotlib.rcParams['image.cmap'] = LondonCalling
		if reverse_cmap:
			matplotlib.rcParams['image.cmap'] = LondonCalling_r

	if palette == 'Antisocialites':
		Antisocialites = LinearSegmentedColormap.from_list("Antisocialites", Antisocialites_['cmap'])
		Antisocialites_r = LinearSegmentedColormap.from_list("Antisocialites_r", Antisocialites_['cmap'][::-1])
		if not reverse_cmap:
			matplotlib.rcParams['image.cmap'] = Antisocialites
		if reverse_cmap:
			matplotlib.rcParams['image.cmap'] = Antisocialites_r

	if palette == 'RhumbLine':
		RhumbLine = LinearSegmentedColormap.from_list("RhumbLine", RhumbLine_['cmap'])
		RhumbLine_r = LinearSegmentedColormap.from_list("RhumbLine_r", RhumbLine_['cmap'][::-1])
		if not reverse_cmap:
			matplotlib.rcParams['image.cmap'] = RhumbLine
		if reverse_cmap:
			matplotlib.rcParams['image.cmap'] = RhumbLine_r

	if palette == 'Matangi':
		Matangi = LinearSegmentedColormap.from_list("Matangi", Matangi_['cmap'])
		Matangi_r = LinearSegmentedColormap.from_list("Matangi_r", Matangi_['cmap'][::-1])
		if not reverse_cmap:
			matplotlib.rcParams['image.cmap'] = Matangi
		if reverse_cmap:
			matplotlib.rcParams['image.cmap'] = Matangi_r


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

	if palette == 'LondonCalling':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=LondonCalling_['cycle']) 
		if verbose:
			print("Cycled colors in %s are: "%(palette) + LondonCalling_['cycle'].values)

	if palette == 'Antisocialites':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=Antisocialites_['cycle']) 
		if verbose:
			print("Cycled colors in %s are: "%(palette) + Antisocialites_['cycle'].values)

	if palette == 'RhumbLine':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=RhumbLine_['cycle'])
		if verbose:
			print("Cycled colors in %s are: "%(palette) + RhumbLine_['cycle'].values)

	if palette == 'Matangi':
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=Matangi_['cycle'])
		if verbose:
			print("Cycled colors in %s are: "%(palette) + Matangi_['cycle'].values)



def return_colors(palette):
	"""
	Return colors in

	"""

	return palettes['palette'][palettes['name'] == palette]['cycle']


