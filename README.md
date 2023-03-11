<div align="center">
  <h1>AirBnB clone - The Console <img src="https://i.imgur.com/elr4ah9.png" width=55 align=center> </h1>
  <h4>
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#storage">Storage</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#console">Console</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#execution">Execution</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#tests">Tests</a>
  </h4>
</div>

<img align="center" src="https://i.imgur.com/MQq3ABc.png" alt="Logo">

## Description

This project is the first version of the AirBnB project, which is an AirBnB clone that includes design, layout, infrastructure and database. In this repository you will find the AirBnB console, which executes specific commands (shown below) to make specific actions.

<img src="https://i.imgur.com/4biBGlj.png" alt="Project">

## Code Style

[Pycodestyle](https://pypi.org/project/pycodestyle/) was taken into account and implemented for all files.

## Storage

The [`FileStorage`](./models/engine/file_storage.py) class is in charge of managing the storage through a JSON file (`file.json`), the instances are created, updated or deleted, all this through a FileStorage instance called `storage`.

## Console

The console is used to manage the storage of class instances (`file.json`), this console can be used and executed in two ways, which are interactive and non-interactive mode.

The following table shows all the commands for storage management and explains how to use them by its format:

| Command     | Description | Format |
| ----------- |:------------| :-------|
| help        | Shows all allowed commands or gives information about a specific command. | `help` / `help <command>` |
| quit or EOF | Exits the program. | `quit` |
| create      | Creates a new instance. | `create <classname>` |
| show        | Shows a specific instance by its `classname` and its `id`. | `show <classname> <id>` |
| all         | Displays all stored instances or all stored instances of a specific class by its `classname`. | `all` / `all <classname>` |
| update      | Updates an instance (adds or modifies attributes) by its `classname`, `id`, `attribute` and its `value` to add/modify.  | `update <classname> <id> <attribute> <attrvalue>` |
| destroy     | Deletes an instance by its `classname` and its `id`. | `destroy <classname> <id>` |

## Execution

`Interactive mode`

```shell
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$
```

`Non-Interactive Mode`

```shell
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```

`Examples using the Hbnb console`

Console execution and `help` command implementation to get information about `quit` command:

<img src="https://i.imgur.com/DCpKxZa.gif" width=550 alt="Example gif">

`Create`, `update` and `show` command implementation to create and display a new instance:

<img src="https://i.imgur.com/SZQqSYb.gif" width=550 alt="Example gif">

`Create`, `destroy` and `all` command implementation to display how the `destroy` command works:

<img src="https://i.imgur.com/Auuj3TI.gif" width=550 alt="Example gif">

## Tests

Tests were developed and implemented for all the classes of the project using `unittest` in a different test environment, in order not to modify the JSON storage working with a file named `test_file.json`, which at the end of the tests will be deleted. All tests are in [this directory](./tests).

To test the classes built in this project this command can be executed:

```
python3 -m unittest discover tests
```

To execute a specific test, the next command can be run with the specific path, as it is shown:

```
python3 -m unittest tests/test_models/test_base_model.py
```

## Authors
| [<img src="https://avatars.githubusercontent.com/u/114111326?v=4" width=85><br><sub> Juan Esteban Duque </sub>](https://github.com/Juanesduque1) | [<img src="https://avatars.githubusercontent.com/u/95534180?v=4" width=85><br><sub> Felipe Villamizar </sub>](https://github.com/felipevcc) |
| :---: | :---: |
