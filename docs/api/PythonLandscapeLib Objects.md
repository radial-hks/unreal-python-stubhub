## PythonLandscapeLib Objects

```python
class PythonLandscapeLib(BlueprintFunctionLibrary)
```

Python Landscape Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonLandscapeLib.h

<a id="unreal.PythonLandscapeLib.set_weightmap_data"></a>

#### set\_weightmap\_data

```python
@classmethod
def set_weightmap_data(cls, landscape_proxy: LandscapeProxy, layer_name: str,
                       data: Array[int]) -> bool
```

X.set_weightmap_data(landscape_proxy, layer_name, data) -> bool
Set Weightmap Data

Args:
    landscape_proxy (LandscapeProxy): 
    layer_name (str): 
    data (Array[uint8]): 

Returns:
    bool:

<a id="unreal.PythonLandscapeLib.set_heightmap_data"></a>

#### set\_heightmap\_data

```python
@classmethod
def set_heightmap_data(cls, landscape: LandscapeProxy,
                       height_data: Array[int]) -> bool
```

X.set_heightmap_data(landscape, height_data) -> bool
Set height data for specified Landscape

Args:
    landscape (LandscapeProxy): The target landscape instance.
    height_data (Array[int32]): The Height Data for landscape in flatten int list format. (0-65535)

Returns:
    bool: Succeeded or not.

<a id="unreal.PythonLandscapeLib.recalculate_normals"></a>

#### recalculate\_normals

```python
@classmethod
def recalculate_normals(cls, landscape_proxy: LandscapeProxy) -> bool
```

X.recalculate_normals(landscape_proxy) -> bool
Recalculate Normals

Args:
    landscape_proxy (LandscapeProxy): 

Returns:
    bool:

<a id="unreal.PythonLandscapeLib.landscape_update_grass"></a>

#### landscape\_update\_grass

```python
@classmethod
def landscape_update_grass(cls, landscape_proxy: LandscapeProxy,
                           cameras: Array[Vector], force_sync: bool) -> None
```

X.landscape_update_grass(landscape_proxy, cameras, force_sync) -> None
Update the grass cache of landscape proxy.
note: added in v1.0.9

Args:
    landscape_proxy (LandscapeProxy): The landscape owned the GrassTypes.
    cameras (Array[Vector]): Cameras to use for culling, if empty, then NO culling
    force_sync (bool): if true, block and finish all work

<a id="unreal.PythonLandscapeLib.landscape_get_grass_components"></a>

#### landscape\_get\_grass\_components

```python
@classmethod
def landscape_get_grass_components(
    cls, landscape_proxy: LandscapeProxy
) -> Array[HierarchicalInstancedStaticMeshComponent]
```

X.landscape_get_grass_components(landscape_proxy) -> Array[HierarchicalInstancedStaticMeshComponent]
Get the HISM component for drawing GrassType.

Args:
    landscape_proxy (LandscapeProxy): The landscape owned the GrassTypes.

Returns:
    Array[HierarchicalInstancedStaticMeshComponent]: 

    out_grasses (Array[HierarchicalInstancedStaticMeshComponent]): The HISM component for drawing GrassTypes.

<a id="unreal.PythonLandscapeLib.landscape_flush_grass_components"></a>

#### landscape\_flush\_grass\_components

```python
@classmethod
def landscape_flush_grass_components(cls,
                                     landscape_proxy: LandscapeProxy,
                                     flush_grass_maps: bool = True) -> None
```

X.landscape_flush_grass_components(landscape_proxy, flush_grass_maps=True) -> None
Flush the grass cache of landscape.

Args:
    landscape_proxy (LandscapeProxy): 
    flush_grass_maps (bool): Flush GrassMaps or not.

<a id="unreal.PythonLandscapeLib.get_weightmap_data"></a>

#### get\_weightmap\_data

```python
@classmethod
def get_weightmap_data(cls, landscape_proxy: LandscapeProxy,
                       layer_name: str) -> Optional[Array[int]]
```

X.get_weightmap_data(landscape_proxy, layer_name) -> Array[uint8] or None
Get Weightmap Data

Args:
    landscape_proxy (LandscapeProxy): 
    layer_name (str): 

Returns:
    Array[uint8] or None: 

    data (Array[uint8]):

<a id="unreal.PythonLandscapeLib.get_visibility_data"></a>

#### get\_visibility\_data

```python
@classmethod
def get_visibility_data(
        cls, landscape_proxy: LandscapeProxy) -> Optional[Array[int]]
```

X.get_visibility_data(landscape_proxy) -> Array[uint8] or None
Get Visibility Data

Args:
    landscape_proxy (LandscapeProxy): 

Returns:
    Array[uint8] or None: 

    data (Array[uint8]):

