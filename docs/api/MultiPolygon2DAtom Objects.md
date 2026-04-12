## MultiPolygon2DAtom Objects

```python
class MultiPolygon2DAtom(EntityAtomBase)
```

Multi Polygon 2DAtom

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGeometryEntity
- **File**: MultiPolygon2DAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``polygon_coord_z`` (Array[double]):  [Read-Write]
- ``polygons`` (Array[WdpPolygon2D]):  [Read-Write]

<a id="unreal.MultiPolygon2DAtom.polygons"></a>

#### polygons

```python
@property
def polygons() -> Array[WdpPolygon2D]
```

(Array[WdpPolygon2D]):  [Read-Only]

<a id="unreal.MultiPolygon2DAtom.polygon_coord_z"></a>

#### polygon\_coord\_z

```python
@property
def polygon_coord_z() -> Array[float]
```

(Array[double]):  [Read-Only]

<a id="unreal.Point2DEntityAtom"></a>