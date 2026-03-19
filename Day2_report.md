# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: [Zhanbyrshy Aibek]
- Group: [IB-23-5b]
- GitHub repo: [https://github.com/aibekZH1/-devnet-day1-IB23-5b-Zhanbyrshy.git]
- Day1 Token: [D1-IB-23-5b-07-9E20]

## 2) NetAcad progress
- Module 2.2 done: [Yes/No] + screenshot
- Module 3.1–3.6 done: [list what completed] + screenshot

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: [Yes/No]
- File `artifacts/day2/conflict_log.txt` exists: [Yes/No]
- Conflict note (1–2 lines): what conflicted, how resolved

## 4) Generated artifacts (Day2)
- normalized.json: [Yes/No]
- normalized.yaml: [Yes/No]
- normalized.xml: [Yes/No]
- normalized.csv: [Yes/No]
- summary.json: [Yes/No]

## 5) Commands output (paste EXACT output)
### 5.1 Generator
{
  "schema_version": "2.0",
  "generated_utc": "2026-03-19T02:02:54.289923+00:00",
  "student": {
    "token": "D1-IB-23-5b-07-9E20",
    "token_hash8": "9238838b",
    "name": "Zhanbyrshy",
    "group": "IB-23-5b"
  },
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_json_sha256": "25880907b2b43367fa5c0c35eeb4ce7b871c1117c252cf87e3ca606058a9d7fc",
    "normalized_yaml_sha256": "36e48423cef22bc0da52396fd06bde44ee7b449c478f5ac89755218260aee734",
    "normalized_xml_sha256": "eec8b43d9be11de9970d5272cde9a54957eefd0bb6223821af21f10129a7f2e1",
    "normalized_csv_sha256": "7eecba49eddca3b4fe7af227a6fbff4e17a9ff4e7e48063df26670a78093c752"
  },
  "computed": {
    "title_len": 18
  }
}

### 5.2 Tests
.                                                                                                        [100%]
1 passed in 0.10s
## 6) What I learned (3–6 bullets)
- ...
- ...

## 7) Problems & fixes (at least 1)
Problem 1: Merge Conflict in README.md

Fix: При попытке слияния ветки feature/day2-readme-B в main возник конфликт в файле README.md. Я вручную отредактировал файл, удалив маркеры конфликта (<<<<, ====, >>>>), объединил изменения и зафиксировал результат с помощью Merge Commit.

Proof: Файл artifacts/day2/conflict_log.txt содержит вывод git status в момент конфликта.

Problem 2: Data Type Mismatch in XML/CSV (Boolean)

Fix: Поле completed в Python имеет тип bool (True/False), но в XML и CSV оно должно быть в нижнем регистре (true/false). В скрипте day2_data_formats.py я применил метод .lower() при приведении к строке, чтобы соответствовать схеме валидации.

Proof: Прохождение теста pytest и содержимое файла normalized.xml.

Problem 3: Python Type Hints Compatibility

Fix: В среде DEVASC VM (Python 3.8) стандартные коллекции не поддерживают индексацию типов (например, list[str]). Решено добавлением from __future__ import annotations для поддержки современного синтаксиса аннотаций.

Proof: Успешный запуск генератора без TypeError.