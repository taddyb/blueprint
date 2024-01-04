from setuptools import setup, find_packages

setup(
    name='blueprint',
    version='0.1.0',
    author='Tadd Bindas',
    author_email='taddbindas@gmail.com',
    description='A Python package for hydrological machine learning experiments',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/taddyb/blueprint',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        # e.g., 'numpy>=1.18.5', 'pandas>=1.1.3', 'torch>=1.6.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.8',
    include_package_data=True,
    keywords='hydrology, machine learning, deep learning, neural networks',
    zip_safe=False
)

