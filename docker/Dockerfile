FROM python:3.12-alpine
# alpine-образ меньше чем full image

WORKDIR /app
# WORKDIR создаёт слой и используется далее автоматически, в отличие от RUN cd, который необходимо будет повторять

COPY app/requirements.txt .
# зависимости копируются отдельно в кэш Docker слоёв

RUN pip install --no-cache-dir -r requirements.txt
# --no-cache-dir уменьшает размер образа

COPY app/app.py .

EXPOSE 8080
# явно указываем порт приложения

ENV STUDENT_NAME=Litovchenko
# указываем явно в переменных окружения фамилию разработчика/студента, позволяет переписывать фамилию, не внося корректировки в app.py

CMD ["python", "app.py"]