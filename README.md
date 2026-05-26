## Documentation update
## Автор

Горкун Ярослав

## Функціонал

- перегляд списку завдань;
- додавання нового завдання;
- позначення завдання як виконаного;
- видалення завдання;
- REST API для роботи із завданнями;
- Swagger/OpenAPI опис 2+ endpoint-ів.

## Технології

- Python
- Flask
- HTML
- CSS
- JavaScript
- Swagger / OpenAPI

## Встановлення

```bash
git clone <посилання-на-репозиторій>
cd docs-practice-web-project
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## Встановлення залежностей

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python app.py
```

Після запуску відкрий у браузері:

```txt
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks` | Отримати всі завдання |
| POST | `/api/tasks` | Створити нове завдання |
| PATCH | `/api/tasks/{id}` | Оновити статус завдання |
| DELETE | `/api/tasks/{id}` | Видалити завдання |

## Документація

- `SSD.md` — System Specification Document
- `BRD.md` — Business Requirements Document
- `swagger.yaml` — OpenAPI документація endpoint-ів

## License

MIT License
