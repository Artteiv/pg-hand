Nothing

## FastAPI Quickstart

### Run locally

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or use the Makefile:

```bash
make run
```

The API will be available at:
- Main API: http://localhost:8000
- Health check: http://localhost:8000/health
- Interactive docs: http://localhost:8000/docs

### Run tests

Execute the test suite:

```bash
pytest
```

Or use the Makefile:

```bash
make test
```
