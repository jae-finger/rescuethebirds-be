# Use a smaller base image, such as Alpine Linux, to reduce the image size.
FROM python:3.11-alpine

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# add app
COPY . .

# Use a non-root user to run the application for security reasons.
RUN adduser -D appuser
USER appuser

# start app
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]