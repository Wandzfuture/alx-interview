0x06. Star Wars API

# Star Wars Characters Lister

This project contains a Node.js script that prints all characters of a Star Wars movie using the Star Wars API.

## Requirements

- Node.js (version 10.14.x)
- Request module

## Installation

1. Install Node.js:
   ```
   $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   $ sudo apt-get install -y nodejs
   ```

2. Install the semistandard style checker:
   ```
   $ sudo npm install semistandard --global
   ```

3. Install the request module:
   ```
   $ sudo npm install request --global
   $ export NODE_PATH=/usr/lib/node_modules
   ```

## Usage

```
$ ./0-starwars_characters.js <Movie_ID>
```

Where `<Movie_ID>` is the ID of the Star Wars movie you want to list characters from.

Example:
```
$ ./0-starwars_characters.js 3
```

This will list all characters from "Return of the Jedi" (Movie ID 3).

## File Descriptions

- `0-starwars_characters.js`: The main script that fetches and prints Star Wars characters.

## Style

This project follows the semistandard style guide (Standard + semicolons).

## Author

[Your Name]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
