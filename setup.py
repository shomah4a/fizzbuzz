import setuptools
import fizzbuzz as pkg

pkgname = pkg.__name__

setuptools.setup(
    name=pkgname,
    version=pkg.__version__,
    modules=[pkgname],
    install_requires=[
        ],
    author=pkg.__author__,
    author_email='shoma.h4a+pypi@gmail.com',
    license=pkg.__license__,
    url='https://github.com/shomah4a/fizzbuzz',
    description='fizzbuzz',
    long_description=pkg.__doc__,
    classifiers='''
Programming Language :: Python
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Topic :: Utilities
'''.strip().splitlines())

