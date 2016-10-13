import requests
from obpy import config

from obpy.util import handle_connection


class OBPY():

    def __init__(self):
        self.OB_URL = config.BASE_URL

    def get_latest_geojson(self, city):
        url = '{BASE_URL}/geojson/{city}'.format(BASE_URL=self.OB_URL, city=city)
        return requests.get(url)

    def get_countries(self, provider=None):
        url = '{BASE_URL}/countries'.format(BASE_URL=self.OB_URL)
        request_params = {'provider': provider} if provider else {}
        return requests.get(url, params=request_params)

    def get_providers(self, country=None):
        url = '{BASE_URL}/providers'.format(BASE_URL=self.OB_URL)
        request_params = {'country': country} if country else {}
        return requests.get(url, params=request_params)

    def get_metrics(self):
        url = '{BASE_URL}/metrics'.format(BASE_URL=self.OB_URL)
        return requests.get(url)

    def get_cities(self, slug=None, country=None, provider=None, predictable=None, active=None):
        url = '{BASE_URL}/cities'.format(BASE_URL=self.OB_URL)
        request_params = {
            'slug': slug,
            'country': country,
            'provider': provider,
            'predictable': predictable,
            'active': active,
        }
        return requests.get(url, params=request_params)

    def get_stations(self, slug=None, city_slug=None):
        url = '{BASE_URL}/stations'.format(BASE_URL=self.OB_URL)
        request_params = {
            'slug': slug,
            'city_slug': city_slug,
        }
        return requests.get(url, params=request_params)

    def get_updates(self, city_slug=None):
        url = '{BASE_URL}/updates'.format(BASE_URL=self.OB_URL)
        return requests.get(url, params={'city_slug': city_slug})

    def get_forecast(self, city_slug, station_slug, kind, moment):
        url = '{BASE_URL}/forecast'.format(BASE_URL=self.OB_URL)
        payload = {
            'city_slug': city_slug,
            'station_slug': station_slug,
            'kind': kind,
            'moment': moment
        }
        return requests.post(url, json=payload)

    def get_filtered_stations(self, city_slug=None, latitude=None, longitude=None, limit=None, kind=None, mode=None, moment=None, desired_quantity=None, confidence=None):
        url = '{BASE_URL}/filtered_stations'.format(BASE_URL=self.OB_URL)
        payload = {
            'city_slug': city_slug,
            'latitude': latitude,
            'longitude': longitude,
            'limit': limit,
            'kind': kind,
            'mode': mode,
            'desired_quantity': desired_quantity,
            'confidence': confidence,
        }
        print(payload)
        return requests.post(url, json=payload)

    # def get_closest_city(self, latitude, longitude):
    #     url = '{BASE_URL}'.format(BASE_URL=self.OB_URL)
    #     res = requests.get(url, params={
    #         'latitude': latitude,
    #         'longitude': longitude})
    #     pass
