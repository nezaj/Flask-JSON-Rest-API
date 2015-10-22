from setuptools import setup, find_packages

# hack to fix a Python 2.7.3 issue with multiprocessing module --
# see http://bugs.python.org/issue15881
try:
    import multiprocessing
except ImportError:
    pass

dependencies = [
    # Flask and extensions
    "flask==0.10.1",
    "flask-script==2.0.5",
    # Static analysis
    "pep8>=1.6.2",
    "pylint>=1.4.4",
    # Testing
    "pytest==2.8.2"
]

setup(
    name="flask-json-api",
    version="0.1",
    packages=find_packages(),
    zip_safe=False,
    install_requires=dependencies
)
