![albumpl_logo 001](https://github.com/user-attachments/assets/5c11856d-1f9f-4418-a977-48aa6d83ba84)

Custom matplotlib color palettes based on album covers.

[![Documentation Status](https://readthedocs.org/projects/albumpl/badge/?version=latest)](https://albumpl.readthedocs.io/en/latest/?badge=latest) [![DOI](https://zenodo.org/badge/426833310.svg)](https://zenodo.org/badge/latestdoi/426833310) [![Downloads](https://static.pepy.tech/badge/albumpl)](https://pepy.tech/project/albumpl)

To install:
```bash
cd ~

git clone git@github.com:avapolzin/albumpl.git

cd albumpl

sudo python3 setupy.py install

````
or 
```bash
pip install albumpl
```

If you use this package or the scripts in this repository in a publication, please add a footnote linking to https://github.com/avapolzin/albumpl and/or consider adding this software to your acknowledgments. If you would like to cite `albumpl`, please use the Zenodo DOI linked here. 
```tex
@software{ava_polzin_2023_8307551,
  author       = {Ava Polzin},
  title        = {albumpl},
  month        = sep,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0.2.0},
  doi          = {10.5281/zenodo.8307551},
  url          = {https://doi.org/10.5281/zenodo.8307551}
}
```


I'd love to feature plots/figures that make use of these palettes in the wild, so should these palettes be of use, please send me a copy of that figure and/or a link to your paper or presentation and I will share it here.

Each of the included palettes has been checked with [COBLIS](https://www.color-blindness.com/coblis-color-blindness-simulator/), and should be legible for individuals with most common forms of color blindness. Best, though, is to check your specific figures' readability, too.

(Interested in university-inspired palettes and colormaps? Check out [`rahrah`](https://github.com/avapolzin/rahrah).)


The palette options (to now) are:
1. __LondonCalling__ inspired by The Clash - _London Calling_ (which, of course, ***technically*** means it was inspired by Elvis Presley's eponymous album)
![LondonCalling_summary](https://github.com/avapolzin/albumpl/assets/29441772/27db7318-20d0-4bc2-8a17-cfb41592ef75)

2. __Antisocialites__ inspired by Alvvays - _Antisocialites_
![Antisocialites_summary](https://github.com/avapolzin/albumpl/assets/29441772/13bd2938-051c-4150-b069-8e9476ba5336)

3. __RhumbLine__ inspired by Ra Ra Riot - _The Rhumb Line_
![RhumbLine_summary](https://github.com/avapolzin/albumpl/assets/29441772/012b07ef-a4dd-4456-a2b4-ae731106a30d)

4. __Matangi__ inspired by M.I.A. - _Matangi_
![Matangi_summary](https://github.com/avapolzin/albumpl/assets/29441772/d26d43c9-96e1-4795-b544-c673e1dddb5f)

5. __MellonCollie__ inspired by the Smashing Pumpkins - _Mellon Collie and the Infinite Sadness_
![MellonCollie_summary](https://github.com/avapolzin/albumpl/assets/29441772/079861b9-7aa6-4854-993e-9f4dbe691ec5)

6. __MellonCollie2012__ inspired by the Smashing Pumpkins - _Mellon Collie and the Infinite Sadness (2012 Deluxe Edition)_
![MellonCollie2012_summary](https://github.com/avapolzin/albumpl/assets/29441772/1004c6cd-a611-4b6f-be02-1ae10b3d6b16)

7. __Yoshimi__ inspired by the Flaming Lips - _Yoshimi Battles the Pink Robots_
![Yoshimi_summary](https://github.com/avapolzin/albumpl/assets/29441772/91fb301e-b39b-49fc-91b1-1f264f532872)

8. __Figure8__ inspired by Elliott Smith - _Figure 8_
![Figure8_summary](https://github.com/avapolzin/albumpl/assets/29441772/97e5e4db-0760-4d5a-8bbf-b0af064e4235)

9. __LiveThroughThis__ inspired by Hole - _Live Through This_
![LiveThroughThis_summary](https://github.com/avapolzin/albumpl/assets/29441772/7379fd94-4e31-4cec-bad3-fd009e4a5b2f)

10. __Post__ inspired by Björk - _Post_
![Post_summary](https://github.com/avapolzin/albumpl/assets/29441772/95687e05-cf27-4987-bf95-3d066d888de6)

11. __VampireWeekend__ inspired by Vampire Weekend's self-titled debut
![VampireWeekend_summary](https://github.com/avapolzin/albumpl/assets/29441772/2d3904fd-f25b-4e8e-980a-140edab69890)

12. __CopperBlue__ inspired by Sugar - _Copper Blue_
![CopperBlue_summary](https://github.com/avapolzin/albumpl/assets/29441772/6f2cc0ef-f354-48f7-b5ed-5c0f419d3ba1)

13. __Dreamland__ inspired by Glass Animals - _Dreamland_
![Dreamland_summary](https://github.com/avapolzin/albumpl/assets/29441772/0b7ba095-098b-4698-bd73-2f072bf57934)

14. __Garbage__ inspired by Garbage - _Garbage_
![Garbage_summary](https://github.com/avapolzin/albumpl/assets/29441772/cf67fe44-b6ce-406f-a4e7-8d9c4fdeb9ad)

15. __BlameItOnGravity__ inspired by Old 97's - _Blame It On Gravity_
![BlameItOnGravity_summary](https://github.com/avapolzin/albumpl/assets/29441772/03f9613e-f7ea-46c8-a9ba-2194fee55291)

16. __ChutesTooNarrow__ inspired by the Shins - _Chutes Too Narrow_
![ChutesTooNarrow_summary](https://github.com/avapolzin/albumpl/assets/29441772/8d330b03-cefa-4062-a176-d1b3e906d9f3)


There are also a handful of alternative colormaps included in `albumpl`, which are not the default colormap associated with a particular palette, but can be accessed individually in the same way as any other colormap.

These standalone colormaps (named for songs on the album that inspired them) are:

<img src="https://github.com/avapolzin/albumpl/assets/29441772/c6188294-eb87-49ab-8a88-ea7a397d8cbe" width=30%> <img src="https://github.com/avapolzin/albumpl/assets/29441772/3dba42e4-b0bd-4998-9594-e1a58794193f" width=30%> <img src="https://github.com/avapolzin/albumpl/assets/29441772/321ddbfb-0a8d-4684-aff2-94d2160fc2f7" width=30%> <img src="https://github.com/avapolzin/albumpl/assets/29441772/6760e7f0-bafd-487b-ba27-4a6abb14e6f0" width=30%> <img src="https://github.com/avapolzin/albumpl/assets/29441772/0d6c3021-53f4-4fcd-8ce6-28c39ebfe054" width=30%> <img src="https://github.com/avapolzin/albumpl/assets/29441772/3de4aa2c-f6fe-4b51-a42e-43425f675790" width=30%> <img src="https://github.com/avapolzin/albumpl/assets/29441772/e600af19-16d4-4b05-aaa2-f716d98866bf" width=30%>


Additional palettes and colormaps will be added moving forward. Is there a specific album you want considered for a future palette? Please open an issue with the name of the album and artist and an image of the album cover.

<sup><sub>About the sample images: For sequential colormaps, the sample image is photometric _HST_ data of the dwarf galaxy [COSMOS-dw1](https://ui.adsabs.harvard.edu/abs/2021ApJ...914L..23P/abstract) in F814W. The sample image for diverging colormaps is an HI velocity map of the galaxy [M33 from GALFA-HI](https://ui.adsabs.harvard.edu/abs/2009ApJ...703.1486P/abstract). </sub></sup>

<sup><sub>And, though it should go without saying, I'll add: use of an artist's album cover to make a palette is not an endorsement of the artist or their (broadcast) personal views.</sub></sup>

***
# How to use `albumpl`:
### Some quick recipes.

If you are using v0.2 or below, before doing anything you will need to register the new album-inspired colormaps. To do this:
```python
from albumpl.cmap import register_all

register_all()
```
This is necessary for any of the `albumpl.palette` functions that use the colormaps, such as `set_default` and `set_default_cmap`. This is not necessary for versions >0.3.

- **To list all palettes and their properties:**
```python
from albumpl.palette import list_palettes

list_palettes()
```
*You can also filter for number of colors in the color cycle or type of colormap (sequential/diverging) with the arguments `mincolors` and `maptype`.*

- **To list all colormaps:**
```python
from albumpl.cmap import list_maps

list_maps()
```

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
You can access all of the colormaps using strings -- i.e., 'Matangi' or 'MellonCollie_r' for the reversed 'MellonCollie' map.

```python
import matplotlib.pyplot as plt
from albumpl.cmap import * #yes, this is bad practice, but easiest in this case!

register_all() #should only be run one time at the beginning of a script
plt.imshow(image, cmap = 'Yoshimi')
```
*or* if you are using version 0.2 or older you can access the colormaps via functions (offered as an option since it can be kind of nice for things like easily toggling whether a map is reversed or not) -- this is deprecated in v0.3 and above:
```python
import matplotlib.pyplot as plt
from albumpl.cmap import * #yes, this is bad practice, but easiest in this case!

plt.imshow(image, cmap = Yoshimi())
```
*To reverse the colormap, use the argument `reverse_cmap = True` or just feed the colormap the string "reverse" or "_r".*
```python
plt.imshow(image, cmap = Figure8(reverse_cmap = True))
```
*or*
```python
plt.imshow(image, cmap = LiveThroughThis('reverse'))
```
*or*
```python
plt.imshow(image, cmap = Post('_r'))
```

- **To access the colors in a color cycle/palette without setting a default:**
```python
from albumpl.palette import return_colors

return_colors('VampireWeekend')
```


<!-- For ease, you may also decide to permanently register these colormaps, effectively adding them to your current installation of `matplotlib`. You can find an up-to-date version of those instructions [here](https://matplotlib.org/stable/api/cm_api.html). -->

***
These palettes and colormaps are designed with a focus on remaining faithful to the appearance of the album covers instead of emphasizing perceptual uniformity. Most are still pretty good in this regard, but, just for everyone's peace of mind, following `matplotlib`, the lightness of each colormap as a function of index is shown below (all sequential maps are shown dark-to-light for easier comparison).
![Lightness](https://github.com/avapolzin/albumpl/assets/29441772/146ce43c-7f5d-48c4-8647-041f79f30b08)

***
# Papers that use `albumpl`:
- [Polzin et al. (2024)](https://arxiv.org/abs/2404.01382)
- [Polzin (2025)](https://arxiv.org/abs/2503.02288)
