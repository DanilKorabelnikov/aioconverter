import setuptools

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="aioconverter",
    version="0.9.0",
    author="DanilKorabelnikov",
    description="",
    url="https://github.com/DanilKorabelnikov/aioconverter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements
)