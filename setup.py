import setuptools
# import sys

# -----------------------------------------------------------------------------

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='grain_geometry_tools',
    version='1.1',
    description=('Python lib to process grain geometries from cuboid files'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='D. Cortés-Ortuño, F. Out, M. Kosters, K. Fabian, L. V. de Groot',
    author_email='d.i.cortes@uu.nl',
    py_modules=['grain_geometry_tools'],
    install_requires=['numpy',
                      'scipy',
                      'pathlib',
                      'shapely',
                      'matplotlib'
                      ],
    # TODO: Update license
    classifiers=['License :: BSD2 License',
                 'Programming Language :: Python :: 3 :: Only',
                 ],
)
