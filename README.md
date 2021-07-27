# encrypt

This is a learning exsample for encrypt and decrypt with RSA by Python.

## Getting Started

```
git clone git@github.com:yamamuteki/encrypt.git
cd encrypt
pip install -r requirements.txt
ssh-keygen -f rsa_key -t rsa -b 4096
```

### Use with local Python

```
echo 'hello world!' | python encrypt.py | python decrypt.py
```

### Use with Docker

```
docker run -v $(pwd):/home python:3.9 /bin/bash -c "cd home && pip install -r requirements.txt && echo 'hello world!' | python encrypt.py | python decrypt.py"
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
