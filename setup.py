from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    ]


setup(name='package',
      version='0.0.1',  # https://www.python.org/dev/peps/pep-0440/
      packages=['pypolynom'],
      python_requires='>=3.4',
      setup_requires=['setuptools','wheel'],
      install_requires=['numpy>=1.8'],
      description='Sample project for distribution training',
      #long_description=long_description,
      url='https://gitlab.esrf.fr/silx/trainingproject',
      classifiers=classifiers,
      author='Someone',
      author_email='someone@somewhere.org',
      # keywords='',
      project_urls={
            'Issues': 'https://gitlab.esrf.fr/silx/trainingproject/issues',
      }
      # or
      # packages=find_packages(exclude=[]),
      )

