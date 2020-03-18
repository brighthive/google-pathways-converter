import setuptools

VERSION = "1.0.0"

REQUIRED_PACKAGES = [
    "stringcase"
]

setuptools.setup(
    name="google-pathways-converter",
    version=VERSION,
    author="BrightHive",
    description="A library that converts programs data into the Schema.org definitions of EducationalOccupationProgram and WorkBasedProgram",
    url="https://github.com/brighthive/google-pathways-converter",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)