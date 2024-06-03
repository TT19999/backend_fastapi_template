# FastAPI template

## Installation

Use Docker & Docker Compose

- Clone Project
- Run docker-compose

```
$ docker-compose build      # build docker image depend on Dockerfile
$ docker-compose up -d      # auto build docker image depend on Dockerfile & run service
```

## Project structure

```
.
├── app
│   ├── api           // api endpoint
│   ├── core          // contain config of project
│   ├── db            // connect to db
│   ├── helpers       // helper functions
│   ├── middlewares   // custom middlewares
│   ├── repositories  // base function for model
│   ├── migrations    // Contain database model, and alembic for auto generating migration
│   ├── schemas       // Pydantic Schema
│   ├── services      // Contain business logic and communicate 
│   └── main.py       // config middleware, handle exception etc
├── tests
│   ├── api           // contain file test for each api
│   ├── .env          // config DB test
│   └── conftest.py   // config for testing
├── generate          // generate data
├── third_party       // like kafka, aws kinesis,...
├── library           // library for 3 party
├── .gitignore
├── alembic.ini
├── docker-compose.yaml
├── Dockerfile
├── env.example
├── logging.ini     // config logging
├── README.md
└── requirements.txt
```

## Migration

- `alembic revision -m "your message" --autogenerate`   # Create migration versions depend on changed in models
- `alembic upgrade head`   # Upgrade to last version migration
- `alembic downgrade -1`   # Downgrade to before version migration

## How to remove cache submodule

```
https://stackoverflow.com/questions/4185365/no-submodule-mapping-found-in-gitmodule-for-a-path-thats-not-a-submodule
```
## Health check 
- health check app: /api/v1/healthcheck/live
- health check db: /api/v1/healthcheck/ready



