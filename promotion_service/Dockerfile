# pull official base image
FROM python:3.12

# set work directory
ENV APP_HOME=/promotion_service
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONPATH="${PYTHONPATH}:/promotion_service"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip cache purge

# copy project
COPY promotion_service .
