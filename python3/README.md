# Sinopsis

This directory compiles a collection of Software Design Patterns implemented in Python3.

# Usage

```bash
pipenv [--python /path/to/python3] install
pipenv shell
[<INFO|DEBUG>=1] python <category>/<pattern>/pattern.py
```

# Structure

Each pattern has its own directory containing one **pattern**.py file and at least 1 'example.py' file.
The **pattern** file is just a simple implementation with inline documentation describing the pattern.
The **example** files are more complex implementations with less or no inline documentation.
All examples come with their own Test Cases.
