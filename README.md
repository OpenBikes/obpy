<div align="center">
  <img src="misc/obpy.png" alt="obpy_logo"/>
</div>

<br/>

<div align="center">
	<a href="https://badge.fury.io/py/obpy">
		<img src="https://badge.fury.io/py/obpy.svg" alt="PyPI version" height="18">
	</a>
	<a href="https://travis-ci.org/OpenBikes/obpy">
    	<img alt="Build Status" src="https://travis-ci.org/OpenBikes/obpy.svg?branch=master">
  	</a>
    <a href="https://coveralls.io/github/OpenBikes/obpy?branch=master">
		<img alt="Coverage Status" src="https://coveralls.io/repos/github/OpenBikes/obpy/badge.svg?branch=master">
    </a>
    <a href="https://www.codacy.com/app/Axel-BellecOrganization/obpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=OpenBikes/obpy&amp;utm_campaign=Badge_Grade">
    	<img src="https://api.codacy.com/project/badge/Grade/1e6a5c56b02d4955a4d87deb3f0538ff"/>
    </a>
	<a href="https://opensource.org/licenses/MIT">
		<img src="http://img.shields.io/:license-mit-ff69b4.svg?style=flat-square" alt="mit"/>
	</a>
</div>


# `obpy`
:snake: Python SDK for OpenBikes API

## Sample usage

By default, each `obpy` method returns a `requests` object. So basically, if you call `obpy.get_countries()`, you will have access to the request status code. To get the JSON data returned by the __OpenBikes API__ (`http://api.openbikes.co`), call the method `.json()`.

Here you can find a set of sample calls:

__Getting the list of countries__

```python
>>> import obpy
>>> response = obpy.get_countries()
>>> countries = response.json()
>>> countries
['Belgium', 'Croatia', 'France', 'Germany', 'Irlande', 'Japan', 'Latvia', 'Lithuania', 'Luxembourg', 'New Zealand', 'Norway', 'Poland', 'Slovenia', 'South Korea', 'Spain', 'Sweden', 'Turkey', 'UAE', 'UK', 'USA']
```

__Getting the closest station according to `lat/lon`__

```python
>>> import obpy
>>> response = obpy.get_closest_station(43.592021, 1.446276)
>>> station = response.json()
>>> station
{'altitude': 148.0,
 'docks': 20,
 'latitude': 43.5906050822776,
 'longitude': 1.44517443093758,
 'name': '00103 - ST MICHEL ST CATHERINE',
 'slug': '00103-st-michel-st-catherine'}
```

__Making a forecast for a station at a certain moment__

```python
>>> import obpy
>>> response = obpy.get_forecast(city_slug='toulouse', station_slug='00103-st-michel-st-catherine', kind='bikes', moment=1480451171)
>>> forecast = response.json()
{'moment': '2016-11-29T21:26:11', 'predicted': 11, 'kind': 'bikes', 'at': '2016-11-28T21:26:30.372014', 'expected_error': 4.04257073103125, 'station': {'longitude': 1.44517443093758, 'slug': '00103-st-michel-st-catherine', 'altitude': 148.0, 'name': '00103 - ST MICHEL ST CATHERINE', 'latitude': 43.5906050822776, 'docks': 20}}
```

__Getting the latest *geojson* for a city__

```python
>>> import obpy
>>> response = obpy.get_latest_geojson('toulouse')
>>> geojson = response.json()
>>> geojson['features'][0]
{'geometry': {'coordinates': [1.441003598726198, 43.608951960496405],
  'type': 'Point'},
 'properties': {'address': '2 RUE GATIEN ARNOULT',
  'bikes': 11,
  'name': '00055 - ST SERNIN G. ARNOULT',
  'slug': '00055-st-sernin-g-arnoult',
  'stands': 4,
  'status': 'OPEN',
  'update': '2016-11-28T21:32:07'},
 'type': 'Feature'}
```

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

## Installation

### **1. PyPI**

```sh
$ pip install obpy
```

### **2. GitHub for the latest development version**

```sh
$ pip install git+https://github.com/openbikes/obpy
```

`obpy` has the following dependencies:

- [`requests`](http://docs.python-requests.org/en/master/): simple HTTP library for Python