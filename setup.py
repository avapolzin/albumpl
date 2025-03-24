import setuptools
from pathlib import Path
albumpl_home = Path(__file__).parent
pypi_descrip = (albumpl_home / "README.md").read_text()

setuptools.setup(
	name = "albumpl",
	version = "0.3.7",
	author = "Ava Polzin",
	author_email = "apolzin@uchicago.edu",
	description = "Matplotlib color palettes based on album covers.",
	packages = ["albumpl", "albumpl/palette", "albumpl/cmap"],
	url = "https://github.com/avapolzin/albumpl",
	license = "MIT",
	classifiers = [
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python"],
	python_requires = ">=3",
	install_requires = ["matplotlib"],
	long_description=pypi_descrip,
	long_description_content_type='text/markdown'
)
