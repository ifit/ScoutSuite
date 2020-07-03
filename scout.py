#!/usr/bin/env python3

import os
from concurrent import futures
from datetime import date
import boto3
from mimetypes import MimeTypes
import sys

from ScoutSuite.__main__ import run_from_cli


def upload_directory(directory, bucket, prefix):
    s3 = boto3.client("s3")

    def error(e):
        raise e

    def walk_directory(directory):
        for root, _, files in os.walk(directory, onerror=error):
            for f in files:
                yield os.path.join(root, f)

    def upload_file(filename):
        s3.upload_file(Filename=filename, Bucket=bucket, Key=prefix + "/" + os.path.relpath(filename, directory))

    with futures.ThreadPoolExecutor() as executor:
        futures.wait(
            [executor.submit(upload_file, filename) for filename in walk_directory(directory)],
            return_when=futures.FIRST_EXCEPTION,
        )


if __name__ == "__main__":
    run_from_cli()

    sys.exit(upload_directory("/opt/scoutsuite-report", "ifit-scout-suite", prefix))
