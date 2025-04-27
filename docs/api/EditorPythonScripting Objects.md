## EditorPythonScripting Objects

```python
class EditorPythonScripting(BlueprintFunctionLibrary)
```

Utility class for Python scripting functionality.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: EditorPythonScriptingLibrary.h

<a id="unreal.EditorPythonScripting.set_keep_python_script_alive"></a>

#### set_keep_python_script_alive

```python
@classmethod
def set_keep_python_script_alive(cls, new_keep_alive: bool) -> None
```

X.set_keep_python_script_alive(new_keep_alive) -> None
Sets the bKeepPythonScriptAlive flag.

If this is false (default), it will close the editor during the next tick (when executing a Python script in the editor-environment using the UnrealEditor-Cmd commandline tool).
If this is true, it will not close the editor by itself, and you will have to close it manually, either by setting this value to false again, or by calling a function like unreal.SystemLibrary.quit_editor().

Args:
    new_keep_alive (bool): The new value of the bKeepPythonScriptAlive flag.

<a id="unreal.EditorPythonScripting.get_keep_python_script_alive"></a>

#### get_keep_python_script_alive

```python
@classmethod
def get_keep_python_script_alive(cls) -> bool
```

X.get_keep_python_script_alive() -> bool
Returns the value of the bKeepPythonScriptAlive flag.

If this is false (default), it will close the editor during the next tick (when executing a Python script in the editor-environment using the UnrealEditor-Cmd commandline tool).
If this is true, it will not close the editor by itself, and you will have to close it manually, either by setting this value to false again, or by calling a function like unreal.SystemLibrary.quit_editor().

Returns:
    bool: The current value of the bKeepPythonScriptAlive flag.

<a id="unreal.PyTestStructLibrary"></a>