from setuptools import find_packages, setup



with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
AUTHOR_USER_NAME = "skazemii"



setup(
    name='{{cookiecutter.project_name}}',
    version=__version__,
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/skazemii/{{ cookiecutter.repo_name }}",
    project_urls={
        "Bug Tracker": "https://github.com/skazemii/{{ cookiecutter.repo_name }}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}'
)