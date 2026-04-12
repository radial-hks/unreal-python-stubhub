## WdpEndActionParams Objects

```python
class WdpEndActionParams(ParamsBase)
```

Wdp End Action Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpActionManagerAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``is_cancel`` (bool):  [Read-Write]

<a id="unreal.WdpEndActionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(is_cancel: bool = False) -> None
```

<a id="unreal.WdpEndActionParams.is_cancel"></a>

#### is\_cancel

```python
@property
def is_cancel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpEndActionParams.is_cancel"></a>

#### is\_cancel

```python
@is_cancel.setter
def is_cancel(value: bool) -> None
```

<a id="unreal.WdpGetCurrentActionResult"></a>