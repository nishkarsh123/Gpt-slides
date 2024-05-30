FROM python:3.12.3 as python
ARG OPENAI_API_KEY
ARG CELERY_BROKER
ENV OPENAI_API_KEY $OPENAI_API_KEY
ENV CELERY_BROKER: ${CELERY_BROKER}
RUN mkdir /gpt_slides
WORKDIR /gpt_slides
COPY requirements.txt /gpt_slides
RUN pip install -r requirements.txt
COPY . gpt_slides/


# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# FROM nginx:latest
# WORKDIR /usr/share/nginx/html
# RUN rm -rf ./*
# COPY nginx.conf /etc/nginx/conf.d/
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput