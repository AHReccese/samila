# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


MINIMAL_DESCRIPTION = ''''''


def get_dev_requires():
    """Read dev-requirements.txt."""
    requirements = open("dev-requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return MINIMAL_DESCRIPTION


setup(
    name='samila',
    packages=['samila'],
    version='0.1',
    description='Generative ART',
    long_description="",
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='sepand@pycm.ir',
    url='https://github.com/sepandhaghighi/samila',
    keywords="generative-art art nft",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/samila',
        'Tracker': 'https://github.com/sepandhaghighi/samila/issues',
    },
    install_requires=[],
    python_requires='>=3.5',
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='MIT',
    include_package_data=True
)