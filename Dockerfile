FROM python:alpine3.7
WORKDIR /aman-project
ADD . /aman-project
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]