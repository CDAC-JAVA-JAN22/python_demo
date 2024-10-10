from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    description="A simple Python calculator project",
    author="Abhijeet",
    packages=find_packages(),
    install_requires=[],  # You can add dependencies like ['numpy', 'requests'] here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
