## WdpLocalToGlobalGeoRefResult Objects

```python
class WdpLocalToGlobalGeoRefResult(ResultBase)
```

Wdp Local to Global Geo Ref Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: ApplicationAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``to`` (Array[Vector]):  [Read-Write]

<a id="unreal.WdpLocalToGlobalGeoRefResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             to: Array[Vector] = []) -> None
```

<a id="unreal.WdpLocalToGlobalGeoRefResult.to"></a>

#### to

```python
@property
def to() -> Array[Vector]
```

(Array[Vector]):  [Read-Write]

<a id="unreal.WdpLocalToGlobalGeoRefResult.to"></a>

#### to

```python
@to.setter
def to(value: Array[Vector]) -> None
```

<a id="unreal.WdpCreateCADGeoRefParams"></a>