from setuptools import setup, find_packages

setup(
    name='chatgpt',
    version='0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chatgpt = chatgpt.chat:main'
        ]
    },
    install_requires=[
        'openai==3.0.0',
    ],
    author='Shiyao Wang',
    author_email='galadata@sina.com',
    description='A package for chatting with GPT-3.',
    url='https://github.com/soluentre/unicellgpt'
)
