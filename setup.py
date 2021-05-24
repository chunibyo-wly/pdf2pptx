import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pdf2pptx-cli",
    version=open("pdf2pptx/version").read(),
    description="convert pdf to 1200 dpi image ppt",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/chunibyo-wly/pdf2pptx",
    author="chunibyo-wly",
    author_email="chunibyo.wly@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=find_packages(),
    install_requires=["pillow>=8.2.0", "pdf2image>=1.15.1", "python-pptx>=0.6.19"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pdf2pptx=pdf2pptx.__main__:main",
        ]
    },
)
