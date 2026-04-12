## WdpGetMeshSizeByIdResult Objects

```python
class WdpGetMeshSizeByIdResult(ResultBase)
```

Wdp Get Mesh Size by Id Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: WdpAssetAPI
- **File**: WdpAssetAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``size`` (Vector):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.WdpGetMeshSizeByIdResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             size: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WdpGetMeshSizeByIdResult.size"></a>

#### size

```python
@property
def size() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WdpGetMeshSizeByIdResult.size"></a>

#### size

```python
@size.setter
def size(value: Vector) -> None
```

<a id="unreal.TestResult"></a>