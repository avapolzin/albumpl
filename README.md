# `albumpl `
Custom matplotlib color palettes based on album covers. New default color cycles and colormaps are stored in style sheets for easy access.

To install:
```bash
cd ~

git clone git@github.com:avapolzin/albuMPL-palette.git

cd albuMPL-palette

sudo python3 setupy.py install

````

If you use this package or the scripts in this repository in a publication, please add a footnote linking to https://github.com/avapolzin/albuMPL-palette and consider adding this software to your acknowledgments. (Or if you would like to cite `albumpl`, please email me, and I will ensure there is a citable DOI available.) I'd love to feature plots/figures that make use of these palettes in the wild, so should these palettes be of use, please send me a copy of that figure and/or a link to your paper or presentation and I will share it here.

Each of the included palettes has been checked with [COBLIS](https://www.color-blindness.com/coblis-color-blindness-simulator/), and should be legible for individuals with most common forms of color blindness. Best, though, is to check your specific figures' readability, too.


The palette options (to now) are:
1. __LondonCalling__ inspired by The Clash - _London Calling_ (which, of course, ***technically*** means it was inspired by Elvis Presley's eponymous album)
![LondonCalling_summary](https://user-images.githubusercontent.com/29441772/149859998-c0d2990b-123f-40f2-90ca-644cfaae0cdf.png)

2. __Antisocialites__ inspired by Alvvays - _Antisocialites_
![Antisocialites_summary](https://user-images.githubusercontent.com/29441772/149859986-f0f7c779-398e-43ab-996a-245179045783.png)

3. __RhumbLine__ inspired by Ra Ra Riot - _The Rhumb Line_
![RhumbLine_summary](https://user-images.githubusercontent.com/29441772/149860002-220f06c8-ed04-4a83-8c00-36e3e424af54.png)

4. __Matangi__ inspired by M.I.A. - _Matangi_
![Matangi_summary](https://user-images.githubusercontent.com/29441772/188256902-6fa7b458-1cb5-4bd6-b4ef-9299ef1097ad.png)

5. __MellonCollie__ inspired by the Smashing Pumpkins - _Mellon Collie and the Infinite Sadness (2012 Deluxe Edition)_
![MellonCollie_summary](https://user-images.githubusercontent.com/29441772/188669272-5d8ce860-5c04-46a2-b38c-b267dec49ec4.png)


Additional palettes will be added moving forward. Is there a specific album you want considered for a future palette? Please open an issue with the name of the album and artist and an image of the album cover.

***
# How to use `albumpl`:
### Some quick recipes.

- **To list all palettes and their properties:**
```python
from albumpl.palette import list_palettes

list_palettes()
```
*You can also filter for number of colors in the color cycle or type of colormap (sequential/diverging) with the arguments `mincolors` and `maptype`.*

- **To set palette as default for both color cycle *and* colormap:**
```python
from albumpl.palette import set_default

set_default('LondonCalling')
```

- **To set a palette as default for color cycle *or* colormap:**
```python
from alumpl.palette import set_default_ccyle or set_default_cmap

set_default_ccyle('Antisocialites')
```
*or*
```python
set_default_cmap('RhumbLine')
```

- **To access colormaps without setting them as default:**
```python
import matplotlib.pyplot as plt
from albumpl.cmap import * #yes, this is bad practice, but easiest in this case!

plt.imshow(image, cmap = Matangi())
```
*To reverse the colormap, use the argument `reverse_cmap = True` or just feed the colormap the string "reverse" or "_r".*

- **To access the colors in a color cycle/palette without setting a default:**
```python
from albumpl.palette import return_colors

return_colors('MellonCollie')
```
