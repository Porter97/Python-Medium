from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

setup(
    name='python-medium',
    version='v1.1',
    packages=find_packages(),
    url='https://github.com/Porter97/Python-Medium',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    author='Spencer Porter',
    author_email='spencer.porter3@gmail.com',
    description='Python Medium API client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests'],
    download_url='https://github.com/Medium/medium-sdk-python/tarball/v0.3.0',
    keywords=['medium', 'sdk', 'oauth', 'api'],
)
