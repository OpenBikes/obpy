import requests
import config

OB_URL = config.BASE_URL


# @handle_connection
def get_latest_geojson(city):
    url = '{BASE_URL}/geojson/{city}'.format(BASE_URL=OB_URL, city=city)
    res = requests.get(url)
    return res


# @handle_connection
def get_countries(provider=None):
    url = '{BASE_URL}/countries'.format(BASE_URL=OB_URL)
    request_params = {'provider': provider} if provider else {}
    return requests.get(url, params=request_params)


# @handle_connection
def get_providers(country=None):
    url = '{BASE_URL}/providers'.format(BASE_URL=OB_URL)
    request_params = {'country': country} if country else {}
    return requests.get(url, params=request_params)


# @handle_connection
def get_metrics():
    url = '{BASE_URL}/metrics'.format(BASE_URL=OB_URL)
    res = requests.get(url)
    return res


# @handle_connection
def get_cities(name=None, slug=None, country=None, provider=None, predictable=None, active=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    return requests.get(url, params={})


# @handle_connection
def get_stations(name=None, city=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


# @handle_connection
def get_updates(city=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


# @handle_connection
def get_forecast(city, station, kind, timestamp):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={
                       'city': city,
                       'station': station,
                       'kind': kind,
                       'timestamp': timestamp})
    pass


# @handle_connection
def get_filtered_stations(city=None, latitude=None, longitude=None, limit=None, kind=None, mode=None, timestamp=None, quantity=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


# @handle_connection
def get_closest_city(latitude, longitude):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={
        'latitude': latitude,
        'longitude': longitude})
    pass
