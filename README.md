<div align="center">
  <img src="misc/obpy.png" alt="obpy_logo"/>
</div>

<br/>

<div align="center">
	<a href="https://travis-ci.org/OpenBikes/obpy">
    <img alt="Build Status" src="https://travis-ci.org/OpenBikes/obpy.svg?branch=master">
  </a>
  <a href="https://coveralls.io/github/OpenBikes/obpy?branch=master">
	<img alt="Coverage Status" src="https://coveralls.io/repos/github/OpenBikes/obpy/badge.svg?branch=master">
  </a>
	<a href="https://opensource.org/licenses/MIT">
	<img src="http://img.shields.io/:license-mit-ff69b4.svg?style=flat-square" alt="mit"/>
	</a>
</div>


# `obpy`
:snake: Python SDK for OpenBikes API

## Available functions

| **Function**              | **API Endpoint**                                          | **Description**                                                   |
|---------------------------|-----------------------------------------------------------|-------------------------------------------------------------------|
| `get_latest_geojson`    	| `GET /geojson/<string:city_slug>`                        		| Return the latest geojson file of a city.                      	|
| `get_countries`         	| `GET /countries`                                         		| Return the list of countries.                                  	|
| `get_metrics`           	| `GET /metrics`                                           		| Returns latest metrics.                                        	|
| `get_cities`            	| `GET /cities`                                            		| Return the list of cities.                                     	|
| `get_stations`          	| `GET /stations`                                          		| Return the list of stations.                                   	|
| `get_providers`         	| `GET /providers`                                         		| Return the list of providers                                   	|
| `get_updates`           	| `GET /updates`                                           		| Return the list of latest updates for each city.               	|
| `get_forecast`          	| `POST /forecast`                                         		| Return a forecast for a station at a given time.               	|
| `get_filtered_stations` 	| `POST /filtered_stations`                                		| Return filtered stations.                                      	|
| `get_closest_city`      	| `GET /closest_city/<float:latitude>/<float:longitude>`    	| Return the closest city for a given latitude and longitude.    	|
| `get_closest_station`   	| `GET /closest_station/<float:latitude>/<float:longitude>` 	| Return the closest station for a given latitude and longitude. 	|
