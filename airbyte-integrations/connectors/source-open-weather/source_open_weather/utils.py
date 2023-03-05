from typing import Tuple
from http import HTTPStatus
import requests

from .streams import OpenWeatherStream


def get_geographical_coordinates(params) -> Tuple[float, float]:
    response = requests.get(f"{OpenWeatherStream.url_base}geo/1.0/direct", params=params)

    if response.status_code == HTTPStatus.OK:
        return tuple(map(response.json()[0].get, ['lat', 'lon']))
    else:
        raise Exception(response.json().get("message"))
