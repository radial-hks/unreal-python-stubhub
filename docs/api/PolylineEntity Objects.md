## PolylineEntity Objects

```python
class PolylineEntity(WdpStandardEntity)
```

Polyline Entity

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGeometryEntity
- **File**: PolylineEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.PolylineEntity.set_polyline"></a>

#### set\_polyline

```python
def set_polyline(new_polyline: WdpPolyline) -> None
```

x.set_polyline(new_polyline) -> None
Set Polyline

Args:
    new_polyline (WdpPolyline):

<a id="unreal.PolylineEntity.get_polyline"></a>

#### get\_polyline

```python
def get_polyline() -> WdpPolyline
```

x.get_polyline() -> WdpPolyline
Get Polyline

Returns:
    WdpPolyline:

<a id="unreal.PointsGraphicsEntity"></a>