## PythonLogOutputEntry Objects

```python
class PythonLogOutputEntry(StructBase)
```

Log output entry captured from Python.

**C++ Source:**

- **Plugin**: PythonScriptPlugin
- **Module**: PythonScriptPlugin
- **File**: PythonScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``output`` (str):  [Read-Only] The log output string.
- ``type`` (PythonLogOutputType):  [Read-Only] The type of the log output.

<a id="unreal.PythonLogOutputEntry.__init__"></a>

#### __init__

```python
def __init__(type: PythonLogOutputType = PythonLogOutputType.INFO,
             output: str = "") -> None
```

<a id="unreal.PythonLogOutputEntry.type"></a>

#### type

```python
@property
def type() -> PythonLogOutputType
```

(PythonLogOutputType):  [Read-Only] The type of the log output.

<a id="unreal.PythonLogOutputEntry.output"></a>

#### output

```python
@property
def output() -> str
```

(str):  [Read-Only] The log output string.

<a id="unreal.PyTestChildStruct"></a>