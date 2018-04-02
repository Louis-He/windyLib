from setuptools import setup, find_packages

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["things/*"]

setup(name = "windyLib",
    version = "0.1",
    description = "weather data access and analysis from www.windy.com",
    author = "Louis He",
    author_email = "1726110778@qq.com",
    url = "https://github.com/Louis-He/windyLib",
    packages= find_packages(),
    long_description = """weather data access and analysis from www.windy.com"""
)