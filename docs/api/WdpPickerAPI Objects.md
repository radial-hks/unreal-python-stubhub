## WdpPickerAPI Objects

```python
class WdpPickerAPI(StandardApiClassBase)
```

Wdp Picker API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPI.h

<a id="unreal.WdpPickerAPI.pick_world_point_by_screen_pos"></a>

#### pick\_world\_point\_by\_screen\_pos

```python
def pick_world_point_by_screen_pos(
        params: WdpPickerApiParams) -> Optional[WdpPickerOutResult]
```

x.pick_world_point_by_screen_pos(params) -> WdpPickerOutResult or None
Pick World Point by Screen Pos

Args:
    params (WdpPickerApiParams): 

Returns:
    WdpPickerOutResult or None: 

    out_result (WdpPickerOutResult):

<a id="unreal.WdpPickerAPI.pick_material_by_screen_pos"></a>

#### pick\_material\_by\_screen\_pos

```python
def pick_material_by_screen_pos(
        params: WdpPickerApiParams) -> Optional[PickMaterialApiResult]
```

x.pick_material_by_screen_pos(params) -> PickMaterialApiResult or None
Pick Material by Screen Pos

Args:
    params (WdpPickerApiParams): 

Returns:
    PickMaterialApiResult or None: 

    out_result (PickMaterialApiResult):

<a id="unreal.WdpPickerAPI.pick_entity_by_screen_pos"></a>

#### pick\_entity\_by\_screen\_pos

```python
def pick_entity_by_screen_pos(
        params: WdpPickerApiParams) -> Optional[WdpPickerOutResult]
```

x.pick_entity_by_screen_pos(params) -> WdpPickerOutResult or None
APIs

Args:
    params (WdpPickerApiParams): 

Returns:
    WdpPickerOutResult or None: 

    out_result (WdpPickerOutResult):

<a id="unreal.WdpPickerAPI.pick_entity_by_rectangle"></a>

#### pick\_entity\_by\_rectangle

```python
def pick_entity_by_rectangle(
        params: WdpRectPickerApiParams) -> Optional[WdpRectPickerResult]
```

x.pick_entity_by_rectangle(params) -> WdpRectPickerResult or None
Pick Entity by Rectangle

Args:
    params (WdpRectPickerApiParams): 

Returns:
    WdpRectPickerResult or None: 

    out_result (WdpRectPickerResult):

<a id="unreal.WdpPickerAPI.pick_aes_tiles_nodes_by_rectangle"></a>

#### pick\_aes\_tiles\_nodes\_by\_rectangle

```python
def pick_aes_tiles_nodes_by_rectangle(
        params: PickAesTilesNodesByRectParam
) -> Optional[PickAesTilesNodesResult]
```

x.pick_aes_tiles_nodes_by_rectangle(params) -> PickAesTilesNodesResult or None
Pick Aes Tiles Nodes by Rectangle

Args:
    params (PickAesTilesNodesByRectParam): 

Returns:
    PickAesTilesNodesResult or None: 

    out_result (PickAesTilesNodesResult):

<a id="unreal.WdpPickerAPI.pick_aes_tiles_node_by_screen_pos"></a>

#### pick\_aes\_tiles\_node\_by\_screen\_pos

```python
def pick_aes_tiles_node_by_screen_pos(
        params: WdpPickerApiParams) -> Optional[WdpPickerOutResult]
```

x.pick_aes_tiles_node_by_screen_pos(params) -> WdpPickerOutResult or None
Pick Aes Tiles Node by Screen Pos

Args:
    params (WdpPickerApiParams): 

Returns:
    WdpPickerOutResult or None: 

    out_result (WdpPickerOutResult):

<a id="unreal.WdpPickerAPI.get_entities_in_viewport"></a>

#### get\_entities\_in\_viewport

```python
def get_entities_in_viewport(
        params: GetEntitiesInViewportParams) -> Optional[IntEidArrayResult]
```

x.get_entities_in_viewport(params) -> IntEidArrayResult or None
Get Entities in Viewport

Args:
    params (GetEntitiesInViewportParams): 

Returns:
    IntEidArrayResult or None: 

    out_result (IntEidArrayResult):

<a id="unreal.WdpPickPointAPI"></a>