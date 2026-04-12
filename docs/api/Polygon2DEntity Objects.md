## Polygon2DEntity Objects

```python
class Polygon2DEntity(WdpStandardEntity)
```

Polygon 2DEntity

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGeometryEntity
- **File**: Polygon2DEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.Polygon2DEntity.set_polygon"></a>

#### set\_polygon

```python
def set_polygon(new_polygon: WdpPolygon2D) -> None
```

x.set_polygon(new_polygon) -> None
Set Polygon

Args:
    new_polygon (WdpPolygon2D):

<a id="unreal.Polygon2DEntity.get_polygon"></a>

#### get\_polygon

```python
def get_polygon() -> WdpPolygon2D
```

x.get_polygon() -> WdpPolygon2D
Get Polygon

Returns:
    WdpPolygon2D:

<a id="unreal.PolygonEntity"></a>