## ErrorCollectorForWeb Objects

```python
class ErrorCollectorForWeb(BlueprintFunctionLibrary)
```

UE内部异常信息收集器，将会在API返回值的message字段中返回给前端

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpLog
- **File**: ErrorCollectorForWeb.h

<a id="unreal.ErrorCollectorForWeb.add"></a>

#### add

```python
@classmethod
def add(cls, error_msg: str) -> None
```

X.add(error_msg) -> None
Add

Args:
    error_msg (str):

<a id="unreal.WdpLogUtils"></a>