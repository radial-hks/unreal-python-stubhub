## PointEntity Objects

```python
class PointEntity(WdpStandardEntity)
```

Point Entity

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGeometryEntity
- **File**: PointEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.PointEntity.set_point"></a>

#### set\_point

```python
def set_point(new_point: Vector) -> None
```

x.set_point(new_point) -> None
Set Point

Args:
    new_point (Vector):

<a id="unreal.PointEntity.get_point"></a>

#### get\_point

```python
def get_point() -> Vector
```

x.get_point() -> Vector
Get Point

Returns:
    Vector:

<a id="unreal.Polygon2DEntity"></a>