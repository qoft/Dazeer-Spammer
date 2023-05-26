# coding: utf8

from anticaptchaofficial.hcaptchaproxyless import hCaptchaProxyless as AnticaptchaTask
from capmonster_python import HCaptchaTask as CapmonsterTask
from capsolver_python import HCaptchaTask as CapsolverTask
from concurrent.futures import ThreadPoolExecutor
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
from websocket import create_connection
from datetime import datetime, timezone
from base64 import b64encode, b64decode
from colorama import Fore, Style, Back
from dataclasses import dataclass
from discord.ext import commands
from websocket import WebSocket
from datetime import datetime
from Crypto.Cipher import AES
from base64 import b64encode
from itertools import cycle
from decimal import Decimal
import json, sys, base64
from pathlib import Path
from json import dumps
import json as jsond
import subprocess
import tls_client
import webbrowser
import threading
import websocket
import pyperclip
import delorean
import binascii
import requests
import hashlib
import secrets
import pystyle
import zipfile
import discord
import asyncio
import winreg
import psutil
import string
import shutil
import random
import typing
import httpx
import types
import time
import colr
import ssl
import sys
import re
import os
os.system("cls")

# -- Define Constants
LOGGING_PATH = (
    Path.home() / "AppData/Roaming/dazeer/logs/Dazeer.log"
    # ""
)  # -- This can be any path

pystyle.Cursor.HideCursor()
global menu_str
menu_str = ""


from functools import wraps
def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)


print("Getting client information...")

class DiscordInfo:
    _req = requests.get("https://raw.githubusercontent.com/EffeDiscord/discord-api/main/fetch").json()
    build_num = int(_req['client_build_number'])
    browser_version = _req["chrome_version"].split(".")[0]
    user_agent = _req['chrome_user_agent']
    
    _get_mobile_x_super_properties = base64.b64encode((json.dumps(separators=(',', ':'), obj={
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "en-US",
            "browser_user_agent": user_agent,
            "browser_version": f"{browser_version}.0.0.0",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": build_num,
            "client_event_source": None,
            "design_id": 0
        })).encode()).decode()
        
    default_headers = None
    

__all__ = [
    'GlobalInfo',
]




class GlobalInfo:
        
    VERSION: str = "3.2.1"
    WHITELISTED_SERVER: list[str] = [
        "1044794654882791455",
        "986666459583348796",
        "1082763111431405711",
        "1096390599684395140"
    ]
    

class CaptchaType:
    capmonster = 1
    anticaptcha = 2
    capsolver = 3
    dort = 4
class BypassableBots:
    CAPTCHA_BOT = "captcha.bot"
    RESTORECORD = "restorecord.com"
    WICK = "wickbot.com"

class SpammerOptions:
    ping_amount: int = 0
    massping: bool = False
    multi_message: bool = False
    users: list[str] = []
    guild_id: int = 0
    invisible_pings: bool = False
    
    channel_ids: list[str] = []
    
    msg_amount: int = 0
    messages: list[str] = []
    crypt_message: bool = False
    emoji_message: bool = False
    
    massping_users: list[str] = []
    massping_iter: cycle = None
    delay: float = 0.0
    
class OnboardingInfo:
    guild_id: int = 0
    required_prompts: list[dict[str, typing.Union[str, list[typing.Union[str, dict, list, bool, None]]]]] = []
    onboarding_prompts_seen: dict[str, int] = {}
    onboarding_responses_seen: dict[str, int] = {}
    onboarding_responses: list[str] = [] # answers have to be in order of the prompts


