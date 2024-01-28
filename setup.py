
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis",
    version="1.0.4",
    author="Dhruv Lotiya",
    author_email="dhruv.lotia@gmail.com",
    description="A package -> Calculates Topsis Score and Ranks models according to weights and impacts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    download_url="https://github.com/Dhruv-os-23/Topsis-Dhruv-102117061/archive/refs/tags/1.0.4.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["Topsis_Dhruv"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Dhruv.__main__:main",
        ]
    },
)
