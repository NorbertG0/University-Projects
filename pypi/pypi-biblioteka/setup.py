from setuptools import setup, find_packages

setup(
    name='my_api_library',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests', 'python-dotenv',
    ],
    author='Norbert',
)