__lock__ = threading.Lock()
spotify_songs = [{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/757aE44tKEUQEqRuT6GnEB"},"href":"https://api.spotify.com/v1/artists/757aE44tKEUQEqRuT6GnEB","id":"757aE44tKEUQEqRuT6GnEB","name":"Roddy Ricch","type":"artist","uri":"spotify:artist:757aE44tKEUQEqRuT6GnEB"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/1eVrpJbHRLBbioB9sb5b94"},"href":"https://api.spotify.com/v1/albums/1eVrpJbHRLBbioB9sb5b94","id":"1eVrpJbHRLBbioB9sb5b94","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2738007e1fcf108e4270b6df942","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e028007e1fcf108e4270b6df942","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048518007e1fcf108e4270b6df942","width":64}],"name":"LIVE LIFE FAST","release_date":"2021-12-17","release_date_precision":"day","total_tracks":18,"type":"album","uri":"spotify:album:1eVrpJbHRLBbioB9sb5b94"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/0urTpYCsixqZwgNTkPJOJ4"},"href":"https://api.spotify.com/v1/artists/0urTpYCsixqZwgNTkPJOJ4","id":"0urTpYCsixqZwgNTkPJOJ4","name":"Aaliyah","type":"artist","uri":"spotify:artist:0urTpYCsixqZwgNTkPJOJ4"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/2t0AfNqhtlMnjFxbTzmPqO"},"href":"https://api.spotify.com/v1/albums/2t0AfNqhtlMnjFxbTzmPqO","id":"2t0AfNqhtlMnjFxbTzmPqO","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273bfa88fd0ac35dca91e77598a","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02bfa88fd0ac35dca91e77598a","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851bfa88fd0ac35dca91e77598a","width":64}],"name":"Poison (feat. The Weeknd)","release_date":"2021-12-17","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:2t0AfNqhtlMnjFxbTzmPqO"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/5YkBrE0wF8cAlq3GCOw5Eu"},"href":"https://api.spotify.com/v1/artists/5YkBrE0wF8cAlq3GCOw5Eu","id":"5YkBrE0wF8cAlq3GCOw5Eu","name":"Best Coast","type":"artist","uri":"spotify:artist:5YkBrE0wF8cAlq3GCOw5Eu"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/1vLgVmLSQgEEM8SBZ4QQQd"},"href":"https://api.spotify.com/v1/albums/1vLgVmLSQgEEM8SBZ4QQQd","id":"1vLgVmLSQgEEM8SBZ4QQQd","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273262af6f60ed3a93688dce24d","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02262af6f60ed3a93688dce24d","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851262af6f60ed3a93688dce24d","width":64}],"name":"Leading","release_date":"2021-12-14","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:1vLgVmLSQgEEM8SBZ4QQQd"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/28gNT5KBp7IjEOQoevXf9N"},"href":"https://api.spotify.com/v1/artists/28gNT5KBp7IjEOQoevXf9N","id":"28gNT5KBp7IjEOQoevXf9N","name":"Camilo","type":"artist","uri":"spotify:artist:28gNT5KBp7IjEOQoevXf9N"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/3b2z5O7s1vxHaaTsn1J1Cz"},"href":"https://api.spotify.com/v1/albums/3b2z5O7s1vxHaaTsn1J1Cz","id":"3b2z5O7s1vxHaaTsn1J1Cz","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2737f067a921cc40f4111475a09","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e027f067a921cc40f4111475a09","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048517f067a921cc40f4111475a09","width":64}],"name":"Pesadilla","release_date":"2021-12-14","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:3b2z5O7s1vxHaaTsn1J1Cz"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/6nB0iY1cjSY1KyhYyuIIKH"},"href":"https://api.spotify.com/v1/artists/6nB0iY1cjSY1KyhYyuIIKH","id":"6nB0iY1cjSY1KyhYyuIIKH","name":"FKA twigs","type":"artist","uri":"spotify:artist:6nB0iY1cjSY1KyhYyuIIKH"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/633MrZ9lAeFFydmcMENiuA"},"href":"https://api.spotify.com/v1/albums/633MrZ9lAeFFydmcMENiuA","id":"633MrZ9lAeFFydmcMENiuA","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273c813333a4bf7b81e7a251566","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02c813333a4bf7b81e7a251566","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851c813333a4bf7b81e7a251566","width":64}],"name":"Tears In The Club (feat. The Weeknd)","release_date":"2021-12-16","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:633MrZ9lAeFFydmcMENiuA"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/1fctva4kpRbg2k3v7kwRuS"},"href":"https://api.spotify.com/v1/artists/1fctva4kpRbg2k3v7kwRuS","id":"1fctva4kpRbg2k3v7kwRuS","name":"Rvssian","type":"artist","uri":"spotify:artist:1fctva4kpRbg2k3v7kwRuS"},{"external_urls":{"spotify":"https://open.spotify.com/artist/1RyvyyTE3xzB2ZywiAwp0i"},"href":"https://api.spotify.com/v1/artists/1RyvyyTE3xzB2ZywiAwp0i","id":"1RyvyyTE3xzB2ZywiAwp0i","name":"Future","type":"artist","uri":"spotify:artist:1RyvyyTE3xzB2ZywiAwp0i"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/1qY5LCrtZDIsh6A86N2Yo2"},"href":"https://api.spotify.com/v1/albums/1qY5LCrtZDIsh6A86N2Yo2","id":"1qY5LCrtZDIsh6A86N2Yo2","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b27380a85658a64eb32504ce426d","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e0280a85658a64eb32504ce426d","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d0000485180a85658a64eb32504ce426d","width":64}],"name":"M&M (with Future feat. Lil Baby)","release_date":"2021-12-15","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:1qY5LCrtZDIsh6A86N2Yo2"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3wcj11K77LjEY1PkEazffa"},"href":"https://api.spotify.com/v1/artists/3wcj11K77LjEY1PkEazffa","id":"3wcj11K77LjEY1PkEazffa","name":"Burna Boy","type":"artist","uri":"spotify:artist:3wcj11K77LjEY1PkEazffa"}],"available_markets":["AD","AE","AG","AL","AM","AR","AT","AU","AZ","BA","BB","BD","BE","BG","BH","BN","BO","BR","BS","BT","BY","BZ","CA","CH","CL","CO","CR","CW","CY","CZ","DE","DK","DM","DO","EC","EE","ES","FI","FJ","FM","FR","GB","GD","GE","GR","GT","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KG","KH","KI","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LT","LU","LV","MC","MD","ME","MH","MK","MN","MO","MT","MV","MX","MY","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","SA","SB","SE","SG","SI","SK","SM","SR","SV","TH","TJ","TL","TO","TR","TT","TV","TW","UA","US","UY","UZ","VC","VE","VN","VU","WS","XK"],"external_urls":{"spotify":"https://open.spotify.com/album/2Nwv16YY4xo8Jm4TVm54i9"},"href":"https://api.spotify.com/v1/albums/2Nwv16YY4xo8Jm4TVm54i9","id":"2Nwv16YY4xo8Jm4TVm54i9","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273ed808ecd866a67c6e47e33f9","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02ed808ecd866a67c6e47e33f9","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851ed808ecd866a67c6e47e33f9","width":64}],"name":"B. D’OR (feat. Wizkid)","release_date":"2021-12-14","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:2Nwv16YY4xo8Jm4TVm54i9"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/6fWVd57NKTalqvmjRd2t8Z"},"href":"https://api.spotify.com/v1/artists/6fWVd57NKTalqvmjRd2t8Z","id":"6fWVd57NKTalqvmjRd2t8Z","name":"24kGoldn","type":"artist","uri":"spotify:artist:6fWVd57NKTalqvmjRd2t8Z"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/0r9uTlzVUjnRvBTGjTLC54"},"href":"https://api.spotify.com/v1/albums/0r9uTlzVUjnRvBTGjTLC54","id":"0r9uTlzVUjnRvBTGjTLC54","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273afae5ae58eb98ab9eb032c47","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02afae5ae58eb98ab9eb032c47","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851afae5ae58eb98ab9eb032c47","width":64}],"name":"More Than Friends","release_date":"2021-12-17","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:0r9uTlzVUjnRvBTGjTLC54"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/6TLwD7HPWuiOzvXEa3oCNe"},"href":"https://api.spotify.com/v1/artists/6TLwD7HPWuiOzvXEa3oCNe","id":"6TLwD7HPWuiOzvXEa3oCNe","name":"Oliver Tree","type":"artist","uri":"spotify:artist:6TLwD7HPWuiOzvXEa3oCNe"},{"external_urls":{"spotify":"https://open.spotify.com/artist/6Xgp2XMz1fhVYe7i6yNAax"},"href":"https://api.spotify.com/v1/artists/6Xgp2XMz1fhVYe7i6yNAax","id":"6Xgp2XMz1fhVYe7i6yNAax","name":"Trippie Redd","type":"artist","uri":"spotify:artist:6Xgp2XMz1fhVYe7i6yNAax"},{"external_urls":{"spotify":"https://open.spotify.com/artist/2rhFzFmezpnW82MNqEKVry"},"href":"https://api.spotify.com/v1/artists/2rhFzFmezpnW82MNqEKVry","id":"2rhFzFmezpnW82MNqEKVry","name":"Ski Mask The Slump God","type":"artist","uri":"spotify:artist:2rhFzFmezpnW82MNqEKVry"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/1ucf98ip08W4dY41QZrXeq"},"href":"https://api.spotify.com/v1/albums/1ucf98ip08W4dY41QZrXeq","id":"1ucf98ip08W4dY41QZrXeq","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273925275230e6804c9a6585269","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02925275230e6804c9a6585269","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851925275230e6804c9a6585269","width":64}],"name":"Life Goes On (feat. Trippie Redd & Ski Mask The Slump God)","release_date":"2021-12-17","release_date_precision":"day","total_tracks":2,"type":"album","uri":"spotify:album:1ucf98ip08W4dY41QZrXeq"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/4IVAbR2w4JJNJDDRFP3E83"},"href":"https://api.spotify.com/v1/artists/4IVAbR2w4JJNJDDRFP3E83","id":"4IVAbR2w4JJNJDDRFP3E83","name":"6LACK","type":"artist","uri":"spotify:artist:4IVAbR2w4JJNJDDRFP3E83"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/06nzu940k6jhkJ5TacM6y5"},"href":"https://api.spotify.com/v1/albums/06nzu940k6jhkJ5TacM6y5","id":"06nzu940k6jhkJ5TacM6y5","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2738b6812afed07f32cbeeb6d6b","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e028b6812afed07f32cbeeb6d6b","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048518b6812afed07f32cbeeb6d6b","width":64}],"name":"Rent Free / By Any Means","release_date":"2021-12-17","release_date_precision":"day","total_tracks":2,"type":"album","uri":"spotify:album:06nzu940k6jhkJ5TacM6y5"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/4lPl9gqgox3JDiaJ1yklKh"},"href":"https://api.spotify.com/v1/artists/4lPl9gqgox3JDiaJ1yklKh","id":"4lPl9gqgox3JDiaJ1yklKh","name":"Tierra Whack","type":"artist","uri":"spotify:artist:4lPl9gqgox3JDiaJ1yklKh"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/1OTZupPjEaLRA8mbO4qvKz"},"href":"https://api.spotify.com/v1/albums/1OTZupPjEaLRA8mbO4qvKz","id":"1OTZupPjEaLRA8mbO4qvKz","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273cd6660cb55c09a195ed326ac","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02cd6660cb55c09a195ed326ac","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851cd6660cb55c09a195ed326ac","width":64}],"name":"R&B?","release_date":"2021-12-16","release_date_precision":"day","total_tracks":3,"type":"album","uri":"spotify:album:1OTZupPjEaLRA8mbO4qvKz"},{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/35CsFzAi3BR19Ar1wRlPb6"},"href":"https://api.spotify.com/v1/artists/35CsFzAi3BR19Ar1wRlPb6","id":"35CsFzAi3BR19Ar1wRlPb6","name":"Johnny Klimek","type":"artist","uri":"spotify:artist:35CsFzAi3BR19Ar1wRlPb6"},{"external_urls":{"spotify":"https://open.spotify.com/artist/1YtTF1pj1ZFufjkP0BEfWE"},"href":"https://api.spotify.com/v1/artists/1YtTF1pj1ZFufjkP0BEfWE","id":"1YtTF1pj1ZFufjkP0BEfWE","name":"Tom Tykwer","type":"artist","uri":"spotify:artist:1YtTF1pj1ZFufjkP0BEfWE"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/6RjA1eIgIas30qqvsu0X9W"},"href":"https://api.spotify.com/v1/albums/6RjA1eIgIas30qqvsu0X9W","id":"6RjA1eIgIas30qqvsu0X9W","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2739c3c13a0643e08a6ccd53b59","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e029c3c13a0643e08a6ccd53b59","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048519c3c13a0643e08a6ccd53b59","width":64}],"name":"The Matrix Resurrections (Original Motion Picture Soundtrack)","release_date":"2021-12-17","release_date_precision":"day","total_tracks":35,"type":"album","uri":"spotify:album:6RjA1eIgIas30qqvsu0X9W"},{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/15iVAtD3s3FsQR4w1v6M0P"},"href":"https://api.spotify.com/v1/artists/15iVAtD3s3FsQR4w1v6M0P","id":"15iVAtD3s3FsQR4w1v6M0P","name":"Chief Keef","type":"artist","uri":"spotify:artist:15iVAtD3s3FsQR4w1v6M0P"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/117i43x9P3zxUQ7UAcxrBV"},"href":"https://api.spotify.com/v1/albums/117i43x9P3zxUQ7UAcxrBV","id":"117i43x9P3zxUQ7UAcxrBV","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2730f30c5c8809fa6e6776dceaa","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e020f30c5c8809fa6e6776dceaa","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048510f30c5c8809fa6e6776dceaa","width":64}],"name":"4NEM","release_date":"2021-12-17","release_date_precision":"day","total_tracks":15,"type":"album","uri":"spotify:album:117i43x9P3zxUQ7UAcxrBV"},{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/13y7CgLHjMVRMDqxdx0Xdo"},"href":"https://api.spotify.com/v1/artists/13y7CgLHjMVRMDqxdx0Xdo","id":"13y7CgLHjMVRMDqxdx0Xdo","name":"Gucci Mane","type":"artist","uri":"spotify:artist:13y7CgLHjMVRMDqxdx0Xdo"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/2akb547l1kwTss6MNU3JyG"},"href":"https://api.spotify.com/v1/albums/2akb547l1kwTss6MNU3JyG","id":"2akb547l1kwTss6MNU3JyG","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273b6792af95651e0c486a2ee62","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02b6792af95651e0c486a2ee62","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851b6792af95651e0c486a2ee62","width":64}],"name":"So Icy Christmas","release_date":"2021-12-17","release_date_precision":"day","total_tracks":17,"type":"album","uri":"spotify:album:2akb547l1kwTss6MNU3JyG"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/5QdyldG4Fl4TPiOIeMNpBZ"},"href":"https://api.spotify.com/v1/artists/5QdyldG4Fl4TPiOIeMNpBZ","id":"5QdyldG4Fl4TPiOIeMNpBZ","name":"Big Thief","type":"artist","uri":"spotify:artist:5QdyldG4Fl4TPiOIeMNpBZ"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/13lNwYutq39VEtYK5nJ617"},"href":"https://api.spotify.com/v1/albums/13lNwYutq39VEtYK5nJ617","id":"13lNwYutq39VEtYK5nJ617","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b27355bc98763f20825e58285a30","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e0255bc98763f20825e58285a30","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d0000485155bc98763f20825e58285a30","width":64}],"name":"No Reason / Spud Infinity","release_date":"2021-12-14","release_date_precision":"day","total_tracks":7,"type":"album","uri":"spotify:album:13lNwYutq39VEtYK5nJ617"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3IhWQSrLj8EJjdvjFTpCyo"},"href":"https://api.spotify.com/v1/artists/3IhWQSrLj8EJjdvjFTpCyo","id":"3IhWQSrLj8EJjdvjFTpCyo","name":"Vince Gill","type":"artist","uri":"spotify:artist:3IhWQSrLj8EJjdvjFTpCyo"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/15t2WXfpVffaNOo92Z3mr0"},"href":"https://api.spotify.com/v1/albums/15t2WXfpVffaNOo92Z3mr0","id":"15t2WXfpVffaNOo92Z3mr0","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2732b0bdfbac00a11bf1260d5c5","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e022b0bdfbac00a11bf1260d5c5","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048512b0bdfbac00a11bf1260d5c5","width":64}],"name":"Love Changes Everything (From The Motion Picture American Underdog)","release_date":"2021-12-17","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:15t2WXfpVffaNOo92Z3mr0"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/77AiFEVeAVj2ORpC85QVJs"},"href":"https://api.spotify.com/v1/artists/77AiFEVeAVj2ORpC85QVJs","id":"77AiFEVeAVj2ORpC85QVJs","name":"Steve Aoki","type":"artist","uri":"spotify:artist:77AiFEVeAVj2ORpC85QVJs"},{"external_urls":{"spotify":"https://open.spotify.com/artist/1lzugG0lqNh9nP6Fp2zG3c"},"href":"https://api.spotify.com/v1/artists/1lzugG0lqNh9nP6Fp2zG3c","id":"1lzugG0lqNh9nP6Fp2zG3c","name":"Global Dan","type":"artist","uri":"spotify:artist:1lzugG0lqNh9nP6Fp2zG3c"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/4su0t3XDFmCCdQaQXd51no"},"href":"https://api.spotify.com/v1/albums/4su0t3XDFmCCdQaQXd51no","id":"4su0t3XDFmCCdQaQXd51no","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2735cfd6668f148e3669a0a31f1","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e025cfd6668f148e3669a0a31f1","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048515cfd6668f148e3669a0a31f1","width":64}],"name":"Stars Don't Shine (feat. Global Dan)","release_date":"2021-12-17","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:4su0t3XDFmCCdQaQXd51no"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/41X1TR6hrK8Q2ZCpp2EqCz"},"href":"https://api.spotify.com/v1/artists/41X1TR6hrK8Q2ZCpp2EqCz","id":"41X1TR6hrK8Q2ZCpp2EqCz","name":"bbno$","type":"artist","uri":"spotify:artist:41X1TR6hrK8Q2ZCpp2EqCz"},{"external_urls":{"spotify":"https://open.spotify.com/artist/2IDLDx25HU1nQMKde4n61a"},"href":"https://api.spotify.com/v1/artists/2IDLDx25HU1nQMKde4n61a","id":"2IDLDx25HU1nQMKde4n61a","name":"Rich Brian","type":"artist","uri":"spotify:artist:2IDLDx25HU1nQMKde4n61a"},{"external_urls":{"spotify":"https://open.spotify.com/artist/5fMUXHkw8R8eOP2RNVYEZX"},"href":"https://api.spotify.com/v1/artists/5fMUXHkw8R8eOP2RNVYEZX","id":"5fMUXHkw8R8eOP2RNVYEZX","name":"Diplo","type":"artist","uri":"spotify:artist:5fMUXHkw8R8eOP2RNVYEZX"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/2pcFjaO7Eouy8DiDV9mmjW"},"href":"https://api.spotify.com/v1/albums/2pcFjaO7Eouy8DiDV9mmjW","id":"2pcFjaO7Eouy8DiDV9mmjW","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273a11f2b07232754bfdc58c29c","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02a11f2b07232754bfdc58c29c","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851a11f2b07232754bfdc58c29c","width":64}],"name":"edamame (feat. Rich Brian) [Diplo Remix]","release_date":"2021-12-15","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:2pcFjaO7Eouy8DiDV9mmjW"},{"album_type":"album","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/4FlG0V0jhLO4qGpayFOphj"},"href":"https://api.spotify.com/v1/artists/4FlG0V0jhLO4qGpayFOphj","id":"4FlG0V0jhLO4qGpayFOphj","name":"EST Gee","type":"artist","uri":"spotify:artist:4FlG0V0jhLO4qGpayFOphj"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/5TJ8D5dMvMYla06T6hTAvA"},"href":"https://api.spotify.com/v1/albums/5TJ8D5dMvMYla06T6hTAvA","id":"5TJ8D5dMvMYla06T6hTAvA","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2739db5054a75dd748d65dbab9a","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e029db5054a75dd748d65dbab9a","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048519db5054a75dd748d65dbab9a","width":64}],"name":"Bigger Than Life Or Death (Deluxe)","release_date":"2021-12-17","release_date_precision":"day","total_tracks":26,"type":"album","uri":"spotify:album:5TJ8D5dMvMYla06T6hTAvA"},{"album_type":"single","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/34Y0ldeyUv7jBvukWOGASO"},"href":"https://api.spotify.com/v1/artists/34Y0ldeyUv7jBvukWOGASO","id":"34Y0ldeyUv7jBvukWOGASO","name":"Bobby Shmurda","type":"artist","uri":"spotify:artist:34Y0ldeyUv7jBvukWOGASO"},{"external_urls":{"spotify":"https://open.spotify.com/artist/0VRj0yCOv2FXJNP47XQnx5"},"href":"https://api.spotify.com/v1/artists/0VRj0yCOv2FXJNP47XQnx5","id":"0VRj0yCOv2FXJNP47XQnx5","name":"Quavo","type":"artist","uri":"spotify:artist:0VRj0yCOv2FXJNP47XQnx5"},{"external_urls":{"spotify":"https://open.spotify.com/artist/6LXRvV2OAtXF7685fzh3mj"},"href":"https://api.spotify.com/v1/artists/6LXRvV2OAtXF7685fzh3mj","id":"6LXRvV2OAtXF7685fzh3mj","name":"Rowdy Rebel","type":"artist","uri":"spotify:artist:6LXRvV2OAtXF7685fzh3mj"}],"available_markets":["AD","AE","AG","AL","AM","AO","AR","AT","AU","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CG","CH","CI","CL","CM","CO","CR","CV","CW","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","FI","FJ","FM","FR","GA","GB","GD","GE","GH","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KI","KM","KN","KR","KW","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MH","MK","ML","MN","MO","MR","MT","MU","MV","MW","MX","MY","MZ","NA","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PG","PH","PK","PL","PS","PT","PW","PY","QA","RO","RS","RU","RW","SA","SB","SC","SE","SG","SI","SK","SL","SM","SN","SR","ST","SV","SZ","TD","TG","TH","TJ","TL","TN","TO","TR","TT","TV","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VN","VU","WS","XK","ZA","ZM","ZW"],"external_urls":{"spotify":"https://open.spotify.com/album/5npQCHNuLe3ydFr1bx4sib"},"href":"https://api.spotify.com/v1/albums/5npQCHNuLe3ydFr1bx4sib","id":"5npQCHNuLe3ydFr1bx4sib","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2730b560238ed2f7c82b4e12ce4","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e020b560238ed2f7c82b4e12ce4","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048510b560238ed2f7c82b4e12ce4","width":64}],"name":"Shmoney (feat. Quavo & Rowdy Rebel)","release_date":"2021-12-17","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:5npQCHNuLe3ydFr1bx4sib"}]




class DiscordSocket(websocket.WebSocketApp):
    
    def __init__(self, token, guild_id, channel_id):
        self.MAX_ITER = 10
        self.token = token
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.blacklisted_roles, self.blacklisted_users = [], []
        self.socket_headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
            "User-Agent": DiscordInfo.user_agent,
        }
        super().__init__(
            "wss://gateway.discord.gg/?encoding=json&v=9",
            header=self.socket_headers,
            on_open=lambda ws: self.sock_open(ws),
            on_message=lambda ws, msg: self.sock_message(ws, msg),
            on_close=lambda ws, close_code, close_msg: self.sock_close(
                ws, close_code, close_msg
            ),
        )
        self.endScraping = False
        self.guilds = {}
        self.members: list[str] = []
        self.ranges = [[0]]
        self.lastRange = 0
        self.packets_recv = 0
        self.msgs = []
        self.d = 1
        self.iter = 0
        self.big_iter = 0
        self.finished = False
        
        

    def getRanges(self, index, multiplier, memberCount):
        initialNum = int(index * multiplier)
        rangesList = [[initialNum, initialNum + 99]]
        if memberCount > initialNum + 99:
            rangesList.append([initialNum + 100, initialNum + 199])
        if [0, 99] not in rangesList:
            rangesList.insert(0, [0, 99])
        return rangesList

    def parseGuildMemberListUpdate(self, response):
        memberdata = {
            "online_count": response["d"]["online_count"],
            "member_count": response["d"]["member_count"],
            "id": response["d"]["id"],
            "guild_id": response["d"]["guild_id"],
            "hoisted_roles": response["d"]["groups"],
            "types": [],
            "locations": [],
            "updates": [],
        }
        for chunk in response["d"]["ops"]:
            memberdata["types"].append(chunk["op"])
            if chunk["op"] in ("SYNC", "INVALIDATE"):
                memberdata["locations"].append(chunk["range"])
                if chunk["op"] == "SYNC":
                    memberdata["updates"].append(chunk["items"])
                else:
                    memberdata["updates"].append([])
            elif chunk["op"] in ("INSERT", "UPDATE", "DELETE"):
                memberdata["locations"].append(chunk["index"])
                if chunk["op"] == "DELETE":
                    memberdata["updates"].append([])
                else:
                    memberdata["updates"].append(chunk["item"])
        return memberdata

    def find_most_reoccuring(self, list):
        return max(set(list), key=list.count)

    def run(self) -> list[str]:
        try:
            self.run_forever()
            self.finished = True
            return self.members
        except Exception as e:
            print(e)
            pass

    def scrapeUsers(self):
        if self.endScraping == False:
            self.send(
                '{"op":14,"d":{"guild_id":"'
                + self.guild_id
                + '","typing":true,"activities":true,"threads":true,"channels":{"'
                + self.channel_id
                + '":'
                + json.dumps(self.ranges)
                + "}}}"
            )

    def sock_open(self, ws):
        self.send(
            '{"op":2,"d":{"token":"'
            + self.token
            + '","capabilities":125,"properties":{"os":"Windows","browser":"Firefox","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0","browser_version":"94.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}'
        )

    def heartbeatThread(self, interval):
        try:
            while True:
                self.send('{"op":1,"d":' + str(self.packets_recv) + "}")
                time.sleep(interval)
        except Exception as e:
            return

    def sock_message(self, ws, message):
        try:
            decoded = json.loads(message)
            if decoded is None:
                return
            if decoded["op"] != 11:
                self.packets_recv += 1
            if decoded["op"] == 10:
                threading.Thread(
                    target=self.heartbeatThread,
                    args=(decoded["d"]["heartbeat_interval"] / 1000,),
                    daemon=True,
                ).start()
            if decoded["t"] == "READY":
                for guild in decoded["d"]["guilds"]:
                    self.guilds[guild["id"]] = {"member_count": guild["member_count"]}
            if decoded["t"] == "READY_SUPPLEMENTAL":
                self.ranges = self.getRanges(
                    0, 100, self.guilds[self.guild_id]["member_count"]
                )
                self.scrapeUsers()
            elif decoded["t"] == "GUILD_MEMBER_LIST_UPDATE":
                parsed = self.parseGuildMemberListUpdate(decoded)
                self.msgs.append(len(self.members))
                print(f"Scraped {len(self.members)} members", end="\r")
                if self.d == len(self.members):
                    self.iter += 1
                    if self.iter == self.MAX_ITER:
                        print(f"Scraped {len(self.members)} members")
                        self.endScraping = True
                        self.close()
                        return
                self.d = self.find_most_reoccuring(self.msgs)
                if parsed["guild_id"] == self.guild_id and (
                    "SYNC" in parsed["types"] or "UPDATE" in parsed["types"]
                ):
                    for (elem, index) in enumerate(parsed["types"]):
                        if index == "SYNC":
                            for item in parsed["updates"]:
                                if len(item) > 0:
                                    for member in item:
                                        if "member" in member:
                                            mem = member["member"]
                                            obj = {
                                                "tag": mem["user"]["username"]
                                                + "#"
                                                + mem["user"]["discriminator"],
                                                "id": mem["user"]["id"],
                                            }
                                            if not mem["user"].get("bot"):
                                                self.members.append(str(mem["user"]["id"]))
                        elif index == "UPDATE":
                            for item in parsed["updates"][elem]:
                                if "member" in item:
                                    mem = item["member"]
                                    obj = {
                                        "tag": mem["user"]["username"]
                                        + "#"
                                        + mem["user"]["discriminator"],
                                        "id": mem["user"]["id"],
                                    }
                                    if not mem["user"].get("bot"):
                                        self.members.append(str(mem["user"]["id"]))
                        self.lastRange += 1
                        self.ranges = self.getRanges(
                            self.lastRange, 100, self.guilds[self.guild_id]["member_count"]
                        )
                        time.sleep(0.45)
                        self.scrapeUsers()
                if self.endScraping:
                    print(f"Scraped {len(self.members)} members")
                    self.close()
        except Exception as e:
            print(e)


class console():
    

    colors_table = {
        "green":"#65fb07",
        "red":"#Fb0707",
        "yellow":"#c4bc18",
        "magenta":"#b207f5",
        "blue":"#4b484e",
        "cyan":"#07baf5"
    }

    def convert(color):
        if not color.__contains__("#"):
            return console.colors_table[color]
        else:
            return color

    def log_with_status(token, action, status):
        __lock__.acquire()
        current_time = datetime.now().strftime("%H:%M:%S")
        log_time=f"{' '*5}[{colr.Colr().hex('#525052', current_time)}]"
        print(
            f"{log_time} {colr.Colr().hex('#65fb07', f'[{action.upper()}]')} "
            f"{colr.Colr().hex('#Eceeee', f'{token[:26]}****')} {colr.Colr().hex('#0754fb', f'({status})')}")
        __lock__.release()

    def simple_log(message):
        __lock__.acquire()
        current_time = datetime.now().strftime("%H:%M:%S")
        log_time=f"{' '*5}[{colr.Colr().hex('#525052', current_time)}]"
        print(
            f'{log_time} {Fore.YELLOW}{message}{Fore.RESET}',
            flush=True)
        __lock__.release()

    def log(token, action, action_clr, thing=None):
        if not thing==None:
            __thing=f" {colr.Colr().hex(console.convert('blue'), f'({thing})')}"
        else:
            __thing=""

        __lock__.acquire()
        current_time = datetime.now().strftime("%H:%M:%S")
        log_time=f"{' '*5}[{colr.Colr().hex('#525052', current_time)}]"
        print(
            f"{log_time} {colr.Colr().hex(console.convert(action_clr), f'[{action.upper()}]')} "
            f"{colr.Colr().hex('#Eceeee', f'{token[:26]}****')}{__thing}")
        __lock__.release()


    def log_error(message):
        __lock__.acquire(); print(
            f'{" " * 1}{Fore.LIGHTWHITE_EX}[{datetime.now().strftime(f"{Fore.BLUE}%H{Fore.LIGHTWHITE_EX}:{Fore.BLUE}%M{Fore.LIGHTWHITE_EX}:{Fore.BLUE}%S{Fore.LIGHTWHITE_EX}")}]  {Fore.RED}{message}{Fore.RESET}{Back.RESET}{Style.RESET_ALL}',
            flush=True)
        __lock__.release()

class config:
    def get(key, default=None):
        try:
            with open("config.json", "r") as f:
                data = jsond.load(f)
                return data.get(key, default)
        except:
            with open("config.json", "w") as f:
                jsond.dump({
                    "use_proxies": False
                }, f, indent=4)
                return False
            return False

    def set(key, value):
        with open("config.json", "r") as f:
            data = jsond.load(f)
            data[key] = value
        with open("config.json", "w") as f:
            jsond.dump(data, f, indent=4)
            
    def get_captcha_type():
        with open("config.json", "r") as f:
            data = jsond.load(f)
        cap = data.get("captcha")
        type = cap.get("type")
        for cap_type, value in CaptchaType.__dict__.items():
            if not isinstance(value, int):
                continue
            if cap_type == type:
                return value

class scraper_utils:
    def rangeCorrector(ranges):
        if [0, 99] not in ranges:
            ranges.insert(0, [0, 99])
        return ranges

    def getRanges(index, multiplier, memberCount):
        initialNum = int(index*multiplier)
        rangesList = [[initialNum, initialNum+99]]
        if memberCount > initialNum+99:
            rangesList.append([initialNum+100, initialNum+199])
        return scraper_utils.rangeCorrector(rangesList)

    def parseGuildMemberListUpdate(response):
        memberdata = {
            "online_count": response["d"]["online_count"],
            "member_count": response["d"]["member_count"],
            "id": response["d"]["id"],
            "guild_id": response["d"]["guild_id"],
            "hoisted_roles": response["d"]["groups"],
            "types": [],
            "locations": [],
            "updates": []
        }

        for chunk in response['d']['ops']:
            memberdata['types'].append(chunk['op'])
            if chunk['op'] in ('SYNC', 'INVALIDATE'):
                memberdata['locations'].append(chunk['range'])
                if chunk['op'] == 'SYNC':
                    memberdata['updates'].append(chunk['items'])
                else:  # invalidate
                    memberdata['updates'].append([])
            elif chunk['op'] in ('INSERT', 'UPDATE', 'DELETE'):
                memberdata['locations'].append(chunk['index'])
                if chunk['op'] == 'DELETE':
                    memberdata['updates'].append([])
                else:
                    memberdata['updates'].append(chunk['item'])

        return memberdata





class GetEphemeralEmbed(websocket.WebSocketApp):
    def __init__(self, token, bot_id):
        self.packets_recv = 0
        
        self.message: dict = {}
        
        self.bot_id = str(bot_id)
        self.token = token
        
        self.open = False
        
        self.create_id = None


        self.socket_headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
            "User-Agent": DiscordInfo.user_agent,
        }
        super().__init__(
            "wss://gateway.discord.gg/?encoding=json&v=9",
            header=self.socket_headers,
            on_open=lambda ws: self.sock_open(ws),
            on_message=lambda ws, msg: self.sock_message(ws, msg)
        )
        
    def run(self) -> dict:
        self.run_forever()
        self.open = True

        return self.message
    def sock_open(self, ws):
        self.send(
            '{"op":2,"d":{"token":"'
            + self.token
            + '","capabilities":125,"properties":{"os":"Windows","browser":"Firefox","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0","browser_version":"94.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}'
        )

    def sock_message(self, ws, message):
        decoded = json.loads(message)
        if decoded.get("t") not in ["INTERACTION_SUCCESS", "MESSAGE_CREATE", "INTERACTION_CREATE"]:
            return
        t = decoded.get("t")
        if t == "INTERACTION_SUCCESS":
            self.packets_recv += 1
        elif t == "MESSAGE_CREATE" and self.packets_recv == 1:
            author = decoded.get("d").get("author")
            if not author.get("bot"):
                return
            if str(author.get("id")) != self.bot_id:
                return
            self.message = decoded.get("d")
            self.close()
        elif t == "INTERACTION_CREATE":
            d = decoded.get("d")
            if not d.get("id"):
                return
            self.create_id = d.get("id")
            

    def sock_close(self, ws, close_code, close_msg):
        pass


