#!/usr/bin/env python
"""
This file generates all the necessary files for packaging for the project.
Read more about it at https://github.com/jpscaletti/mastermold/
"""
data = {
    "title": "SQLA-wrapper",
    "name": "sqla_wrapper",
    "pypi_name": "sqla-wrapper",
    "version": "3.0.0",
    "author": "Juan-Pablo Scaletti",
    "author_email": "juanpablo@jpscaletti.com",
    "description": "A framework-independent wrapper for SQLAlchemy that makes it really easy to set up.",
    "copyright": "2013",
    "repo_name": "jpscaletti/sqla-wrapper",
    "home_url": "https://jpscaletti.com/sqla-wrapper",
    # Displayed in the pypi project page
    "project_urls": {
        "Documentation": "https://jpscaletti.com/sqla-wrapper/",
    },
    "extra_classifiers": [
    ],
    "development_status": "5 - Production/Stable",
    "minimal_python": 3.6,
    "install_requires": [
        "inflection",
        "sqlalchemy ~= 1.0",
    ],
    "testing_requires": [
        "pytest",
        "pytest-cov",
        "mock",
    ],
    "development_requires": [
        "tox",
        "sphinx",
    ],
    "entry_points": "",
    "coverage_omit": [],
}


exclude = [
    "hecto.yml",
    "README.md",
    ".git",
    ".git/*",
    ".venv",
    ".venv/*",
    "CHANGELOG.md.md",
]


def do_the_thing():
    import hecto

    hecto.copy(
        # "gh:jpscaletti/mastermold.git",
        "../mastermold",  # Path to the local copy of Master Mold
        ".",
        data=data,
        exclude=exclude,
        force=False,
    )


if __name__ == "__main__":
    do_the_thing()
