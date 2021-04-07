import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auto-flutter",
    version="1.1.0",
    author="jspw",
    author_email="mhshifat757@gmail.com",
    description="Auto Flutter is a python package to create structured base flutter projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jspw/Auto-Flutter",
    license="GNU General Public License v3.0",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "auto-flutter=auto_flutter.__main__:main",
        ]
    },
)
