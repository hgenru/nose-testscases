from setuptools import setup, find_packages

try:
    desc = open('README.rst').read()
except:
    desc = 'see README.rst'


setup(
    name="testscases",
    version="0.1",
    description="Nosetests plugin to create different test cases",
    long_description=desc,
    url="https://github.com/hgenru/nose-testscases",
    license="WTFPL",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['nose'],
    entry_points={
        'nose.plugins': ['testscases = testscases.testscases:ExtendedTestsCases']
    },

)
