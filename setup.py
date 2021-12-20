import pathlib
from setuptools import setup


# This call to setup() does all the work
setup(
    name="embed-templator",
    version="1.0.4",
    description=(
        "A Python Template manager for your discord bot to keep your embeds"
        " simple & consistent. "
    ),
    url="https://github.com/Sigmanificient/Embed-Templator",
    author="Sigmanificient",
    author_email="edhyjox@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=['embed_templator'],  # Pkg name
    include_package_data=True,
    install_requires=['disnake']
)
