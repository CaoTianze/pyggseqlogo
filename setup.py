import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyggseqlogo",
    version="0.9.0",
    author="Cao Tianze",
    author_email="hnrcao@qq.com",
    description="Python version of ggseqlogo. Based on plotnine (Python version of ggplot2). A derivative of plotnineSeqSuite.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caotianze/pyggseqlogo",
    project_urls={
        "Bug Tracker": "https://github.com/caotianze/pyggseqlogo/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['pyggseqlogo'],
    python_requires=">=3.10",
    install_requires=['plotnineseqsuite==0.9.1'],
    license="MIT",
    keywords=['ggplot2', 'plotnine', 'ggseqlogo', 'Sequence logo'],
    package_data={
        "": ["*.csv"]
    }
)
