## Polyline2DEntity Objects

```python
class Polyline2DEntity(WdpStandardEntity)
```

Polyline 2DEntity

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGeometryEntity
- **File**: Polyline2DEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.Polyline2DEntity.set_polyline"></a>

#### set\_polyline

```python
def set_polyline(new_polyline: WdpPolyline2D) -> None
```

x.set_polyline(new_polyline) -> None
Set Polyline

Args:
    new_polyline (WdpPolyline2D):

<a id="unreal.Polyline2DEntity.get_polyline"></a>

#### get\_polyline

```python
def get_polyline() -> WdpPolyline2D
```

x.get_polyline() -> WdpPolyline2D
Get Polyline

Returns:
    WdpPolyline2D:

<a id="unreal.PolylineEntity"></a>