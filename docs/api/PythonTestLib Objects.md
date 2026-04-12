## PythonTestLib Objects

```python
class PythonTestLib(BlueprintFunctionLibrary)
```

Python Test Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonTestLib.h

<a id="unreal.PythonTestLib.get_logs"></a>

#### get\_logs

```python
@classmethod
def get_logs(cls,
             number_limit: int = -1,
             category_regex: str = "") -> Array[str]
```

X.get_logs(number_limit=-1, category_regex="") -> Array[str]
Get Logs from Log History
note: added in v1.0.9

Args:
    number_limit (int32): Logs Maximum Number Limit, -1 for No Limit
    category_regex (str): Regular expression for category filter.

Returns:
    Array[str]: The Logs with timestamps and frame identifier (FrameCounter % 1000)

<a id="unreal.PythonTestLib.delay_call"></a>

#### delay\_call

```python
@classmethod
def delay_call(cls,
               python_cmd: str,
               delay_seconds: float,
               on_finished_cmd: str = "",
               repeat_count: int = 1) -> Guid
```

X.delay_call(python_cmd, delay_seconds, on_finished_cmd="", repeat_count=1) -> Guid
Push a 'delay call' python command.
note: added in v1.0.9

Args:
    python_cmd (str): Python command in string
    delay_seconds (float): Time seconds for delay call
    on_finished_cmd (str): Python command in string, when delay call finished
    repeat_count (int32): The number of repeated calls

Returns:
    Guid: Guid

<a id="unreal.PythonTestLib.clear_log_buffer"></a>

#### clear\_log\_buffer

```python
@classmethod
def clear_log_buffer(cls) -> int
```

X.clear_log_buffer() -> int32
Clear the Log History buffers. The Log history is different with log in Output Console window. Clear History in Output Log Window will not clear the History Buffer
note: added in v1.0.9

Returns:
    int32: The number of Cleared logs

<a id="unreal.PythonTestLib.cancel_delay_call_by_id"></a>

#### cancel\_delay\_call\_by\_id

```python
@classmethod
def cancel_delay_call_by_id(cls, guid: Guid) -> bool
```

X.cancel_delay_call_by_id(guid) -> bool
Cancel specified  delay call
note: added in v1.0.10

Args:
    guid (Guid): 

Returns:
    bool: None

<a id="unreal.PythonTestLib.cancel_delay_call"></a>

#### cancel\_delay\_call

```python
@classmethod
def cancel_delay_call(cls) -> bool
```

X.cancel_delay_call() -> bool
Cancel all running delay call
note: added in v1.0.9

Returns:
    bool: None

<a id="unreal.PythonTextureLib"></a>