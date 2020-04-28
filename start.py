'''
source env/bin/activate
export PATH=$PATH:/Users/rijumone/Kitchen/Farming/dependencies
python start.py
'''

from config import Config
from instapy import InstaPy

def main():
    session = InstaPy(
        username=Config.CREDENTIALS['INSTAGRAM']['USERNAME'], 
        password=Config.CREDENTIALS['INSTAGRAM']['PASSWORD'],
        headless_browser=True,
        )
    session.login()
    session.like_by_tags([
        "cars",
        "car",
        "carsofinstagram",
        "bmw",
        "carporn",
        "auto",
        "carlifestyle",
        "s",
        "supercars",
        "photography",
        "ford",
        "instacar",
        "mercedes",
        "carswithoutlimits",
        "automotive",
        "racing",
        "porsche",
        "audi",
        "jdm",
        "turbo",
        "instacars",
        "luxury",
        "supercar",
        "ferrari",
    ], amount=2)
    session.set_dont_like([
        "naked", 
        "nsfw",
        "nude",
        ])
    session.set_do_follow(True, percentage=50)
    session.set_do_comment(True, percentage=50)
    session.set_comments([
        "Want!", 
        "Fast!", 
        "Race?", 
        "Speed", 
        ":heart: from India!",
        "Veloster",
        ":heart_eyes:",
        ])
    session.set_quota_supervisor(enabled=True, peak_comments_daily=100, peak_comments_hourly=4)
    session.end()

if __name__ == '__main__':
    main()