<a id="unreal.PythonLandscapeLib.get_used_paint_layers"></a>

#### get\_used\_paint\_layers

```python
@classmethod
def get_used_paint_layers(cls, landscape_proxy: LandscapeProxy) -> Array[str]
```

X.get_used_paint_layers(landscape_proxy) -> Array[str]
Get Used Paint Layers

Args:
    landscape_proxy (LandscapeProxy): 

Returns:
    Array[str]:

<a id="unreal.PythonLandscapeLib.get_layer_names"></a>

#### get\_layer\_names

```python
@classmethod
def get_layer_names(cls, landscape_proxy: LandscapeProxy) -> Array[str]
```

X.get_layer_names(landscape_proxy) -> Array[str]
Get Layer Names

Args:
    landscape_proxy (LandscapeProxy): 

Returns:
    Array[str]:

<a id="unreal.PythonLandscapeLib.get_landscape_guid"></a>

#### get\_landscape\_guid

```python
@classmethod
def get_landscape_guid(cls, landscape_proxy: LandscapeProxy) -> Guid
```

X.get_landscape_guid(landscape_proxy) -> Guid
Get the guid from landscape

Args:
    landscape_proxy (LandscapeProxy): The landscape instance.

Returns:
    Guid: The Guid of the landscape.

<a id="unreal.PythonLandscapeLib.get_landscape_extent"></a>

#### get\_landscape\_extent

```python
@classmethod
def get_landscape_extent(
        cls, landscape_proxy: LandscapeProxy) -> Tuple[int, int, int, int]
```

X.get_landscape_extent(landscape_proxy) -> (out_min_x=int32, out_min_y=int32, out_max_x=int32, out_max_y=int32)
UFUNCTION(BlueprintCallable, meta = (Keywords = "Python Editor"), Category = "PythonEditor")
static void LandscapeTickGrass(ALandscapeProxy* LandscapeProxy);

Args:
    landscape_proxy (LandscapeProxy): 

Returns:
    tuple: 

    out_min_x (int32): 

    out_min_y (int32): 

    out_max_x (int32): 

    out_max_y (int32):

<a id="unreal.PythonLandscapeLib.get_landscape_components"></a>

#### get\_landscape\_components

```python
@classmethod
def get_landscape_components(
        cls, landscape_proxy: LandscapeProxy) -> Array[LandscapeComponent]
```

X.get_landscape_components(landscape_proxy) -> Array[LandscapeComponent]
Get the Components from landscape

Args:
    landscape_proxy (LandscapeProxy): The landscape instance.

Returns:
    Array[LandscapeComponent]: The Components of the landscape.

<a id="unreal.PythonLandscapeLib.get_heightmap_data"></a>

#### get\_heightmap\_data

```python
@classmethod
def get_heightmap_data(cls, landscape: LandscapeProxy) -> Array[int]
```

X.get_heightmap_data(landscape) -> Array[int32]
Get height data for specified Landscape

Args:
    landscape (LandscapeProxy): The landscape instance for query.

Returns:
    Array[int32]: 

    height_data (Array[int32]): The Height Data of the landscape in flatten int list format. (0-65535)

<a id="unreal.PythonLandscapeLib.create_landscape_proxy_with_guid"></a>

#### create\_landscape\_proxy\_with\_guid

```python
@classmethod
def create_landscape_proxy_with_guid(
        cls,
        landscape_transform: Transform,
        section_size: int,
        sections_per_component: int,
        component_count_x: int,
        component_count_y: int,
        guid: Guid,
        quads_space_offset_x: int = -1,
        quads_space_offset_y: int = -1) -> LandscapeStreamingProxy
```

X.create_landscape_proxy_with_guid(landscape_transform, section_size, sections_per_component, component_count_x, component_count_y, guid, quads_space_offset_x=-1, quads_space_offset_y=-1) -> LandscapeStreamingProxy
Create A StreamingProxy in Editor.
note: Haven't test in UE5 yet.

Args:
    landscape_transform (Transform): The transform of landscape.
    section_size (int32): The Section Size of the landscape. (63, 127, 255 and so on.)
    sections_per_component (int32): The Section count of each component. (1 or 2)
    component_count_x (int32): Number of components in Axis X
    component_count_y (int32): Number of components in Axis Y
    guid (Guid): The GUID with the proxy
    quads_space_offset_x (int32): 
    quads_space_offset_y (int32): 

Returns:
    LandscapeStreamingProxy: The created LandscapeStreamingProxy.

<a id="unreal.PythonLandscapeLib.create_landscape_proxy"></a>

#### create\_landscape\_proxy

