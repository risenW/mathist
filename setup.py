"""Setup for the mathist package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Dr Minion",
    author_email="minion@mail.com",
    name='mathist',
    license="MIT",
    description='Mathist is an efficient library for doing complicated mathematical operations',
    version='v0.1',
    long_description=README,
    url='https://github.com/risenW/mathist',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)