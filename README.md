# windyLib
version: 0.0.1 [![](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/download/releases/3.5/)
ONLY WORK ON PYTHON 3.
## Description
windyLib is a library including helper functions which can request and analyze the weather forecast data from www.windy.com

## How to install
```
pip3 install windyLib
```


## Functions
```
getWeatherData(org, lon, lat)
```
- org (string): 'EC' or 'GFS' (one of the world weather models)
- lon (float): longitude of the location
- lat (float): latitude of the location

return type:

- (json) the raw json file from windy.com

```
getTimeSeriesVerticalWeather(org, lon, lat)
```
- org (string): 'EC' or 'GFS' (one of the world weather models)
- lon (float): longitude of the location
- lat (float): latitude of the location

return type:

- (array) 3D array([element, time, pressure(Geoheight)]) after the analysis from the json data from windy.com

[time, Pressure(Geoheight), Temperature, Humidity, windUcomonent, windVcomponent]
- every component is a 2D array, if you want to achieve only one time point, for example, the initial value of Temperature, you can use Temperature[0]
- every 1D array in the previous 2D array is element vs. Pressure(Geoheight)
## Further

more functions will be added