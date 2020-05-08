from setuptools import setup, find_packages  
setup(  
    name="backend",
    version="1.0",
    description="watch list",
    author="lmk",
    author_email="lmk030@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flask"],
    extras_require={"dev": []},
)
