#!/usr/bin/python

import argparse
import ConfigParser


def has_valid_section(config, section):
    if not (set(config.options(section)) - set(config.defaults())):
        return 0
    return 1

def main():
    parser = argparse.ArgumentParser(description='Cleanup INI file')
    parser.add_argument('--input', required=True, help='input INI file')
    parser.add_argument('--output', required=True, help='ouput INI file')

    args = parser.parse_args()

    Config = ConfigParser.ConfigParser()
    Config.read(args.input)

    for section in Config.sections():
        if not has_valid_section(Config, section):
            Config.remove_section(section)

    with open(args.output, 'wb') as configfile:
        Config.write(configfile)

if __name__ == "__main__":
    main()

