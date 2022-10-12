import requests
import re
import sys
import getopt

arg_list = sys.argv[1:]


def statuscode_resolver():
    global url, code
    with open(sys.argv[1]) as ap:
        for domains in ap:
            domains_list = domains.split("\n")
            try:
                for domain in domains_list:
                    urls = re.findall(
                        "https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}",
                        domain)
                    for url in urls:
                        code = str(requests.get(
                            url, allow_redirects=False).status_code)
                        print("[+]" + domain + "\t" + code)
            except Exception as e:
                continue
            except KeyboardInterrupt as k:
                print("KeyboardInterrupt")
                break


def help():
    print("Syntax: python ./codes.py <file> -o <output.txt>")
    print("-h: help")
    print("-o: output to file")


def output():
    with open(filename, "w+") as op:
        op.write(url + "  " + code)


try:
    opts, args = getopt.getopt(arg_list, "f:o:h", ["file=", "output=", "help"])
except getopt.GetoptError as e:
    print(e)

for opt, arg in opts:
    if opt in ('-f', '--file'):
        sys.argv[1] = arg
        statuscode_resolver()
    elif opt in ('-o', '--output'):
        filename = arg
        output()
    elif opt in ('-h', '--help'):
        help()
