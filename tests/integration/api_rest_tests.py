import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

#Load enviroment variable defined in /home/username/.bashrc
BASE_URL = os.environ.get("BASE_URL_PROD")
DEFAULT_TIMEOUT = 2  # in secs