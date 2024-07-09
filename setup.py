from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ScrapySub",  # The name of your package
    version="0.1.1",
    author="ZULQAR NAIN",
    author_email="zulqarnainhumbly258@gmail.com",
    description="A simple web scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ENGRZULQARNAIN/ScrapySub",
    project_urls={
        "Bug Tracker": "https://github.com/ENGRZULQARNAIN/ScrapySub/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
