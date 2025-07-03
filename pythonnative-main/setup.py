from setuptools import setup, find_packages
import platform


if platform.system() == "Windows":
    lib_file = 'interpolator/lib/newton.dll'
else:
    lib_file = 'interpolator/lib/newton.so'

setup(
    name='pythonnative',
    version='1.0.0',
    description='Interpolacja Newtona z natywną biblioteką w C++',
    author='Norbert',
    packages=find_packages(),
    package_data={
        'interpolator': ['lib/*.dll', 'lib/*.so'],
    },
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
)
