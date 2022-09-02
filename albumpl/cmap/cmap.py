import matplotlib
from matplotlib.colors import LinearSegmentedColormap

LondonCalling_ = {'cycle':["#343530", "#d67892", "#c0b7b0", "#018c51"], 'cmap':['#343530', '#d8d4cb']}
Antisocialites_ = {'cycle':["#1b201c", "#d44f2c", "#f6d339", "#4855a4", "#5d7661", "#d4e0ec"], 'cmap':['#d4e0ec', '#faf0e6', '#d44f2c']}
RhumbLine_ = {'cycle':["#31343b", "#579eb2", "#8f8c7b", "#e7a834", "#256c82", "#e9ddb7"], 'cmap':['#579eb2', '#e9ddb7', '#e7a834']}

palettes = {'name':['LondonCalling', 'Antisocialites', 'Rhumbline'], 'palette':[LondonCalling_, Antisocialites_, RhumbLine_], 'ncolors': [4, 6, 6], 'maptype':['sequential', 'diverging', 'diverging']}


##########
# * * * *
##########


def LondonCalling(reverse_cmap = False):
	if not reverse_cmap:
		cmap = LinearSegmentedColormap.from_list("LondonCalling", LondonCalling_['cmap'])
	if reverse_cmap:
		cmap = LinearSegmentedColormap.from_list("LondonCalling_r", LondonCalling_['cmap'][::-1])
	return cmap

def Antisocialites(reverse_cmap = False):
	if not reverse_cmap:
		cmap = LinearSegmentedColormap.from_list("Antisocialites", Antisocialites_['cmap'])
	if reverse_cmap:
		cmap = LinearSegmentedColormap.from_list("Antisocialites_r", Antisocialites_['cmap'][::-1])
	return cmap

def RhumbLine(reverse_cmap = False):
	if not reverse_cmap:
		cmap = LinearSegmentedColormap.from_list("RhumbLine", RhumbLine_['cmap'])
	if reverse_cmap:
		cmap = LinearSegmentedColormap.from_list("RhumbLine_r", RhumbLine_['cmap'][::-1])
	return cmap