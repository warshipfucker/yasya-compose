FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENV PATH="/usr/local/lib/python3.9/site-packages:${PATH}"

COPY . /app/


EXPOSE 3000
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
