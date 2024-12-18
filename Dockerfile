FROM python:3.10-slim
ENV TOKEN='<personal_token>'
WORKDIR /app
COPY .gitignore bot.py README.md requirements.txt /app/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]