## PythonScriptLibrary Objects

```python
class PythonScriptLibrary(BlueprintFunctionLibrary)
```

Python Script Library

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PythonScriptLibrary.h

<a id="unreal.PythonScriptLibrary.is_python_available"></a>

#### is_python_available

```python
@classmethod
def is_python_available(cls) -> bool
```

X.is_python_available() -> bool
Check to see whether Python support is available in the current build.

Returns:
    bool:

<a id="unreal.PythonScriptLibrary.execute_python_command_ex"></a>

#### execute_python_command_ex

```python
@classmethod
def execute_python_command_ex(
    cls,
    python_command: str,
    execution_mode: PythonCommandExecutionMode = PythonCommandExecutionMode.
    EXECUTE_FILE,
    file_execution_scope: PythonFileExecutionScope = PythonFileExecutionScope.
    PRIVATE
) -> Optional[Tuple[str, Array[PythonLogOutputEntry]]]
```

X.execute_python_command_ex(python_command, execution_mode=PythonCommandExecutionMode.EXECUTE_FILE, file_execution_scope=PythonFileExecutionScope.PRIVATE) -> (command_result=str, log_output=Array[PythonLogOutputEntry]) or None
Execute the given Python command.

Args:
    python_command (str): The command to run. This may be literal Python code, or a file (with optional arguments) that you want to run.
    execution_mode (PythonCommandExecutionMode): Controls the mode used to execute the command.
    file_execution_scope (PythonFileExecutionScope): Controls the scope used when executing Python files.

Returns:
    tuple or None: true if the command ran successfully, false if there were errors (the output log will show the errors).

    command_result (str): The result of running the command. On success, for EvaluateStatement mode this will be the actual result of running the command, and will be None in all other cases. On failure, this will be the error information (typically a Python exception trace).

    log_output (Array[PythonLogOutputEntry]): The log output captured while running the command.

<a id="unreal.PythonScriptLibrary.execute_python_command"></a>

#### execute_python_command

```python
@classmethod
def execute_python_command(cls, python_command: str) -> bool
```

X.execute_python_command(python_command) -> bool
Execute the given Python command.

Args:
    python_command (str): The command to run. This may be literal Python code, or a file (with optional arguments) that you want to run.

Returns:
    bool: true if the command ran successfully, false if there were errors (the output log will show the errors).

<a id="unreal.PythonObjectHandle"></a>