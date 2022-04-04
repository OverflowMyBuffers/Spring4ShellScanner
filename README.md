# Spring4ShellScanner (CVE-2022-22965)
![spring4shell](spring4shell.png)

Spring4Shell (CVE-2022-22965) Scanner

## Details

This scanner scans your java applications for possibilities of the Spring4Shell exploit. 

Currently supports calling a single url, a file containing url's, or calling your swagger documentation (tested on Openapi 3). 

This script tests both GET requests as well as POST requests. Both seem vulnerable.

If you use the --jwt or --cookie argument it may occur that your provided value is too long for the terminal. In that case, use **stty -icanon;python3 main.py [args]** on Linux/MacOS terminals to overcome that issue

## Todo's

- Go more in depth into the swagger file, supporting calling specific endpoints with a random string or integer added
- Make a fileless payload which wouldn't trigger any AV/EDR
- Create such a payload that it automatically calls back to the host you're running this script from. Making the script not depend on a successfull file retrieval anymore
- ~~Add option for Authentication, jwt or cookie~~
- Silence certificate warning

## Honours

Many thanks to jbaines-r7 for the vulnerable application, which made testing very easy
The exploit was inspired by BobTheShoplifter, although slightly modified




