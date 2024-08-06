# Rolodex Reader

 Rolodex Reader is a simple project that processes a bulk of personal information in various formats and normalizing them into standard JSON format.

## Documentation

* [Getting Started](GETTING_STARTED.md) - Shows how to get project setup
* [Rolodex Python Notebook](docs\rolodex_notebook.ipynb) - Shows how project was constructed

## Running the Rolodex

### Default

```bash
$ python rolodex_input.py
Reading input from data.in
Processing input...
Writing output to result.out
```

### Using Different Input and Output Files

```bash
$ python rolodex_input.py -i new_input.in -o new_output.out
Reading input from new_input.in
Processing input...
Writing output to new_output.out
```

### Available commands

```bash
$ python rolodex_input.py --help
Usage: rolodex_input.py [OPTIONS]

  Starts processing the rolodex

Options:
  -i, --input_file PATH   Path to data file for
                          input
  -o, --output_file PATH  Path to output file
  --help                  Show this message and
                          exit.
```

## Running Python Notebook

To run the python notebook, use the following command from root of project:
```bash
$ jupyter notebook
```

After a few moments, your browser should open to the root of the project.
Navigate to the `docs/` folder and click on the `rolodex_notebook.ipynb` file

## Running Tests

```bash
$ pytest tests/ -v  
============================= test session starts =============================
platform win32 -- Python 2.7.13, pytest-3.2.0, py-1.4.34, pluggy-0.4.0 -- d:\git                                                                                                            s\rolodex-challenge\.venv\scripts\python.exe
cachedir: .cache
rootdir: D:\gits\rolodex-challenge, inifile:
plugins: cov-2.5.1
collecting ... collected 4 items

tests/components/test_entry.py::test_create_ouput PASSED
tests/utils/test_process.py::test_process_entries PASSED
tests/utils/test_process.py::test_process_valid_entries PASSED
tests/utils/test_process.py::tests_process_invalid_entries PASSED

========================== 4 passed in 0.10 seconds ===========================
```
