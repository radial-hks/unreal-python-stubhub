## TransactionBoolResult Objects

```python
class TransactionBoolResult(ResultBase)
```

Transaction Bool Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpTransactionAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_do`` (bool):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.TransactionBoolResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             can_do: bool = False) -> None
```

<a id="unreal.TransactionBoolResult.can_do"></a>

#### can\_do

```python
@property
def can_do() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransactionBoolResult.can_do"></a>

#### can\_do

```python
@can_do.setter
def can_do(value: bool) -> None
```

<a id="unreal.DCPAssetInfo"></a>