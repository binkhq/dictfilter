import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dictfilter',
    version='2.0.0',
    author='Chris Latham',
    author_email='opensource@bink.com',
    description='Filter dictionaries based on a list of field names.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/binkhq/dictfilter',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
