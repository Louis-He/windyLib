from setuptools import setup, find_packages

setup(name = "windyLib",
    version = "0.1.5",
    description = "weather data access and analysis from www.windy.com",
    author = "Louis He",
    author_email = "1726110778@qq.com",
    url = "https://github.com/Louis-He/windyLib",
    packages= find_packages(),
    py_modules=['windyLib'],
    long_description = """windyLib
version: 0.1.5 [ONLY COMPATIBLE WITH PYTHON 3]

Description
windyLib is a library including helper functions which can request and analyze the weather forecast data from www.windy.com, please visit project homepage for more information: https://github.com/Louis-He/windyLib

How to install:
pip3 install windyLib

"""
)