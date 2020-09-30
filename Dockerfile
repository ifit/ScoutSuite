FROM python:slim

COPY . /opt

WORKDIR /opt
RUN pip install -r requirements.txt
RUN mkdir /root/.aws

ENTRYPOINT ["python", "scout.py"]
CMD ["aws --no-browser --exceptions ifit-exceptions.js"]
