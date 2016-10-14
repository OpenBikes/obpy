import pytest
import datetime as dt
import obpy.obpy as obpy


obapi = obpy.OBPY()


def test_api_geojson_valid_city():
    ''' Check api_geojson handles a valid city. '''
    res = obapi.get_latest_geojson('toulouse')
    assert res.status_code == 200


def test_api_geojson_invalid_city():
    ''' Check api_geojson handles an invalid city. '''
    res = obapi.get_latest_geojson('gnfkdgjldjls')
    assert res.status_code == 412


def test_api_countries_valid_parameters():
    ''' Check api_countries handles all valid parameters. '''
    response = obapi.get_countries(provider='jcdecaux')
    assert response.status_code == 200


def test_api_providers_valid_parameters():
    ''' Check api_providers handles all valid parameters. '''
    response = obapi.get_providers(country='France')
    assert response.status_code == 200


def test_api_cities_valid_parameters():
    ''' Check api_cities handles all valid parameters. '''
    response = obapi.get_cities(slug='toulouse', predictable=1, active=1, country='France', provider='jcdecaux')
    assert response.status_code == 200


def test_api_stations_valid_parameters():
    ''' Check api_stations handles all valid parameters. '''
    response = obapi.get_stations(slug='00003-pomme', city_slug='toulouse')
    assert response.status_code == 200


def test_api_updates_all():
    ''' Check api_updates works with no parameters. '''
    response = obapi.get_updates()
    assert response.status_code == 200


def test_api_metrics():
    ''' Check api_metrics works. '''
    response = obapi.get_metrics()
    assert response.status_code == 200


def test_api_updates_valid_city():
    ''' Check api_updates handles valid city. '''
    response = obapi.get_updates(city_slug='toulouse')
    assert response.status_code == 200


def test_api_filtered_without_forecasts():
    ''' Check api_filtered_stations works without forecasts. '''
    response = obapi.get_filtered_stations(
        city_slug='toulouse',
        latitude=43.6,
        longitude=1.4333,
        limit=1
    )
    assert response.status_code == 200


def test_api_filtered_with_forecasts():
    ''' Check api_filtered_stations works with forecasts. '''
    response = obapi.get_filtered_stations(
        city_slug='toulouse',
        latitude=43.6,
        longitude=1.4333,
        limit=1,
        kind='bikes',
        mode='walking',
        desired_quantity=1,
        moment=(dt.datetime.now() + dt.timedelta(minutes=1)).timestamp()
    )
    assert response.status_code == 200


def test_api_filtered_invalid_city():
    ''' Check api_filtered_stations handles invalid city names. '''
    response = obapi.get_filtered_stations(
        city_slug='xyz',
        latitude=43.6,
        longitude=1.4333,
        limit=1
    )
    assert response.status_code == 412


def test_api_closest_city():
    ''' Check api_closest_city works. '''
    response = obapi.get_closest_city(
        latitude='43.6',
        longitude='1.4333'
    )
    assert response.status_code == 200


def test_api_closest_station():
    ''' Check api_closest_station works. '''
    response = obapi.get_closest_city(
        latitude='43.6',
        longitude='1.4333'
    )
    assert response.status_code == 200


def test_api_forecast_invalid_city():
    ''' Check api_forecast handles invalid city. '''
    response = obapi.get_forecast(
        city_slug='xyz',
        station_slug='00003-pomme',
        kind='bikes',
        moment=(dt.datetime.now() + dt.timedelta(minutes=1)).timestamp()
    )
    assert response.status_code == 412


def test_api_forecast_invalid_station():
    ''' Check api_forecast handles invalid station. '''
    response = obapi.get_forecast(
        city_slug='toulouse',
        station_slug='xyz',
        kind='bikes',
        moment=(dt.datetime.now() + dt.timedelta(minutes=1)).timestamp()
    )
    assert response.status_code == 412


def test_api_forecast_invalid_kind():
    ''' Check api_forecast handles invalid kind. '''
    response = obapi.get_forecast(
        city_slug='toulouse',
        station_slug='00003-pomme',
        kind='xyz',
        moment=(dt.datetime.now() + dt.timedelta(minutes=1)).timestamp()
    )
    assert response.status_code == 400


# def test_api_forecast_bikes():
#     ''' Check api_forecast can forecast bikes. '''
#     response = obapi.get_forecast(
#         city_slug='toulouse',
#         station_slug='00003-pomme',
#         kind='bikes',
#         moment=(dt.datetime.now() + dt.timedelta(minutes=1)).timestamp()
#     )
#     print(response.text)
#     assert response.status_code == 200


# def test_api_forecast_spaces():
#     ''' Check api_forecast can forecast spaces. '''
#     response = obapi.get_forecast(
#         city_slug='toulouse',
#         station_slug='00003-pomme',
#         kind='spaces',
#         moment=(dt.datetime.now() + dt.timedelta(minutes=1)).timestamp()
#     )
#     assert response.status_code == 200
