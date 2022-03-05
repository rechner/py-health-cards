from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="healthcards",
    packages=["healthcards"],
    version="0.1.4",
    description="Python parser for https://spec.smarthealth.cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rechner/py-health-cards",
    author="Rechner Fox",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=["jwcrypto"],
)
