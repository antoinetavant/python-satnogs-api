# flake8: noqa
"""
SatNOGS API client module initialization
"""
from __future__ import absolute_import

from ._version import get_versions
from .satnogs_api_client import fetch_observation_data_from_id, \
                                fetch_observation_data, \
                                fetch_ground_station_data, \
                                fetch_satellite_data, \
                                fetch_tle_of_observation, \
                                fetch_telemetry, \
                                fetch_transmitters, \
                                fetch_satellites, \
                                post_telemetry, \
                                NETWORK_DEV_BASE_URL, \
                                NETWORK_BASE_URL, \
                                DB_DEV_BASE_URL, \
                                DB_BASE_URL

__version__ = get_versions()['version']

del get_versions
