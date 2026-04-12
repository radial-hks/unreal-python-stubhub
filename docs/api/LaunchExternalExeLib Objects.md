## LaunchExternalExeLib Objects

```python
class LaunchExternalExeLib(BlueprintFunctionLibrary)
```

Launch External Exe Lib

**C++ Source:**

- **Plugin**: VFVideoPlayer
- **Module**: VFVideoPlayer
- **File**: LaunchExternalExeLib.h

<a id="unreal.LaunchExternalExeLib.open_exe"></a>

#### open\_exe

```python
@classmethod
def open_exe(cls, exe_url: str, args: str) -> bool
```

X.open_exe(exe_url, args) -> bool
Open Exe

Args:
    exe_url (str): 
    args (str): 

Returns:
    bool:

<a id="unreal.LaunchExternalExeLib.kill_process_by_name"></a>

#### kill\_process\_by\_name

```python
@classmethod
def kill_process_by_name(cls, process_name: str) -> None
```

X.kill_process_by_name(process_name) -> None
Kill Process by Name

Args:
    process_name (str):

<a id="unreal.LaunchExternalExeLib.is_exe_running"></a>

#### is\_exe\_running

```python
@classmethod
def is_exe_running(cls) -> bool
```

X.is_exe_running() -> bool
Is Exe Running

Returns:
    bool:

<a id="unreal.LaunchExternalExeLib.close_exe"></a>

#### close\_exe

```python
@classmethod
def close_exe(cls) -> None
```

X.close_exe() -> None
Close Exe

<a id="unreal.VFPlayerActor"></a>