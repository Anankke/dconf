import setuptools

setuptools.setup(
    name="dconf",
    version="0.0.1",
    author="Anankke W",
    author_email="anankke@pm.me",
    description="Easy dot representation configuration module.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    license="LICENSE",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Anankke/dconf",
    project_urls={
        "Bug Tracker": "https://github.com/Anankke/dconf/issues",
    },
    python_requires=">=3.6",
    package_dir={"": "src"},
    install_requires=[],
)
