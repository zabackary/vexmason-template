# vexmason template repository

Simply click "Fork this Repository" to get started with
[vexmason](https://github.com/zabackary/vexmason), the VEX V5 Python bundler
that Just Works.

vexmason is a bundler that allows you to write modern, OOP, abstract Python code
and yet still use the VEXCode V5 build/upload tools maintained by VEX.

## Things to modify

- `.vscode/vexmason-config.json`  
  This contains the program name, description and defines.
- `.vscode/vexmason-local-config.json`  
  This file is gitignored, but you should use
  [`vexmason-local-config.example.json`](./.vscode/vexmason-local-config.example.json)
  as an example to get started. It contains the computer name (which you can use
  as a placeholder in the description like this: `{{ computer-name }}`) and the
  local defines overrides.
- `src/`  
  This is where your code lives!
