#!/usr/bin/env python
"""Python setup file"""

from setuptools import setup

setup(
    name='fbcid',
    version='1.0.0',
    description='Facebook Conversation Image Downloader',
    author='Ezioleq',
    install_requires=[
        'fbchat==1.9.7',
        'wget>=3.2'
    ]
)
