# **Test_task** :floppy_disk:

## Процесс тестирования нового функционала

---

## Автоматизация тестирования API. Часть 1

## Description

Test_task is a set of test scripts to test the functionality of API endpoints.

  *  API url https://jsonplaceholder.typicode.com/
  *  Methods: GET /posts, POST /posts, DELETE /posts
  *  Parametrs: userId, id, title, body

## Installation and Run

1. Clone repo: `git clone https://github.com/RadmirSh/Test_task.git`
2. Install Dependencies: `pip install -r requirements.txt`
3. Run Tests: `pytest test_jph_methods.py`

Requires Python 3 and Requests

---

## Автоматизация тестирования API. Часть 2

## Dockerfile 🐳

```python
FROM python:3.10
RUN pip install --upgrade pip && \
    pip install pytest requests
COPY . /app/
WORKDIR /app
CMD ["pytest", "-v", "test_jph_methods.py"]
```
