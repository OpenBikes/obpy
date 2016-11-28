import requests
from obpy import config

from obpy.util import remove_none_values_from_dict

OB_URL = config.BASE_URL


def get_latest_geojson(city):
    """ Return the latest geojson file of a city. """

    url = '{BASE_URL}/geojson/{city}'.format(BASE_URL=OB_URL, city=city)
    return requests.get(url)


def get_countries(provider=None):
    """ Return the list of countries. """

    url = '{BASE_URL}/countries'.format(BASE_URL=OB_URL)
    request_params = {'provider': provider} if provider else {}
    return requests.get(url, params=request_params)


def get_providers(country=None):
    """ Returns the list of providers. """

    url = '{BASE_URL}/providers'.format(BASE_URL=OB_URL)
    request_params = {'country': country} if country else {}
    return requests.get(url, params=request_params)


def get_metrics():
    """ Returns latest metrics. """

    url = '{BASE_URL}/metrics'.format(BASE_URL=OB_URL)
    return requests.get(url)


def get_cities(slug=None, country=None, provider=None, predictable=None, active=None):
    """ Return the list of cities. """

    url = '{BASE_URL}/cities'.format(BASE_URL=OB_URL)
    request_params = {
        'slug': slug,
        'country': country,
        'provider': provider,
        'predictable': predictable,
        'active': active,
    }
    return requests.get(url, params=request_params)


def get_stations(slug=None, city_slug=None):
    """ Return the list of stations. """

    url = '{BASE_URL}/stations'.format(BASE_URL=OB_URL)
    request_params = {
        'slug': slug,
        'city_slug': city_slug,
    }
    return requests.get(url, params=request_params)


def get_updates(city_slug=None):
    """ Return the list of latest updates for each city. """

    url = '{BASE_URL}/updates'.format(BASE_URL=OB_URL)
    return requests.get(url, params={'city_slug': city_slug})


def get_forecast(city_slug, station_slug, kind, moment):
    """ Return a forecast for a station at a given time. """

    url = '{BASE_URL}/forecast'.format(BASE_URL=OB_URL)
    payload = remove_none_values_from_dict({
        'city_slug': city_slug,
        'station_slug': station_slug,
        'kind': kind,
        'moment': moment,
    })
    return requests.post(url, json=payload)


def get_filtered_stations(city_slug=None, latitude=None, longitude=None, limit=None, kind=None, mode=None, moment=None, desired_quantity=None, confidence=None):
    """ Return filtered stations. """

    url = '{BASE_URL}/filtered_stations'.format(BASE_URL=OB_URL)
    payload = remove_none_values_from_dict({
        'city_slug': city_slug,
        'latitude': latitude,
        'longitude': longitude,
        'limit': limit,
        'kind': kind,
        'mode': mode,
        'desired_quantity': desired_quantity,
        'confidence': confidence,
    })
    return requests.post(url, json=payload)


def get_closest_city(latitude, longitude):
    """ Return the closest city for a given latitude and longitude. """

    url = '{BASE_URL}/closest_city/{lat}/{lon}'.format(BASE_URL=OB_URL, lat=latitude, lon=longitude)
    return requests.get(url)


def get_closest_station(latitude, longitude):
    """ Return the closest station for a given latitude and longitude."""

    url = '{BASE_URL}/closest_station/{lat}/{lon}'.format(
        BASE_URL=OB_URL, lat=latitude, lon=longitude)
    return requests.get(url)
