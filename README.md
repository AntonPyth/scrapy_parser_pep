# Проект парсинга PEP

## 📌 Описание проекта

Парсер позволяет получать данные о версиях Python, документации и статусах PEP, и скачивать архив документации.

---

## 🔹 Функционал:

- Парсинг статусов версий и документов PEP по адресу:  https://peps.python.org/
- Вывод данных парсинга в 2 раздельных файла **CSV**

---

## 🛠 Технологии

- Python 3.9
- Scrapy 2.5.1

---

## 🚀 Запуск проекта

1. Клонировать репозиторий и перейти в него
   
  ```
  git clone git@github.com:AntonPyth/scrapy_parser_pep.git
  cd scrapy_parser_pep
  ```
2. Cоздать и активировать виртуальное окружение
  ```
  python -m venv venv
  . venv/bin/activate     # для Linux/macOS
  . venv\Scripts\activate        # для Windows
  ```
3. Установить зависимости из файла requirements.txt
  ```
  pip install -r requirements.txt
  ```
4. Пример запуска
  ```
  scrapy crawl pep
  ```

---

## 🧑‍💻 Автор:

Разработано: (https://github.com/AntonPyth) в рамках учебного спринта Яндекс Практикум по парсингу.