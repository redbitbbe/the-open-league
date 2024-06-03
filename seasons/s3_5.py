"""
S3.5 - test season between S3 and S4
"""
from models.season_config import SeasonConfig
from projects.apps.QuackQuack import QuackQuack

S3_5_apps = SeasonConfig(
    leaderboard=SeasonConfig.APPS,
    name="S3_5",
    start_time=1716980400, # 2024-05-29 11:00:00 +0000
    end_time=1718190000, # Wed Jun 12 2024 11:00:00 GMT+0000
    projects=[
        QuackQuack
    ]
)