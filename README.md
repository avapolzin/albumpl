# `albumpl`
Custom matplotlib color palettes based on album covers.

To install:
```bash
cd ~

git clone git@github.com:avapolzin/albumpl.git

cd albumpl

sudo python3 setupy.py install

````

If you use this package or the scripts in this repository in a publication, please add a footnote linking to https://github.com/avapolzin/albuMPL-palette and consider adding this software to your acknowledgments. (Or if you would like to cite `albumpl`, please email me, and I will ensure there is a citable DOI available.) I'd love to feature plots/figures that make use of these palettes in the wild, so should these palettes be of use, please send me a copy of that figure and/or a link to your paper or presentation and I will share it here.

Each of the included palettes has been checked with [COBLIS](https://www.color-blindness.com/coblis-color-blindness-simulator/), and should be legible for individuals with most common forms of color blindness. Best, though, is to check your specific figures' readability, too.


The palette options (to now) are:
1. __LondonCalling__ inspired by The Clash - _London Calling_ (which, of course, ***technically*** means it was inspired by Elvis Presley's eponymous album)
![LondonCalling_summary](https://github.com/avapolzin/albumpl/assets/29441772/780dc5a5-1a4f-47cc-9cf1-f2e0aad68a6c)

2. __Antisocialites__ inspired by Alvvays - _Antisocialites_
![Antisocialites_summary](https://github.com/avapolzin/albumpl/assets/29441772/79e3f41f-2634-458d-88d0-ce69bb5eae34)

3. __RhumbLine__ inspired by Ra Ra Riot - _The Rhumb Line_
![RhumbLine_summary](https://github.com/avapolzin/albumpl/assets/29441772/38d0058c-5a89-47dd-887a-92e2cba95765)

4. __Matangi__ inspired by M.I.A. - _Matangi_
![Matangi_summary](https://github.com/avapolzin/albumpl/assets/29441772/a2514337-34ce-42f6-bc06-7cb50d9b16f4)

5. __MellonCollie__ inspired by the Smashing Pumpkins - _Mellon Collie and the Infinite Sadness_
![MellonCollie_summary](https://github.com/avapolzin/albumpl/assets/29441772/762333f5-a749-4a31-8556-c135ce286d78)

6. __MellonCollie2012__ inspired by the Smashing Pumpkins - _Mellon Collie and the Infinite Sadness (2012 Deluxe Edition)_
![MellonCollie2012_summary](https://github.com/avapolzin/albumpl/assets/29441772/2daef05d-9b29-41f3-b7ee-d45ac8da2142)

7. __Yoshimi__ inspired by the Flaming Lips - _Yoshimi Battles the Pink Robots_
![Yoshimi_summary](https://github.com/avapolzin/albumpl/assets/29441772/f2c3ff06-eaa3-4cd9-aa40-82379451af82)

8. __Figure8__ inspired by Elliott Smith - _Figure 8_
![Figure8_summary](https://github.com/avapolzin/albumpl/assets/29441772/dfd75c64-e5ef-4808-b490-55c1b22e1fc0)

9. __LiveThroughThis__ inspired by Hole - _Live Through This_
![LiveThroughThis_summary](https://github.com/avapolzin/albumpl/assets/29441772/e15d78bb-afc8-4099-a92b-9289a07af508)

10. __Post__ inspired by Björk - _Post_
![Post_summary](https://github.com/avapolzin/albumpl/assets/29441772/60ebd12f-3a9c-4435-aa57-bcef7a439afa)

11. __VampireWeekend__ inspired by Vampire Weekend's self-titled debut
![VampireWeekend_summary](https://github.com/avapolzin/albumpl/assets/29441772/50c3015a-31e6-416a-89ac-c13f4f9ddf08)

12. __CopperBlue__ inspired by Sugar - _Copper Blue_
![CopperBlue_summary](https://github.com/avapolzin/albumpl/assets/29441772/612794be-43a7-469f-b79b-fcc14ad0093c)

13. __Dreamland__ inspired by Glass Animals - _Dreamland_
![Dreamland_summary](https://github.com/avapolzin/albumpl/assets/29441772/14e07728-374d-44cc-85ac-c6c4c84b29da)

14. __Garbage__ inspired by their self-titled debut
![Garbage_summary](https://github.com/avapolzin/albumpl/assets/29441772/d754af41-f976-4198-a1e6-97fc4cac8d81)


There are also a handful of alternative colormaps included in `albumpl`, which are not the default colormap associated with a particular palette, but can be accessed individually in the same way as any other colormap.

These standalone colormaps (named for songs on the album that inspired them) are:

![Clampdown_summary](https://user-images.githubusercontent.com/29441772/213897847-131d6c8f-ab4e-4f95-bee7-4cc77fde2ec6.png) ![Winter05_summary](https://user-images.githubusercontent.com/29441772/210009492-2f98280c-4451-4ae7-88f6-a58724e4fa3c.png)



Additional palettes and colormaps will be added moving forward. Is there a specific album you want considered for a future palette? Please open an issue with the name of the album and artist and an image of the album cover.

<sup><sub>About the sample images: For sequential colormaps, the sample image is photometric _HST_ data of the dwarf galaxy [COSMOS-dw1](https://ui.adsabs.harvard.edu/abs/2021ApJ...914L..23P/abstract) in F814W. The sample image for diverging colormaps is an HI velocity map of the galaxy [M33 from GALFA-HI](https://ui.adsabs.harvard.edu/abs/2009ApJ...703.1486P/abstract). </sub></sup>

<sup><sub>And, though it should go without saying, I'll add: use of an artist's album cover to make a palette is not an endorsement of the artist or their (broadcasted) personal views.</sub></sup>

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
from alumpl.palette import set_default_ccyle, set_default_cmap

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
```python
plt.imshow(image, cmap = MellonCollie(reverse_cmap = True))
```
*or*
```python
plt.imshow(image, cmap = Yoshimi('reverse'))
```
*or*
```python
plt.imshow(image, cmap = Figure8('_r'))
```
- **To access the colors in a color cycle/palette without setting a default:**
```python
from albumpl.palette import return_colors

return_colors('LiveThroughThis')
```

For ease, you may also decide to register these colormaps, effectively adding them to your current installation of `matplotlib`. You can find an up-to-date version of those instructions [here](https://matplotlib.org/stable/api/cm_api.html).

***
These palettes and colormaps are designed with a focus on remaining faithful to the appearance of the album covers instead of emphasizing perceptual uniformity. Most are still pretty good in this regard, but, just for everyone's peace of mind, following `matplotlib`, the lightness of each colormap as a function of index is shown below.

