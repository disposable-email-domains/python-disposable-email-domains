from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

__version__ = "0.0.151"

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
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Typing :: Typed",
    ],
    keywords="disposable email domains blocklist",
    packages=["disposable_email_domains"],
    package_data={"disposable_email_domains": ["py.typed"]},
    extras_require={
        "dev": ["check-manifest"],
    },
)
