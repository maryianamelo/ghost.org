# Ghost.org Test Automation Project

## How to run

First you must have install python in your system by following this link: (https://www.tutorialspoint.com/how-to-install-python-in-windows)

After that download the repository to a folder, go to behave folder and run `pip install -r requirements.txt` to install all of the Python modules and packages listed in the requirements.txt file.

If pip is not installed, please verify wich version you have. After check pip version, run `pip[your_version] install -r requirements.txt`

## How to run all features

1. Open the cmd
2. Go to the folder you have downloaded the project
3. Open behave folder
4. Run `behave`

## How to run a scenario in debug mode using Visual Studio Code

Add this vscode launch code to your vscode "Run and Debug" mode and add a tag "@debug" to the scenario you want to execute.

```
{
    "configurations": [
        {
            "name": "Python: Behave current file",
            "type": "python",
            "request": "launch",
            "module": "behave",
            "cwd": "${workspaceFolder}\\behave",
            "console": "integratedTerminal",
            "env": {"PYTHONPATH": "${cwd}"},
            "args": [
                "--tags=@debug"
            ]
        }
    ]
}

```
