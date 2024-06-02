name: Publish json_to_table to PyPi
on: push

jobs:
  build:
    name: Build and publish
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install setuptools wheel twine

    - name: Build and publish
      run: |
        python setup.py sdist bdist_wheel
        python -m twine upload dist/*
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