class utility:
    def dazeer_init():
        try:
            
            required_keys = {
                    "use_proxies": False,
                    "proxy_type": "http",
                    "captcha": {
                        "type": "capmonster",
                        "key": "YOUR_CAPMONSTER_KEY"
                    }
                }
            
            if not os.path.exists("data"):
                os.mkdir("data")
            
            if not os.path.exists("data/songs"):
                os.mkdir("data/songs")
                url = "https://cdn.discordapp.com/attachments/1017817011679674550/1075957811453898762/Lowlife_-_Lucki_X.mp3"
                r = requests.get(url, allow_redirects=True)
                with open("data/songs/lucki.mp3", "wb") as f:
                    f.write(r.content)

            if not os.path.exists("scraped"):
                os.mkdir("scraped")

            if not os.path.exists("data/tokens.txt"):
                open("data/tokens.txt", "w").close()

            if not os.path.exists("data/proxies.txt"):
                open("data/proxies.txt", "w").close()
                
            if not os.path.exists("data/blacklisted_ids.txt"):
                open("data/blacklisted_ids.txt", "w").close()    
                
            if not os.path.exists("data/messages.txt"):
                with open("data/messages.txt", "w") as f:
                    f.write("hahahahha\nlol\nlmao\n")

            if not os.path.exists("config.json"):
                with open("config.json", "w") as f:
                    json.dump(required_keys, f, indent=4)
            
            try:
                with open("config.json", "r") as f:
                    config = json.load(f)
                    for key, value in required_keys.items():
                        if isinstance(value, dict):
                            for k, v in value.items():
                                if not config.get(key):
                                    config[key] = value
                                elif not config[key].get(k):
                                    config[key][k] = v
                        else:
                            if key not in config:
                                config[key] = value
                with open("config.json", "w") as f:
                    json.dump(config, f, indent=4)
            except Exception as e:
                print(f"{Fore.RED}Error while checking if all keys are valid in config: {e}")
                time.sleep(5)
                sys.exit()

            try:
                with open("config.json", "r") as f:
                    required_keys = json.load(f)
                    cap = required_keys.get("captcha")
                    if cap.get("solve") and not utility.is_valid_captcha_type(cap.get("type")):
                        console.log_error(f"Invalid captcha type: {cap.get('type')}")
                        print()
                        for cap_type, value in CaptchaType.__dict__.items():
                            if not isinstance(value, int):
                                continue
                            console.simple_log(f"Valid captcha types: {Fore.LIGHTWHITE_EX}{cap_type}")
                        utility.option("Press enter to exit")
                        sys.exit()
            except Exception as e:
                print(f"{Fore.RED}Error while checking if captcha type is valid: {e}")
                time.sleep(5)
                sys.exit()

        except Exception as e:
            print(f"{Fore.RED}Error creating files: {e}")
            time.sleep(5)
            sys.exit()

    def exit():
        print(f"{Fore.RED}Exiting...")
        time.sleep(5)
        sys.exit()
        os._exit(0)

    def get_proxies():
        with open("data/proxies.txt", "r") as f:
            proxies = f.read().strip().splitlines()
        proxies = [proxy for proxy in proxies if proxy not in [" ", "", "\n"]]
        return proxies

    def get_tokens():
        with open("data/tokens.txt", "r") as f:
            tokens = f.read().strip().splitlines()
        tokens = [token for token in tokens if token not in [" ", "", "\n"]]
        return tokens
            
    def is_valid_captcha_type(cap_type):
        return cap_type in [_type.lower() for _type in CaptchaType.__dict__.values() if isinstance(_type, str)]

    def x_content_props(guild):
        guild_id=guild["guild"]["id"]
        channel_id=guild["channel"]["id"]
        return base64.b64encode(str('{"location":"Join Guild","location_guild_id":"'+guild_id+'","location_channel_id":"'+channel_id+'","location_channel_type":0}').encode()).decode()

    def get_board_info(token, guild_id) -> dict:
        session, default_headers, cookie = utility.get_client(token) 
        req = session.get(f"https://discord.com/api/v9/guilds/{guild_id}/onboarding", headers=default_headers, cookies=cookie)
        return req.json()
    
    def get_default_soundboard_sounds(token):
        session, headers, cookie = utility.get_client(token) 
        return session.get("https://discord.com/api/v9/soundboard-default-sounds", headers=headers, cookies=cookie).json()
    
    def ask_onboard_option(prompt) -> str:
        console.simple_log(prompt.get("title"))
        for i in range(len(prompt.get("options"))):
            opt = prompt.get("options")[i]
            console.simple_log(f"{Fore.LIGHTWHITE_EX}[{i + 1}] {opt.get('title')}")
        while True:
            try:
                option = int(input(f"{Fore.LIGHTWHITE_EX}Enter an option: "))
                if option < 1 or option > len(prompt.get("options")):
                    raise ValueError
                break
            except ValueError:
                console.simple_log(f"{Fore.RED}Invalid option")
        return str(prompt.get("options")[option - 1].get("id"))
    
    def get_self_info(token):
        session, default_headers, cookie = utility.get_client(token) 
        req = session.get("https://discord.com/api/v9/users/@me", headers=default_headers, cookies=cookie).json()
        return req

    def download_ffmpeg():
        try:
            if not os.path.exists("ffmpeg.exe"):
                url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2023-04-12-12-48/ffmpeg-n6.0-12-ga6dc92968a-win64-lgpl-6.0.zip"
                console.simple_log(f"Downloading ffmpeg from {Fore.LIGHTWHITE_EX}{url}")
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open("ffmpeg.zip", 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                console.simple_log("Extracting ffmpeg")
                with zipfile.ZipFile("ffmpeg.zip", 'r') as zip_ref:
                    zip_ref.extractall("ffmpeg")
                os.remove("ffmpeg.zip")
                folder_name = url.split("/")[-1].split(".zip")[0]
                os.rename(f"ffmpeg/{folder_name}", "ffmpeg/ffmpeg")
                os.rename("ffmpeg/ffmpeg/bin/ffmpeg.exe", "ffmpeg.exe")
                shutil.rmtree("ffmpeg")
                
            return "ffmpeg.exe"
        except Exception as e:
            console.log_error(f"Error downloading ffmpeg: {e}")
            return None

    def get_random_proxy():
        try:
            return random.choice(utility.get_proxies())
        except:
            return {}

    def short_string(string: str, length: int = None):
        if length is None or not str(length).isdigit():
            length = os.get_terminal_size().columns
        if len(string) > int(length):
            return string[:int(length)] + "..."
        else:
            return string

    def clean_proxy(proxy):
        if isinstance(proxy, str):
            if '@' in proxy:
                return proxy
            elif len(proxy.split(':')) == 2:
                return proxy
            elif len(proxy.split(':')) == 4:
                return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
            else:
                if '.' in proxy.split(':')[0]:
                    return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
                else:
                    return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])
        elif isinstance(proxy, dict):
            if proxy.get("http://") or proxy.get("https://"):
                return proxy
            else:
                if proxy in [dict(), {}]:
                    return {}
                return {
                    "http://": proxy.get("http") or proxy.get("https"),
                    "https://": proxy.get("https") or proxy.get("http")
                }

        

    def get_proxy_type():
        h = config.get("proxy_type", "http")
        if "socks5" in h and "h" in h:
            h = "socks5"
        return h



    def get_session() -> tls_client.Session:
        client = tls_client.Session(
            client_identifier=f"chrome_113",
            random_tls_extension_order=True,
            ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,10-23-27-43-13-65281-16-5-45-18-0-11-35-17513-51-21-41,29-23-24,0",
            h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},
            h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],
            supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],
            supported_versions=["GREASE", "1.3", "1.2"],
            key_share_curves=["GREASE", "X25519"],
            cert_compression_algo="brotli",
            pseudo_header_order=[":method",":authority",":scheme",":path"],
            connection_flow=15663105,
            header_order=["accept","user-agent","accept-encoding","accept-language"]
        )
        if config.get("use_proxies"):
            prox = utility.clean_proxy(utility.get_random_proxy())
            if isinstance(prox, str):
                client.proxies = {
                    "http": f"{utility.get_proxy_type()}://{prox}", 
                    "https": f"{utility.get_proxy_type()}://{prox}"
                }
            elif isinstance(prox, dict):
                client.proxies = prox
        return client

    def get_client(token):
        default_headers = DiscordInfo.default_headers.copy()
        default_headers["authorization"] = token

        session = utility.get_session()
        cookie = utility.get_cookies(session, headers=default_headers)
        default_headers[
            "cookie"] = f'__dcfduid={cookie["__dcfduid"]}; __sdcfduid={cookie["__sdcfduid"]}; __cfruid={cookie["__cfruid"]}; __cf_bm={cookie["__cf_bm"]}; locale={cookie["locale"]}',
        return session, default_headers, cookie


    def get_cookies(session, headers):
        cookies= dict(session.get(
            "https://discord.com/api/v9/experiments", headers=headers
        ).cookies)

        cookies["__cf_bm"]="0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="
        cookies["locale"]="en-US"

        return cookies
    

    def option(msg: str = "", spaces=5, extra=""):
        inp = input(f"{' '*spaces}{Fore.CYAN}[{msg.upper()}]{extra}{Fore.LIGHTWHITE_EX} -> ")
        if inp in GlobalInfo.WHITELISTED_SERVER:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}You cannot use this server. Please kys!")
            input()
            visual.main_screen()
        return inp
    
    def test_proxies():
        ips = []
        for i in range(5):
            try:
                proxy = utility.get_random_proxy()
                proxy = utility.clean_proxy(proxy)
                session = utility.get_session()
                ip = session.get("https://api64.ipify.org").text
                console.simple_log(f"{Fore.GREEN}SUCCESS: {Fore.LIGHTWHITE_EX}Proxy {Fore.CYAN}{utility.short_string(proxy, int(os.get_terminal_size().columns/6))}{Fore.LIGHTWHITE_EX} is working! IP: {Fore.CYAN}{utility.short_string(ip, int(os.get_terminal_size().columns/4))}")
                ips.append(ip)
            except Exception as e:
                print(e)
        if len(set(ips)) == 1:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}All proxies are the same IP. Please use different proxies.")
        else:
            console.simple_log(f"{Fore.GREEN}SUCCESS: {Fore.LIGHTWHITE_EX}Proxies are working!")
        input("Press enter to continue...")
        visual.main_screen()

    def get_message_info(msg_link = None):
        if msg_link is None:
            msg_link = utility.option(msg="message link")
        rg = re.compile(r"^https:\/\/(ptb.|canary.|)discord.com\/channels\/\d+\/\d+\/\d+$")
        if rg.match(msg_link):
            guild_id = msg_link.split("/")[4]
            channel_id = msg_link.split("/")[5]
            message_id = msg_link.split("/")[6]
            return {
                "guild_id": guild_id,
                "channel_id": channel_id,
                "message_id": message_id,
            }
        else:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid message link")
            return None

    def scrape_members(bot_token, guild_id, channel_id):
        return DiscordSocket(bot_token, guild_id, channel_id).run()
    
    

    def get_latest_messages(bot_token, channel_id, limit=100):
        session, headers, cookie = utility.get_client(bot_token)
        messages = session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers=headers,
                               cookies=cookie).json()
        return messages
    
    def has_access_to_channel(bot_token, channel_id):
        session, headers, cookie = utility.get_client(bot_token)
        channel = session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers,
                              cookies=cookie)
        return channel.status_code == 200
    
    
    
    def has_nitro(bot_token, session = None, headers= None, cookie = None):
        try:
            if session is None or headers is None or cookie is None:
                session, headers, cookie = utility.get_client(bot_token)
            sub_ids = []
            sex = session.get(
                "https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots",
                headers=headers,
                cookies=cookie,
            )
            if sex.status_code in [403, 401]:
                console.log_error("Token is invalid, removing.")
                return False
            data = sex.json()
            try:
                for sub in data:
                    sub_ids.append(sub["id"])
            except Exception as e:
                return False, None

            if len(sub_ids) == 0:
                console.log_error("Token does not have any nitro boosts.")
                return False, None
            return True, sub_ids
        except Exception as e:
            console.log_error(f"Error: {e}")
            return False, None
    
    
    def get_message(bot_token, channel_id, message_id, session=None, headers=None, cookie=None):
        if session is None or headers is None or cookie is None:
            session, headers, cookie = utility.get_client(bot_token)
        try:
            message = session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=1&around={message_id}", headers=headers,
                                cookies=cookie).json()
            return message[0]
        except Exception as e:
            return {"code": 10008}
    
    def get_forum_tags(bot_token, channel_id):
        session, headers, cookie = utility.get_client(bot_token)
        forum_tags = []
        try:
            forum = session.get(f"https://discord.com/api/v9/channels/{channel_id}/threads/search?sort_by=last_message_time&sort_order=desc&limit=25&tag_setting=match_some&offset=0", headers=headers, cookies=cookie).json()
            for thread in forum["threads"]:
                if "applied_tags" not in thread:
                    continue
                for applied_tag in thread["applied_tags"]:
                    if applied_tag not in forum_tags:
                        forum_tags.append(applied_tag)
            return forum_tags
        except Exception as e:
            print(e)
            return {"code": 10008}
    
    def get_message_reactions(channel_id, message_id, iteration=0):
        try:
            if iteration > 5:
                return None
            message = utility.get_message(
                bot_token=random.choice(open("data/tokens.txt", "r").read().splitlines()),
                channel_id=channel_id,
                message_id=message_id
            )

            if message.get("code") == 10008:
                return utility.get_message_reactions(channel_id, message_id, iteration=iteration+1)
            emojis = []
            if len(message["reactions"]) == 0:
                return None
            for reaction in message["reactions"]:
                emoji = reaction["emoji"]
                if emoji["id"] == None:
                    emojis.append({
                        "name": emoji["name"],
                        "count": reaction["count"],
                        "custom": False
                    })
                else:
                    emojis.append({
                        "name": f"{emoji['name']}:{emoji['id']}",
                        "count": reaction["count"],
                        "custom": True
                    })

            return emojis
        except Exception as e:
            print(e)

            return None
    


    def get_message_buttons(bot_token, guild_id, channel_id, message_id, session=None, headers=None, cookie=None):
        try:
            message = utility.get_message(
                bot_token=bot_token,
                channel_id=str(channel_id),
                message_id=str(message_id),
                session=session,
                headers=headers,
                cookie=cookie
            )
            if message.get("code") == 10008:
                return None
            buttons = []
            if len(message["components"]) == 0:
                return None
            for component in message["components"]:
                for button in component["components"]:
                    buttons.append({
                        "label": button.get("label"),
                        "custom_id": button["custom_id"],
                        "application_id": message["author"]["id"],
                    })

            return buttons
        except Exception as e:
            print(e)
            return None

    def delete_token(bot_token):
        with open("data/tokens.txt", "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if bot_token not in line:
                    f.write(line)
            f.truncate()


    def extract(bot_token):
        
        r = re.compile(r"(.+):(.+):(.+)")
        if r.match(bot_token):
            return bot_token.split(":")[2]
        else:
            token = bot_token
        return token

    def get_oauth_redirect(client_id):
        try:
            token = utility.extract(random.choice(utility.get_tokens()))
            session, headers, cookie = utility.get_client(token)
            return session.get(f"https://discord.com/api/v9/oauth2/authorize?client_id={client_id}&response_type=code", headers=headers, cookies=cookie).json().get("redirect_uri")
        except Exception as e:
            print(e)
            return None

    def start_threads(func: types.FunctionType, args=[], delay=0, extra_text = "", max_threads = None, do_return = True):
        try:
            tokens = utility.get_tokens()
            gerger = max_threads
            if max_threads == None:
                visual.main_title()
                max_threads = utility.option(msg=f"Max Threads{extra_text}", extra=f" (1-{len(tokens)})")
                visual.main_title()
                try:
                    max_threads = int(max_threads)
                except:
                    pass
                    #pass
                if max_threads == "":
                    max_threads = len(tokens)
                
                if max_threads > len(tokens):
                   max_threads = len(tokens)
            if len(tokens) > 0:
                try:
                    with ThreadPoolExecutor(max_workers=int(max_threads)) as executor:
                        for bot_token in tokens:
                            try:
                                bot_token = utility.extract(bot_token)
                                args.append(bot_token)
                                executor.submit(func, *args)
                                args.remove(bot_token)
                                time.sleep(delay)
                                    
                            except Exception as e:
                                console.log_error(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")
                    if gerger != None:
                        name = " ".join([name.capitalize() for name in func.__name__.split('_')])
                        if do_return:
                            input(f"\n{' ' * 34}{name} Finished, Press enter to continue\n")
                            visual.main_screen()
                    time.sleep(5)
                    if do_return:
                        visual.main_screen()
                except Exception as e:
                    console.log_error(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")
                    input()
                    if do_return:
                        visual.main_screen()
            else:
                console.simple_log(f"No tokens in '{Fore.YELLOW}data/tokens.txt{Fore.LIGHTWHITE_EX}'")
                input()
                if do_return:
                    visual.main_screen()
        except Exception as e:
            console.log_error(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")
            input()
            if do_return:
                visual.main_screen()


    def is_mutal(user_id, guild_id, session, cookie, headers):
        req = session.get(
            f"https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&guild_id={guild_id}",
            headers=headers,
            cookies=cookie
        )

        if req.status_code == 200:
            return True
        else:
            return False

    def get_guild_info(invite):
        try:
            session = tls_client.Session(
                client_identifier="chrome_108"
            )
            if config.get("use_proxies"):
                prox = utility.clean_proxy(utility.get_random_proxy())
                if isinstance(prox, str):
                    session.proxies = "http://" + prox
                elif isinstance(prox, dict):
                    session.proxies = prox
            url = f"https://discord.com/api/v9/invites/{invite}?with_counts=true&with_expiration=true"
            req = session.get(url=url)
            data = req.json()
            if "Unknown Invite" in data.get("message"):
                return None
            return data
        except:
            return None

    def open_dm(user_id, session, cookie, headers, bot_token):
        req = session.post(
            "https://discord.com/api/v9/users/@me/channels",
            headers=headers,
            cookies=cookie,
            json={
                "recipients": [
                    user_id
                ]
            }
        )

        if req.status_code == 200:
            console.log(bot_token, action="OPENED DM", action_clr="green", thing=f"dm channel: {req.json()['id']}")
            return req.json()["id"]
        
        else:
            return None    

    def solve_cap(type: CaptchaType, sitekey, url, rqdata = None):
        key = config.get("captcha").get("key")
        if type == CaptchaType.anticaptcha:
            solver = AnticaptchaTask()
            solver.set_verbose(0)
            solver.set_key(key)
            solver.set_website_url(url)
            solver.set_website_key(sitekey)
            #solver.set_user_agent(f"Discord-Android/{DiscordInfo.build_num};RNA")
            if rqdata is not None:
                solver.set_enterprise_payload({
                    'rqdata': rqdata,
                    'sentry': True })
            g_response = solver.solve_and_return_solution()
            if g_response != 0:
                return g_response
            else:
                print("failed")
            
        elif type == CaptchaType.capmonster:
            capmonster = CapmonsterTask(key)
            capmonster.set_user_agent(f"Discord-Android/{DiscordInfo.build_num};RNA")
            task_id = capmonster.create_task(
                website_url=url, 
                website_key=sitekey, 
                custom_data=rqdata,
            )
            result = capmonster.join_task_result(task_id)
            return result.get("gRecaptchaResponse")
        
        elif type == CaptchaType.capsolver:
            capmonster = CapsolverTask(key)
            capmonster.set_user_agent(f"Discord-Android/{DiscordInfo.build_num};RNA")
            
            task_id = capmonster.create_task(
                website_url=url, 
                website_key=sitekey, 
                is_enterprise=rqdata is not None,
                enterprise_payload={
                    "rqdata": rqdata,
                    "sentry": True
                } if rqdata is not None else None
            )
            result = capmonster.join_task_result(task_id)
            return result.get("gRecaptchaResponse")
        elif type == CaptchaType.dort:
            req = httpx.post("https://api.dort.shop/captcha/solve/hc-enterprise", json={
                "rqdata": rqdata,
                "site_key": sitekey,
                "site_url": url,
                "api_key": key
            }, timeout=200)
            if req.json().get("game[token]") is not None:
                return req.json()["game[token]"]
            return utility.solve_cap(type, sitekey, url, rqdata)


class run():
    def dm_thread(user_id, message, bot_token):
        session, default_headers, cookie = utility.get_client(bot_token)

        default_headers["x-context-properties"]="e30="
        open_dm = session.post("https://discord.com/api/v9/users/@me/channels",headers=default_headers, cookies=cookie,json={
            "recipients": [
                str(user_id)
            ]
        })

        if open_dm.status_code==200:
            del default_headers["x-context-properties"]
            threading.Thread(target=run.send_dm, args=[user_id, message, session, default_headers, cookie, open_dm, bot_token]).start()
        else:
            if open_dm.json().get("message"):
                console.simple_log(f"{open_dm.json()['message']}")
            else:
                console.simple_log(f"{Fore.RED}failed to open dm")
    
    def call_thread(user_id, bot_token):
        try:
            session, default_headers, cookie = utility.get_client(bot_token)
            user_id = str(user_id)
            default_headers["x-context-properties"]="e30="
            open_dm = session.post("https://discord.com/api/v9/users/@me/channels",headers=default_headers, cookies=cookie,json={
                "recipients": [
                    str(user_id)
                ]
            })
            if open_dm.status_code==200:
                del default_headers["x-context-properties"]
                run.send_call(open_dm, bot_token)
            else:
                if open_dm.json().get("message"):
                    console.simple_log(f"{open_dm.json()['message']}")
                else:
                    console.simple_log(f"{Fore.RED}failed to open dm")
        except Exception as e:
            console.simple_log(f"{Fore.RED}failed to open dm")
            print(e)

    def send_dm(user_id, message, session, default_headers, cookie, open_dm, bot_token):
            data={
                    "content": message,
                    "nonce": str(round(Decimal(time.time()*1000-1420070400000)*4194304)),
                    "tts": False,
                    "flags": 0
                }

            while True:
                send =session.post(f"https://discord.com/api/v9/channels/{open_dm.json()['id']}/messages",headers=default_headers, cookies=cookie,json=data)
                if send.status_code==200:
                    console.simple_log(f"{Fore.LIGHTGREEN_EX}sent private message")
                    continue

                elif "captcha" in send.text:
                    console.simple_log(f"captcha on dm")


                    captcha_sitekey = send.json()["captcha_sitekey"]
                    captcha_rqdata = send.json()["captcha_rqdata"]
                    captcha_rqtoken = send.json()["captcha_rqtoken"]

                    cap_key = utility.solve_cap(config.get_captcha_type(), captcha_sitekey, f"https://discord.com/", captcha_rqdata)
                    console.log(bot_token, action="SOLVED CAPTCHA", action_clr='magenta', thing=cap_key[0:30])

                    data = {
                        "content": message,
                        "nonce": str(round(Decimal(time.time()*1000-1420070400000)*4194304)),
                        "tts": False,
                        "flags": 0,
                        "captcha_key": cap_key,
                        "captcha_rqtoken": captcha_rqtoken
                    }
                    continue

                else:
                    if send.json().get("message"):
                        console.simple_log(f"{send.json()['message']}")
                    else:
                        console.simple_log(f"{Fore.RED}failed to send dm")
    
    def send_call(open_dm, bot_token):

        try:
            
            user_id = open_dm.json().get("id")            
            def _call(user_id, bot_token):
                skip = False
                while True:
                    try:
                        if skip:
                            skip = not skip
                            time.sleep(1.75)
                            continue
                        console.log(bot_token, action="CALLING", action_clr='magenta', thing=user_id)
                        ws = WebSocket()
                        ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
                        hello = json.loads(ws.recv())
                        ws.send(json.dumps({"op": 2,"d": {"token": bot_token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
                        ws.send(json.dumps({"op": 4,"d": {"guild_id": None,"channel_id": str(user_id),"self_mute": False,"self_deaf": False, "self_stream": False, "self_video": False}}))
                        ws.send(json.dumps({"op": 18,"d": {"type": "guild","guild_id": None,"channel_id": str(user_id),"preferred_region": "singapore"}}))
                        ws.send(json.dumps({"op": 1,"d": None}))
                        time.sleep(1)
                        ws.send(json.dumps({
                            "op":4,
                            "d":{
                                "guild_id":None,
                                "channel_id":None,
                                "self_mute":True,
                                "self_deaf":False,
                                "self_video":False
                            }
                        }))
                        time.sleep(1.75)
                    except Exception as e:
                        console.simple_log(f"{Fore.RED}failed to call {user_id} with {bot_token.split('.')[0]}")
                        continue
            while True:
                _call(user_id, bot_token)
        except:
            console.simple_log(f"{Fore.RED}failed to call {user_id} with {bot_token.split('.')[0]}")
            
        
    
    def delete_join_msg(session, headers, cookie, join_channel_id):
        messages = session.get(f"https://discord.com/api/v9/channels/{join_channel_id}/messages?limit=100",headers=headers,cookies=cookie).json()

        for message in messages:
            bot_token_id = base64.b64decode(headers["authorization"].split(".")[0]+"==").decode()

            if message["content"]=="" and bot_token_id == message["author"]["id"]:
                deleted_join = session.delete(f"https://discord.com/api/v9/channels/{join_channel_id}/messages/{message['id']}")
                if deleted_join.status_code==204:
                    console.log(headers["authorization"], action="deleted join message", action_clr='green')
                else:
                    console.log(headers["authorization"], action="failed to delete", action_clr='red', thing=deleted_join.json()["message"])     
                break
        
        console.log(headers["authorization"], action="cant find", action_clr='yellow') 

    def join(invite, message, channel_id, silent, join_channel_id, bypass_rules, guild_id, xcontent, bot_token, extra="", data = None):
        try:
            threading.Thread(target=run.online,args=[False, bot_token]).start()
            if data is None:
                data = {}
            session, headers, cookie = utility.get_client(bot_token)


            try:
                res = session.get(
                    f"https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true", headers=headers).json()
                
                jsonContext = {
                    "location": "Join Guild",
                    "location_guild_id": str(res['guild']['id']),
                    "location_channel_id": str(res['channel']['id']),
                    "location_channel_type": int(res['channel']['type'])
                }
                json_str = json.dumps(jsonContext)
                xContext = b64encode(json_str.encode()).decode()
                headers["x-context-properties"] = xContext

            except:
                pass

            headers["content-length"] = "2"
            req = session.post(f'https://discord.com/api/v9/invites/{invite}', headers=headers, json={})




        except Exception as e:
            console.log(bot_token, action="FAILED", action_clr='red', thing=str(e))

        try:
            json.loads(req.text)
        except Exception as e:
            if isinstance(e, json.decoder.JSONDecodeError) and "cloudflare" in req.text.lower():
                console.log(bot_token, action="ratelimited by cloudflare", action_clr='cyan')

        else:
            if req.status_code == 200:
                console.log(bot_token, action=f"JOINED{extra}", action_clr='green', thing=f"discord.gg/{invite}")
                
                if bypass_rules == "y":
                    run.accept_rule(guild_id, bot_token, session, headers, cookie)

                if silent=="y":
                    run.delete_join_msg(session, headers, cookie, join_channel_id)

                if not message=="":
                    msg_amount=999999999;delay=0;pings_per_message=0;massping=False;massping_iter=0
                    run.send_message(message, channel_id, msg_amount, delay, pings_per_message, massping, massping_iter, bot_token)

            elif "captcha_key" in req.text:
                time.sleep(1)
                console.log(bot_token, action="CAPTCHA", action_clr="yellow", thing="a9b5fb07-92ff-493f-86fe-352a2803b3df")

                if config.get("captcha").get("key") == "":
                    console.simple_log(f"{Fore.RED}CAPTCHA KEY NOT FOUND")
                    return
                
                captcha_sitekey = req.json()["captcha_sitekey"]
                captcha_rqdata = req.json()["captcha_rqdata"]
                captcha_rqtoken = req.json()["captcha_rqtoken"]

                cap_key = utility.solve_cap(config.get_captcha_type(), captcha_sitekey, f"https://discord.com/invite/{invite}", captcha_rqdata)
                console.log(bot_token, action="SOLVED CAPTCHA", action_clr='magenta', thing=cap_key[0:30])

                data = {
                    "captcha_key": cap_key,
                    "captcha_rqtoken": captcha_rqtoken
                }
                
                extra=" WITH CAPTCHA"

                run.join(invite, message, channel_id, silent, join_channel_id, bypass_rules, guild_id, xcontent, bot_token, extra, data)

            else:
                if "unknown message" in req.text.lower():
                    run.join(invite, message, channel_id, silent, join_channel_id, bypass_rules, guild_id, xcontent, bot_token)
                else:
                    console.log(bot_token, action="FAILED", action_clr='#Fb0707', thing=req.json()['message'])



    def leave(guild_id: str, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"

        req = session.delete(
            f"https://discord.com/api/v9/users/@me/guilds/{guild_id}",
            headers=headers,
            cookies=cookie,
            json={
                "lurking": False
            }
        )

        if req.status_code == 204:
            console.log(bot_token, action="left", action_clr="green",thing=f"Guild ID: {guild_id}")
        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])

    def shuffle_emojis():
        order = list("😀😃😄😁😆😅😂🤣🥲🥹☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😮‍💨😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🫣🤗🫡🤔🫢🤭🤫🤥😶😶‍🌫️😐😑😬🫠🙄😯😦😧😮😲🥱😴🤤😪😵😵‍💫🫥🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾😀😃😄😁😆😅😂🤣🥲🥹☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😮‍💨😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🫣🤗🫡🤔🫢🤭🤫🤥😶😶‍🌫️😐😑")
        random.shuffle(order)

        emojis=""
        for emoji in order:
            emojis+=emoji
        return emojis

    def send_message(options: SpammerOptions, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"

        for _ in range(int(options.msg_amount)):
            try:
                message1 = random.choice(options.messages).replace("<down>","\n")
                bru = [
                    "# ",
                    "## ",
                    "### ",
                ]
                # message1 = random.choice(bru) + message1
                
                bru = f"""```ansi\n[39m{message1}\n```"""
                message1 = bru
                if options.crypt_message:
                    leet = {
                        'a':['4', 'Α', 'α', 'Δ', 'Λ', 'λ'],
                        'b':['Β', 'β',],
                        'e':['3', 'Ε', 'ε', 'Σ', 'Ξ', 'ξ'],
                        'i':['1', 'Ι',],
                        'o':['0', 'Θ', 'θ', 'Ο', 'ο'],
                        'k':['Κ', 'κ'],
                        't':['Τ', 'τ'],
                        'n':['Ν', 'η', 'Π'],
                        'm':['Μ']
                    }
                        
                    words = message1.split(" ")
                    for word in words:
                        if ("discord.gg/" or "http://" or "https://") not in word:
                            message1 = message1.replace(word, (lambda message: ''.join([random.choice(leet[char.lower()]) if char.lower() in leet and random.random() <= 0.5 else char for char in message]))(word))
                    
                if options.invisible_pings:
                    message1 += " ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| "
                
                if options.emoji_message:
                    message1 +=run.shuffle_emojis()

                if options.massping:
                    message1 += " ¦ "
                    users = [str(next(options.massping_iter)) for i in range(int(options.ping_amount))]
                    for user in users:
                        if len(message1) + len(f"<@{user}> ") <= 2000:
                            message1 += f"<@{user}> "
                
                cn_id = random.choice(options.channel_ids)

                req = session.post(
                    f"https://discord.com/api/v9/channels/{cn_id}/messages",
                    headers=headers,
                    cookies=cookie,
                    json={
                        "content": message1,
                        "nonce": str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                        "flags": 0,
                        "tts": False
                    }
                )

                if req.status_code == 200:
                    console.log(bot_token, action="sent message", action_clr="green",thing=f"Channel ID: {cn_id}")
                else:
                    if "exceeds the mention limit set by this server" in req.text:
                        console.log(bot_token, action="failed", action_clr="yellow",thing=f"Exceeded mention limit")
                        return
                    elif "This content is blocked by this server" in req.text:
                        console.log(bot_token, action="failed", action_clr="yellow",thing=f"Word is blocked")
                        return
                    
                    if req.status_code == 429:
                        time.sleep(5)

                time.sleep(float(options.delay) + random.uniform(0.05, 0.5))
            except Exception as e:
                print(e)


    def accept_rule(guild_id, bot_token, session = None, headers = None, cookie = None):
        if session is None or headers is None or cookie is None:
            session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"

        get_rules = session.get(
            f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false",
            headers=headers,
            cookies=cookie
        ).json()

        req = session.put(
            f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me",
            headers=headers,
            cookies=cookie,
            json=get_rules
        )

        if req.status_code == 201:
            console.log(bot_token, action="accepted", action_clr="green",thing=f"Guild ID: {guild_id}")
        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])


    def send_webhook_message(message, webhook, msg_amount):
        for _ in range(int(msg_amount)):
            req = httpx.post(webhook, data={"content": message})
            if req.status_code == 204:
                console.simple_log(f"{Fore.LIGHTGREEN_EX}sent message")
            else:
                console.simple_log(f"{Fore.RED}failed to send message")


    def react(emoji, message_id, channel_id, bot_token):
        session, headers, cookie = utility.get_client(bot_token)

        req = session.put(
            f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/%40me?location=Message&burst=false",
            headers=headers,
            cookies=cookie
        )

        if req.status_code == 204:
            console.log(bot_token, action="reacted", action_clr="green",thing=f"Message ID: {message_id}")
        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])

    def spam_ticket(guild_id, ticket_channel_id, bot_token):
        def get_ticket_button(channel_id,headers,cookie,session):
            messages = session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=20",headers=headers,cookies=cookie).json()
            try:
                for message in messages:
                    if not message["embeds"] == []:
                        if "TicketTool.xyz" in message["embeds"][0]["footer"]["text"]:
                            message_id = message["id"]
                            custom_id = message["components"][0]["components"][0]["custom_id"]

                            return message_id, custom_id
            except:
                return None, None

        def get_close_message(channel_id,headers,cookie,session):
            while True:
                try:
                    messages = session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=20",headers=headers,cookies=cookie).json()
                    for message in messages:
                        if message["content"] == "Are you sure you would like to close this ticket?":
                            message_id = message["id"]
                            custom_id = message["components"][0]["components"][0]["custom_id"]

                            return message_id, custom_id
                    break
                
                except:
                    time.sleep(5)
                    continue

        def click(session, headers, cookie, guild_id, channel_id, message_id, custom_id):
            payload = {
                "type": 3,
                "nonce": str(Decimal(time.time()*1000-1420070400000)*4194304).split(".")[0],
                "guild_id": guild_id,
                "channel_id": channel_id,
                "message_flags": 0,
                "message_id": message_id,
                "application_id": "557628352828014614",
                "session_id": "".join(random.sample(string.ascii_lowercase+string.digits,32)),
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id
                }
            }

            return session.post("https://discord.com/api/v9/interactions", headers=headers, json=payload, cookies=cookie)

        def open_ticket(guild_id, channel_id, message_id, custom_id, session, headers, cookie):
            payload = {
                "type": 3,
                "nonce": str(Decimal(time.time()*1000-1420070400000)*4194304).split(".")[0],
                "guild_id": guild_id,
                "channel_id": channel_id,
                "message_flags": 0,
                "message_id": message_id,
                "application_id": "557628352828014614",
                "session_id": "".join(random.sample(string.ascii_lowercase+string.digits,32)),
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id
                }
            }

            req = session.post("https://discord.com/api/v9/interactions", headers=headers, json=payload, cookies=cookie)

        def get_ticket_made(guild_id,headers,cookie,session):
            channels = session.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels",headers=headers, cookies=cookie).json()
            bot_token_id = base64.b64decode(str(headers["authorization"].split(".")[0]+"==").encode()).decode()

            for channel in channels:
                if "ticket-" in channel["name"]:
                    for perm in channel["permission_overwrites"]:
                        if perm["id"] == bot_token_id and not perm["allow"] == "0":
                            return channel["id"]
            return None

        def close_ticket(guild_id, ticket_id, session, headers, cookie):
            message_id, custom_id = get_ticket_button(ticket_id,headers,cookie,session)
            click(session, headers, cookie, guild_id, ticket_id, message_id, custom_id)

            time.sleep(3)
            message_id1, custom_id1 = get_close_message(ticket_id,headers,cookie,session)
            req = click(session, headers, cookie, guild_id, ticket_id, message_id1, custom_id1)
            if req.status_code==204:
                console.simple_log(f"{Fore.YELLOW}Closed ticket")

        def ticket_thread(bot_token, guild_id, channel_id):
            session, headers, cookie = utility.get_client(bot_token)
            headers["content-type"] = "application/json"

            while True:
                message_id1, custom_id1 = get_ticket_button(channel_id,headers,cookie,session)
                if not message_id1 == None:
                    open_ticket(guild_id, channel_id, message_id1, custom_id1, session, headers, cookie)
                    time.sleep(5)

                    ticket_id = get_ticket_made(guild_id,headers,cookie,session)
                    if ticket_id==None:
                        console.simple_log(f"{Fore.RED}Failed to make ticket")
                        time.sleep(10)
                        
                    else:
                        console.simple_log(f"{Fore.LIGHTGREEN_EX}Made ticket {ticket_id}")
                        close_ticket(guild_id, ticket_id, session, headers, cookie)
                        time.sleep(5.2)

                else:
                    time.sleep(10)
        ticket_thread(bot_token, guild_id, ticket_channel_id)

    def make_thread(channel_id, message, title, amount, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"
        
        for i in range(int(amount)):
            req = session.post(
                f"https://discord.com/api/v9/channels/{channel_id}/threads",
                headers=headers,
                cookies=cookie,
                json={
                    "auto_archive_duration": "4320",
                    "location": "Plus Button",
                    "name": title,
                    "type": "11"
                }
            )
            if req.status_code == 201:
                req1 = session.post(
                    f"https://discord.com/api/v9/channels/{req.json()['id']}/messages",
                    headers=headers,
                    cookies=cookie,
                    json={
                        "content": message,
                        "nonce": str(Decimal(time.time()*1000-1420070400000)*4194304).split(".")[0],
                        "tts": False
                    }
                )

                if req1.status_code == 200:
                    console.log(bot_token, action="thread created", action_clr="green",thing=f"Channel ID: {channel_id}")
                else:
                    console.log(bot_token, action="failed", action_clr="red",thing=req1.json()['message'])
                    
            elif req.status_code == 429:
                console.log(bot_token, action="ratelimited", action_clr="yellow",thing=f"for {str(req.json()['retry_after'])}s")
                time.sleep(float(req.json()['retry_after']))
            else:
                console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])
    
    def make_forum_post(channel_id, message, title, tags, amount=1, bot_token=""):
        try:
            for i in range(amount):
                if message == "RANDOM":
                    message = str(secrets.token_urlsafe(16))
                if title == "RANDOM":
                    title = str(secrets.token_urlsafe(16))
                session, headers, cookie = utility.get_client(bot_token)
                headers["content-type"] = "application/json"
                tags = [str(random.choice(tags))] if len(tags) > 0 else []
                req = session.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/threads?use_nested_fields=true",
                    headers=headers,
                    cookies=cookie,
                    json={
                        "name":title,
                        "auto_archive_duration":10080,
                        "applied_tags": tags,
                        "message":
                        {
                            "content": message
                        }
                    }
                )

                if req.status_code == 201:
                    req1 = session.post(
                        f"https://discord.com/api/v9/channels/{req.json()['id']}/messages",
                        headers=headers,
                        cookies=cookie,
                        json={
                            "content": message,
                            "nonce": str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                            "tts": False
                        }
                    )

                    if req1.status_code == 200:
                        console.log(bot_token, action="created post", action_clr="green",thing=f"Channel ID: {channel_id}")
                    else:
                        console.log(bot_token, action="failed", action_clr="red",thing=req1.json()['message'])
                        
                elif req.status_code == 429:
                    console.log(bot_token, action="ratelimited", action_clr="yellow",thing=f"for {req.json()['retry_after']}s")
                    time.sleep(float(req.json()['retry_after']))
                else:
                    console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])

        except Exception as e:
            console.log(bot_token, action="failed", action_clr="red",thing=str(e))

    def click_button(guild_id, channel_id, message_id, custom_id, application_id, amount = 999999999, bot_token = None, flags = 0):
        try:
            session, headers, cookie = utility.get_client(bot_token)

            post_data = {
                "application_id": str(application_id),
                "channel_id": str(channel_id),
                "data": {
                    "component_type": 2,
                    "custom_id": str(custom_id)
                },
                "guild_id": str(guild_id),
                "message_flags": flags,
                "message_id": str(message_id),
                "nonce": str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0],
                "session_id": str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
                "type": 3,
                
            }
            headers.update({"content-type": "application/json"})
            headers.update({"referer": f"https://discord.com/channels/{guild_id}/{channel_id}"}) # discord checks referer now xd
            for i in range(amount):
                req = session.post(f"https://discord.com/api/v9/interactions", headers=headers, cookies=cookie, json=post_data)
                if req.status_code == 204:
                    console.simple_log(f"{Fore.LIGHTGREEN_EX}Pressed button")
                else:
                    console.simple_log(f"{Fore.RED}Couldn't press button {req.status_code}")


        except Exception as e:
            console.log(bot_token, action="failed", action_clr="red",thing=str(e))



    def nick_bot(guild_id, nick_name, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"

        req = session.patch(
            f"https://discord.com/api/v9/guilds/{guild_id}/members/%40me/nick",
            headers=headers,
            cookies=cookie,
            json={
                "nick": nick_name
            }
        )

        if req.status_code == 200:
            console.log(bot_token, action="nicked", action_clr="green",thing=f"Nick: {nick_name}")
        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])


    def unfriend_user(user_id: str, bot_token: str):
        session, headers, cookie = utility.get_client(bot_token)
        headers["x-context-properties"] = "eyJsb2NhdGlvbiI6IkZyaWVuZHMifQ=="

        req = session.delete(
            f"https://discord.com/api/v9/users/@me/relationships/{user_id}",
            headers=headers,
            cookies=cookie
        )

        if req.status_code == 204:
            console.log(bot_token, action="unfriended", action_clr="green",thing=user_id)
        elif "captcha_key" in req.text:
            console.log(bot_token, action="captcha", action_clr="yellow",thing="a9b5fb07-92ff-493f-86fe-352a2803b3df")
        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])


    def friend_user(username: str, bot_token: str, data={}, extra=""):
        session, headers, cookie = utility.get_client(bot_token)
        headers["x-context-properties"] = "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ=="
        headers["content-type"] = "application/json"

        if data=={}:
            name, discrim = username.split("#")
            data={
                    "username": name,
                    "discriminator": int(discrim)
                }
        else:
            pass

        try:
            req = session.post(
                "https://discord.com/api/v9/users/@me/relationships",
                headers=headers,
                cookies=cookie,
                json=data
            )
        except ValueError:
            console.log(bot_token, action="failed", action_clr="red",thing="Invalid username")
            return

        if req.status_code == 204:
            console.log(bot_token, action="friended", action_clr="green",thing=username)

        elif "captcha_key" in req.text:
            threading.Thread(target=run.online,args=[False,bot_token]).start()
            time.sleep(1)
            console.log(bot_token, action="captcha", action_clr="yellow",thing="a9b5fb07-92ff-493f-86fe-352a2803b3df")

            if config.get("captcha").get("key") == "":
                console.simple_log(f"{Fore.RED}CAPTCHA KEY NOT FOUND")
                return
            
            captcha_sitekey = req.json()["captcha_sitekey"]
            captcha_rqdata = req.json()["captcha_rqdata"]
            captcha_rqtoken = req.json()["captcha_rqtoken"]

            cap_key = utility.solve_cap(config.get_captcha_type(), captcha_sitekey, f"https://discord.com/", captcha_rqdata)
            console.log(bot_token, action="SOLVED CAPTCHA", action_clr='magenta', thing=cap_key[0:30])

            data = {
                "captcha_key": cap_key,
                "captcha_rqtoken": captcha_rqtoken,
                "username": name,
                "discriminator": int(discrim)
            }
            
            extra=f"{Fore.YELLOW}[CAPTCHA SOLVED] "

            run.friend_user(username, bot_token, data, extra)
            
        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])


    def join_hypesquad(hypesquad_id: int, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"

        req = session.post(
            "https://discord.com/api/v9/hypesquad/online",
            headers=headers,
            cookies=cookie,
            json={
                "house_id": hypesquad_id
            }
        )

        if req.status_code == 204:
            console.log(bot_token, action="joined hypesquad", action_clr="green",thing=f"Type: {str(hypesquad_id)}")

        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])

    def change_bio(bio, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"

        req = session.patch(
            "https://discord.com/api/v9/users/%40me/profile",
            headers=headers,
            cookies=cookie,
            json={
                "bio": bio
            },
        )

        if req.status_code == 200:
            console.log(bot_token, action="updated bio", action_clr="green",thing=f"new bio: {bio}")
        else:
            console.log(bot_token, action="failed", action_clr="red",thing=req.json()['message'])

    def connect_vc(guild_id, voice_id, bot_token):
        ws = WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
        hello = json.loads(ws.recv())
        ws.send(json.dumps({"op": 2,"d": {"token": bot_token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
        ws.send(json.dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": voice_id,"self_mute": False,"self_deaf": False, "self_stream?": False, "self_video": False}}))
        ws.send(json.dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": voice_id,"preferred_region": "singapore"}}))
        ws.send(json.dumps({"op": 1,"d": None}))
        while True:
            ws.recv()
            time.sleep(hello.get("d").get("heartbeat_interval") / 1000)

    def spam_vc(guild_id, voice_id, bot_token):
        while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = json.loads(ws.recv())
            ws.send(json.dumps({"op": 2,"d": {"token": bot_token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(json.dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": voice_id,"self_mute": True,"self_deaf": True, "self_stream?": True, "self_video": True}}))
            ws.send(json.dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": voice_id,"preferred_region": "singapore"}}))
            ws.send(json.dumps({"op": 1,"d": None}))
            ws.close()
            time.sleep(0.1)

    def type(channel_id, type_time, bot_token):
        session, headers, cookie = utility.get_client(bot_token)

        req = session.post(
            f"https://discord.com/api/v9/channels/{channel_id}/typing",
            headers=headers,
            cookies=cookie
        )

        if req.status_code == 204:
            console.log(bot_token, action="bot typing", action_clr="green",thing=f"Channel ID: {channel_id}")

            for _ in range(int(type_time) // 5):
                session.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/typing",
                    headers=headers,
                    cookies=cookie
                )
                time.sleep(5)

        else:
            console.log(bot_token, action="failed", action_clr="red",thing=f"{req.json()['message']}")


    def online(debug=False, bot_token=None):
        def connect(token):
            try:
                random_with_percentage = lambda data: next(iter(random.choices(population=list({k: v/sum(data.values()) for k, v in data.items()}), weights={k: v/sum(data.values()) for k, v in data.items()}.values(), k=1)))
                get_random_time = lambda: (int(delorean.Delorean(datetime.now(timezone.utc), timezone="UTC").epoch) * 1000) - random.randint(100000, 10000000)
                get_nonce = lambda: str((int(time.mktime(datetime.now().timetuple()))*1000-1420070400000)*4194304)
                ws = websocket.WebSocket()
                ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
                data = json.loads(ws.recv())
                heartbeat_interval = data["d"]["heartbeat_interval"]
                device = random_with_percentage({"Discord iOS": 25,"Windows": 75})
                ws.send(json.dumps({"op":2,"d":{"token":token,"properties":{"$os":device,"$browser":device,"$device":device}},"s":None,"t":None}))
                type = random_with_percentage({"normal": 65, "playing": 15, "spotify": 15, "visual_studio": 5})
                if type == "normal":
                    activities = []
                if type == "playing":
                    activities = [{"type":0,"timestamps":{"start":get_random_time()},"name":random_with_percentage({"Battlerite":10,"League of Legends":10,"PLAYERUNKNOWN'S BATTLEGROUNDS":10,"Counter-Strike: Global Offensive":10,"Overwatch":10,"Minecraft":15,"World of Warcraft":5,"Grand Theft Auto V":10,"Tom Clancy's Rainbow Six Siege":10,"Rocket League":10}),}]
                if type == "spotify":
                    song = random.choice(spotify_songs)
                    activities = [{"id":"spotify:1","type":2,"flags":48,"name":"Spotify","state":song["artists"][0]["name"],"details":song["name"],"timestamps":{"start":(int(delorean.Delorean(datetime.now(timezone.utc),timezone="UTC").epoch)*1000),"end":(int(delorean.Delorean(datetime.now(timezone.utc),timezone="UTC").epoch)*1000)+random.randint(100000,300000)},"party":{"id":f"spotify:{get_nonce()}"},"assets":{"large_image":f"spotify:{song['images'][0]['url'].split('https://i.scdn.co/image/')[1]}"}}]
                if type == "visual_studio":
                    vsc = {"images":{"py":"565945350645481492","js":"808841241142755358"},"workspaces":["vscode","files","projects","bot","github","personal","Downloads","Desktop"],"names":["main.py","bot.py","index.js","run.js","install.py","install.js","test.js","test.py","abc.js","abc.py"]}
                    workspace = random.choice(vsc["workspaces"])
                    filename = random.choice(vsc["names"])
                    activities = [{"type":0,"name":"Visual Studio Code","state":f"Workspace: {workspace}","details":f"Editing {filename}","application_id":"383226320970055681","timestamps":{"start":get_random_time()},"assets":{"small_text":"Visual Studio Code","small_image":"565945770067623946","large_image":vsc["images"][filename.split(".")[1]]},}]

                payload = json.dumps({"op": 3,"d": {"since": 0,"activities": activities,"status": random_with_percentage({"online": 35, "dnd": 45, "idle": 20}),"afk": False}})
                ws.send(payload)
                if debug:
                    console.log_with_status(token, action="online", status=type.replace('_', ' ').title())

                
                while True:
                    time.sleep(heartbeat_interval / 1000)
                    try:
                        ws.send(json.dumps({
                            "op": 1,
                            "d": None
                        }))
                        ws.send(payload)
                    except Exception as b:
                        print(str(b))
                        connect(token)
            except Exception as e:
                print(str(e))
                connect(token)

        connect(bot_token)
        
    def spotify_spam(user_id, bot_token):
        def connect(token):
            try:
                random_with_percentage = lambda data: next(iter(random.choices(population=list({k: v/sum(data.values()) for k, v in data.items()}), weights={k: v/sum(data.values()) for k, v in data.items()}.values(), k=1)))

                ws = websocket.WebSocket()
                ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
                data = json.loads(ws.recv())
                heartbeat_interval = data["d"]["heartbeat_interval"]
                device = random_with_percentage({"Discord iOS": 25,"Windows": 75})
                ws.send(json.dumps({"op":2,"d":{"token":token,"properties":{"$os":device,"$browser":device,"$device":device}},"s":None,"t":None}))
                song = random.choice(spotify_songs)
                
                payload = {
                    "op":3,
                    "d":{
                        "status":"dnd",
                        "since":0,
                        "activities":[
                            {
                                "type":2,
                                "name":"Spotify",
                                "assets":{
                                    "large_image":f"spotify:{song['images'][0]['url'].split('https://i.scdn.co/image/')[1]}",
                                    "large_text":"RAM RANCH NIGGA"
                                },
                                "details":"NIGGA PENIS",
                                "state":"QOFT > YOU",
                                "timestamps":{"start":(int(delorean.Delorean(datetime.now(timezone.utc),timezone="UTC").epoch)*1000),"end":(int(delorean.Delorean(datetime.now(timezone.utc),timezone="UTC").epoch)*1000)+random.randint(1000,3000)},
                                "party":{
                                    "id":f"spotify:{user_id}"
                                },
                                "sync_id":f"1a{secrets.token_hex(10)}",
                                "flags":48,
                                "metadata":{
                                "album_id":song.get('id'),
                                "artist_ids":[song.get('artists')[0].get('id')]
                                }
                            }
                        ],
                        "afk":False
                    }
                }
                payload = json.dumps(payload)
                ws.send(payload)
                console.log(bot_token, action="listening", action_clr="green")

                while True:
                    time.sleep(heartbeat_interval / 1000)
                    try:
                        ws.send(json.dumps({
                            "op": 1,
                            "d": None
                        }))
                        ws.send(payload)
                    except Exception:
                        connect(token)
            except Exception as e:
                print(e)
                connect(token)
        connect(bot_token)
        
    def vc_raper(files, channel_id, amount):
        async def vc_rape_main(channel_id, files):
            tokens = utility.get_tokens()
            tkns = [random.choice(tokens) for i in range(amount)]
            ready = {
                t: False for t in tkns
            }
            
            async def spam_vc(files, token, channel_id):
                class VcBot(commands.Bot):
                    def __init__(self, channel_id):
                        super().__init__(command_prefix="!!", self_bot=True, chunk_guilds_on_startup=False)
                        self.channel_id = int(channel_id)
                        self.file = os.path.join(os.getcwd(), "data", "songs", self.pick_file())
                        self.vc = None
                        
                    def pick_file(self):
                        return next(files)
                    
                    async def on_ready(self):
                        read = sum(1 for token, readd in ready.items() if readd)
                        console.simple_log(f"Logged in as {self.user} ({read + 1}/{len(ready)} ready) {Fore.LIGHTBLACK_EX} [Playing: {self.file.split(os.sep)[-1]}]")
                        
                        self.channel: discord.VoiceChannel = self.get_channel(self.channel_id)
                        ready[token] = True
                        # while not all(ready.values()):
                        #     await asyncio.sleep(0.001)
                        await self.spam_channel()
                        
                    async def on_voice_state_update(self, member, before, after):
                        if member.id != self.user.id:
                            return 
                        if before.channel is None:
                            return
                        if after.channel is not None:
                            return
                        
                        try:
                            console.simple_log(f"{Fore.RED}Reconnecting due to disconnection {Fore.LIGHTWHITE_EX}-> {self.user} {Fore.LIGHTBLACK_EX}")
                            await self.spam_channel()
                        except Exception as e:
                            print(e)
                            await asyncio.sleep(1)

                    async def spam_channel(self):
                        try:
                            if (self.vc is None) or (not self.vc.is_connected()):
                                try:
                                    self.vc = await self.channel.connect()
                                except Exception as e:
                                    print(e)
                                    console.log_error(f"Failed to connect to {self.channel} {Fore.LIGHTWHITE_EX}-> {self.user} {Fore.LIGHTBLACK_EX} ({e})")
                                    if self.channel is None:
                                        return console.log_error(f"Channel {self.channel_id} not found {Fore.LIGHTWHITE_EX}-> {self.user} {Fore.LIGHTBLACK_EX}")
                                    return print("Failed to connect")
                            print(f"Playing {self.file} {Fore.LIGHTWHITE_EX}-> {self.user} {Fore.LIGHTBLACK_EX}")
                            self.vc.play(discord.FFmpegOpusAudio(source=self.file))
                            
                            while self.vc.is_playing():
                                await asyncio.sleep(0.001)
                            await self.spam_channel()
                        except Exception as e:
                            console.log_error(f"Erorr while playing {self.file} {Fore.LIGHTWHITE_EX}-> {self.user} {Fore.LIGHTBLACK_EX} ({e})")
                            await asyncio.sleep(1)
                try:
                    await VcBot(channel_id=channel_id).start(token)
                except Exception as e:
                    print(e)
                    ready.pop(token)
                    
                
            try:
                tasks = [spam_vc(files, utility.extract(tkns[i].strip()), channel_id) for i in range(amount)]
                await asyncio.gather(*tasks)
            except Exception as e:
                console.log_error(e)
        asyncio.run(vc_rape_main(channel_id, files))
    
    def clean(bot_token):
        class TokenCleaner:
            def __init__(self, bot_token: str):
                self.bot_token = bot_token
                self.session, self.headers, self.cookie = utility.get_client(self.bot_token)
            

            def leave_all_guilds(self):
                guilds = [guild['id'] for guild in self.session.get("https://discord.com/api/v9/users/@me/guilds", headers=self.headers, cookies=self.cookie).json()]
                print(guilds)
                if len(guilds) == 0:
                    console.log(bot_token, action="no guilds", action_clr="green")
                    
                for guild in guilds:
                    self.headers["Content-Type"] = "application/json"
                    console.log(bot_token, action="leaving", action_clr="green", thing=f"Guild: {guild}")
                    statuscode = self.session.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}", headers=self.headers, cookies=self.cookie).status_code
                    if statuscode == 204:
                        console.log(bot_token, action="left", action_clr="green", thing=f"Guild: {guild}")
                    else:
                        console.log(bot_token, action="failed", action_clr="red", thing=f"Statuscode: {statuscode}")

            def delete_friends(self):
                blocks = self.session.get("https://discord.com/api/v9/users/@me/relationships", headers=self.headers, cookies=self.cookie).json()
                if len(blocks) == 0:
                    console.log(bot_token, action="no blocks", action_clr="green")

                for block in blocks:
                    console.simple_log(f"Deleting block with {block['user']['username']}#{block['user']['discriminator']}")
                    self.session.delete(f"https://discord.com/api/v9/users/@me/relationships/{block['id']}", headers=self.headers, cookies=self.cookie)
            
            def delete_all_dms(self):
                dms = self.session.get("https://discord.com/api/v9/users/@me/channels", headers=self.headers, cookies=self.cookie).json()
                if len(dms) == 0:
                    console.log(bot_token, action="no dms", action_clr="red")
                    
                for dm in dms:
                    console.simple_log(f"Deleting DM with {Fore.LIGHTWHITE_EX}{dm['recipients'][0]['username']}#{dm['recipients'][0]['discriminator']}")
                    self.session.delete(f"https://discord.com/api/v9/channels/{dm['id']}", headers=self.headers, cookies=self.cookie)
                
            def delete_all_guilds(self):
                guilds = self.session.get("https://discord.com/api/v9/users/@me/guilds", headers=self.headers, cookies=self.cookie).json()
                if len(guilds) == 0:
                    console.log(bot_token, action="no guilds", action_clr="green")
                    
                for guild in guilds:
                    console.simple_log(f"Deleting guild {Fore.LIGHTWHITE_EX}{guild['name']}")
                    self.session.delete(f"https://discord.com/api/v9/guilds/{guild['id']}", headers=self.headers, cookies=self.cookie, data={"lurking":False}, json={"lurking":False})

            def start(self):
                time.sleep(1)
                console.simple_log(f"{Fore.LIGHTGREEN_EX}STARTING CLEANER {Fore.LIGHTWHITE_EX}-> **{self.bot_token.split('.')[0]}** {Fore.LIGHTBLACK_EX}")
                self.leave_all_guilds()
                time.sleep(1)
                console.simple_log(f"{Fore.LIGHTGREEN_EX}FINISHED LEAVING GUILDS {Fore.LIGHTWHITE_EX}-> **{self.bot_token.split('.')[0]}** {Fore.LIGHTBLACK_EX}")
                self.delete_friends()
                time.sleep(1)
                console.simple_log(f"{Fore.LIGHTGREEN_EX}FINISHED REMOVING BLOCKS {Fore.LIGHTWHITE_EX}-> **{self.bot_token.split('.')[0]}** {Fore.LIGHTBLACK_EX}")
                self.delete_all_dms()
                time.sleep(1)
                console.simple_log(f"{Fore.LIGHTGREEN_EX}FINISHED REMOVING DMs {Fore.LIGHTWHITE_EX}-> **{self.bot_token.split('.')[0]}** {Fore.LIGHTBLACK_EX}")
                self.delete_all_guilds()
                console.simple_log(f"{Fore.LIGHTGREEN_EX}FINISHED CLEANER {Fore.LIGHTWHITE_EX}-> **{self.bot_token.split('.')[0]}** {Fore.LIGHTBLACK_EX}")
        try:
            TokenCleaner(bot_token).start()
        except Exception as e:
            console.simple_log(f"{Fore.RED}ERROR {Fore.LIGHTWHITE_EX}-> **{bot_token.split('.')[0]}** {Fore.LIGHTBLACK_EX}{e}")

    def boost(guild_id, bot_token):
        session, headers, cookie = utility.get_client(bot_token)

        def boostServer(guildID, sub_ids):
            for i in range(len(sub_ids)):
                headers["Content-Type"] = "application/json"
                r = session.put(
                    url=f"https://discord.com/api/v9/guilds/{guildID}/premium/subscriptions",
                    headers=headers,
                    cookies=cookie,
                    json={
                        "user_premium_guild_subscription_slot_ids": [f"{sub_ids[i]}"]
                    },
                )
                if r.status_code == 201:
                    data = {
                        "success": True,
                        "message": "Successfully boosted server.",
                    }
                elif r.status_code == 400:
                    data = {
                        "success": False,
                        "message": "You already boosted this server.",
                    }
                else:
                    data = {
                        "success": False,
                        "message": utility.short_string(r.text),
                    }
            return data

        has_nitro, sub_ids = utility.has_nitro(bot_token, session, headers, cookie)
        if has_nitro and sub_ids is not None:
            bost = boostServer(guild_id, sub_ids)
            if bost.get("success", False):
                console.log(bot_token, action="boosted", action_clr="green")
            else:
                console.log(bot_token, action="failed", action_clr="red")
        else:
            console.log(bot_token, action="no nitro", action_clr="red")

    def onboard_bypass(board_info: OnboardingInfo, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"
        headers["referer"] = f"https://discord.com/channels/{board_info.guild_id}/onboarding"
        post_data = {
            "onboarding_prompts_seen": board_info.onboarding_prompts_seen,
            "onboarding_responses": board_info.onboarding_responses,
            "onboarding_responses_seen": board_info.onboarding_responses_seen,
            "update_roles_and_channels": True,
        }
        r = session.post(
            url=f"https://discord.com/api/v9/guilds/{board_info.guild_id}/onboarding-responses",
            headers=headers,
            cookies=cookie,
            json=post_data,
        )
        if not r.status_code == 200:
            console.log(bot_token, action="FAILED", action_clr="red")
        data = r.json()
        if "guild_id" in data:
            console.log(bot_token, action="SUCCESS", action_clr="green")
        
        
        

    def change_pfp(encoded_strings, bot_token):
        threading.Thread(target=run.online, args=[False, bot_token]).start()
        time.sleep(1)
        encoded_string = random.choice(encoded_strings)
        session, headers, cookie = utility.get_client(bot_token)
        headers["content-type"] = "application/json"

        req = session.patch(
            "https://discord.com/api/v9/users/@me",
            headers=headers,
            cookies=cookie,
            json={
                'avatar': f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
            }
        )
        if req.status_code == 200:
            console.log(bot_token, action="changed avatar", action_clr="green", thing=f"pfp: {encoded_string.decode('utf-8')[0:15]}")

        else:
            console.log(bot_token, action="failed", action_clr="red")

    def restorecord_bypass(guild_id, bot_id, custom_redirect = None, bot_token = None):
        session, headers, cookie = utility.get_client(bot_token)
        querystring = {
            "client_id":str(bot_id),
            "response_type":"code",
            "redirect_uri":custom_redirect,
            "scope":"identify guilds.join",
            "state":str(guild_id)
        }
        request = session.post(
                        f"https://discord.com/api/v9/oauth2/authorize",
                        headers=headers,
                        cookies=cookie,
                        params=querystring,
                        json={"permissions":"0","authorize":True}
                    )
        if "location" in request.text:
            answer = request.json()["location"]
            result = session.get(answer, headers=headers, cookies=cookie, allow_redirects=True)
            if result.status_code in [307, 403]:
                console.simple_log(f"{Fore.LIGHTGREEN_EX}Bypassed: {Fore.BLUE}{bot_token.split('.')[0]}")
            else:
                console.log_error(f"{Fore.RED}Failed: {Fore.BLUE}{bot_token.split('.')[0]} {Fore.LIGHTBLACK_EX}({result.status_code})")
        else:
            console.log_error(f"{Fore.RED}Failed to request discord: {Fore.BLUE}{bot_token.split('.')[0]} {Fore.LIGHTBLACK_EX}({request.text})")

    def bypass_captcha_bot(bot_id, msg_info, button, bot_token):
        session, headers, cookie = utility.get_client(bot_token)
        
        def oauth():
            request = session.post(
                    f"https://discord.com/api/v9/oauth2/authorize",
                    headers=headers,
                    cookies=cookie,
                    params={
                        "client_id": "512333785338216465",
                        "response_type":"code",
                        "redirect_uri": "https://captcha.bot/callback",
                        "scope":"identify guilds guilds.members.read role_connections.write",
                    },
                    json={"permissions":"0","authorize":True}
                )
            return request.json()["location"].split("?code=")[1]
        
        t = GetEphemeralEmbed(bot_token, bot_id)
        thread =threading.Thread(target=t.run)
        thread.start()
        
        guild_id = str(msg_info["guild_id"])
        channel_id = str(msg_info["channel_id"])
        message_id = str(msg_info["message_id"])
        run.click_button(guild_id, channel_id, message_id, button["custom_id"], button["application_id"], 1, bot_token)
        while not t.open:
            print("waiting for embed")
            time.sleep(0.1)
        print("embed opened")

        
        

        thread.join()
        link = t.message.description.split("verify](")[1].replace(")", "")
        link = link.replace("https://captcha.bot/verify/guild/", "")
        
        captcha_hash = link.split("/")[1]
        oauth_code = oauth()
        try:
            client = tls_client.Session(
                client_identifier="chrome_107",
                ja3_string="772,4866-4867-4865-49196-49200-159-52393-52392-52394-49195-49199-158-49188-49192-107-49187-49191-103-49162-49172-57-49161-49171-51-157-156-61-60-53-47-255,0-11-10-13172-16-22-23-49-13-43-45-51,29-23-30-25-24-256-257-258-259-260,0-1-2"
            )
            client.proxies = session.proxies
                                                                                                #TODO IGNORE THIS SHIT CODE, NORMAL utils.get_client() DIDNT WORK AT ALL
            headers = {                                                                         #TODO IGNORE THIS SHIT CODE, NORMAL utils.get_client() DIDNT WORK AT ALL
                "Host": "captcha.bot",
                "User-Agent": DiscordInfo.user_agent,
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Authorization": "null",
                "Origin": "https://captcha.bot",
                "Connection": "keep-alive",
                "Referer": f"https://captcha.bot/callback?code={oauth_code}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers"
            }
            client.headers = headers
            request = client.post("https://captcha.bot/api/v1/oauth/callback", data="", headers=headers, params={"code":f"{oauth_code}"})
            auth_token = request.json()["token"]
            headers["Authorization"] = auth_token
            headers["Referer"] = f"https://captcha.bot/verify/guild/{guild_id}/{captcha_hash}"
            
            console.simple_log(f"{Fore.LIGHTCYAN_EX}{bot_token.split('.')[0]}{Fore.LIGHTWHITE_EX} - Solving captcha {Fore.YELLOW}")
            captcha = utility.solve_cap(config.get_captcha_type(), "8223d1d4-b37a-46cc-b0e6-f9bf43658d5d", "https://captcha.bot")
            
            data = {
                "token": captcha,
                "hash": captcha_hash,
                "guildID": str(guild_id),
            }
                        
            request = client.post("https://captcha.bot/api/v1/captcha/verify", json=data, headers=headers)
            if request.status_code == 200:
                if request.json()["status"] == "ACKNOWLEDGED":
                    return console.simple_log(f"{Fore.LIGHTGREEN_EX}BYPASSED CAPTCHA BOT: {Fore.BLUE}{bot_token.split('.')[0]}")
                elif request.json()["status"] == "TRY_AGAIN":
                    console.log_error(f"{Fore.RED}Trying again: {Fore.BLUE}{bot_token.split('.')[0]} {Fore.LIGHTBLACK_EX}({request.json()}")
                    run.bypass_captcha_bot(bot_id, msg_info, button, bot_token)
                else:
                    console.log_error(f"{Fore.RED}Status not acknowleged: {Fore.BLUE}{bot_token.split('.')[0]} {Fore.LIGHTBLACK_EX}({request.json()}")
            else:
                console.log_error(f"{Fore.RED}Failed to solve captcha: {Fore.BLUE}{bot_token.split('.')[0]} {Fore.LIGHTBLACK_EX}({request.json()}")

            
            
            
        except Exception as e:
            print(e)
            console.log_error(f"{Fore.RED}Failed to solve captcha: {Fore.BLUE}{bot_token.split('.')[0]}")
    
    def bypass_wick(bot_id, msg_info, button, bot_token):  
        try:      
            t = GetEphemeralEmbed(bot_token, bot_id)
            thread = threading.Thread(target=t.run)
            thread.start()
            
            guild_id = str(msg_info["guild_id"])
            channel_id = str(msg_info["channel_id"])
            message_id = str(msg_info["message_id"])
            run.click_button(guild_id, channel_id, message_id, button["custom_id"], button["application_id"], 1, bot_token)
            i = 0
            while not t.open and i < 100:
                time.sleep(0.1)
                i += 1
            if not t.open:
                t.close()
                console.log_error(f"{Fore.RED}Failed to open embed: {Fore.BLUE}{bot_token.split('.')[0]}")
                return
            
            message = t.message
            embed = message.get("embeds")[0]
            
            if "image" not in embed:
                console.simple_log(f"{Fore.LIGHTCYAN_EX}{bot_token.split('.')[0]}{Fore.LIGHTWHITE_EX} - Already being verified, sleeping for 30 seconds {Fore.YELLOW}")
                time.sleep(30)
                return run.bypass_wick(bot_id, msg_info, button, bot_token)
            
            image = embed["image"]["url"]
            button_id = message["components"][0]["components"][0]["custom_id"]
            def ocr(image_url) -> typing.Union[bool, str]:
                resp = httpx.get(f"https://yiffing.zone/api/solve?captcha={image_url}").json()
                if resp["success"]:
                    return resp["solve"]
                httpx.post(f"https://yiffing.zone/api/captcha/wrongSolve?captcha={image_url}")
                return False
            
            captcha = ocr(image)
            if not captcha:
                console.log_error(f"{Fore.RED}Failed to solve captcha: {Fore.BLUE}{bot_token.split('.')[0]}")
                return

            t = GetEphemeralEmbed(bot_token, bot_id)
            thread = threading.Thread(target=t.run)
            thread.start()
            
            run.click_button(guild_id, channel_id, message.get("id"), button_id, button["application_id"], 1, bot_token, 64)
            while not t.create_id:
                time.sleep(0.1)
            create_id = t.create_id
            modal_id = button_id.split("_")[2]
            modal_veri_id = f"modalmmbrver_{modal_id}"

            
            def do_modal(guild_id, channel_id, create_id, custom_id, bot_token = None):
                try:
                    session, headers, cookie = utility.get_client(bot_token)
                    post_data = {
                        "type":5,
                        "application_id":str(button["application_id"]),
                        "channel_id":str(channel_id),
                        "guild_id":str(guild_id),
                        "data":{
                            "id": create_id,
                            "custom_id":custom_id,
                            "components":[
                                {
                                    "type":1,
                                    "components":[
                                    {
                                        "type":4,
                                        "custom_id":"answer",
                                        "value":str(captcha).upper(),
                                    }
                                    ]
                                }
                            ]
                        },
                        "session_id":str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
                        "nonce": str(Decimal(time.time() * 1000 - 1420070400000) * 4194304).split(".")[0]
                    }
                    headers.update({"content-type": "application/json"})
                    headers.update({"referer": f"https://discord.com/channels/{guild_id}/{channel_id}"}) # discord checks referer now xd
                    req = session.post(f"https://discord.com/api/v9/interactions", headers=headers, cookies=cookie, json=post_data)
                    if req.status_code == 204:
                        status = f"{Fore.LIGHTGREEN_EX}Submitted modal"
                    else:
                        status = f"{Fore.RED}Couldn't submit modal {req.status_code}"
                        
                    console.simple_log(
                        f"{Fore.LIGHTCYAN_EX}{bot_token.split('.')[0]}{Fore.LIGHTWHITE_EX} - {status} {Fore.YELLOW}")
                    return "Couldn't" not in status
                except Exception as e:
                    console.simple_log(
                        f"{Fore.RED}FAILED{Fore.LIGHTWHITE_EX} - {Fore.BLUE}{e} {Fore.LIGHTWHITE_EX}[**{bot_token.split('.')[0]}**]")
                    return False
            if do_modal(guild_id, channel_id, create_id, modal_veri_id, bot_token):
                console.simple_log(f"{Fore.LIGHTCYAN_EX}{bot_token.split('.')[0]}{Fore.LIGHTWHITE_EX} - {Fore.LIGHTGREEN_EX}Successfully bypassed wick {Fore.YELLOW}")
            else:
                console.simple_log(f"{Fore.LIGHTCYAN_EX}{bot_token.split('.')[0]}{Fore.LIGHTWHITE_EX} - {Fore.RED}Failed to bypass wick {Fore.YELLOW}")
            
        except Exception as e:
            print(e)
            time.sleep(300)
            console.log_error(f"{Fore.RED}Failed to bypass wick: {Fore.BLUE}{bot_token.split('.')[0]}")
            
    def soundboard_spam(guild_id, channel_id, sounds: list[dict[str, typing.Union[str, int]]], bot_token):
        session, default_headers, cookie=utility.get_client(bot_token)
        threading.Thread(target=run.connect_vc, args=(guild_id, channel_id, bot_token)).start()
        while True:
            sound = random.choice(sounds)
            data = {
                "sound_id":sound.get("sound_id"),
                "emoji_id":None,
                "emoji_name":sound.get("emoji_name"),
                "override_path": sound.get("override_path")
            }
            req = session.post(f"https://discord.com/api/v9/channels/{channel_id}/voice-channel-effects", headers=default_headers, cookies=cookie, json=data) 
            if req.status_code == 204:
                console.simple_log(f"{Fore.LIGHTCYAN_EX}{bot_token.split('.')[0]}{Fore.LIGHTWHITE_EX} - {Fore.LIGHTGREEN_EX}Successfully played sound {Fore.YELLOW}{sound.get('emoji_name')}")
            else:
                console.simple_log(f"{Fore.LIGHTCYAN_EX}{bot_token.split('.')[0]}{Fore.LIGHTWHITE_EX} - {Fore.RED}Failed to play sound {Fore.YELLOW}{sound.get('emoji_name')}")
            time.sleep(0.3 + random.random() * 0.3)

    
    def report(channel_id, message_id, amount_for_token, bot_token):
        try:
            session, default_headers, cookie=utility.get_client(bot_token)
            reasons={
                31: "MESSAGE_SPAM",
                11: "ABUSE_OR_HARASSMENT",
                34: "MESSAGE_VERBAL_HARASSMENT",
                35: "MESSAGE_VULGAR_LANG",
                39: "MESSAGE_HATE_IDENTITY",
                19: "NSFW_UNWANTED",
                40: "MESSAGE_GORE",
                41: "MESSAGE_NSFW_UNWANTED",
                42: "MESSAGE_NSFW_DEGRADING",
                43: "MESSAGE_REVENGE_NCP",
                21: "NSFW_MINOR",
                44: "MESSAGE_LOLI",
                45: "MESSAGE_SEXUALIZING_MINOR",
                46: "MESSAGE_ICWM",
                47: "MESSAGE_ICAAM",
                48: "MESSAGE_CSAM",
                23: "THREAT_IRL",
                49: "MESSAGE_THREAT_IRL",
                50: "MESSAGE_GLORIFY_VIOLENCE",
                14: "SOMETHING_ELSE",
                52: "MESSAGE_FRAUD",
                54: "MESSAGE_ATO",
                55: "MESSAGE_ILLICIT_GOODS",
                57: "MESSAGE_HACKS_CHEATS",
                24: "UNDERAGE_USER",
                58: "MESSAGE_UNDERAGE_CONFIRM",
                10: "UNDERAGE_NEEDS_MORE_INFO",
                26: "SELF_HARM",
                65: "MESSAGE_SELF_HARM_RISK",
                59: "MESSAGE_SELF_HARM_ENCOURAGE",
                27: "EVASION_RAID",
                60: "MESSAGE_RAID_THREAT",
                61: "MESSAGE_ACTIVE_RAID",
                62: "MESSAGE_SERVER_BAN_EVASION",
                63: "MESSAGE_USER_BAN_EVASION",
                28: "MISINFO_EXTREMISM",
                29: "SPREADING_MISINFO",
                64: "MESSAGE_HARMFUL_MISINFO",
                68: "SELF_HARM_INTERSTITIAL",
            }
            for x in range(int(amount_for_token)):
                reason=random.choice(list(reasons.keys()))
                report = session.post("https://discord.com/api/v9/reporting/message",headers=default_headers, cookies=cookie, json={
                    "version": "1.0",
                    "variant": "3",
                    "language": "en",
                    "breadcrumbs": [
                        3,#Report Message
                        reason
                    ],
                    "elements": {},
                    "name": "message",
                    "channel_id": channel_id,
                    "message_id": message_id
                })

                if report.status_code==200:
                    console.log(bot_token, action="reported", action_clr="green", thing=reasons[reason].lower().replace('_', ' ').title())

                elif report.status_code==429:
                    console.log(bot_token, action="ratelimited", action_clr="yellow", thing="Very sad")
                    time.sleep(5) 
                
                else:
                    console.log(bot_token, action="failed", action_clr="red", thing=report.json()["message"])

        except Exception as e:
            print(e)

class selection():
    def dm_spammer():
        user_id = utility.option(msg="user id")
        message = utility.option(msg="message")

        utility.start_threads(func=run.dm_thread, delay=0, args=[user_id, message])

    def mass_report():
        msg_info = utility.get_message_info()
        channel_id = msg_info["channel_id"]
        message_id = msg_info["message_id"]

        report_amount = utility.option(msg="report amount")
        if report_amount == "":
            report_amount = 1
        tokens_amount = len(utility.get_tokens())
        amount_for_token = int(round(int(report_amount)/tokens_amount))
        if amount_for_token == 0:
            amount_for_token = 1

        utility.start_threads(func=run.report, delay=0, args=[channel_id, message_id, amount_for_token])

    def call_spam():
        user_id = utility.option(msg="user id")
        utility.start_threads(func=run.call_thread, args=[user_id])

    def server_joiner():
        channel_id="";message="";join_channel_id="";guild_id=""

        bypass_rules = utility.option(msg="bypass rules (y/n)")
        if bypass_rules=="y":
            guild_id = utility.option(msg="guild id")

        silent = utility.option(msg="silent (y/n)")
        if silent=="y":
            join_channel_id = utility.option(msg="join channel id")

        auto_spam = utility.option(msg="auto spam (y/n)")
        if auto_spam=="y":
            message = utility.option(msg="message", extra="(<down> for next line)").replace("<down>","\n")
            if message == "":
                visual.main_screen()
            channel_id = utility.option(msg="channel id")
            

        invite = utility.option(msg="invite")
        if invite == "":
            visual.main_screen()
        if invite.__contains__('discord.gg/'):
            invite = invite.replace('discord.gg/', '').replace('https://', '').replace('http://', '')
        elif invite.__contains__('discord.com/invite/'):
            invite = invite.replace('discord.com/invite/', '').replace('https://', '').replace('http://', '')
        try:
            invite = invite.split(".gg/")[1]
        except:
            pass#Fire code
        
        
        delay = utility.option(msg="delay")
        if delay == "":
            delay = 0
        if isinstance(delay, str) and not delay.isdigit() and not "." in delay:
            console.simple_log(f"{Fore.RED}FAILED{Fore.WHITE} {Fore.LIGHTBLACK_EX}(Delay must be a number)")
            time.sleep(3)
            visual.main_screen()
        delay = float(delay)
            
       
        console.simple_log(f"Getting guild info...")
        guild = utility.get_guild_info(invite)
        if guild is not None:
            xcontent=utility.x_content_props(guild)
            console.simple_log(f"Joining {Fore.WHITE}{guild['guild']['name']}")
            time.sleep(1)
        else:
            xcontent = "eyJsb2NhdGlvbiI6IkFjY2VwdCBJbnZpdGUgUGFnZSJ9"
            
        utility.start_threads(func=run.join, delay=float(delay), do_return=False,args=[invite,message,channel_id,silent,join_channel_id,bypass_rules,guild_id,xcontent])


    def mass_friender():
        
        friend_funcs = {
            "add user": run.friend_user,
            "remove user": run.unfriend_user
        }
        
        for i in range(len(friend_funcs)):
            console.simple_log(f"{Fore.LIGHTWHITE_EX}[{i+1}] {list(friend_funcs.keys())[i].title()}")

        option = utility.option(msg="option")
        if option == "":
            visual.main_screen()
        if not option.isdigit() or int(option) > len(friend_funcs):
            console.simple_log(f"{Fore.RED}FAILED{Fore.WHITE} {Fore.LIGHTBLACK_EX}(Invalid option)")
            time.sleep(3)
            visual.main_screen()
        
        option = list(friend_funcs.keys())[int(option)-1]
        
        if option == "add user":
            username = utility.option(msg="username (user#1234)")
            if username == "":
                visual.main_screen()
        
        elif option == "remove user":
            user_id = utility.option(msg="user id")
            if user_id == "":
                visual.main_screen()
            
        

        utility.start_threads(func=friend_funcs[option], args=[username if option == "add user" else user_id])

    def server_leaver():
        guild_id = utility.option(msg="guild id")
        utility.start_threads(func=run.leave, args=[guild_id])

    def ruler():
        guild_id = utility.option(msg="guild id")
        utility.start_threads(func=run.accept_rule, args=[guild_id])

    def spammer():
            
            
        options: SpammerOptions = SpammerOptions()
        use_previous = False
        
        if os.path.exists("C:/Windows/Temp/spammer_config.json"):
            use_previous = utility.option(msg="use previous spammer config (y/n)").lower() == "y"

        if not use_previous:
            options.massping = utility.option(msg="massping (y/n)").lower() == "y"
            options.multi_message = utility.option(msg="multi message (y/n)", extra=" (data/messages.txt)").lower() == "y"
            if not options.multi_message:
                options.messages = utility.option(msg="message", extra="(<down> for next line)").replace("<down>","\n")
                if options.messages == "":
                    visual.main_screen()
                if isinstance(options.messages, str):
                    options.messages = [options.messages]
                    
            else:
                with open("data/messages.txt", "r", encoding = "utf-8") as f:
                    options.messages = f.read().splitlines()
                if isinstance(options.messages, str):
                    options.messages = [options.messages]
            
            options.crypt_message = utility.option(msg="crypt message (y/n)", extra = " (1337 speak)").lower() == "y"
            options.emoji_message = utility.option(msg="emoji mode (y/n)", extra = " (can freeze ur discord)").lower() == "y"
            
            options.channel_ids = utility.option(msg="channel id(s) (seperate with commas)").strip().replace(" ", "").replace("\n", "").split(',')
            
            if options.channel_ids == "":
               visual.main_screen()
            
            if isinstance(options.channel_ids, str):
               options.channel_ids = [options.channel_ids]    
            
            
            options.massping_users = []

            if options.massping:
                options.guild_id = utility.option(msg="guild id")
                if os.path.exists(f"scraped/{options.guild_id}.txt"):
                    if utility.option(f"use scraped (y/n)", extra=f" ({len(open(f'scraped/{options.guild_id}.txt').read().strip().splitlines())} users)").lower() == "y":
                        with open(f"scraped/{options.guild_id}.txt", "r") as f:
                            options.massping_users = f.read().strip().split("\n")
                if options.massping_users == []:
                    tokens = utility.get_tokens()
                    token = random.choice(tokens)
                    console.simple_log(f"{Fore.LIGHTWHITE_EX}Scraping users (this may take a while)...")
                    options.massping_users = utility.scrape_members(token, options.guild_id, random.choice(options.channel_ids))
                    console.simple_log(f"{Fore.LIGHTWHITE_EX}Found {Fore.LIGHTGREEN_EX}{len(options.massping_users)}{Fore.LIGHTWHITE_EX} users in channel (press enter to continue)")
                    with open(f"scraped/{options.guild_id}.txt","a+") as b:
                        for user in options.massping_users:
                            b.write(user+"\n")
                options.ping_amount = utility.option(msg="pings per message")
                if options.ping_amount == "":
                    visual.main_screen()
                elif not options.ping_amount.isdigit():
                    console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid input, defaulting to 3 ping per message")
                    options.ping_amount = 3
                

                options.invisible_pings = utility.option(msg="invisible pings (y/n)").lower() == "y"
                if options.invisible_pings == "":
                    visual.main_screen()
            
                


            options.msg_amount = utility.option(msg="amount (leave blank for inf)")
            if options.msg_amount == "":
                options.msg_amount = 999_999_999

            options.delay = utility.option(msg="delay")
            if options.delay == "": 
                options.delay = 0
                
            try:
                options.delay = float(options.delay)
            except ValueError:
                console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid input, defaulting to 0 delay")
                options.delay = 0

            visual.main_title()
            
            options.massping_iter = cycle(options.massping_users)
            with open("C:/Windows/Temp/spammer_config.json","w+") as b:
                b.write(json.dumps({
                        "massping": options.massping,
                        "channel_ids": options.channel_ids,
                        "guild_id": options.guild_id,
                        "msg_amount": options.msg_amount,
                        "pings_per_message": options.ping_amount,
                        "delay": options.delay,
                        "invisible_pings": options.invisible_pings,
                        "crypt_message": options.crypt_message,
                        "messages": options.messages,
                    }, indent=4))

        elif use_previous:
            with open("C:/Windows/Temp/spammer_config.json", "r") as f:
                settings = jsond.load(f)
            
            options.massping = settings["massping"]
            options.channel_ids = settings["channel_ids"]
            options.invisible_pings = settings["invisible_pings"]
            options.crypt_message = settings["crypt_message"]
            options.messages = settings["messages"]
            options.guild_id = settings["guild_id"]
            
            
            options.massping_users = []
            if options.massping:
                if os.path.exists(f"scraped/{options.guild_id}.txt"):
                    if utility.option(f"use scraped (y/n)", extra=f" ({len(open(f'scraped/{options.guild_id}.txt').read().strip().splitlines())} users)").lower() == "y":
                        with open(f"scraped/{options.guild_id}.txt", "r") as f:
                            options.massping_users = f.read().splitlines()
                if options.massping_users == []:
                    console.simple_log(f"{Fore.LIGHTWHITE_EX}Scraping users (this may take a while)...")
                    options.massping_users = utility.scrape_members(token, options.guild_id, random.choice(options.channel_ids))
                    console.simple_log(f"{Fore.LIGHTWHITE_EX}Found {Fore.LIGHTGREEN_EX}{len(options.massping_users)}{Fore.LIGHTWHITE_EX} users in channel (press enter to continue)")

                    with open(f"scraped/{options.guild_id}.txt","a+") as b:
                        for user in options.massping_users:
                            b.write(user+"\n")

            options.ping_amount = settings["pings_per_message"]
            options.msg_amount = settings["msg_amount"]
            options.delay = settings["delay"]

            visual.main_title()
            options.massping_iter = cycle(options.massping_users)
        
        tokens = utility.get_tokens()
        
        token = random.choice(tokens)
        console.simple_log(f"{Fore.LIGHTWHITE_EX}Checking if random token has access to channel{'s' if len(options.channel_ids) > 1 else ''}")
        for channel_id in options.channel_ids:
            if not utility.has_access_to_channel(token, channel_id):
                console.simple_log(f"{Fore.RED}token does not have access to {channel_id} {Fore.LIGHTBLACK_EX}(removing)")
                options.channel_ids.remove(channel_id)
                
        if options.channel_ids == []:
            console.simple_log(f"{Fore.RED}No valid channels")
            time.sleep(3)
            visual.main_screen()    

        
        max_threads = utility.option(msg=f"Max Threads", extra=f" (1-{len(tokens)})")
        # float or int
        if max_threads.isdigit():
            max_threads = int(max_threads)
        else:
            max_threads = ""
        
        if max_threads == "":
            max_threads = len(tokens)
        
        if max_threads > len(tokens):
            max_threads = len(tokens)
        
        try:
            threads = []
            for channel_id in options.channel_ids:
                print(f"{Fore.LIGHTWHITE_EX}Starting {Fore.LIGHTGREEN_EX}{max_threads}{Fore.LIGHTWHITE_EX} threads for {Fore.LIGHTGREEN_EX}{channel_id}")
                t = threading.Thread(target=utility.start_threads, args=[run.send_message, [options], float(options.delay), "", int(max_threads), False, ])
                threads.append(t)
                t.start()
            for thread in threads:
                thread.join()
            input(f"\n{' ' * 34}Spammer Finished, Press enter to continue\n")
            visual.main_screen()
        except Exception as e:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")
            time.sleep(3)
            visual.main_screen()
        
    def threader():
        message = utility.option(msg="message")
        if message == "":
            visual.main_screen()
        title = utility.option(msg="title")
        if title == "":
            visual.main_screen()
        delay = utility.option(msg="delay")
        channel_id = utility.option(msg="channel id")
        amount = utility.option(msg="amount")
        if not amount.isdigit():
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid input, defaulting to 5 loops")
            amount = 5

        visual.main_title()
        utility.start_threads(func=run.make_thread, args=[channel_id, message, title, amount], delay=float(delay))


    def webhooker():
        message = utility.option(msg="message")
        webhook = utility.option(msg="webhook")
        msg_amount = utility.option(msg="amount")

        visual.main_title()

        run.send_webhook_message(message, webhook, msg_amount)
        input()
        visual.main_screen()
    
    def ticket_spammer():
        msg = utility.get_message_info()
        if msg is None:
            visual.main_screen()
        guild_id = msg["guild_id"]
        ticket_channel_id = msg["channel_id"]
        utility.start_threads(func=run.spam_ticket, do_return=False,args=[guild_id, ticket_channel_id])

    def reactor():
        automatic = utility.option(msg="automatic (y/n)").lower()
        msg = utility.get_message_info()
        if msg is None:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid message link")
            time.sleep(3)
            visual.main_screen()
        channel_id = msg["channel_id"]
        message_id = msg["message_id"]


        if automatic=="y":
            emojis = utility.get_message_reactions(channel_id, message_id)
            if emojis == None:
                console.simple_log(f"{Fore.RED}Invalid message id (press enter to continue)")
                input()
                visual.main_screen()

            for num, emoji in enumerate(emojis):
                console.simple_log(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}{num}{Fore.LIGHTWHITE_EX}] Emoji: {Fore.LIGHTGREEN_EX}{emoji['name'].replace(' ', '')} {'[CUSTOM]' if emoji['custom'] else ''}   {Fore.LIGHTWHITE_EX}Reaction count: {Fore.LIGHTGREEN_EX}{emoji['count']}")

            emojinum = utility.option(msg="emoji number")
            for emoji in emojis:
                if emojis.index(emoji)==int(emojinum):
                    emoji = emoji['name'].replace(" ", "")
                    break

        else:
            option = utility.option(msg="normal/custom").lower()
            if option=="normal": emoji= utility.option(msg="emoji")
            elif option=="custom": emoji = utility.option(msg="emojiname:id")

        utility.start_threads(func=run.react,args=[emoji.replace(":", "%3A"), message_id, channel_id])

    def server_checker():
        global tokens
        tokens = utility.get_tokens()
        tkns = []
        guild_id = utility.option(msg="guild id")
        def check_server(guild_id, bot_token):
            session, headers, cookie = utility.get_client(bot_token)

            req = session.get(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers, cookies=cookie)

            if req.status_code == 200:
                status = Fore.LIGHTGREEN_EX + "True"
            else:
                status = Fore.RED + "False " + Fore.LIGHTBLACK_EX + "(removing)"
                tkns.remove(bot_token)

            console.log(bot_token, action="SERVER", action_clr="magenta",thing=f"{Fore.CYAN}IN SERVER: {status}{Fore.LIGHTBLACK_EX}")

        max_threads = utility.option(msg="Max Threads", extra=f" (1-{len(tokens)})")
        try:
            max_threads = int(max_threads)
        except:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid input, defaulting to 50 threads")
            max_threads = len(tokens)
        if max_threads == "":
            max_threads = len(tokens)
        
        if max_threads > len(tokens):
            max_threads = len(tokens)
        visual.main_title()
        if len(tokens) > 0:
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                args = [guild_id]
                for bot_token in tokens:
                    try:
                        if bot_token in ["", " ", "\n"]:
                            continue
                        bot_token = utility.extract(bot_token)
                        tkns.append(bot_token)
                        args.append(bot_token)
                        executor.submit(check_server, *args)
                        args.remove(bot_token)
                    except Exception as e:
                        console.log_error(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")
    
            name = " ".join([name.capitalize() for name in check_server.__name__.split('_')])
            with open("data/tokens.txt", "w") as f:
                for token in tkns:
                    f.write(f"{token}\n")
            input(f"\n{' ' * 34}{name} Finished, Press enter to continue\n")
            visual.main_screen()

        else:
            console.simple_log(f"{Fore.LIGHTWHITE_EX}No tokens in '{Fore.YELLOW}data/tokens.txt{Fore.LIGHTWHITE_EX}'")
            input()
            visual.main_screen()

    def button_presser():
        msg = utility.get_message_info()
        if msg is None:
            visual.main_screen()
        guild_id = msg["guild_id"]
        channel_id = msg["channel_id"]
        message_id = msg["message_id"]

        buttons = utility.get_message_buttons(
            bot_token=random.choice(utility.get_tokens()),
            guild_id=guild_id,
            channel_id=channel_id,
            message_id=message_id
        )
        
        if buttons == None:
            console.simple_log(f"{Fore.RED}Invalid message id [or message has no buttons] (press enter to continue)")
            input()
            visual.main_screen()

        for num, button in enumerate(buttons):
            console.simple_log(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}{num}{Fore.LIGHTWHITE_EX}] Button label: {Fore.LIGHTGREEN_EX}{button['label'].replace(' ', '') if button['label'] != None else 'None'}")

        buttonum = utility.option(msg="button number")
        for button in buttons:
            if buttons.index(button)==int(buttonum):
                custom_id = button['custom_id']
                application_id = button['application_id']
                break
                
        amount = utility.option(msg="amount", extra=" (leave blank for infinite)")
        if amount == "":
            amount = 999999999
            
        elif not amount.isdigit():
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid input, defaulting to infinite")
            amount = 999999999
        
        amount = int(amount)
        
        utility.start_threads(func=run.click_button, args=[guild_id, channel_id, message_id, custom_id, application_id, amount])

    def formater():
        tokens = utility.get_tokens()
        formated_tokens = []

        if len(tokens) > 0:
            for bot_token in tokens:
                tk = utility.extract(bot_token)
                formated_tokens.append(tk)
                console.simple_log(f"{Fore.LIGHTGREEN_EX}FORMATED TOKEN: {Fore.LIGHTWHITE_EX}{tk.split('.')[0]}")

            open("data/tokens.txt", "w").close()
            with open("data/tokens.txt", "a") as b:
                for formated_token in formated_tokens:
                    b.write(formated_token + "\n")
            print(f"\n{' ' * 34}Formating Finished, Press enter to continue\n")
            input()
            visual.main_screen()

        else:
            console.simple_log(f"{Fore.LIGHTWHITE_EX}No tokens in '{Fore.YELLOW}data/tokens.txt{Fore.LIGHTWHITE_EX}'")
            input()
            visual.main_screen()

    def nicker():
        guild_id = utility.option(msg="guild id")
        nick_name = utility.option(msg="nick")

        utility.start_threads(func=run.nick_bot, args=[guild_id, nick_name])

    def change_bio():
        bio = utility.option(msg="bio")

        utility.start_threads(func=run.change_bio, args=[bio])

    def hypesquad():
        hypesquads = {
            "1": "bravery",
            "2": "brilliance",
            "3": "balance"
        }
        for hypesquad in hypesquads:
            console.simple_log(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}{hypesquad}{Fore.LIGHTWHITE_EX}] {hypesquads[hypesquad]}")
        hypesquad_id = utility.option(msg="hypesquad type")
        utility.start_threads(func=run.join_hypesquad, args=[hypesquad_id])

    def voice_chat():
        
        vc_funcs = {
            "join and leave": run.spam_vc,
            "join and stay": run.connect_vc
        }
        for i in range(len(vc_funcs)):
            console.simple_log(f"{Fore.LIGHTWHITE_EX}[{i+1}] {list(vc_funcs.keys())[i].title()}")
        
        selected_option  = utility.option(msg="option")
        if selected_option  == "":
            visual.main_screen()
        if not selected_option .isdigit() or int(selected_option ) > len(vc_funcs):
            console.simple_log(f"{Fore.RED}FAILED{Fore.WHITE} {Fore.LIGHTBLACK_EX}(Invalid option)")
            time.sleep(3)
            visual.main_screen()
        
        option_index = int(selected_option) - 1
        selected_function = list(vc_funcs.values())[option_index]
        
        guild_id = utility.option(msg="guild id")
        if not guild_id.isdigit():
            console.simple_log(f"{Fore.RED}Invalid guild id (press enter to continue)")
            input()
            visual.main_screen()
        voice_id = utility.option(msg="voice id")
        if not voice_id.isdigit():
            console.simple_log(f"{Fore.RED}Invalid voice id (press enter to continue)")
            input()
            visual.main_screen()
        utility.start_threads(func=selected_function, args=[guild_id, voice_id])
    
    def mass_forum():

        message = utility.option(msg="message (blank for random message)")
        if message == "":
            message = "RANDOM"
        title = utility.option(msg="title (blank for random title)")
        if title == "":
            title = "RANDOM"
        delay = utility.option(msg="delay")
        amount = utility.option(msg="amount")
        channel_id = utility.option(msg="channel id")

        visual.main_title()
        tags = utility.get_forum_tags(random.choice(utility.get_tokens()), channel_id)
        utility.start_threads(func=run.make_forum_post, args=[channel_id, "RANDOM" if message == "RANDOM" else message, "RANDOM" if title == "RANDOM" else title, tags, int(amount)], delay=float(delay))

    def mp3_player():
        path = f"ffmpeg.exe"
        if not os.path.exists(path):
            console.simple_log(f"{Fore.RED}ffmpeg not found, downloading it now")
            path = utility.download_ffmpeg()
            console.simple_log(f"{Fore.LIGHTGREEN_EX}ffmpeg downloaded")
        channel_id = utility.option(msg="channel_id")
        if not os.path.exists("data/songs"):
            console.simple_log(f"{Fore.RED}data/songs not found in the Dazeer folder (press enter to continue)")
            input()
            visual.main_screen()
            
        def get_biggest(path):
            max_size = 0
            max_file = ""
            for folder, subfolders, files in os.walk(path):
                
                for file in files:
                    size = os.stat(os.path.join( folder, file  )).st_size

                    if size>max_size:
                        max_size = size
                        max_file = os.path.join( folder, file  )
                        
            max_size = round(max_size / 1000000, 2)
            return max_file, max_size
        file, size = get_biggest("data/songs")
        console.simple_log(f"Get your {file} size (in MB), multiply it by how many tokens you have. ")
        console.simple_log(f"If it exceeds your Wifi speed, it will not work.")
        console.simple_log(f"Example: {size}MB * 1000 tokens = {size * 1000}MB = {(size)}GBp/s")
        amount = utility.option(msg="amount")
        if not amount.isdigit():
            console.simple_log(f"{Fore.RED}Invalid amount (press enter to continue)")
            input()
            visual.main_screen()
        amount = int(amount)
        if len(utility.get_tokens()) <= 0:
            console.simple_log(f"{Fore.RED}No tokens found (press enter to continue)")
            input()
            visual.main_screen()
        songs = os.listdir("data/songs")
        iteration = cycle(songs)
        run.vc_raper(iteration, channel_id, amount)
        
        
    def fake_typing():
        channel_id = utility.option(msg="channel id")
        type_time = utility.option(msg="time")

        utility.start_threads(func=run.type, args=[channel_id, type_time])

    def onliner():
        utility.start_threads(func=run.online, args=[True], do_return=False, extra_text=" total wanted online")
        
    def spotify_spam():
        user_id = utility.option(msg="user id")
        utility.start_threads(func=run.spotify_spam, args=[user_id])

    def checker():
        global unlocked, locked, invalid, error

        unlocked=0
        locked=0
        invalid=0
        error=0

        tokens = utility.get_tokens()
        __new_tokens = []

        def check_token(bot_token):
            global unlocked, locked, invalid, error
            session, headers, cookie = utility.get_client(bot_token)

            req = session.get(
                "https://discord.com/api/v9/users/@me/settings",
                headers=headers,
                cookies=cookie
            )

            try:
                token_part = int(
                    base64.b64decode(str(bot_token.split(".")[0] + "==").encode()).decode()) / 4194304 + 1420070400000
                a = datetime.strptime(datetime.today().strftime("%Y:%m:%d"), "%Y:%m:%d")
                b = datetime.strptime(datetime.fromtimestamp(token_part // 1000).strftime('%Y:%m:%d'), "%Y:%m:%d")
                age = a - b

                if req.status_code == 200:
                    console.log(bot_token, action="UNLOCKED", action_clr="green", thing=f"Age: {age.days}d")
                    unlocked+=1

                elif "You need to verify your account in order to perform this action." in req.text:
                    console.log(bot_token, action="LOCKED", action_clr="yellow", thing=f"Age: {age.days}d {Fore.LIGHTBLACK_EX}(removing)")
                    __new_tokens.remove(bot_token); locked+=1 

                elif "Unauthorized" in req.text:
                    console.log(bot_token, action="INVALID", action_clr="red", thing=f"Age: {age.days}d {Fore.LIGHTBLACK_EX}(removing)")
                    __new_tokens.remove(bot_token); invalid+=1

                else:
                    console.log(bot_token, action="ERROR", action_clr="blue", thing=f"Age: {age.days}d")
                    error+=1
                    
            except:
                __new_tokens.remove(bot_token) 
                
        
        visual.main_title()
        tokens = utility.get_tokens()
        max_threads = utility.option(msg=f"Max Threads", extra=f" (1-{len(tokens)})")
        try:
            max_threads = int(max_threads)
        except:
            pass
        if max_threads == "":
            max_threads = len(tokens)
        if max_threads > len(tokens):
            max_threads = len(tokens)

        visual.main_title()
        if len(tokens) > 0:
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                args = []
                for bot_token in tokens:
                    try:
                        if bot_token in ["", " ", "\n"]:
                            continue
                        bot_token = utility.extract(bot_token)
                        __new_tokens.append(bot_token)
                        args.append(bot_token)
                        executor.submit(check_token, *args)
                        args.remove(bot_token)
                    except Exception as e:
                        console.log_error(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")

            with open("data/tokens.txt", "w") as f:
                for token in __new_tokens:
                    f.write(f"{token}\n")
                    
            input(f"\n{' ' * 34}{Fore.LIGHTGREEN_EX}Unlocked: {str(unlocked)} | {Fore.YELLOW}Locked: {str(locked)} | {Fore.RED}Invalid: {str(invalid)} | {Fore.BLUE}Errors: {str(error)}"
                  .replace("|",f"{Fore.LIGHTWHITE_EX}|")+"\n")
            visual.main_screen()

        else:
            console.simple_log(f"No tokens in '{Fore.YELLOW}data/tokens.txt{Fore.LIGHTWHITE_EX}'")
            input()
            visual.main_screen()
    
    def cleaner():
        utility.start_threads(func=run.clean)
    
    def boost_guild():
        guild_id = utility.option(msg="guild id")
        utility.start_threads(func=run.boost, args=[guild_id])

    
    
    def onboard_bypass():
        
        
            
        info = OnboardingInfo()
        
        info.guild_id = utility.option(msg="guild id")
        
        board_info = False
        while not board_info:
            token = random.choice(utility.get_tokens())
            board_info = utility.get_board_info(token, info.guild_id)
            if not board_info:
                console.simple_log("Failed to get board info, retrying")
                time.sleep(1)
            elif board_info.get("code", 0) == 50001:
                console.log(token, "NOT IN GUILD", action_clr="red")
                time.sleep(2)
                continue
            elif not board_info.get("enabled"):
                console.simple_log("Board is not enabled")
                time.sleep(5)
                visual.main_screen()
                return

        console.simple_log(f"Removing any non-required prompts")
        updated_prompts = []
        for i in range(len(board_info["prompts"])):
            if board_info["prompts"][i]["required"]:
                updated_prompts.append(board_info["prompts"][i])
            
            
        board_info["prompts"] = updated_prompts
        for prompt in board_info["prompts"]:
            info.onboarding_prompts_seen[str(prompt["id"])] = 1681404058976
        for prompt in board_info["prompts"]:
            for option in prompt["options"]:
                info.onboarding_responses_seen[str(option["id"])] = 1681404058976
            
        randomize_answers = utility.option(msg="pick answers (y/n)").lower() == "y"
        if not randomize_answers:
            console.simple_log(f"Randomizing answers")
            for prompt in board_info["prompts"]:
                info.onboarding_responses.append(random.choice(prompt["options"])["id"])
        else:
            for prompt in board_info["prompts"]:
                answer = utility.ask_onboard_option(prompt)
                info.onboarding_responses.append(answer)
                
        
        utility.start_threads(func=run.onboard_bypass, args=[info])

    def avatar_changer():
        agreement = utility.option(msg="are you sure you want to continue, this is known to lock tokens no matter what? (y/n)").lower()
        if agreement != "y":
            visual.main_screen()
        pfp_list = os.listdir("data/pfps")
        
        if len(pfp_list) == 0:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}No images in 'data/pfps'")
            input()
            visual.main_screen()
            
        encoded_strings = []
        
        for pfp in pfp_list:
            with open(f"data/pfps/{pfp}", "rb") as image_file:
                encoded_strings.append(base64.b64encode(image_file.read()))

        utility.start_threads(func=run.change_pfp, args=[encoded_strings])

    def member_scraper():
        guild_id = utility.option(msg="guild id")
        channel_id = utility.option(msg="channel id")
        
        token = utility.extract(random.choice(utility.get_tokens()))
        
        users = utility.scrape_members(token, guild_id, channel_id)
        with open(f"scraped/{guild_id}.txt", "w") as f:
            for user in users:
                f.write(f"{user}\n")
            
        console.simple_log(f"{Fore.LIGHTBLACK_EX}Scraped {len(users)} users")
        console.simple_log(f"{Fore.LIGHTBLACK_EX}Saved to scraped/{guild_id}.txt")
        utility.option(msg="Press enter to continue")
        visual.main_screen()
        
    def bypasses():
        bypasses = {
            BypassableBots.RESTORECORD: selection._restorecord_bypass,
            BypassableBots.CAPTCHA_BOT: selection._captcha_bot_bypass,
            BypassableBots.WICK: selection._wick_bypass,
        }
        for i, bot in enumerate(bypasses):
            console.simple_log(f"{Fore.LIGHTBLACK_EX}[{i + 1}] {bot.title()}")
        bypass = utility.option(msg="bypass")
        if bypass == "":
            visual.main_screen()
        
        visual.main_title()
        try:
            bypass = int(bypass)
        except:
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid input")
            visual.main_screen()
            
        if bypass > len(bypasses):
            console.simple_log(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}Invalid input")
            visual.main_screen()
            
        bypasses[list(bypasses.keys())[bypass - 1]]()
        
        
        
        
    def _restorecord_bypass():
        bot_id = utility.option(msg="bot id")
        guild_id = utility.option(msg="guild id")
        if guild_id == "":
            visual.main_screen()
        custom_redirect = utility.get_oauth_redirect(bot_id)        
        utility.start_threads(func=run.restorecord_bypass, args=[guild_id, bot_id, custom_redirect])
        
    def _captcha_bot_bypass():
        msg_link = utility.get_message_info()

        iteration = 0
        token = utility.extract(random.choice(utility.get_tokens()))
        console.simple_log(f"{Fore.LIGHTBLACK_EX}Checking if randomly selected token has access to channel")
        while (not utility.has_access_to_channel(token, msg_link["channel_id"])) and iteration < 3:
            if utility.has_access_to_channel(token, msg_link["channel_id"]):
                break
            iteration += 1
            console.simple_log(f"{Fore.RED}Scrape token does not have access to {msg_link['channel_id']} {Fore.LIGHTBLACK_EX}(picking next token)")
            token = utility.extract(random.choice(utility.get_tokens()))
        buttons = utility.get_message_buttons(token, msg_link["guild_id"], msg_link["channel_id"], msg_link["message_id"])
        unwanted = [
            "Why?",
            "ONLY verify on https://captcha.bot"
        ]
        button = [x for i, x in enumerate(buttons) if x["label"] not in unwanted or i == next((i for i, x in enumerate(buttons) if x["label"] not in unwanted), None)][0]
        
        utility.start_threads(func=run.bypass_captcha_bot, args=["512333785338216465", msg_link, button])
    
    def _wick_bypass():
        msg_link = utility.get_message_info()
        
        iteration = 0
        token = utility.extract(random.choice(utility.get_tokens()))
        console.simple_log(f"{Fore.LIGHTBLACK_EX}Checking if randomly selected token has access to channel")
        while (not utility.has_access_to_channel(token, msg_link["channel_id"])) and iteration < 3:
            if utility.has_access_to_channel(token, msg_link["channel_id"]):
                break
            iteration += 1
            console.simple_log(f"{Fore.RED}Scrape token does not have access to {msg_link['channel_id']} {Fore.LIGHTBLACK_EX}(picking next token)")
            token = utility.extract(random.choice(utility.get_tokens()))
        console.simple_log(f"{Fore.LIGHTBLACK_EX}Getting message info...")
        session, headers, cookies = utility.get_client(token)
        buttons = utility.get_message_buttons(token, msg_link["guild_id"], msg_link["channel_id"], msg_link["message_id"], session, headers, cookies)
        msg_info = utility.get_message(token, msg_link["channel_id"], msg_link["message_id"], session, headers, cookies)
        unwanted = [
            "Help",
        ]
        button = [x for i, x in enumerate(buttons) if x["label"] not in unwanted or i == next((i for i, x in enumerate(buttons) if x["label"] not in unwanted), None)][0]
        
        utility.start_threads(func=run.bypass_wick, args=[msg_info["author"]["id"], msg_link, button])

    def soundboard_spam():
        guild_id = utility.option(msg="guild id")
        channel_id = utility.option(msg="channel id")
        
        sounds = False
        while not sounds:
            token = random.choice(utility.get_tokens())
            sounds = utility.get_default_soundboard_sounds(token)
        random_sounds = utility.option(msg="random sounds (y/n)") == "y"
        if not random_sounds:
            for sound in sounds:
                console.simple_log(f"{Fore.LIGHTBLACK_EX}[{sounds.index(sound) + 1}] {sound['name']}")
            sound_index = utility.option(msg="sound")
            sounds = [sounds[int(sound_index) - 1]]

        utility.start_threads(func=run.soundboard_spam, args=[guild_id, channel_id, sounds])
    
    def test_proxy():
        utility.option(msg="Press enter to start")
        if not utility.test_proxies():
            console.simple_log(f"{Fore.RED}Proxy is invalid")
        else:
            console.simple_log(f"{Fore.GREEN}Proxy is valid")
        visual.main_screen()
    
class authentication():
    def __init__(self):
        try:
            utility.dazeer_init()


            # was all old AUTH stuff
        
            
        except Exception as e:
            print(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")
            time.sleep(5)
            os._exit(0)
    
    def _login(self, username: str) -> None:  
        try:
            
            # was all old AUTH stuff
            
            visual.initialize()
        except Exception as e:
            print(f"{Fore.RED}ERROR: {Fore.LIGHTWHITE_EX}{e}")
            time.sleep(5)
            os._exit(0)
            sys.exit(0)
        
    def register(self) -> None:
        webbrowser.open("https://vantageclients.com")
        self.start()

    def login(self) -> None:
        
        with open(self.user_path, "r") as f:
            username = f.read().strip()
            
        if username == "":
            username = utility.option(msg="username")
        if username == "":
            self.start()
        
        if not os.path.exists(self.user_path):
            open(self.user_path, "w").close()
        with open(self.user_path, "w") as f:
            f.write(username)
        console.simple_log(f"Logging in as {username}...")
        self._login(username)


    def start(self, check = True):
        visual.main_title()
        if open(self.user_path, "r").read().strip() != "" and check:
            console.simple_log(f"Found saved credentials, logging in...")
            return self.login()

        msg = """
1) Login
2) Register
        """
        print(pystyle.Center.XCenter(msg))
        h = " ~/> "
        option = int(input(pystyle.Center.XCenter(h, pystyle.Center._xspaces(text=h) - 10)))
        opts = {
            1: self.login,
            2: self.register,
        }
        try:
            if option in opts:
                opts[option]()
            else:
                self.start()
        except Exception as e:
            print(e)

class visual():

    def main_title():
        os.system("cls")
        
        msg = f"Total Tokens: {len(utility.get_tokens())} | Total Proxies: {len(utility.get_proxies())}\n\n\n"
        
        thing = f"""
        
      :::::::::      :::     ::::::::: :::::::::: :::::::::: ::::::::: 
     :+:    :+:   :+: :+:        :+:  :+:        :+:        :+:    :+: 
    +:+    +:+  +:+   +:+      +:+   +:+        +:+        +:+    +:+  
   +#+    +:+ +#++:++#++:    +#+    +#++:++#   +#++:++#   +#++:++#:    
  +#+    +#+ +#+     +#+   +#+     +#+        +#+        +#+    +#+    
 #+#    #+# #+#     #+#  #+#      #+#        #+#        #+#    #+#     
#########  ###     ### ######### ########## ########## ###    ###      
"""

        thing = pystyle.Center.XCenter(thing) + GlobalInfo.VERSION
        thing = pystyle.Colorate.Horizontal(pystyle.Colors.cyan_to_blue, thing)

        msg = pystyle.Center.XCenter(msg)
        msg = pystyle.Colorate.Horizontal(pystyle.Colors.cyan_to_blue, msg)
        print(thing + "\n\n" + msg)


    def initialize():
        os.system("title ")
        try:
            utility.dazeer_init()
        except Exception as e:
            print(e)
            time.sleep(5)
            os.abort()

        visual.main_screen()


    def format_function_name(func: types.FunctionType):
        return func.__name__.replace("_", " ").upper()



    def main_screen():
        global menu_str
        os.system("cls")
        visual.main_title()
        os.system("title Dazeer Spammer")

        ops = {
            "1": {
                "joiner": (selection.server_joiner),
                "leaver": (selection.server_leaver),
                "spammer": (selection.spammer),
                "accept rules": (selection.ruler),
                "spam webhook": (selection.webhooker),
                "ticket spammer": (selection.ticket_spammer),
                "spotify spam": (selection.spotify_spam),
                "mass report": (selection.mass_report),
                "proxy tester": (selection.test_proxy),
                
            },
            "2": {
                "reactor": (selection.reactor),
                "formater": (selection.formater),
                "mass thread": (selection.threader),
                "mass nick": (selection.nicker),
                "vc spam": (selection.voice_chat),
                "forum flood": (selection.mass_forum),
                "mp3 player": (selection.mp3_player),
                "call spam": (selection.call_spam),
            },
            "3": {
                "mass friend": (selection.mass_friender),
                "change bio": (selection.change_bio),
                "change hypesquad": (selection.hypesquad),
                "fake typing": (selection.fake_typing),
                "token checker": (selection.checker),
                "clean tokens": (selection.cleaner),
                "boost guild": (selection.boost_guild),
                "onboard bypass": (selection.onboard_bypass),
                
            },
            "4": {
                "onliner": (selection.onliner),
                "avatar changer": (selection.avatar_changer),
                "dm spammer": (selection.dm_spammer),
                "server checker": (selection.server_checker),
                "button presser": (selection.button_presser),
                "member scraper": (selection.member_scraper),
                "bypasses": (selection.bypasses),
                "soundboard spam": (selection.soundboard_spam),
            }
        }
        numer = 1
        for sub_menu in ops:
            for func_name in ops[sub_menu]:
                ops[sub_menu][func_name] = (ops[sub_menu][func_name], numer)
                numer += 1
            
        menu = ""
        options = [i for i in range(10)] 
        try:
            for num in options:
                for sub_menu in ops:
                    try:
                        func_name = list(ops[sub_menu].keys())[num]
                        func_num = ops[sub_menu][func_name][1]
                        menu += f"[{'0' if func_num < 10 else ''}{func_num}] - {func_name.upper()} {' ' * (16 - len(func_name.upper()))} "
                    except:
                        pass
                menu += "\n"
        except Exception as e:
            print(e)
        menu = pystyle.Colorate.Horizontal(pystyle.Colors.cyan_to_blue, pystyle.Center.XCenter(menu)).replace("-", Fore.LIGHTWHITE_EX + "-" + Fore.LIGHTMAGENTA_EX)

        print(menu)

        try:
            option = str(input(pystyle.Center.XCenter(" ~/> ", 30)))
            try:
                option = int(option)
            except:
                time.sleep(1)
                visual.main_screen()
            visual.main_title()
            for name, submenu in ops.items():
                for name, opt in submenu.items():
                    if opt[1] == int(option):
                        opt[0]()
            console.simple_log(f"Invalid option: {option}")
            time.sleep(1)
            visual.main_screen()
        except KeyboardInterrupt:
            os.abort()
        except Exception as e:
            print(e)
            time.sleep(5)
            visual.main_screen()
def main():
 try:
    authentication().start()
 except Exception as e:
    print(e)
    os.abort()
main()
