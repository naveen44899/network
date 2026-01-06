"""
Setup configuration for the networkSecurity package.
"""

from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    Reads requirements.txt and returns a list of dependencies.
    """
    requirements: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            for line in file:
                requirement = line.strip()
                if requirement and not requirement.startswith("-e"):
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements


setup(
    name="networkSecurity",
    version="0.0.1",
    author="Naveen Kumar S",
    author_email="naveen8296088066@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)


