import matplotlib.pyplot as plt
import matplotlib.colors as colors
from seaborn import diverging_palette

######### Customized cmap 1 ############
cmap_main = plt.cm.Greens  # define the colormap
cmap_yellow = plt.cm.YlOrBr
cmap_org = plt.cm.Oranges
cmap_blues = plt.cm.Blues
cmap_purple = plt.cm.Purples
cmap_red = plt.cm.RdPu
cmap_summer = plt.cm.summer
cmap_ryg = plt.cm.RdYlGn

# extract all colors from the cmap
cmaplist_main= [cmap_main(cmap_main.N-i) for i in range(cmap_main.N)]
cmaplist_yellow = [cmap_yellow(i) for i in range(cmap_yellow.N)]
cmaplist_purple = [cmap_purple(i) for i in range(cmap_purple.N)]
cmaplist_org = [cmap_org(i) for i in range(cmap_org.N)]
cmaplist_blues= [cmap_blues(i) for i in range(cmap_blues.N)]
cmaplist_red= [cmap_red(i) for i in range(cmap_red.N)]
cmaplist_summer= [cmap_summer(cmap_summer.N-i) for i in range(cmap_summer.N)]
cmaplist_ryg= [cmap_ryg(i) for i in range(cmap_ryg.N)]

cmaplist = []
cmaplist.extend(cmaplist_main[120:185:5])
cmaplist.extend(cmaplist_blues[70:139:3])
cmap_custom = colors.LinearSegmentedColormap.from_list(
    'Custom cmap', cmaplist, len(cmaplist))  # create the new map

##### Seaborn
cmap_sb = diverging_palette(250, 10, n=12, as_cmap=True)
cmaplist_sb = [cmap_sb(i) for i in range(cmap_sb.N)]
cmaplist_sb_custom = []
cmaplist_sb_custom.extend(cmaplist_sb[0:126:14])   # 9 colors for [target time -2 hours] (include 0)
cmaplist_sb_custom.extend(cmaplist_sb[140:236:6])  # 16 colors for [target time +4 hours]
cmap_sb_custom = colors.LinearSegmentedColormap.from_list(
    'Custom cmap', cmaplist_sb_custom, len(cmaplist_sb_custom))
