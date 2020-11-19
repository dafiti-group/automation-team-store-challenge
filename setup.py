from setuptools import setup, find_packages

def read(filename):
    return [req.strip() for req in open(filename).readlines()]

setup(
    name="store",
    version="0.1.0",
    description="Application of control and delivery of products for the footwear industry",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt")
)