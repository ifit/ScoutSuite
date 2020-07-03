#!/usr/bin/env python3

import sys

from ScoutSuite.__main__ import run_from_cli

import os
from concurrent import futures
from datetime import date
import boto3


def upload_directory(directory, bucket, prefix):
    s3 = boto3.client("s3")

    def error(e):
        raise e

    def walk_directory(directory):
        for root, _, files in os.walk(directory, onerror=error):
            for f in files:
                yield os.path.join(root, f)

    def upload_file(filename):
        s3.upload_file(Filename=filename, Bucket=bucket, Key=prefix + os.path.relpath(filename, directory), ExtraArgs={'ContentType':'text/html'})

    with futures.ThreadPoolExecutor() as executor:
        futures.wait(
            [executor.submit(upload_file, filename) for filename in walk_directory(directory)],
            return_when=futures.FIRST_EXCEPTION,
        )


if __name__ == "__main__":
    print("# start running scout.py")
    print("### start report")
    run_from_cli()
    print("### finish report")
    print("### start ls")
    os.system('ls -R')
    print("### finish ls")
    print("### start upload")
    prefix = date.today().isoformat()
    sys.exit(upload_directory("/opt/scoutsuite-report", "ifit-sandbox-scout-suite", prefix))
    print("### finish upload")
    print("# finished running scout.py")

    #sys.exit(run_from_cli())
