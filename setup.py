from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

keywords = [ 'Dinheiro', 'dinheiro brasileiro', 'reias', 'Dinheiro em reais', 
            'Real_brasileiro', 'Real brasileiro', 'R$'
            ]

setup(name='Real-Brasileiro',
    version='0.0.1',
    license='MIT License',
    author='Daniel Mendonca',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='heromon.9010@gmai.com',
    keywords= keywords,
    description='Classe para formatar valores para o formato de Real Brasileiro',
    packages=['real_br'],
    install_requires=['re'],)