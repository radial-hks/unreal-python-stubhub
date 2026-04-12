## CreateGeometryEntitiesResult Objects

```python
class CreateGeometryEntitiesResult(ResultBase)
```

Create Geometry Entities Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: ApiParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``point_eids`` (Array[str]):  [Read-Write]
- ``polygon2d_eids`` (Array[str]):  [Read-Write]
- ``polyline_eids`` (Array[str]):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.CreateGeometryEntitiesResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             point_eids: Array[str] = [],
             polyline_eids: Array[str] = [],
             polygon2d_eids: Array[str] = []) -> None
```

<a id="unreal.CreateGeometryEntitiesResult.point_eids"></a>

#### point\_eids

```python
@property
def point_eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.CreateGeometryEntitiesResult.point_eids"></a>

#### point\_eids

```python
@point_eids.setter
def point_eids(value: Array[str]) -> None
```

<a id="unreal.CreateGeometryEntitiesResult.polyline_eids"></a>

#### polyline\_eids

```python
@property
def polyline_eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.CreateGeometryEntitiesResult.polyline_eids"></a>

#### polyline\_eids

```python
@polyline_eids.setter
def polyline_eids(value: Array[str]) -> None
```

<a id="unreal.CreateGeometryEntitiesResult.polygon2d_eids"></a>

#### polygon2d\_eids

```python
@property
def polygon2d_eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.CreateGeometryEntitiesResult.polygon2d_eids"></a>

#### polygon2d\_eids

```python
@polygon2d_eids.setter
def polygon2d_eids(value: Array[str]) -> None
```

<a id="unreal.Point2DResult"></a>