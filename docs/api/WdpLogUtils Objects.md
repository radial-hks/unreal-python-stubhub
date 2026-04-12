## WdpLogUtils Objects

```python
class WdpLogUtils(BlueprintFunctionLibrary)
```

brief: WDP Log工具类

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpLog
- **File**: WdpLogUtils.h

<a id="unreal.WdpLogUtils.warning"></a>

#### warning

```python
@classmethod
def warning(cls,
            log_text: str,
            context: str = "",
            also_for_web: bool = False) -> None
```

X.warning(log_text, context="", also_for_web=False) -> None
Warning

Args:
    log_text (str): 
    context (str): 
    also_for_web (bool):

<a id="unreal.WdpLogUtils.log"></a>

#### log

```python
@classmethod
def log(cls,
        log_text: str,
        context: str = "",
        print_screen: bool = False,
        also_for_web: bool = False) -> None
```

X.log(log_text, context="", print_screen=False, also_for_web=False) -> None
Log

Args:
    log_text (str): 
    context (str): 
    print_screen (bool): 
    also_for_web (bool):

<a id="unreal.WdpLogUtils.get_debug_log"></a>

#### get\_debug\_log

```python
@classmethod
def get_debug_log(cls) -> str
```

X.get_debug_log() -> str
Get Debug Log

Returns:
    str:

<a id="unreal.WdpLogUtils.error_exit"></a>

#### error\_exit

```python
@classmethod
def error_exit(cls, log_text: str, context: str = "") -> None
```

X.error_exit(log_text, context="") -> None
Error Exit

Args:
    log_text (str): 
    context (str):

<a id="unreal.WdpLogUtils.error"></a>

#### error

```python
@classmethod
def error(cls,
          log_text: str,
          context: str = "",
          also_for_web: bool = False) -> None
```

X.error(log_text, context="", also_for_web=False) -> None
Error

Args:
    log_text (str): 
    context (str): 
    also_for_web (bool):

<a id="unreal.MovieSceneSpawnableChaosCacheBinding"></a>