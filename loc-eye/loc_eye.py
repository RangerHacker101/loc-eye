#!/usr/bin/env python3

# LocEye - OSINT GPS Metadata Extractor
# Created by: Ranger Hacker
# Year: 2025

import exifread
import argparse
import os

def convert_to_degrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)

def extract_gps(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)

    lat_ref = tags.get('GPS GPSLatitudeRef')
    lat = tags.get('GPS GPSLatitude')
    lon_ref = tags.get('GPS GPSLongitudeRef')
    lon = tags.get('GPS GPSLongitude')

    if lat and lon and lat_ref and lon_ref:
        lat_decimal = convert_to_degrees(lat)
        if lat_ref.values != 'N':
            lat_decimal = -lat_decimal

        lon_decimal = convert_to_degrees(lon)
        if lon_ref.values != 'E':
            lon_decimal = -lon_decimal

        print(f"[+] Latitude: {lat_decimal}")
        print(f"[+] Longitude: {lon_decimal}")
        print(f"[+] Google Maps: https://www.google.com/maps?q={lat_decimal},{lon_decimal}")
    else:
        print("[-] No GPS metadata found in the image.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LocEye - Extract GPS location from image metadata (EXIF).")
    parser.add_argument("image", help="Path to the image file")

    args = parser.parse_args()

    if not os.path.exists(args.image):
        print("[-] File not found.")
    else:
        extract_gps(args.image)
