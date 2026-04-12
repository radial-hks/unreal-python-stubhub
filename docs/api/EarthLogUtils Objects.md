## EarthLogUtils Objects

```python
class EarthLogUtils(BlueprintFunctionLibrary)
```

brief: WDP Log工具类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthCore
- **File**: EarthLogUtils.h

<a id="unreal.EarthLogUtils.warning"></a>

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

<a id="unreal.EarthLogUtils.log"></a>

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

<a id="unreal.EarthLogUtils.error_exit"></a>

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

<a id="unreal.EarthLogUtils.error"></a>

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

<a id="unreal.EarthScene"></a>