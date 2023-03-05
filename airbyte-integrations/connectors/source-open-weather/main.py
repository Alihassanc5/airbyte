import sys

from airbyte_cdk.entrypoint import launch
from source_open_weather import SourceOpenWeather

if __name__ == "__main__":
    source = SourceOpenWeather()
    launch(source, sys.argv[1:])
