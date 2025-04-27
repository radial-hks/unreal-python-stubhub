## PCGBlueprintHelpers Objects

```python
class PCGBlueprintHelpers(BlueprintFunctionLibrary)
```

PCGBlueprint Helpers

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGBlueprintHelpers.h

<a id="unreal.PCGBlueprintHelpers.set_seed_from_position"></a>

#### set_seed_from_position

```python
@classmethod
def set_seed_from_position(cls, point: PCGPoint) -> PCGPoint
```

X.set_seed_from_position(point) -> PCGPoint
Set Seed from Position

Args:
    point (PCGPoint): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGBlueprintHelpers.set_local_center"></a>

#### set_local_center

```python
@classmethod
def set_local_center(cls, point: PCGPoint, local_center: Vector) -> PCGPoint
```

X.set_local_center(point, local_center) -> PCGPoint
Set Local Center

Args:
    point (PCGPoint): 
    local_center (Vector): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGBlueprintHelpers.set_extents"></a>

#### set_extents

```python
@classmethod
def set_extents(cls, point: PCGPoint, extents: Vector) -> PCGPoint
```

X.set_extents(point, extents) -> PCGPoint
Set Extents

Args:
    point (PCGPoint): 
    extents (Vector): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGBlueprintHelpers.refresh_pcg_runtime_component"></a>

#### refresh_pcg_runtime_component

```python
@classmethod
def refresh_pcg_runtime_component(cls,
                                  component: PCGComponent,
                                  flush_cache: bool = False) -> None
```

X.refresh_pcg_runtime_component(component, flush_cache=False) -> None
Refresh a component set to Generate At Runtime, if some parameters changed. Can also flush the cache.

Args:
    component (PCGComponent): 
    flush_cache (bool):

<a id="unreal.PCGBlueprintHelpers.get_transformed_bounds"></a>

#### get_transformed_bounds

```python
@classmethod
def get_transformed_bounds(cls, point: PCGPoint) -> Box
```

X.get_transformed_bounds(point) -> Box
Get Transformed Bounds

Args:
    point (PCGPoint): 

Returns:
    Box:

<a id="unreal.PCGBlueprintHelpers.get_task_id"></a>

#### get_task_id

```python
@classmethod
def get_task_id(cls, context: PCGContext) -> Tuple[int, PCGContext]
```

X.get_task_id(context) -> (int64, context=PCGContext)
Get Task Id

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.get_target_actor"></a>

#### get_target_actor

```python
@classmethod
def get_target_actor(cls, context: PCGContext,
                     spatial_data: PCGSpatialData) -> Tuple[Actor, PCGContext]
```

X.get_target_actor(context, spatial_data) -> (Actor, context=PCGContext)
Get Target Actor

Args:
    context (PCGContext): 
    spatial_data (PCGSpatialData): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.get_settings"></a>

#### get_settings

```python
@classmethod
def get_settings(cls, context: PCGContext) -> Tuple[PCGSettings, PCGContext]
```

X.get_settings(context) -> (PCGSettings, context=PCGContext)
Get Settings

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.get_random_stream_from_two_points"></a>

#### get_random_stream_from_two_points

```python
@classmethod
def get_random_stream_from_two_points(
        cls,
        point_a: PCGPoint,
        point_b: PCGPoint,
        optional_settings: PCGSettings = None,
        optional_component: PCGComponent = None) -> RandomStream
```

X.get_random_stream_from_two_points(point_a, point_b, optional_settings=None, optional_component=None) -> RandomStream
Creates a random stream from using the random seeds from two points, as well as settings/component's seed (optional)

Args:
    point_a (PCGPoint): 
    point_b (PCGPoint): 
    optional_settings (PCGSettings): 
    optional_component (PCGComponent): 

Returns:
    RandomStream:

<a id="unreal.PCGBlueprintHelpers.get_random_stream_from_point"></a>

#### get_random_stream_from_point

```python
@classmethod
def get_random_stream_from_point(
        cls,
        point: PCGPoint,
        optional_settings: PCGSettings = None,
        optional_component: PCGComponent = None) -> RandomStream
```

X.get_random_stream_from_point(point, optional_settings=None, optional_component=None) -> RandomStream
Creates a random stream from a point's seed and settings/component's seed (optional)

Args:
    point (PCGPoint): 
    optional_settings (PCGSettings): 
    optional_component (PCGComponent): 

Returns:
    RandomStream:

<a id="unreal.PCGBlueprintHelpers.get_random_stream"></a>

#### get_random_stream

```python
@classmethod
def get_random_stream(cls,
                      point: PCGPoint,
                      optional_settings: PCGSettings = None,
                      optional_component: PCGComponent = None) -> RandomStream
```

deprecated: 'get_random_stream' was renamed to 'get_random_stream_from_point'.

<a id="unreal.PCGBlueprintHelpers.get_original_component"></a>

#### get_original_component

```python
@classmethod
def get_original_component(
        cls, context: PCGContext) -> Tuple[PCGComponent, PCGContext]
```

