.. _albumpl.options:

Palette/Colormap Options
========================

Each of the included palettes has been checked with `COBLIS <https://www.color-blindness.com/coblis-color-blindness-simulator/>`_, and should be legible for individuals with most common forms of color blindness. Best, though, is to check your specific figures' readability, too.

Additional palettes and colormaps will be added moving forward. Is there a specific album you want considered for a future palette? Please open an `issue <https://github.com/avapolzin/albumpl/issues>`_ with the name of the album and artist and an image of the album cover.

The palette options (to now) are:

* **LondonCalling** inspired by The Clash - *London Calling* (which, of course, **technically** means it was inspired by Elvis Presley's eponymous album)
|londoncalling|

* **Antisocialites** inspired by Alvvays - *Antisocialites*
|antisocialites|

* **RhumbLine** inspired by Ra Ra Riot - *The Rhumb Line*
|rhumbline|

* **Matangi** inspired by M.I.A. - *Matangi*
|matangi|

* **MellonCollie** inspired by the Smashing Pumpkins - *Mellon Collie and the Infinite Sadness*
|melloncollie|

* **MellonCollie2012** inspired by the Smashing Pumpkins - *Mellon Collie and the Infinite Sadness (2012 Deluxe Edition)*
|melloncollie2012|

* **Yoshimi** inspired by the Flaming Lips - *Yoshimi Battles the Pink Robots*
|yoshimi|

* **Figure8** inspired by Elliott Smith - *Figure 8*
|figure8|

* **LiveThroughThis** inspired by Hole - *Live Through This*
|livethroughthis|

* **Post** inspired by Björk - *Post*
|post|

* **VampireWeekend** inspired by Vampire Weekend's self-titled debut
|vampireweekend|

* **CopperBlue** inspired by Sugar - *Copper Blue*
|copperblue|

* **Dreamland** inspired by Glass Animals - *Dreamland*
|dreamland|

* **Garbage** inspired by Garbage - *Garbage*
|garbage|

* **BlameItOnGravity** inspired by Old 97's - *Blame It On Gravity*
|blameitongravity|

* **ChutesTooNarrow** inspired by the Shins - *Chutes Too Narrow*
|chutestoonarrow|


There are also a handful of alternative colormaps included in `albumpl`, which are not the default colormap associated with a particular palette, but can be accessed individually in the same way as any other colormap.

These standalone colormaps (named for songs on the album that inspired them) are:

|clampdown| |plimsollpunks| |winter05|
|missworld| |heatwaves| |vow|
|youngpilgrims|    


About the sample images: For sequential colormaps, the sample image is photometric *HST* data of the dwarf galaxy `COSMOS-dw1 <https://ui.adsabs.harvard.edu/abs/2021ApJ...914L..23P/abstract>`_ in F814W. The sample image for diverging colormaps is an HI velocity map of the galaxy `M33 from GALFA-HI <https://ui.adsabs.harvard.edu/abs/2009ApJ...703.1486P/abstract>`_.

And, though it should go without saying, I'll add: use of an artist's album cover to make a palette is not an endorsement of the artist or their (broadcast) personal views.

These palettes and colormaps are designed with a focus on remaining faithful to the appearance of the album covers instead of emphasizing perceptual uniformity. Most are still pretty good in this regard, but, just for everyone's peace of mind, following ``matplotlib``, the lightness of each colormap as a function of index is shown below (all sequential maps are shown dark-to-light for easier comparison).

|lightnessv0.3|
