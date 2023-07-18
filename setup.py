from setuptools import setup

with open('README.md', 'rt') as arq:
      readme = arq.read()

setup(
    name='real-brasileiro',
    version='0.2.1',
    long_description=readme,
    author='Daniel Coêlho',
    long_description_content_type='text/markdown',
    author_email='heromon.9010@gmail.com',
    url='https://github.com/MikalROn/Real_br',
    python_requires='>=3'
)
