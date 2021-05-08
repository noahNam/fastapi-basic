# What is fastapi-basic?
- fastapi practice
- know how to use the fastapi
- version
    * python : 3.8
    * fastapi : 0.63
    
# Usage
## [poetry](https://python-poetry.org/)
* install poetry : `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
* set env
```
$ vi ~/.zshrc
  export PATH="$HOME/.poetry/bin:$PATH"
```
* install packages in poetry.lock : `poetry install`
* install package : `poetry add {package name}`
* uninstall package : `pipenv remove {package name}`
* dependencies update - newest version : `poetry update`
* show pakage : `poery show`
* env info : `poery env info`

# How to use
```
$ uvicorn main:app --reload
```