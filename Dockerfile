FROM python:slim

COPY . /opt

WORKDIR /opt
RUN pip install -r requirements.txt
RUN mkdir /root/.aws

ENTRYPOINT ["python"]
CMD ["scout.py", "aws", "--no-browser", "--exceptions", "ifit-exceptions.js"]
