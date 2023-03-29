#!/usr/bin/env python
#
# Appspand Cognica
#
# Copyright (c) 2023 Appspand, Inc.
#

import setuptools


setuptools.setup(
    name="cognica",
    description="Python client for Appspand Cognica database",
    long_description=open("README.md").read().strip(),
    long_description_content_type="text/markdown",
    keywords=["Cognica", "key-value", "document store",
              "full-text search", "database"],
    version="0.1.0",
    packages=setuptools.find_packages(include=["cognica"]),
    url="https://github.com/appspand/cognica-python",
    project_urls={
        "Documentation": "https://github.com/appspand/cognica-python",
        "Changes": "https://github.com/appspand/cognica-python/releases",
        "Code": "https://github.com/appspand/cognica-python",
        "Issue tracker": "https://github.com/appspand/cognica-python/issues",
    },
    author="Appspand, Inc.",
    author_email="jaepil@appspand.com",
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
        "pyarrow>=11.0.0",
        "grpcio>=1.53.0",
    ],
    extras_require={
        "protobuf": ["grpcio>=1.43.0"]
    },
)
