"""
Test runner for github tests
"""
import sys

import psycopg2
from loguru import logger

from backends.redoubt.apps import RedoubtAppBackend
from backends.redoubt.tokens import RedoubtTokensBackend
from models.render_method import JsonRenderMethod, HTMLRenderMethod
from seasons.s3_5 import S3_5_apps, S3_5_tokens

if __name__ == "__main__":
    with psycopg2.connect() as conn:
        backend = RedoubtTokensBackend(conn)
        season = S3_5_tokens
        res = backend.calculate(season, dry_run=False)
        logger.info(res)
        render = JsonRenderMethod("output_s3_5.json")
        render.render(res, season)
        render = HTMLRenderMethod("output_s3_5.html")
        render.render(res, season)
