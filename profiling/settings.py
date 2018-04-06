"""
Settings for all scripts
"""
import yass
import logging
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str,
                        help="Path to config file")
    parser.add_argument("-l", "--logger", type=str,
                        help="YASS logger level",
                        default="WARNING")
    args = parser.parse_args()

    # set yass configuration parameters
    yass.set_config(args.config)

    # configure logs from yass
    logging.getLogger("yass").setLevel(args.logger)
    # logs from this script
    logging.basicConfig(level=logging.INFO)

    return args
