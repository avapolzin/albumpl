import os
import sys
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../albumpl'))

autodoc_preserve_defaults = True

project = 'albumpl'
copyright = '2024, Ava Polzin'
author = 'Ava Polzin'
root_doc = 'index'

release = '0.3.5'

extensions = [
	'sphinx_rtd_theme',
	'sphinx.ext.autodoc',
	'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', '.DS_STORE']

html_theme = 'sphinx_rtd_theme'

html_static_path = []

rst_epilog = """
.. |logo| image:: https://github.com/user-attachments/assets/5c11856d-1f9f-4418-a977-48aa6d83ba84
            :alt: albumpl-logo
.. |londoncalling| image:: https://github.com/avapolzin/albumpl/assets/29441772/27db7318-20d0-4bc2-8a17-cfb41592ef75
            :alt: london-calling	 
.. |antisocialites| image:: https://github.com/avapolzin/albumpl/assets/29441772/13bd2938-051c-4150-b069-8e9476ba5336
            :alt: antisocialites
.. |rhumbline| image:: https://github.com/avapolzin/albumpl/assets/29441772/012b07ef-a4dd-4456-a2b4-ae731106a30d
            :alt: rhumb-line
.. |matangi| image:: https://github.com/avapolzin/albumpl/assets/29441772/d26d43c9-96e1-4795-b544-c673e1dddb5f
            :alt: matangi
.. |melloncollie| image:: https://github.com/avapolzin/albumpl/assets/29441772/079861b9-7aa6-4854-993e-9f4dbe691ec5
            :alt: mellon-collie
.. |melloncollie2012| image:: https://github.com/avapolzin/albumpl/assets/29441772/1004c6cd-a611-4b6f-be02-1ae10b3d6b16
            :alt: mellon-collie-2012
.. |yoshimi| image:: https://github.com/avapolzin/albumpl/assets/29441772/91fb301e-b39b-49fc-91b1-1f264f532872
            :alt: yoshimi
.. |figure8| image:: https://github.com/avapolzin/albumpl/assets/29441772/97e5e4db-0760-4d5a-8bbf-b0af064e4235
            :alt: figure8
.. |livethroughthis| image:: https://github.com/avapolzin/albumpl/assets/29441772/7379fd94-4e31-4cec-bad3-fd009e4a5b2f
            :alt: live-through-this
.. |post| image:: https://github.com/avapolzin/albumpl/assets/29441772/95687e05-cf27-4987-bf95-3d066d888de6
            :alt: post
.. |vampireweekend| image:: https://github.com/avapolzin/albumpl/assets/29441772/2d3904fd-f25b-4e8e-980a-140edab69890
            :alt: vampire-weekend
.. |copperblue| image:: https://github.com/avapolzin/albumpl/assets/29441772/6f2cc0ef-f354-48f7-b5ed-5c0f419d3ba1
            :alt: copper-blue
.. |dreamland| image:: https://github.com/avapolzin/albumpl/assets/29441772/0b7ba095-098b-4698-bd73-2f072bf57934
            :alt: dreamland
.. |garbage| image:: https://github.com/avapolzin/albumpl/assets/29441772/cf67fe44-b6ce-406f-a4e7-8d9c4fdeb9ad
            :alt: garbage
.. |blameitongravity| image:: https://github.com/avapolzin/albumpl/assets/29441772/03f9613e-f7ea-46c8-a9ba-2194fee55291
            :alt: blame-it-on-gravity
.. |chutestoonarrow| image:: https://github.com/avapolzin/albumpl/assets/29441772/8d330b03-cefa-4062-a176-d1b3e906d9f3
            :alt: chutes-too-narrow
.. |clampdown| image:: https://github.com/avapolzin/albumpl/assets/29441772/c6188294-eb87-49ab-8a88-ea7a397d8cbe
            :alt: london-calling-alt-clampdown
            :scale: 30%
.. |plimsollpunks| image:: https://github.com/avapolzin/albumpl/assets/29441772/3dba42e4-b0bd-4998-9594-e1a58794193f
            :alt: antisocialites-alt-plimsoll-punks
            :scale: 30%
.. |winter05| image:: https://github.com/avapolzin/albumpl/assets/29441772/321ddbfb-0a8d-4684-aff2-94d2160fc2f7
            :alt: rhumb-line-alt-winter05
            :scale: 30%
.. |missworld| image:: https://github.com/avapolzin/albumpl/assets/29441772/6760e7f0-bafd-487b-ba27-4a6abb14e6f0
            :alt: live-through-this-alt-miss-world
            :scale: 30%
.. |heatwaves| image:: https://github.com/avapolzin/albumpl/assets/29441772/0d6c3021-53f4-4fcd-8ce6-28c39ebfe054
            :alt: dreamland-alt-heat-waves
            :scale: 30%
.. |vow| image:: https://github.com/avapolzin/albumpl/assets/29441772/3de4aa2c-f6fe-4b51-a42e-43425f675790
            :alt: garbage-alt-vow
            :scale: 30%
.. |youngpilgrims| image:: https://github.com/avapolzin/albumpl/assets/29441772/e600af19-16d4-4b05-aaa2-f716d98866bf
            :alt: chutes-too-narrow-alt-young-pilgrims
            :scale: 30%

"""