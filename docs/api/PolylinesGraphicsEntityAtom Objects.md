## PolylinesGraphicsEntityAtom Objects

```python
class PolylinesGraphicsEntityAtom(EntityAtomBase)
```

Polylines Graphics Entity Atom

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGraphicsEntity
- **File**: PolylinesGraphicsEntityAtom.h

<a id="unreal.PolylinesGraphicsEntityAtom.remove_entities"></a>

#### remove\_entities

```python
def remove_entities(eids: Array[int]) -> None
```

x.remove_entities(eids) -> None
Remove Entities

Args:
    eids (Array[int64]):

<a id="unreal.PolylinesGraphicsEntityAtom.add_entities"></a>

#### add\_entities

```python
def add_entities(eids: Array[int],
                 coord_z_ref: Coord_Z_Ref = Coord_Z_Ref.ALTITUDE,
                 coord_z: float = 0.000000) -> None
```

x.add_entities(eids, coord_z_ref=Coord_Z_Ref.ALTITUDE, coord_z=0.000000) -> None
Add Entities

Args:
    eids (Array[int64]): 
    coord_z_ref (Coord_Z_Ref): 
    coord_z (double):

<a id="unreal.WdpCameraSettingsAtom"></a>