## GetTransactionResult Objects

```python
class GetTransactionResult(ResultBase)
```

Get Transaction Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpTransactionAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``transaction_list`` (Array[str]):  [Read-Write]

<a id="unreal.GetTransactionResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             transaction_list: Array[str] = []) -> None
```

<a id="unreal.GetTransactionResult.transaction_list"></a>

#### transaction\_list

```python
@property
def transaction_list() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.GetTransactionResult.transaction_list"></a>

#### transaction\_list

```python
@transaction_list.setter
def transaction_list(value: Array[str]) -> None
```

<a id="unreal.TransactionBoolResult"></a>