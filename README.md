# ETA - PROJETO FINAL
Avner Augusto dos Anjos - aaa4

## Summary
Com o objetivo de simular um código de produção, algumas features foram implementadas:
- Todas os métodos retornam apenas um dos 3 valores do tipo ReturnCode: STATUS_OK, STATUS_INVALID ou STATUS_ERROR.
- Informações adicionais podem ser vistas e verificadas pelos logs.
- O arquivo helper_functions contém alguns métodos ou enum auxiliares.
- Nos testes sãoo verificados os retornos das funçōes assim como os logs.
- Cada classe de test possui seu próprio seu setup, que é responsável por definir os parâmetros do objeto de teste.
## Setup

```bash
pip install -r requirements.txt
```

## Unittest

```bash
python -m unittest -v
```

## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest --cov-report term-missing --cov .
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```

### With `unittest`

To generate report:

```bash
python -m coverage run -m unittest
```

To view report in terminal:

```bash
python -m coverage report
```

To view report in HTML:

```bash
python -m coverage html
```

