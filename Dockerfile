FROM python:3.9-alpine
ADD . blogor
WORKDIR /blogor
RUN python -m pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "-m", "gunicorn", "-b", "0.0.0.0", "blogor.wsgi"]