#!/usr/bin/env python3

import sys
import argparse
import urllib.parse



def URLencode(text: str) -> str:
    return urllib.parse.quote_plus(text)

def URLdecode(text: str) -> str:
    return urllib.parse.unquote(text.replace('+', ' '))

def read_file(filepath: str) -> str:
    text = ""
    with open(filepath, "r") as f:
        text = f.read()
    return text



def main(args: list[str], exit_on_error=False) -> int:
    """
    Parse command-line and start relative actions

    :param args: are comand line argument (callable also via scripting; keep in mind that 1st argument is script name)
    :type args: list[str]
    :return: error code (0 if success)
    :rtype: int
    """
    parser = argparse.ArgumentParser(description='URL encoder / decoder', exit_on_error=exit_on_error)
    cmdgroup = parser.add_mutually_exclusive_group()
    cmdgroup.add_argument('--decode', '-d', action='store_true', help='decode')
    cmdgroup.add_argument('--encode', '-e', action='store_true', help='encode')
    ingroup = parser.add_mutually_exclusive_group()
    ingroup.add_argument('--file', '-f', metavar='FILEPATH', type=argparse.FileType('r'), help='input file', default=sys.stdin)
    ingroup.add_argument('--text', '-t', metavar='TEXT', type=str, help='input text')
    
    try:
        if len(args) == 0:
            parser.print_usage()
            return 1
        
        try:
            parsed_args = parser.parse_args(args)
        except argparse.ArgumentError as ex:
            sys.stderr.print(str(ex))
            return 2

        if parsed_args.text != None:
            text = parsed_args.text
        else:
            text = parsed_args.file.read()
        
        if parsed_args.decode:
            sys.stdout.write(URLdecode(text))
        elif parsed_args.encode:
            sys.stdout.write(URLencode(text))
        else:
            parser.print_usage()
            return 1
        
        return 0
    except Exception as ex:
        sys.stderr.print(str(ex))
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], exit_on_error=True))
