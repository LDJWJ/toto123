from setuptools import setup, find_packages

setup(
    name                = 'toto123',
    version             = '0.1',
    description         = 'toto123',
    author              = 'ldjwj',
    author_email        = 'colabstart@gmail.com',
    url                 = 'https://github.com/LDJWJ/toto123/',
    download_url        = 'https://github.com/LDJWJ/toto123/archive/0.0.tar.gz',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['toto123'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)