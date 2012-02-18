import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid >= 1.3'
    ]

setup(name='pyramid_modern',
      version='1.0',
      description='Modern Frontend Pyramid Scaffold',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Luke Dary',
      author_email='',
      url='https://github.com/KamiQuasi/pyramid_modern',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_modern",
      entry_points = """\
      [pyramid.scaffold] 
      pyramid_modern=pyramid_modern.scaffolds:ModernPyramidTemplate
      """,
      )

