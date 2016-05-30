import requests


def get_latest_geojson(city):
    pass


def get_countries(name=None, provider=None):
    pass


def get_providers(name=None, country=None):
    pass


def get_cities(name=None, country=None, provider=None, predictable=None, active=None):
    pass


def get_stations(name=None, city=None):
    pass


def get_updates(city=None):
    pass


def get_forecast(city, station, kind, timestamp):
    pass


def get_filtered_stations(city=None, latitude=None, longitude=None, limit=None, kind=None, mode=None, timestamp=None, quantity=None):
    pass


def get_closed_city(latitude, longitude):
    pass
