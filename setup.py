from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    author="Rana Abouhussein",
    description="A simple math quiz ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ranaabouhussein/DSSS_homework_2.git",
    license="MIT",
)