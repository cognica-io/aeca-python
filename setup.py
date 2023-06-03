#!/usr/bin/env python
#
# Cognica
#
# Copyright (c) 2023 Cognica, Inc.
#

import setuptools


setuptools.setup(
    name="cognica",
    description="Python client for Cognica database",
    long_description=open("README.md").read().strip(),
    long_description_content_type="text/markdown",
    keywords=[
        "Cognica",
        "key-value",
        "document store",
        "full-text search",
        "vector search",
        "search engine",
        "database",
    ],
    version="0.1.2",
    packages=setuptools.find_namespace_packages(where="src"),
    package_dir={"": "src"},
    url="https://github.com/cognicadb/cognica-python",
    project_urls={
        "Documentation": "https://github.com/cognicadb/cognica-python",
        "Changes": "https://github.com/cognicadb/cognica-python/releases",
        "Code": "https://github.com/cognicadb/cognica-python",
        "Issue tracker": "https://github.com/cognicadb/cognica-python/issues",
    },
    author="Cognica, Inc.",
    author_email="jaepil@cognica.io",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.5.3",
        "polars>=0.16.18",
        "pyarrow>=11.0.0",
        "grpcio>=1.53.0",
        "protobuf>=4.22.1",
    ],
    extras_require={"protobuf": ["grpcio>=1.43.0"]},
)
