import requests
import config

OB_URL = config.BASE_URL


def handle_connection(func):
    def _wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            assert result.status_code == requests.codes.ok
        except requests.exceptions.Timeout:
            print("The server has not issued a response for 'timeout' seconds")
        except requests.exceptions.ConnectionError:
            print("Refused connection or DNS failure")
        except requests.exceptions.HTTPError:
            print("Invalid HTTP response")
        except requests.exceptions.TooManyRedirects:
            print("The request exceeds the configured number of maximum redirections")
        else:
            return result.json()
    return _wrapper


@handle_connection
def get_latest_geojson(city):
    url = '{BASE_URL}/geojson/'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={'city': city})
    pass


@handle_connection
def get_countries():
    url = '{BASE_URL}/countries'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    return res


@handle_connection
def get_providers(name=None, country=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


@handle_connection
def get_cities(name=None, country=None, provider=None, predictable=None, active=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


@handle_connection
def get_stations(name=None, city=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


@handle_connection
def get_updates(city=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


@handle_connection
def get_forecast(city, station, kind, timestamp):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={
                       'city': city,
                       'station': station,
                       'kind': kind,
                       'timestamp': timestamp})
    pass


@handle_connection
def get_filtered_stations(city=None, latitude=None, longitude=None, limit=None, kind=None, mode=None, timestamp=None, quantity=None):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={})
    pass


@handle_connection
def get_closest_city(latitude, longitude):
    url = '{BASE_URL}'.format(BASE_URL=OB_URL)
    res = requests.get(url, params={
        'latitude': latitude,
        'longitude': longitude})
    pass
