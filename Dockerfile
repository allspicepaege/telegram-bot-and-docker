FROM python:3.10-slim
ENV TOKEN='<personal_token>'
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]