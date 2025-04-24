# Getting started

0. Get ollama ready
```shell
ollama serve
```
then, get your model
```shell
ollama pull gemma3:1b
```

1. Create environment
```shell
python -m venv .venv
```

2. Activate environment
```shell
. .venv/bin/activate
```

3. Install dependencies
```shell
pip install -r requirements.txt
```

4. Run tests
```shell
make test
```
or
```shell
pytest -s ./tests
```
