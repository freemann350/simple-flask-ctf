FROM python:3.9-slim
WORKDIR /app
COPY webapp.py /app
RUN pip install flask
EXPOSE 80
ENV FLAG="CTF35f3224b5a78932f1c0161a932dd310137d38107e4c4da0d26948bd041ff3a92"
ENV SCENARIO="1"
CMD ["python", "webapp.py"]
