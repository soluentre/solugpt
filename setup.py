from setuptools import setup, find_packages

setup(
    name='chatgpt',
    version='0.5',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chatgpt = chatgpt.chat:main'
        ]
    },
    install_requires=[
        'openai==0.27.4',
    ],
    author='Shiyao Wang',
    author_email='galadata@sina.com',
    description='A package for chatting with GPT-3.',
    url='https://github.com/soluentre/unicellgpt'
)
