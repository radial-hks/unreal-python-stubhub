## RamaVictoryPluginCreateProcessPipe Objects

```python
class RamaVictoryPluginCreateProcessPipe(Object)
```

Made With Love By Rama for Use with
VictoryCreateProc: So that you can receive feedback from your processes. ♥ Rama

**C++ Source:**

- **Plugin**: VictoryBPLibrary
- **Module**: VictoryBPLibrary
- **File**: VictoryBPFunctionLibrary.h

<a id="unreal.RamaVictoryPluginCreateProcessPipe.read_from_pipe"></a>

#### read\_from\_pipe

```python
def read_from_pipe() -> Optional[str]
```

x.read_from_pipe() -> str or None
This has exec pins because it is an expensive action and the output is saved/cached on the output pin, whereas a Pure node would repeat the action many times, each time node is accessed.

Returns:
    str or None: false if the pipes were not created yet ♥ Rama

    pipe_contents (str):

<a id="unreal.RamaVictoryPluginCreateProcessPipe.pipe_is_valid"></a>

#### pipe\_is\_valid

```python
def pipe_is_valid() -> bool
```

x.pipe_is_valid() -> bool
Pipe Is Valid

Returns:
    bool:

<a id="unreal.RamaVictoryPluginCreateProcessPipe.create_pipe"></a>

#### create\_pipe

```python
def create_pipe() -> bool
```

x.create_pipe() -> bool
Create Pipe

Returns:
    bool:

<a id="unreal.RamaVictoryPluginCreateProcessPipe.close_pipe"></a>

#### close\_pipe

```python
def close_pipe() -> None
```

x.close_pipe() -> None
Close Pipe

<a id="unreal.VictoryBPFunctionLibrary"></a>