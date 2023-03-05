from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple
import requests

from airbyte_cdk.sources.streams.http import HttpStream


class OpenWeatherStream(HttpStream, ABC):
    url_base = "https://api.openweathermap.org/"

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        return None

    def request_params(
            self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, any] = None, next_page_token: Mapping[str, Any] = None
    ) -> MutableMapping[str, Any]:
        return {}

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        yield {}


class CurrentWeather(OpenWeatherStream):
    primary_key = None

    def __init__(self, appid: str, lat: float, lon: float, units: str = None, lang: str = None):
        super().__init__()
        self.appid = appid
        self.lat = lat
        self.lon = lon
        self.units = units
        self.lang = lang

    def path(
        self,
        *,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None,
    ) -> str:
        return 'data/2.5/weather'

    def request_params(
        self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, any] = None, next_page_token: Mapping[str, Any] = None
    ) -> MutableMapping[str, Any]:
        return {
            "appid": self.appid,
            "lat": self.lat,
            "lon": self.lon,
            "units": self.units,
            "lang": self.lang,
        }

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        return [response.json()]
