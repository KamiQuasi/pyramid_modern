import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid'
    ]

setup(name='pyramid_modern',
      version='1.0',
      description='Modern Frontend Pyramid Scaffold',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Framework :: Pylons",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Luke Dary',
      author_email='lukedary@gmail.com',
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

