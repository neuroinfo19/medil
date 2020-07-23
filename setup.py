from distutils.core import setup


setup(name='medil',
      version='0.4.0',
      packages=['medil'],
      install_requires=['numpy']
      extras_require={
          'dcor': ['dcor'],
          'GAN' : ['pytorch'],
          'visualization' : ['matplotlib', 'networkx']
      }
)
