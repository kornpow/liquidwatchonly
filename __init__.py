from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_liquidwatchonly")

liquidwatchonly_static_files = [
    {
        "path": "/liquidwatchonly/static",
        "name": "liquidwatchonly_static",
    }
]

liquidwatchonly_ext: APIRouter = APIRouter(prefix="/liquidwatchonly", tags=["liquidwatchonly"])


def liquidwatchonly_renderer():
    return template_renderer(["liquidwatchonly/templates"])


from .views import *  # noqa: F401,F403
from .views_api import *  # noqa: F401,F403
