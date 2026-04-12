## WdpPicker Objects

```python
class WdpPicker(BlueprintFunctionLibrary)
```

Wdp Picker

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpPicker
- **File**: WdpPicker.h

<a id="unreal.WdpPicker.transform_position_by_z_ref"></a>

#### transform\_position\_by\_z\_ref

```python
@classmethod
def transform_position_by_z_ref(cls,
                                coord_z_ref: Coord_Z_Ref) -> Optional[Vector]
```

X.transform_position_by_z_ref(coord_z_ref) -> Vector or None
Transform Position by ZRef

Args:
    coord_z_ref (Coord_Z_Ref): 

Returns:
    Vector or None: 

    inout_point (Vector):

<a id="unreal.WdpPicker.pick_point"></a>

#### pick\_point

```python
@classmethod
def pick_point(
        cls,
        location: Vector,
        direction: Vector,
        pick_filter: WdpPickFilter = [[], True,
                                      []]) -> Optional[WdpPickResult]
```

X.pick_point(location, direction, pick_filter=[[], True, []]) -> WdpPickResult or None
Pick Point

Args:
    location (Vector): 
    direction (Vector): 
    pick_filter (WdpPickFilter): 

Returns:
    WdpPickResult or None: 

    out_result (WdpPickResult):

<a id="unreal.WdpPicker.pick_material"></a>

#### pick\_material

```python
@classmethod
def pick_material(
    cls,
    location: Vector,
    direction: Vector,
    pick_filter: WdpPickFilter = [[], True, []]
) -> Optional[WdpPickMaterialResult]
```

X.pick_material(location, direction, pick_filter=[[], True, []]) -> WdpPickMaterialResult or None
Pick Material

Args:
    location (Vector): 
    direction (Vector): 
    pick_filter (WdpPickFilter): 

Returns:
    WdpPickMaterialResult or None: 

    out_result (WdpPickMaterialResult):

<a id="unreal.WdpPicker.pick_entity"></a>

#### pick\_entity

```python
@classmethod
def pick_entity(
        cls,
        location: Vector,
        direction: Vector,
        pick_filter: WdpPickFilter = [[], True,
                                      []]) -> Optional[WdpPickResult]
```

X.pick_entity(location, direction, pick_filter=[[], True, []]) -> WdpPickResult or None
Pick Entity

Args:
    location (Vector): 
    direction (Vector): 
    pick_filter (WdpPickFilter): 

Returns:
    WdpPickResult or None: 

    out_result (WdpPickResult):

<a id="unreal.WdpPicker.pick_entities"></a>

#### pick\_entities

```python
@classmethod
def pick_entities(
    cls,
    location: Vector,
    direction: Vector,
    pick_filter: WdpPickFilter = [[], True,
                                  []]) -> Optional[Array[WdpPickResult]]
```

X.pick_entities(location, direction, pick_filter=[[], True, []]) -> Array[WdpPickResult] or None
Pick Entities

Args:
    location (Vector): 
    direction (Vector): 
    pick_filter (WdpPickFilter): 

Returns:
    Array[WdpPickResult] or None: 

    out_results (Array[WdpPickResult]):

<a id="unreal.WdpPicker.pick_components"></a>

#### pick\_components

```python
@classmethod
def pick_components(
    cls,
    location: Vector,
    direction: Vector,
    pick_filter: WdpPickFilter = [[], True,
                                  []]) -> Optional[Array[WdpPickResult]]
```

X.pick_components(location, direction, pick_filter=[[], True, []]) -> Array[WdpPickResult] or None
Pick Components

Args:
    location (Vector): 
    direction (Vector): 
    pick_filter (WdpPickFilter): 

Returns:
    Array[WdpPickResult] or None: 

    out_results (Array[WdpPickResult]):

<a id="unreal.WdpPicker.pick_component"></a>

#### pick\_component

```python
@classmethod
def pick_component(
        cls,
        location: Vector,
        direction: Vector,
        pick_filter: WdpPickFilter = [[], True,
                                      []]) -> Optional[WdpPickResult]
```

X.pick_component(location, direction, pick_filter=[[], True, []]) -> WdpPickResult or None
Pick Component

Args:
    location (Vector): 
    direction (Vector): 
    pick_filter (WdpPickFilter): 

Returns:
    WdpPickResult or None: 

    out_result (WdpPickResult):

<a id="unreal.WdpPicker.get_position_by_z_ref"></a>

#### get\_position\_by\_z\_ref

```python
@classmethod
def get_position_by_z_ref(
        cls,
        world_pos: Vector,
        z_ref: Coord_Z_Ref,
        pick_filter: WdpPickFilter = [[], True, []]) -> Optional[Vector]
```

X.get_position_by_z_ref(world_pos, z_ref, pick_filter=[[], True, []]) -> Vector or None
Get Position by ZRef

Args:
    world_pos (Vector): 
    z_ref (Coord_Z_Ref): 
    pick_filter (WdpPickFilter): 

Returns:
    Vector or None: 

    out_pos (Vector):

<a id="unreal.WdpPicker.get_entities_in_viewport"></a>

#### get\_entities\_in\_viewport

```python
@classmethod
def get_entities_in_viewport(
        cls,
        must_be_fully_enclosed: bool,
        pick_filter: WdpPickFilter = [[], True, []]) -> Array[int]
```

X.get_entities_in_viewport(must_be_fully_enclosed, pick_filter=[[], True, []]) -> Array[int64]
Get Entities in Viewport

Args:
    must_be_fully_enclosed (bool): 
    pick_filter (WdpPickFilter): 

Returns:
    Array[int64]:

<a id="unreal.WdpAssetBPLibrary"></a>