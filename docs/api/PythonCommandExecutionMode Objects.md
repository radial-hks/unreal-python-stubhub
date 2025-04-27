## PythonCommandExecutionMode Objects

```python
class PythonCommandExecutionMode(EnumBase)
```

Controls the execution mode used for the Python command.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PythonScriptTypes.h

<a id="unreal.PythonCommandExecutionMode.EXECUTE_FILE"></a>

#### EXECUTE_FILE

0: Execute the Python command as a file. This allows you to execute either a literal Python script containing multiple statements, or a file with optional arguments.

<a id="unreal.PythonCommandExecutionMode.EXECUTE_STATEMENT"></a>

#### EXECUTE_STATEMENT

1: Execute the Python command as a single statement. This will execute a single statement and print the result. This mode cannot run files.

<a id="unreal.PythonCommandExecutionMode.EVALUATE_STATEMENT"></a>

#### EVALUATE_STATEMENT

2: Evaluate the Python command as a single statement. This will evaluate a single statement and return the result. This mode cannot run files.

<a id="unreal.PythonFileExecutionScope"></a>