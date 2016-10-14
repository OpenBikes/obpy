import requests


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


def remove_none_values_from_dict(dict_obj):
    return dict((k, v) for k, v in dict_obj.items() if v)
