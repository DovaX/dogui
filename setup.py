import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='dogui',
    version='0.1.3',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='Code enabling easy gui creation for general applications ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/dogui',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'Pillow'
     ],
    python_requires='>=3.6',
)
    