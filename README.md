# encrypt

This is a learning exsample for encrypt and decrypt with RSA by Python.

## Getting Started

```
git clone git@github.com:yamamuteki/encrypt.git
cd encrypt
```

### Use with local Python

```
pip install -r requirements.txt
echo 'hello world!' | python encrypt.py | python decrypt.py
```

### Use with Docker

```
docker run -v $(pwd):/home python:3.9 /bin/bash -c "cd home && pip install -r requirements.txt && echo 'hello world!' | python encrypt.py | python decrypt.py"
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
