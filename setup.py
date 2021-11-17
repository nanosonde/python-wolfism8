""" setup for creating pypi package """
import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-wolfism8",
    version="1.4",
    author="marcschmiedchen",
    author_email="marc.schmiedchen@protonmail.com",
    description="Get data from wolf heating system via ISM8",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test.*", "test"]),
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",   
    ],
)
