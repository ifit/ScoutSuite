# iFit

See corresponding CloudFormation template for ECR repository information

## Build Steps

### Log into ECR

* `aws ecr get-login`

### Build image

* `docker build -t scout-suite/scout-suite:latest .`

### Tag image

* `docker tag scout-suite/scout-suite:latest <account_id>.dkr.ecr.<region>.amazonaws.com/scout-suite/scout-suite:latest`

### Push image to ECR

* `docker push <account_id>.dkr.ecr.<region>.amazonaws.com/scout-suite/scout-suite:latest`

## Changelog

* 2020-07-03
  * Add ability to push output report to a parameterized S3 bucket (pulled from env var)
  * Set mime types on objects pushed to S3
  * Prefix report keys with current date for report grouping
