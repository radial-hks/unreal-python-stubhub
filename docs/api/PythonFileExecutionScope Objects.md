## PythonFileExecutionScope Objects

```python
class PythonFileExecutionScope(EnumBase)
```

Controls the scope used when executing Python files.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PythonScriptTypes.h

<a id="unreal.PythonFileExecutionScope.PRIVATE"></a>

#### PRIVATE

0: Execute the Python file with its own unique locals and globals dict to isolate any changes it makes to the environment (like imports).

<a id="unreal.PythonFileExecutionScope.PUBLIC"></a>

#### PUBLIC

1: Execute the Python file with the shared locals and globals dict as used by the console, so that executing it behaves as if you'd ran the file contents directly in the console.

<a id="unreal.InterchangePropertyTracks"></a>