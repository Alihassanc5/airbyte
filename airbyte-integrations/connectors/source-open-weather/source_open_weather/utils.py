from typing import Tuple

import requests
from http import HTTPStatus

from .streams import OpenWeatherStream


def get_geographical_coordinates(params) -> Tuple[float, float]:
    response = requests.get(f"{OpenWeatherStream.url_base}geo/1.0/direct", params=params)
    if response.status_code == HTTPStatus.OK:
        return response.json()[0].get('lat'), response.json()[0].get('lon')
    else:
        raise Exception(response.json().get("message"))
