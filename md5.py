import hashlib, argparse, os, urllib.request
import http.client

argparser = argparse.ArgumentParser()

argparser.add_argument('file')

args = argparser.parse_args()

try:
    with open(args.file, 'rb') as f:
        readed = f.read()

        print(f"File MD5:  {hashlib.md5(readed).hexdigest()}")
        print(f"File SHA1: {hashlib.sha1(readed).hexdigest()}")
        print(f"File size: {os.path.getsize(args.file)} B / {round(os.path.getsize(args.file) / 1024, 1)} KB")
except:
    with urllib.request.urlopen(args.file) as r:
        readed: http.client.HTTPResponse = r.read()

        print(f"File MD5:  {hashlib.md5(readed).hexdigest()}")
        print(f"File SHA1: {hashlib.sha1(readed).hexdigest()}")