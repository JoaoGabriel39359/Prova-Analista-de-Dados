# CSV Validation & Relational Data Pipeline

A Python data-processing project that validates CSV records, separates valid and invalid rows, persists clean data in a relational database, and exposes the results through a small API.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Validation-150458?style=flat-square&logo=pandas&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Automated-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

## Project goal

The pipeline turns an untrusted CSV file into structured, traceable data. It validates schema and field types, keeps useful error reasons for rejected rows, and stores accepted records in a relational database.

## Capabilities

- Validate expected CSV headers
- Check integer and numeric fields
- Reject missing names and email addresses
- Detect malformed and duplicate records
- Separate valid rows from validation errors
- Persist processed data in a relational database
- Run through Docker
- Cover core behavior with automated tests

## Processing flow

```text
CSV input
   |
   v
Schema and row validation
   |
   +--> Valid records --> Relational database
   |
   +--> Invalid records --> Error reasons
```

## Repository structure

```text
.
├── main.py              # Application entry point
├── csv_utils.py         # CSV parsing and validation
├── db_utils.py          # Relational persistence
├── sample_data.csv      # Reproducible sample input
├── tests/               # Automated tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Run locally

```bash
git clone https://github.com/JoaoGabriel39359/Prova-Analista-de-Dados.git
cd Prova-Analista-de-Dados
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

On Windows, activate the environment with `.venv\\Scripts\\activate`.

## Run with Docker

```bash
docker compose up --build
```

## Tests

```bash
pytest -q
```

## Engineering focus

- Validation rules are separated from persistence.
- Invalid rows retain actionable rejection reasons.
- The sample dataset makes the behavior reproducible.
- Containerization reduces environment differences.
- Automated tests protect the data-processing contract.

## Author

**João Gabriel Vieira Barbosa**  
Full-Stack Developer focused on Python, APIs, data processing, and business automation.

[GitHub profile](https://github.com/JoaoGabriel39359)
