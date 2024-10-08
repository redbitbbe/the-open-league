from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
CatGoldMiner app
"""

CatGoldMiner = App(
    name="CAT GOLD MINER",
    analytics_key="cat-gold-miner",
    url="https://t.me/catgoldminerbot",
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQBg_0I3h4L7f1ca_tY30VUTEilVS0d6QAx8IcwGjIjLZTLr",
        ),
        SmartContractInteraction(
            "In-app purchasing", 
            address="EQCHoSb0kxasrZ-XhGdQ4vQz-ZEGQuX1Pzq-HYiWQi8-FMpy",
        )
    ]
)
