from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scrapysub",  # The name of your package
    version="0.1.2",
    author="ZULQAR NAIN",
    author_email="zulqarnainhumbly258@gmail.com",
    description=(
        "ScrapySub is a Python library designed to recursively scrape website content, including subpages. "
        "It fetches the visible text from web pages and stores it in a structured format for easy access and analysis. "
        "This library is particularly useful for NLP and AI developers who need to gather large amounts of web content for their projects."
    ),
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
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
        "langchain_core>=0.0.0",  # Adjust version as needed
        "aiohttp>=3.7.4",  # Needed for asynchronous fetching
        "tqdm>=4.59.0",  # Optional: for progress logging
        "langchain_core"
        "fake_useragent>=0.1.11",  # Optional: for generating random user agents
    ],
)
