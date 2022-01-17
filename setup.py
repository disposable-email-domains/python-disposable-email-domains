from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

__version__ = "0.0.70"

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="disposable-email-domains",
    version=__version__,
    description="A set of disposable email domains",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/disposable-email-domains/disposable-email-domains",
    author="Dustin Ingram",
    author_email="github@dustingram.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="disposable email domains blocklist",
    packages=["disposable_email_domains"],
    extras_require={
        "dev": ["check-manifest"],
    },
)
