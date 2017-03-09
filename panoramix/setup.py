from setuptools import setup, find_packages
import os

CURPATH = os.path.dirname(os.path.realpath(__file__))

PACKAGE_NAME = "panoramix"
SHORT_DESCRIPTION = "The Panoramix Project"

version_file = os.path.join(CURPATH, "..", "version.txt")
with open(version_file) as f:
    VERSION = f.read().strip()

PACKAGES_ROOT = '.'
PACKAGES = find_packages(PACKAGES_ROOT)

# Package meta
CLASSIFIERS = []


requirements_file = os.path.join(CURPATH, "requirements.txt")
with open(requirements_file) as f:
    INSTALL_REQUIRES = [
        x.strip('\n')
        for x in f.readlines()
        if x and x[0] != '#'
    ]

EXTRAS_REQUIRES = {
}

TESTS_REQUIRES = [
]


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    license='Affero GPL v3',
    author='GRNET S.A.',
    author_email='panoramix@dev.grnet.gr',
    description=SHORT_DESCRIPTION,
    classifiers=CLASSIFIERS,
    packages=PACKAGES,
    package_dir={'': PACKAGES_ROOT},
    namespace_packages=['panoramix'],
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRES,
    tests_require=TESTS_REQUIRES,

    entry_points={
        'console_scripts': [
            'panoramix = panoramix.cli:main',
            'panoramix-wizard = panoramix.wizard:main',
            'sphinxmix-client = panoramix.sphinxmix_client:main',
        ],
    },
)
