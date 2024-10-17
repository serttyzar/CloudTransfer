from setuptools import setup, find_packages

setup(
    name='cloud_transfer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'requests',
        'python-dotenv',
        'typer',
    ],
    entry_points={
        'console_scripts': [
            'cloudtransfer = cloud_transfer.cli:app',
        ],
    },
)