from setuptools import setup, find_packages

setup(
    name="yantra_patterns",
    version="1.0.1",
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    description="A package to generate yantras with Sinhala and English text.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/yantra_patterns",  # Replace with your actual GitHub repo
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["fonts/*.ttf"],  # Include font files
    },
    install_requires=[
        "Pillow",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
