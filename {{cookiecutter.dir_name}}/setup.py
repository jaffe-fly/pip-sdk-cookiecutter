from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.app_name}}',
    version='{{cookiecutter.version}}',
    description='',
    long_description="",
    url='',
    author='etherfurnace',
    author_email='core@etherfurnace.com',
    classifiers=[],
    keywords='',
    install_requires=['logzero==1.5.0', 'tqdm==4.62.2'],
    extras_require={},
    packages=find_packages(),
    package_data={},
    data_files=[],
    project_urls={},
)
