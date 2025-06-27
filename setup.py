from setuptools import setup, find_packages

setup(
    name="minimocker",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "watchdog",
        "python-jose",
    ],
    entry_points={
        'console_scripts': [
            'minimocker=minimocker.cli:main',
        ],
    },
    author="Ram Awasthi",
    description="A lightweight mock API server with JWT and hot reload",
    python_requires=">=3.7",
)
