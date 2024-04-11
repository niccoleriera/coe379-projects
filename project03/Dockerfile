# Image: niccoleriera/ml-hurricane-api
FROM python:3.11

RUN pip install tensorflow==2.15
RUN pip install tensorflow-datasets==4.9.4
RUN pip install Flask==3.0

COPY models /models
COPY hurricane_api.py /hurricane_api.py


CMD ["python", "hurricane_api.py"]