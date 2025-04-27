## JumpFloodComponent2D Objects

```python
class JumpFloodComponent2D(ActorComponent)
```

Jump Flood Component 2D

**C++ Source:**

- **Plugin**: Water
- **Module**: WaterEditor
- **File**: JumpFloodComponent2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``blur_edges_material`` (MaterialInterface):  [Read-Write]
- ``blur_edges_mid`` (MaterialInstanceDynamic):  [Read-Only]
- ``blur_passes`` (int32):  [Read-Write]
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``completed_blur_passes`` (int32):  [Read-Only]
- ``completed_passes`` (int32):  [Read-Only]
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``find_edges_material`` (MaterialInterface):  [Read-Write]
- ``find_edges_mid`` (MaterialInstanceDynamic):  [Read-Only]
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``jump_step_material`` (MaterialInterface):  [Read-Write]
- ``jump_step_mid`` (MaterialInstanceDynamic):  [Read-Only] Transient properties (exposed only for debugging reasons) :
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``required_passes`` (int32):  [Read-Only]
- ``rta`` (TextureRenderTarget2D):  [Read-Only]
- ``rtb`` (TextureRenderTarget2D):  [Read-Only]
- ``use_blur`` (bool):  [Read-Write]

<a id="unreal.JumpFloodComponent2D.jump_step_material"></a>

#### jump_step_material

```python
@property
def jump_step_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.JumpFloodComponent2D.jump_step_material"></a>

#### jump_step_material

```python
@jump_step_material.setter
def jump_step_material(value: MaterialInterface) -> None
```

<a id="unreal.JumpFloodComponent2D.find_edges_material"></a>

#### find_edges_material

```python
@property
def find_edges_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.JumpFloodComponent2D.find_edges_material"></a>

#### find_edges_material

```python
@find_edges_material.setter
def find_edges_material(value: MaterialInterface) -> None
```

<a id="unreal.JumpFloodComponent2D.blur_edges_material"></a>

#### blur_edges_material

```python
@property
def blur_edges_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.JumpFloodComponent2D.blur_edges_material"></a>

#### blur_edges_material

```python
@blur_edges_material.setter
def blur_edges_material(value: MaterialInterface) -> None
```

<a id="unreal.JumpFloodComponent2D.use_blur"></a>

#### use_blur

```python
@property
def use_blur() -> bool
```

(bool):  [Read-Write]

<a id="unreal.JumpFloodComponent2D.use_blur"></a>

#### use_blur

```python
@use_blur.setter
def use_blur(value: bool) -> None
```

<a id="unreal.JumpFloodComponent2D.blur_passes"></a>

#### blur_passes

```python
@property
def blur_passes() -> int
```

(int32):  [Read-Write]

<a id="unreal.JumpFloodComponent2D.blur_passes"></a>

#### blur_passes

```python
@blur_passes.setter
def blur_passes(value: int) -> None
```

<a id="unreal.JumpFloodComponent2D.single_jump_step"></a>

#### single_jump_step

```python
def single_jump_step() -> TextureRenderTarget2D
```

x.single_jump_step() -> TextureRenderTarget2D
Single Jump Step

Returns:
    TextureRenderTarget2D:

<a id="unreal.JumpFloodComponent2D.single_blur_step"></a>

#### single_blur_step

```python
def single_blur_step() -> TextureRenderTarget2D
```

x.single_blur_step() -> TextureRenderTarget2D
Single Blur Step

Returns:
    TextureRenderTarget2D:

<a id="unreal.JumpFloodComponent2D.jump_flood"></a>

#### jump_flood

```python
def jump_flood(seed_rt: TextureRenderTarget2D, scene_capture_z: float,
               curl: LinearColor, use_depth: bool,
               zx_location_t: float) -> None
```

x.jump_flood(seed_rt, scene_capture_z, curl, use_depth, zx_location_t) -> None
Jump Flood

Args:
    seed_rt (TextureRenderTarget2D): 
    scene_capture_z (float): 
    curl (LinearColor): 
    use_depth (bool): 
    zx_location_t (float):

<a id="unreal.JumpFloodComponent2D.find_edges_debug"></a>

#### find_edges_debug

```python
def find_edges_debug(seed_rt: TextureRenderTarget2D, capture_z: float,
                     curl: LinearColor, dest_rt: TextureRenderTarget2D,
                     z_offset: float) -> None
```

x.find_edges_debug(seed_rt, capture_z, curl, dest_rt, z_offset) -> None
Find Edges Debug

Args:
    seed_rt (TextureRenderTarget2D): 
    capture_z (float): 
    curl (LinearColor): 
    dest_rt (TextureRenderTarget2D): 
    z_offset (float):

<a id="unreal.JumpFloodComponent2D.find_edges"></a>

#### find_edges

```python
def find_edges(seed_rt: TextureRenderTarget2D, capture_z: float,
               curl: LinearColor, use_depth: bool,
               zx_location_t: float) -> TextureRenderTarget2D
```

x.find_edges(seed_rt, capture_z, curl, use_depth, zx_location_t) -> TextureRenderTarget2D
Find Edges

Args:
    seed_rt (TextureRenderTarget2D): 
    capture_z (float): 
    curl (LinearColor): 
    use_depth (bool): 
    zx_location_t (float): 

Returns:
    TextureRenderTarget2D:

<a id="unreal.JumpFloodComponent2D.create_mi_ds"></a>

#### create_mi_ds

```python
def create_mi_ds() -> bool
```

x.create_mi_ds() -> bool
Create MIDs

Returns:
    bool:

<a id="unreal.JumpFloodComponent2D.assign_render_targets"></a>

#### assign_render_targets

```python
def assign_render_targets(rta: TextureRenderTarget2D,
                          rtb: TextureRenderTarget2D) -> None
```

x.assign_render_targets(rta, rtb) -> None
Assign Render Targets

Args:
    rta (TextureRenderTarget2D): 
    rtb (TextureRenderTarget2D):

<a id="unreal.WaterBodyBrushCacheContainer"></a>