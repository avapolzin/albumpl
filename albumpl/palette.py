import matplotlib
from matplotlib.colors import LinearSegmentedColormap


LondonCalling_ = {'cycle':["#343530", "#d67892", "#c0b7b0", "#018c51"], 'cmap':['#343530', '#d8d4cb']}
Antisocialites_ = {'cycle':["#1b201c", "#d44f2c", "#f6d339", "#4855a4", "#5d7661", "#d4e0ec"], 'cmap':['#d4e0ec', '#faf0e6', '#d44f2c']}
RhumbLine_ = {'cycle':["#31343b", "#579eb2", "#8f8c7b", "#e7a834", "#256c82", "#e9ddb7"], 'cmap':['#579eb2', '#e9ddb7', '#e7a834']}

palettes = {'name':['LondonCalling', 'Antisocialites', 'Rhumbline'], 'palette':[LondonCalling_, Antisocialites_, RhumbLine_], 'ncolors': [4, 6, 6], 'maptype':['sequential', 'diverging', 'diverging']}


##########
# * * * *
##########

def list_palettes(mincolors = False, maptype = False, verbose = False):
	"""
	List all available palettes by name. Optionally filter for color cycle and colormap properties.
	"""
	
	if not mincolors & maptype:
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



def set_default(palette, verbose = False):

	if palette == 'LondonCalling':
		global LondonCalling
		global LondonCalling_r
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=LondonCalling_['cycle']) 
		LondonCalling = LinearSegmentedColormap.from_list("LondonCalling", LondonCalling_['cmap'])
		LondonCalling_r = LinearSegmentedColormap.from_list("LondonCalling_r", LondonCalling_['cmap'][::-1])
		if verbose:
			print("Cycled colors in %s are: "%(palette) + LondonCalling_['cycle'].values)

	if palette == 'Antisocialites':
		global Antisocialites
		global Antisocialites_r
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=Antisocialites_['cycle']) 
		Antisocialites = LinearSegmentedColormap.from_list("Antisocialites", Antisocialites_['cmap'])
		Antisocialites_r = LinearSegmentedColormap.from_list("Antisocialites_r", Antisocialites_['cmap'][::-1])
		if verbose:
			print("Cycled colors in %s are: "%(palette) + Antisocialites_['cycle'].values)

	if palette == 'RhumbLine':
		global RhumbLine
		global RhumbLine_r
		matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=RhumbLine_['cycle'])
		RhumbLine = LinearSegmentedColormap.from_list("RhumbLine", RhumbLine_['cmap'])
		RhumbLine_r = LinearSegmentedColormap.from_list("RhumbLine_r", RhumbLine_['cmap'][::-1])
		if verbose:
			print("Cycled colors in %s are: "%(palette) + RhumbLine_['cycle'].values)


def set_default_cmap(palette):

	if palette == 'LondonCalling':
		global LondonCalling
		global LondonCalling_r
		LondonCalling = LinearSegmentedColormap.from_list("LondonCalling", LondonCalling_['cmap'])
		LondonCalling_r = LinearSegmentedColormap.from_list("LondonCalling_r", LondonCalling_['cmap'][::-1])

	if palette == 'Antisocialites':
		global Antisocialites
		global Antisocialites_r
		Antisocialites = LinearSegmentedColormap.from_list("Antisocialites", Antisocialites_['cmap'])
		Antisocialites_r = LinearSegmentedColormap.from_list("Antisocialites_r", Antisocialites_['cmap'][::-1])

	if palette == 'RhumbLine':
		global RhumbLine
		global RhumbLine_r
		RhumbLine = LinearSegmentedColormap.from_list("RhumbLine", RhumbLine_['cmap'])
		RhumbLine_r = LinearSegmentedColormap.from_list("RhumbLine_r", RhumbLine_['cmap'][::-1])



def set_default_ccycle(palette, verbose = False):

	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=palettes['palette'][palettes['name'] == palette]['cycle']) 
	if verbose:
		print("Cycled colors in %s are: "%(palette) + palettes['palette'][palettes['name'] == palette]['cycle'].values)

	# if palette == 'LondonCalling':
	# 	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=LondonCalling_['cycle']) 
	# 	if verbose:
	# 		print("Cycled colors in %s are: "%(palette) + LondonCalling_['cycle'].values)

	# if palette == 'Antisocialites':
	# 	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=Antisocialites_['cycle']) 
	# 	if verbose:
	# 		print("Cycled colors in %s are: "%(palette) + Antisocialites_['cycle'].values)

	# if palette == 'RhumbLine':
	# 	matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=RhumbLine_['cycle'])
	# 	if verbose:
	# 		print("Cycled colors in %s are: "%(palette) + RhumbLine_['cycle'].values)



def return_colors(palette):

	return palettes['palette'][palettes['name'] == palette]['cycle']

def add_cmaps(cmap = 'all', verbose = False):
	if cmap == 'all':
		global LondonCalling
		global LondonCalling_r
		LondonCalling = LinearSegmentedColormap.from_list("LondonCalling", LondonCalling_['cmap'])
		LondonCalling_r = LinearSegmentedColormap.from_list("LondonCalling_r", LondonCalling_['cmap'][::-1])

		global Antisocialites
		global Antisocialites_r
		Antisocialites = LinearSegmentedColormap.from_list("Antisocialites", Antisocialites_['cmap'])
		Antisocialites_r = LinearSegmentedColormap.from_list("Antisocialites_r", Antisocialites_['cmap'][::-1])

		global RhumbLine
		global RhumbLine_r
		RhumbLine = LinearSegmentedColormap.from_list("RhumbLine", RhumbLine_['cmap'])
		RhumbLine_r = LinearSegmentedColormap.from_list("RhumbLine_r", RhumbLine_['cmap'][::-1])



