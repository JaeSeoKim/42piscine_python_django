#!/usr/bin/python3

import sys
import antigravity


def main():
    if (len(sys.argv) == 4):
        try:
            latitude = float(sys.argv[1])
        except:
            return print("latitude required type: float")
        try:
            longitude = float(sys.argv[2])
        except:
            return print("longitude required type: float")
        try:
            datedow = sys.argv[3].encode('utf-8')
        except:
            return print("datedow required type: string")
        antigravity.geohash(latitude, longitude, datedow)
    else:
        print("3 arguments required(latitude, longitude, datedow)")


if __name__ == '__main__':
    main()
