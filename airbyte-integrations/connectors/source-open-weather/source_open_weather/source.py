from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from http import HTTPStatus
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream

from .streams import OpenWeatherStream, CurrentWeather
from.utils import get_geographical_coordinates


class SourceOpenWeather(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        params = {
            "appid": config["appid"],
            "q": config["city"],
            "units": config.get("units"),
            "lang": config.get("lang")
        }

        response = requests.get(f'{OpenWeatherStream.url_base}data/2.5/weather', params=params)

        if response.status_code == HTTPStatus.OK:
            return True, None
        else:
            message = response.json().get("message")
            return False, message

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        lat, lon = get_geographical_coordinates({'appid': config['appid'], 'q': config['city']})

        return [
            CurrentWeather(
                appid=config["appid"],
                lat=lat,
                lon=lon,
                lang=config.get("lang"),
                units=config.get("units"),
            )
        ]