X.get_original_component(context) -> (PCGComponent, context=PCGContext)
Get Original Component

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.get_local_center"></a>

#### get_local_center

```python
@classmethod
def get_local_center(cls, point: PCGPoint) -> Vector
```

X.get_local_center(point) -> Vector
Get Local Center

Args:
    point (PCGPoint): 

Returns:
    Vector:

<a id="unreal.PCGBlueprintHelpers.get_interpolated_pcg_landscape_layer_weights"></a>

#### get_interpolated_pcg_landscape_layer_weights

```python
@classmethod
def get_interpolated_pcg_landscape_layer_weights(
        cls, world_context_object: Object,
        location: Vector) -> Array[PCGLandscapeLayerWeight]
```

X.get_interpolated_pcg_landscape_layer_weights(world_context_object, location) -> Array[PCGLandscapeLayerWeight]
Get Interpolated PCGLandscape Layer Weights

Args:
    world_context_object (Object): 
    location (Vector): 

Returns:
    Array[PCGLandscapeLayerWeight]:

<a id="unreal.PCGBlueprintHelpers.get_input_data"></a>

#### get_input_data

```python
@classmethod
def get_input_data(cls, context: PCGContext) -> Tuple[PCGData, PCGContext]
```

X.get_input_data(context) -> (PCGData, context=PCGContext)
Get Input Data

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.get_extents"></a>

#### get_extents

```python
@classmethod
def get_extents(cls, point: PCGPoint) -> Vector
```

X.get_extents(point) -> Vector
Get Extents

Args:
    point (PCGPoint): 

Returns:
    Vector:

<a id="unreal.PCGBlueprintHelpers.get_component"></a>

#### get_component

```python
@classmethod
def get_component(cls, context: PCGContext) -> Tuple[PCGComponent, PCGContext]
```

X.get_component(context) -> (PCGComponent, context=PCGContext)
Get Component

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.get_actor_local_bounds_pcg"></a>

#### get_actor_local_bounds_pcg

```python
@classmethod
def get_actor_local_bounds_pcg(cls,
                               actor: Actor,
                               ignore_pcg_created_components: bool = True
                               ) -> Box
```

X.get_actor_local_bounds_pcg(actor, ignore_pcg_created_components=True) -> Box
Get Actor Local Bounds PCG

Args:
    actor (Actor): 
    ignore_pcg_created_components (bool): 

Returns:
    Box:

<a id="unreal.PCGBlueprintHelpers.get_actor_data"></a>

#### get_actor_data

```python
@classmethod
def get_actor_data(cls, context: PCGContext) -> Tuple[PCGData, PCGContext]
```

X.get_actor_data(context) -> (PCGData, context=PCGContext)
Get Actor Data

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.get_actor_bounds_pcg"></a>

#### get_actor_bounds_pcg

```python
@classmethod
def get_actor_bounds_pcg(cls,
                         actor: Actor,
                         ignore_pcg_created_components: bool = True) -> Box
```

X.get_actor_bounds_pcg(actor, ignore_pcg_created_components=True) -> Box
Get Actor Bounds PCG

Args:
    actor (Actor): 
    ignore_pcg_created_components (bool): 

Returns:
    Box:

<a id="unreal.PCGBlueprintHelpers.flush_pcg_cache"></a>

#### flush_pcg_cache

```python
@classmethod
def flush_pcg_cache(cls) -> bool
```

X.flush_pcg_cache() -> bool
Flush the cache, to be used if you have changed something PCG depends on at runtime. Same as `pcg.FlushCache` command. Returns true if it succeeded.

Returns:
    bool:

<a id="unreal.PCGBlueprintHelpers.duplicate_data"></a>

#### duplicate_data

```python
@classmethod
def duplicate_data(
        cls,
        data: PCGData,
        context: PCGContext,
        initialize_metadata: bool = True) -> Tuple[PCGData, PCGContext]
```

X.duplicate_data(data, context, initialize_metadata=True) -> (PCGData, context=PCGContext)
Return a copy of the data, with Metadata inheritance for spatial data.

Args:
    data (PCGData): 
    context (PCGContext): 
    initialize_metadata (bool): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGBlueprintHelpers.create_pcg_data_from_actor"></a>

#### create_pcg_data_from_actor

```python
@classmethod
def create_pcg_data_from_actor(cls,
                               actor: Actor,
                               parse_actor: bool = True) -> PCGData
```

X.create_pcg_data_from_actor(actor, parse_actor=True) -> PCGData
Create PCGData from Actor

Args:
    actor (Actor): 
    parse_actor (bool): 

Returns:
    PCGData:

<a id="unreal.PCGBlueprintHelpers.compute_seed_from_position"></a>

#### compute_seed_from_position

```python
@classmethod
def compute_seed_from_position(cls, position: Vector) -> int
```

X.compute_seed_from_position(position) -> int32
Compute Seed from Position

Args:
    position (Vector): 

Returns:
    int32:

<a id="unreal.PCGInstanceDataPackerBase"></a>