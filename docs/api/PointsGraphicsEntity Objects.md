## PointsGraphicsEntity Objects

```python
class PointsGraphicsEntity(WdpStandardEntity)
```

Points Graphics Entity

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpGraphicsEntity
- **File**: PointsGraphicsEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]

<a id="unreal.PointsGraphicsEntity.set_points"></a>

#### set\_points

```python
def set_points(point_data: Array[PointGraphicsData]) -> None
```

x.set_points(point_data) -> None
Set Points

Args:
    point_data (Array[PointGraphicsData]):

<a id="unreal.PointsGraphicsEntity.set_point_image_color"></a>

#### set\_point\_image\_color

```python
def set_point_image_color(guid: Guid, in_color: LinearColor) -> None
```

x.set_point_image_color(guid, in_color) -> None
Set Point Image Color

Args:
    guid (Guid): 
    in_color (LinearColor):

<a id="unreal.PointsGraphicsEntity.remove_points"></a>

#### remove\_points

```python
def remove_points(guids: Array[Guid]) -> None
```

x.remove_points(guids) -> None
Remove Points

Args:
    guids (Array[Guid]):

<a id="unreal.PointsGraphicsEntity.remove_entities"></a>

#### remove\_entities

```python
def remove_entities(eids: Array[int]) -> None
```

x.remove_entities(eids) -> None
Remove Entities

Args:
    eids (Array[int64]):

<a id="unreal.PointsGraphicsEntity.get_point"></a>

#### get\_point

```python
def get_point(guid: Guid) -> Optional[PointGraphicsData]
```

x.get_point(guid) -> PointGraphicsData or None
Get Point

Args:
    guid (Guid): 

Returns:
    PointGraphicsData or None: 

    out_graphics_data (PointGraphicsData):

<a id="unreal.PointsGraphicsEntity.clear"></a>

#### clear

```python
def clear() -> None
```

x.clear() -> None
Clear

<a id="unreal.PointsGraphicsEntity.add_entities"></a>

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

<a id="unreal.PointsWidget"></a>