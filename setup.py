from setuptools import setup, find_packages

setup(name = "windyLib",
    version = "0.1.2",
    description = "weather data access and analysis from www.windy.com",
    author = "Louis He",
    author_email = "1726110778@qq.com",
    url = "https://github.com/Louis-He/windyLib",
    packages= find_packages(),
    py_modules=['windyLib'],
    long_description = """weather data access and analysis from www.windy.com"""
)