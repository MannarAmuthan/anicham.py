FROM python:3.12-slim

WORKDIR /working_directory

RUN pip3 install pipenv

COPY tests .

RUN pip3 install pytest
RUN pip3 install anicham

CMD python -m pytest test_anicham.py