from setuptools import setup, find_packages

setup(
    name='python-medium',
    version='v1.0.2',
    packages=find_packages(),
    url='https://github.com/Porter97/Python-Medium',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    author='Spencer Porter',
    author_email='spencer.porter3@gmail.com',
    description='Python Medium API client',
    install_requires=['requests'],
    download_url='https://github.com/Medium/medium-sdk-python/tarball/v0.3.0',
    keywords=['medium', 'sdk', 'oauth', 'api'],
)
