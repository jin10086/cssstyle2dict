import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cssstyle2dict",  # Replace with your own username
    version="0.0.1",
    author="Gaojin",
    author_email="igaojin@qq.com",
    description="css style to dict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jin10086/cssstyle2dict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["cssutils"],
)
