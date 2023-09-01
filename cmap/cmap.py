import matplotlib
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


def get_map(palette, reverse_cmap):
	"""
	Access colormaps for each album cover.

	Parameters:
		palette (str): Name of album cover.
		reverse_cmap (str): Default is False.
	"""

	if not reverse_cmap:
		cmap = LinearSegmentedColormap.from_list(palette, covers[palette]['cmap'])
	if reverse_cmap:
		cmap = LinearSegmentedColormap.from_list(palette+"_r", covers[palette]['cmap'][::-1])
	return cmap


##########
# * * * *
##########


def LondonCalling(reverse_cmap = False):
	"""
	Colormap generated for London Calling by the Clash.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., LondonCalling('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('LondonCalling', reverse_cmap)


def Clampdown(reverse_cmap = False):
	"""
	Alternative colormap generated for London Calling by the Clash.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Clampdown', reverse_cmap)


def Antisocialites(reverse_cmap = False):
	"""
	Colormap generated for Antisocialites by Alvvays.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Antisocialites('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Antisocialites', reverse_cmap)


def PlimsollPunks(reverse_cmap = False):
	"""
	Alternative colormap generated for Antisocialites by Alvvays.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('PlimsollPunks', reverse_cmap)


def RhumbLine(reverse_cmap = False):
	"""
	Colormap generated for Rhumb Line by Ra Ra Riot.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., RhumbLine('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('RhumbLine', reverse_cmap)


def Winter05(reverse_cmap = False):
	"""
	Alternative colormap generated for Rhumb Line by Ra Ra Riot.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Winter05', reverse_cmap)


def Matangi(reverse_cmap = False):
	"""
	Colormap generated for Matangi by M.I.A.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Matangi', reverse_cmap)


def MellonCollie(reverse_cmap = False):
	"""
	Colormap generated for Mellon Collie and the Infinite Sadness by the Smashing Pumpkins.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('MellonCollie', reverse_cmap)


def MellonCollie2012(reverse_cmap = False):
	"""
	Colormap generated for Mellon Collie and the Infinite Sadness by the Smashing Pumpkins.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('MellonCollie2012', reverse_cmap)


def Yoshimi(reverse_cmap = False):
	"""
	Colormap generated for Yoshimi Battles the Pink Robots by the Flaming Lips.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Yoshimi', reverse_cmap)


def Figure8(reverse_cmap = False):
	"""
	Colormap generated for Figure 8 by the Elliott Smith.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Figure8', reverse_cmap)


def LiveThroughThis(reverse_cmap = False):
	"""
	Colormap generated for Live Through This by Hole.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('LiveThroughThis', reverse_cmap)


def MissWorld(reverse_cmap = False):
	"""
	Alternative colormap generated for Live Through This by Hole.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('MissWorld', reverse_cmap)


def Post(reverse_cmap = False):
	"""
	Colormap generated for Post by Bjork.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Post', reverse_cmap)


def VampireWeekend(reverse_cmap = False):
	"""
	Colormap generated for Vampire Weekend by Vampire Weekend.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('VampireWeekend', reverse_cmap)


def CopperBlue(reverse_cmap = False):
	"""
	Colormap generated for Copper Blue by Sugar.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('CopperBlue', reverse_cmap)


def Dreamland(reverse_cmap = False):
	"""
	Colormap generated for Dreamland by Glass Animals.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Dreamland', reverse_cmap)


def HeatWaves(reverse_cmap = False):
	"""
	Alternative colormap generated for Dreamland by Glass Animals.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('HeatWaves', reverse_cmap)


def Garbage(reverse_cmap = False):
	"""
	Colormap generated for Garbage by Garbage.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Garbage', reverse_cmap)


def Vow(reverse_cmap = False):
	"""
	Alternative colormap generated for Garbage by Garbage.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('Vow', reverse_cmap)


def BlameItOnGravity(reverse_cmap = False):
	"""
	Alternative colormap generated for BlameItOnGravity by Old 97's.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('BlameItOnGravity', reverse_cmap)


def ChutesTooNarrow(reverse_cmap = False):
	"""
	Colormap generated for Chutes Too Narrow by the Shins.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('ChutesTooNarrow', reverse_cmap)


def YoungPilgrims(reverse_cmap = False):
	"""
	Alternative colormap generated for Chutes Too Narrow by the Shins.

	To reverse the colormap, use the keyword argument reverse_cmap = True or just use a string -- e.g., Matangi('reverse').

	Parameters:
		reverse_cmap (str): Default is False.
	"""
	get_map('YoungPilgrims', reverse_cmap)





	