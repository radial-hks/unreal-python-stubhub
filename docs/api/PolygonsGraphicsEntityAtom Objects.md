## PolygonsGraphicsEntityAtom Objects

```python
class PolygonsGraphicsEntityAtom(EntityAtomBase)
```

Polygons Graphics Entity Atom

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGraphicsEntity
- **File**: PolygonsGraphicsEntityAtom.h

<a id="unreal.PolygonsGraphicsEntityAtom.remove_entities"></a>

#### remove\_entities

```python
def remove_entities(eids: Array[int]) -> None
```

x.remove_entities(eids) -> None
Remove Entities

Args:
    eids (Array[int64]):

<a id="unreal.PolygonsGraphicsEntityAtom.add_entities"></a>

#### add\_entities

```python
def add_entities(eids: Array[int],
                 coord_z: float = 0.000000,
                 coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.ALTITUDE) -> None
```

x.add_entities(eids, coord_z=0.000000, coord_z_ref=Coord_Z_Ref.ALTITUDE) -> None
Add Entities

Args:
    eids (Array[int64]): 
    coord_z (double): 
    coord_z_ref (Coord_Z_Ref):

<a id="unreal.PolylinesGraphicsEntityAtom"></a>