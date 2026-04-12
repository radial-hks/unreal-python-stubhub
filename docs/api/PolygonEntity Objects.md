## PolygonEntity Objects

```python
class PolygonEntity(WdpStandardEntity)
```

Polygon Entity

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGeometryEntity
- **File**: PolygonEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.PolygonEntity.set_polygon"></a>

#### set\_polygon

```python
def set_polygon(new_polygon: WdpPolygon) -> None
```

x.set_polygon(new_polygon) -> None
Set Polygon

Args:
    new_polygon (WdpPolygon):

<a id="unreal.PolygonEntity.get_polygon"></a>

#### get\_polygon

```python
def get_polygon() -> WdpPolygon
```

x.get_polygon() -> WdpPolygon
Get Polygon

Returns:
    WdpPolygon:

<a id="unreal.Polyline2DEntity"></a>