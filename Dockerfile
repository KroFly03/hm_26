FROM python:3.10

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN python -m pip install --no-cache -r requirements.txt

COPY . .
CMD ["python", "run.py"]
