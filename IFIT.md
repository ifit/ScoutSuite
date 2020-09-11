# iFit

[![Deployments](https://github.com/ifit/ScoutSuite/workflows/Deploy%20ScoutSuite%20Docker%20Image%20to%20ECR/badge.svg)](https://github.com/ifit/ScoutSuite/actions?query=workflow%3A%22Build%20and%20Push%20Docker%20Images%20to%20ECR%22)

See corresponding CloudFormation template for ECR repository information

## Deployments

Github Actions build, tag (short `sha1` && `latest`), and push docker images to ECR for every PR/Push to the `master` branch via the [`Deploy ScoutSuite Docker Image to ECR`](../.ScoutSuite/.github/workflows/deploy.yml) workflow using a dedicated [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users) with [least priveledge granted](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and keeping AWS Access Keys stored as [GitHub Actions secrets](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets).

The ECR LifecyclePolicy for the ScouteSuite Repo only retains 3 docker images. Each time the task runs the `lastest` image will be used.

### RollingBack

To rollback a bad deploy/broken image you can delete the defective image, and ensure that the image in the rpo you wish to be used is tagged as `latest`.

## Manual Build Steps

### Log into ECR

* `aws ecr get-login`

### Build image

* `docker build -t scout-suite/scout-suite:latest .`

### Tag image

* `docker tag scout-suite/scout-suite:latest <account_id>.dkr.ecr.<region>.amazonaws.com/scout-suite/scout-suite:latest`

### Push image to ECR

* `docker push <account_id>.dkr.ecr.<region>.amazonaws.com/scout-suite/scout-suite:latest`

## Changelog
* 2020-09-11
  * added deployments of docker images to ECR via Github Actions
* 2020-07-03
  * Add ability to push output report to a parameterized S3 bucket (pulled from env var)
  * Set mime types on objects pushed to S3
  * Prefix report keys with current date for report grouping
  * Delete .travis.yml
