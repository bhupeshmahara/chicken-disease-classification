import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "chicken-disease-classification"
AUTHOR_NAME = "bhupeshmahara"
SRC_REPO = "chicken-disease"
AUTHOR_EMAIL = "bhupeshmahara@gmail.com"

setuptools.setup(
    name = REPO_NAME,
    version = __version__,
    author = AUTHOR_NAME,
    description = "A small python package for CNN App",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where='src')
)
