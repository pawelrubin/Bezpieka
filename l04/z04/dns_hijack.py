#!/usr/bin/env python3
# Paweł Rubin 2019
#
"""DNS hijacking tool."""
from typing import List
from argparse import ArgumentParser
from pprint import pprint
from scapyx

import pyshark


def hijack_dns(interface:str, name:str):
    """Listens on given interface until session cookie has been found.
    Opens Firefox webdriver with the cookie."""
    capture = pyshark.LiveCapture(
        interface=interface,
        display_filter="dns"
    )

    for packet in capture.sniff_continuously():
        try:
            if packet.dns.qry_name == name:
                print(packet)
        except AttributeError as e:
            print("no qry_name")
            pass

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

    parser.add_argument(
        "--name",
        "-name",
        type=str,
        required=True,
        help="Domain name.",
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_cli()
    hijack_dns(args.interface, args.name)
