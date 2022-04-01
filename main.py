#coding:utf-8
import argparse
from exploit import Exploit
from swagger import Swagger, getSchema
from banner import banner

def main():
    parser = argparse.ArgumentParser(description=f'{banner} \r\nScan you application(s) for the Spring4Shell vulnerability. This scanner creates a harmless file (sniffer.txt) which the scanner simply scans for it\'s existance.')
    parser.add_argument('--file',help='Supply a file with 1 url per-line.',required=False)
    parser.add_argument('--url',help='Target a specific URL',required=False)
    parser.add_argument('--swagger',help='When given the link to the applications swagger documentation (swagger.json url), automatically retrieve all GET & POST endpoints and tries to exploit them. Testen on openapi specification 3.0.2',required=False)
    args = parser.parse_args()
    if not args.url and not args.file and not args.swagger:
        print("Please supply an argument...")
        return
    print(banner)
    print("[*] Starting scanning...")

    if args.url:
        exploit = Exploit(args.url)
        getVuln = exploit.exploitGet()
        if not getVuln:
            exploit.exploitPost()
    if args.file:
        with open (args.file) as f:
            for i in f.readlines():
                i = i.strip()
                exploit = Exploit(i)
                getVuln = exploit.exploitGet()
                if not getVuln:
                    exploit.exploitPost()
    if args.swagger:
       host, schema = getSchema(args.swagger)
       swagger = Swagger(schema)
       paths = swagger.getPaths()
       for path in paths:
           fullUrl = host + path
           exploit = Exploit(fullUrl)
            getVuln = exploit.exploitGet()
            if not getVuln:
                exploit.exploitPost()

    print("[*] Done scanning, goodbye")


if __name__ == '__main__':
    main()
