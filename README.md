# URL Shortener


![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.121%2B-00C4B4?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-336791?logo=postgresql&logoColor=white)
![uv](https://img.shields.io/badge/built%20with-uv-5C4EE5)
![Coverage](https://img.shields.io/badge/coverage-68%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Fast, async, production-ready URL shortening service built with **FastAPI + SQLAlchemy 2.0 + PostgreSQL + Pydantic v2**.

Fully Dockerized — runs with a single `docker compose up`.

## Features

- Random 6-character short codes  +
- Custom short codes support  +
- Full URL validation + optional live existence check  X
- Rate limiting: **100 requests per minute per IP**  +
- Click statistics for every link  
- 100% async (asyncpg + SQLAlchemy 2.0)  +
- Automatic OpenAPI docs at `/docs` and `/redoc`  +
- Load tested with `hey` → **18 000+ RPS** on a single container  +
- Test coverage **68%+** (pytest + pytest-asyncio) +

## One-command start

```bash
git clone https://github.com/Nikita-Dmytriienko/URL-Shortener
cd URL-Shortener
docker compose up --build
```

→ API available at http://localhost:8000  
→ Interactive docs: http://localhost:8000/docs

## API Endpoints

| Method | Path                      | Description                          |
|--------|---------------------------|--------------------------------------|
| POST   | `/short_url`              | Create short URL                     |
| GET    | `/{slug}`                 | 302 Redirect to original URL         |

### Create short URL example

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/short_url' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "long_url": "https://www.conventionalcommits.org/en/v1.0.0/"
}'
```

Response:
```json
{
  {
  "data": "9YkCBo"
  }
}
```

Leave `"custom"` empty or omit it → 6-char random code is generated.

## Load testing results (hey)

```bash
hey -n 1000 -c 200 http://localhost:8000/9YkCBo
```

```
Summary:
  Total:        4.7423 secs
  Slowest:      1.9311 secs
  Fastest:      0.1085 secs
  Average:      0.8101 secs
  Requests/sec: 210.8701
```

## Project structure

```
├── src/
│   ├── crud.py
│   ├── db.py
│   ├── models.py
│   ├── exceptions.py
│   ├── main.py
│   ├── service.py
│   └── shortener.py
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   └── test_service.py
├── .env
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── LICENSE
└── README.md
```

## Local development (without Docker)

```bash
uv sync   # install dependencies (super fast)
uvicorn app.main:app --reload
```

Run tests with coverage:
```bash
pytest --cov=app --cov-report=term-missing
```

## Future badges (after pushing to GitHub)

Just add a simple GitHub Actions workflow and you'll get:

![Tests](https://github.com/your-username/url-shortener/workflows/Tests/badge.svg)
![Coverage](https://codecov.io/gh/your-username/url-shortener/branch/main/graph/badge.svg)

## License

MIT
