from setuptools import setup, find_packages
import npm

setup(
    name='npm',
    version=npm.VERSION,
    packages=find_packages(exclude=('tests',)),
    description='Python bindings and utils for npm.',
    install_requires=[
        'optional-django==0.1.0',
    ],
    author='mrlee2024',
    author_email='li.xiaolong@126.com',
)
