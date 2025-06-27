import setuptools 

with open("README.md", "r", encoding ="utf-8") as f:
    long_description = f.read()


__version__ = " 0.0.0"

REPO_NAME = "text-summarizer-project"
AUTHOR_USER_NAME = "shweta_kush"
SRC_REPO ="TextSummarizer"
AUTHOR_EMAIL = "kushishweta@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarizer using the Transformer model",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME,
    packages_url={
        "bug Tracker": "https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)