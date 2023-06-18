FROM python:3.10
RUN pip install --upgrade pip && \
    pip install pytest requests
COPY . /app/
WORKDIR /app
CMD ["pytest", "-v", "test_jph_methods.py"]