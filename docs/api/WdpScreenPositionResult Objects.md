## WdpScreenPositionResult Objects

```python
class WdpScreenPositionResult(ResultBase)
```

Wdp Screen Position Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``to`` (Array[Vector2D]):  [Read-Write]

<a id="unreal.WdpScreenPositionResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             to: Array[Vector2D] = []) -> None
```

<a id="unreal.WdpScreenPositionResult.to"></a>

#### to

```python
@property
def to() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.WdpScreenPositionResult.to"></a>

#### to

```python
@to.setter
def to(value: Array[Vector2D]) -> None
```

<a id="unreal.WdpGlobalSettingsFPSParams"></a>