```python
@classmethod
def create_landscape_proxy(
        cls, landscape_transform: Transform, section_size: int,
        sections_per_component: int, component_count_x: int,
        component_count_y: int,
        shared_landscape_actor: Landscape) -> LandscapeStreamingProxy
```

X.create_landscape_proxy(landscape_transform, section_size, sections_per_component, component_count_x, component_count_y, shared_landscape_actor) -> LandscapeStreamingProxy
Create A StreamingProxy in Editor.
note: Haven't test in UE5 yet.

Args:
    landscape_transform (Transform): The transform of landscape.
    section_size (int32): The Section Size of the landscape. (63, 127, 255 and so on.)
    sections_per_component (int32): The Section count of each component. (1 or 2)
    component_count_x (int32): Number of components in Axis X
    component_count_y (int32): Number of components in Axis Y
    shared_landscape_actor (Landscape): The shared landscape witch share the GUID with the proxy

Returns:
    LandscapeStreamingProxy: The created LandscapeStreamingProxy.

<a id="unreal.PythonLandscapeLib.create_landscape"></a>

#### create\_landscape

```python
@classmethod
def create_landscape(cls, landscape_transform: Transform, section_size: int,
                     sections_per_component: int, component_count_x: int,
                     component_count_y: int) -> Landscape
```

X.create_landscape(landscape_transform, section_size, sections_per_component, component_count_x, component_count_y) -> Landscape
Create A Landscape in Editor.

Args:
    landscape_transform (Transform): The transform of landscape.
    section_size (int32): The Section Size of the landscape. (63, 127, 255 and so on.)
    sections_per_component (int32): The Section count of each component. (1 or 2)
    component_count_x (int32): Number of components in Axis X
    component_count_y (int32): Number of components in Axis Y

Returns:
    Landscape: The created Landscape.

<a id="unreal.PythonLandscapeLib.clear_layer"></a>

#### clear\_layer

```python
@classmethod
def clear_layer(cls, landscape_proxy: LandscapeProxy, layer_name: str) -> bool
```

X.clear_layer(landscape_proxy, layer_name) -> bool
Clear Layer

Args:
    landscape_proxy (LandscapeProxy): 
    layer_name (str): 

Returns:
    bool:

<a id="unreal.PythonLandscapeLib.clear_all_layers"></a>

#### clear\_all\_layers

```python
@classmethod
def clear_all_layers(cls, landscape_proxy: LandscapeProxy) -> bool
```

X.clear_all_layers(landscape_proxy) -> bool
Clear All Layers

Args:
    landscape_proxy (LandscapeProxy): 

Returns:
    bool:

<a id="unreal.PythonLandscapeLib.cal_landscape_size"></a>

#### cal\_landscape\_size

```python
@classmethod
def cal_landscape_size(cls, section_size: int, sections_per_component: int,
                       component_count_x: int,
                       component_count_y: int) -> Tuple[int, int]
```

X.cal_landscape_size(section_size, sections_per_component, component_count_x, component_count_y) -> (out_size_x=int32, out_size_y=int32)
Calculate the Size of Landscape (the size of heightmap data).

Args:
    section_size (int32): The Section Size of the landscape.
    sections_per_component (int32): The Section count of each component. (1 or 2)
    component_count_x (int32): Number of components in Axis X.
    component_count_y (int32): Number of components in Axis Y.

Returns:
    tuple: 

    out_size_x (int32): The size of landscape in Axis X, (ComponentCountX * QuadsPerComponent + 1).

    out_size_y (int32): The size of landscape in Axis Y.

<a id="unreal.PythonLandscapeLib.assign_layer_info"></a>

#### assign\_layer\_info

```python
@classmethod
def assign_layer_info(cls, landscape_proxy: LandscapeProxy, index: int,
                      layer_info: LandscapeLayerInfoObject) -> bool
```

X.assign_layer_info(landscape_proxy, index, layer_info) -> bool
Assign Layer Info

Args:
    landscape_proxy (LandscapeProxy): 
    index (int32): 
    layer_info (LandscapeLayerInfoObject): 

Returns:
    bool:

<a id="unreal.PythonLandscapeLib.add_adjacent_landscape_proxy"></a>

#### add\_adjacent\_landscape\_proxy

```python
@classmethod
def add_adjacent_landscape_proxy(cls, world_in: World,
                                 source_landscape: LandscapeProxy,
                                 direction: int) -> LandscapeStreamingProxy
```

X.add_adjacent_landscape_proxy(world_in, source_landscape, direction) -> LandscapeStreamingProxy
East:0 South:1 West:2 North:3

Args:
    world_in (World): 
    source_landscape (LandscapeProxy): 
    direction (int32): 

Returns:
    LandscapeStreamingProxy:

<a id="unreal.PythonLevelLib"></a>