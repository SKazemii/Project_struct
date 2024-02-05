from setuptools import find_packages, setup



with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
AUTHOR_USER_NAME = "skazemii"
AUTHOR_EMAIL = "skazemi1@unb.ca"


setup(
    name='{{cookiecutter.project_name}}',
    version=__version__,
    author='{{ cookiecutter.author_name }}',
    author_email=AUTHOR_EMAIL,
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{{ cookiecutter.repo_name }}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{{ cookiecutter.repo_name }}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}'
)