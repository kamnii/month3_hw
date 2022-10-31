FROM python:3.9

EXPOSE 1111

RUN mkdir -p /opt/services/bot/kaniet-bot
WORKDIR /opt/services/bot/kaniet-bot

COPY . /opt/services/bot/kaniet-bot/

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/kaniet-bot/main.py"]
