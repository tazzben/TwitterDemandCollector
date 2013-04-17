try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	A collection tool for economists using the fact that twitter presents a demand curve for information
"""


setup(name="TwitterDemandCollector",
      version=1.0,
      description="A collection tool for economists using the fact that twitter presents a demand curve for information",
      author="Ben Smith",
      author_email="tazz_ben@ad.wsu.edu",
      url="https://github.com/tazzben/TwitterDemandCollector",
      license="Public Domain",
      packages=[],
	  scripts=['TwitterDemandCollector'],
	  package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Scientific/Engineering',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Science/Research'
      ]
     )