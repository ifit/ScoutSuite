#!/usr/bin/env python3

import os
from concurrent import futures
from datetime import date
import boto3
from mimetypes import MimeTypes
import sys

from ScoutSuite.__main__ import run_from_cli


# This function was based on an example found here: https://github.com/boto/boto3/issues/358
# It was modified to determine mime type and set Content-Type HTTP metadata automatically.
def upload_directory(directory, bucket, prefix):
    mime = MimeTypes()
    s3 = boto3.client("s3")

    def error(e):
        raise e

    def walk_directory(directory):
        for root, _, files in os.walk(directory, onerror=error):
            for f in files:
                yield os.path.join(root, f)

    def upload_file(filename):
        mime_type = mime.guess_type(filename)
        if mime_type[0] is not None:
            extra_args={'ContentType':mime_type[0]}
        else:
            extra_args={}
        s3.upload_file(Filename=filename, Bucket=bucket, Key=prefix + "/" + os.path.relpath(filename, directory), ExtraArgs=extra_args)

    with futures.ThreadPoolExecutor() as executor:
        futures.wait(
            [executor.submit(upload_file, filename) for filename in walk_directory(directory)],
            return_when=futures.FIRST_EXCEPTION,
        )


if __name__ == "__main__":
    run_from_cli()

    output_bucket = os.environ.get("OUTPUT_BUCKET")
    prefix = date.today().isoformat()

    sys.exit(upload_directory("/opt/scoutsuite-report", output_bucket, prefix))
