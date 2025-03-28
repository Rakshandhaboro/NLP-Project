from setuptools import setup, find_packages

setup(
    name="n2p",
    version="0.1.0",
    description="Natural Language Processing Utilities for Colab",
    packages=find_packages(),
    install_requires=[
        'nltk>=3.5',
        'numpy>=1.19.0',
        'tqdm>=4.45.0',
    ],
    python_requires=">=3.7",
    zip_safe=False,  # Critical for Colab compatibility
)
