## Point2DResult Objects

```python
class Point2DResult(ResultBase)
```

Point 2DResult

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: ApiParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``point`` (Vector2D):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.Point2DResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             point: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.Point2DResult.point"></a>

#### point

```python
@property
def point() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.Point2DResult.point"></a>

#### point

```python
@point.setter
def point(value: Vector2D) -> None
```

<a id="unreal.APIEventSwitch"></a>