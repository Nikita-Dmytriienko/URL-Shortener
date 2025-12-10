# URL Shortener

[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.121+-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-326789?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Coverage](https://img.shields.io/badge/coverage-68%25-brightgreen)](#tests)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Simple, fast and production-ready URL shortening service (like bit.ly) built with **FastAPI + SQLAlchemy 2 + PostgreSQL**.

All requirements and most of the “nice-to-have” complications are implemented.

## Features

- POST `/api/shorten` → create short link (random or custom)
- GET `/<short_code>` → 301 redirect to original URL
- Custom short codes (`/my-custom-link`)
- Full URL validation + optional HEAD check that target exists
- Rate limiting: **100 requests per minute per IP**
- Click statistics (total clicks counter)
- Full async, ready for high load
- Load tested with `hey` (~18k RPS on modest hardware)
- Test coverage **68%+** (with badge)

## Quick Start (one command)

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
docker compose up --build