import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uottawa-gym-scheduler", # Replace with your own username
    version="0.0.3",
    author="Vladislav Jidkov",
    author_email="vladjdk@gmail.com",
    description="uOttawa COVID Gym Scheduler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/photonized/uOttawa-Gym-Scheduler",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['uottawa-gym-scheduler=uottawa_scheduler.scheduler:main'],
    },
    install_requires=[
        'pandas',
        'beautifulsoup4',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)