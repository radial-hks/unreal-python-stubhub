## PolylinesGraphicsEntity Objects

```python
class PolylinesGraphicsEntity(WdpStandardEntity)
```

Polylines Graphics Entity

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGraphicsEntity
- **File**: PolylinesGraphicsEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.PolylinesGraphicsEntity.set_polylines"></a>

#### set\_polylines

```python
def set_polylines(polylines: Array[PolylineGraphicsData]) -> None
```

x.set_polylines(polylines) -> None
Set Polylines

Args:
    polylines (Array[PolylineGraphicsData]):

<a id="unreal.PolylinesGraphicsEntity.remove_polylines"></a>

#### remove\_polylines

```python
def remove_polylines(guids: Array[Guid]) -> None
```

x.remove_polylines(guids) -> None
Remove Polylines

Args:
    guids (Array[Guid]):

<a id="unreal.PolylinesGraphicsEntity.remove_entities"></a>

#### remove\_entities

```python
def remove_entities(eids: Array[int]) -> None
```

x.remove_entities(eids) -> None
Remove Entities

Args:
    eids (Array[int64]):

<a id="unreal.PolylinesGraphicsEntity.get_polyline"></a>

#### get\_polyline

```python
def get_polyline(guid: Guid) -> Optional[PolylineGraphicsData]
```

x.get_polyline(guid) -> PolylineGraphicsData or None
Get Polyline

Args:
    guid (Guid): 

Returns:
    PolylineGraphicsData or None: 

    out_graphics_data (PolylineGraphicsData):

<a id="unreal.PolylinesGraphicsEntity.clear"></a>

#### clear

```python
def clear() -> None
```

x.clear() -> None
Clear

<a id="unreal.PolylinesGraphicsEntity.add_entities"></a>

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

<a id="unreal.PolylinesWidget"></a>