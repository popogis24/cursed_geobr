from setuptools import setup, find_packages

setup(
    name="cursed_geobr",
    version="0.1.0",
    author="Anderson Stolfi",
    author_email="",  # Adicione seu email se desejar
    description="Fork personalizado do geobr com funcionalidades extras como download de dados da ANM",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/popogis24/cursed_geobr",
    packages=["cursed_geobr"],
    install_requires=[
        "geopandas>=0.9.0",
        "pandas>=1.0.0",
        "requests>=2.0.0",
        "fiona>=1.8.0",
        "shapely>=1.7.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.6",
)
