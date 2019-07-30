import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymaze",
    version="0.0.1",
    author="Jostein Brændshøi",
    author_email="jostbr@github",
    description="PyMaze package",
    long_description=long_description,
    long_description_content_type="python",
    url="https://github.com/jostbr/pymaze",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
