import setuptools

setuptools.setup(
	name = "albumpl",
	version = "0.1",
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
	install_requires = ["matplotlib"]
)
