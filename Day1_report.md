# Day 1 Report — DevNet Sprint

## 1. Student
- Name: [Zhanbyrshy Aibek]
- Group: [IB-23-5b]
- GitHub repo: [https://github.com/aibekZH1/-devnet-day1-IB23-5b-Zhanbyrshy.git]
- Day1 Token: [D1-IB-23-5b-07-9E20]   

## 2. NetAcad progress (Module 1)
- Completed items: [1.1 / 1.2 / 1.3] (кратко)
- Screenshot(s): 
  - [СКРИНШОТ_1: прогресс NetAcad]

## 3. VM evidence
- File: `artifacts/day1/env.txt` exists: [Yes/No]
- Screenshot(s):
  - [СКРИНШОТ_2: терминал в DEVASC VM + hostnamectl/date]

## 4. Repo structure (must match assignment)
- `src/day1_api_hello.py` : [Yes]
- `tests/test_day1_api_hello.py` : [Yes]
- `schemas/day1_summary.schema.json` : [Yes]
- `artifacts/day1/summary.json` : [Yes]
- `artifacts/day1/response.json` : [Yes]

## 5. Commands run (paste EXACT output)
### 5.1 Script run
{
  "schema_version": "1.0",
  "generated_utc": "2026-03-19T01:28:26.166024+00:00",
  "student": {
    "token": "D1-IB-23-5b-07-9E20",
    "name": "Zhanbyrshy Aibek",
    "group": "IB-23-5b"
  },
  "api": {
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "status_code": 200,
    "validation_passed": true,
    "validation_errors": [],
    "response_sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
### 5.2 Tests
.                                              [100%]1 passed in 0.16s
## 6. Что я изучил сегодня (3–6 bullets)

Настройка и работа в терминале Linux внутри DEVASC VM.

Работа с переменными окружения через файл .env и команду export.

Использование библиотеки requests для взаимодействия с внешними REST API.

Валидация JSON-данных с использованием JSON Schema и библиотеки jsonschema.

Автоматизация тестирования с помощью Pytest.

Расчет контрольных сумм SHA256 для проверки целостности данных.
## 7. Проблемы и решения (как минимум 1)
Fix: В Python 3.8 аннотации типов вроде list[str] не поддерживаются напрямую. Добавил from __future__ import annotations в начало скрипта для совместимости.

Problem 2: Ошибка аутентификации Git (ENOENT / Missing credentials)

Fix: Отключил конфликтный помощник паролей VS Code через unset GIT_ASKPASS и использовал Personal Access Token (PAT) вместо обычного пароля.