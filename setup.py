from setuptools import setup
from codecs import open


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    my_license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='SeriousGame',
    version='0.1.0',
    description='A serious simulation game',
    long_description=readme,
    url='https://github.com/ThT12/SeriousGame',
    author='Romain ThT12 Bourget',
    author_email='romain@bourget-olivier.fr',
    license=my_license,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Gamer',
        'Topic :: Serious Game',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='serious game simulation ecology economy social',
    packages=['seriousgame', 'seriousgame.io', 'seriousgame.data'],
    package_dir={'': 'src'},
    install_requires=required,
    entry_points={
        'console_scripts': [
            'play=seriousgame.game:play',
        ],
    },
)
