## PCGWorldRayHitQueryParams Objects

```python
class PCGWorldRayHitQueryParams(PCGWorldRaycastQueryParams)
```

PCGWorld Ray Hit Query Params

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGWorldData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_tag_filter`` (PCGWorldQueryFilterByTag):  [Read-Write]
- ``actor_tags_list`` (str):  [Read-Write]
- ``apply_metadata_from_landscape`` (bool):  [Read-Write] Will apply landscape layers and their values at the impact point.
- ``collision_channel`` (CollisionChannel):  [Read-Write]
- ``get_distance`` (bool):  [Read-Write] Create an attribute for the distance between the ray origin and the impact point.
- ``get_element_index`` (bool):  [Read-Write] Create an attribute for the index of the element hit. Unique to the hit primitive.
- ``get_face_index`` (bool):  [Read-Write] Create an attribute for index of the hit face. Note: Will only work in complex traces.
- ``get_impact`` (bool):  [Read-Write] Create an attribute for whether the raycast resulted in a hit.
- ``get_impact_normal`` (bool):  [Read-Write] Create an attribute for the impact normal.
- ``get_impact_point`` (bool):  [Read-Write] Create an attribute for the impact location in world space.
- ``get_local_impact_point`` (bool):  [Read-Write] Create an attribute for the impact point in the hit object's local space.
- ``get_reference_to_actor_hit`` (bool):  [Read-Write]
- ``get_reference_to_physical_material`` (bool):  [Read-Write]
- ``get_reference_to_render_material`` (bool):  [Read-Write] Create an attribute for the render material.
- ``get_reference_to_static_mesh`` (bool):  [Read-Write] Create an attribute for the static mesh.
- ``get_reflection`` (bool):  [Read-Write] Create an attribute for the reflection vector based on the ray incoming direction and the impact normal.
- ``get_uv_coords`` (bool):  [Read-Write] Create an attribute for UV Coordinates of the surface hit. Note: Will only work in complex traces and must have 'Project Settings->Physics->Support UV From Hit Results' set to true.
- ``ignore_backface_hits`` (bool):  [Read-Write] Ignore rays that hit backfaces.
- ``ignore_landscape_hits`` (bool):  [Read-Write]
  deprecated: IgnoreLandscapeHits has been deprecated in favor of SelectLandscapeHits
- ``ignore_pcg_hits`` (bool):  [Read-Write] If true, will ignore hits/overlaps on content created from PCG.
- ``ignore_self_hits`` (bool):  [Read-Write]
- ``override_default_params`` (bool):  [Read-Write] Set ray parameters including origin, direction and length explicitly rather than deriving these from the generating actor bounds.
- ``ray_direction`` (Vector):  [Read-Write]
- ``ray_length`` (double):  [Read-Write]
- ``ray_origin`` (Vector):  [Read-Write]
- ``render_material_index`` (int32):  [Read-Write] The index of the render material when it is queried from the hit.
- ``select_landscape_hits`` (PCGWorldQuerySelectLandscapeHits):  [Read-Write]
- ``trace_complex`` (bool):  [Read-Write] Queries against complex collision if enabled, performance warning
- ``uv_channel`` (int32):  [Read-Write] This UV Channel will be selected when retrieving UV Coordinates from a raycast query.

<a id="unreal.PCGWorldRayHitQueryParams.__init__"></a>

#### __init__

```python
def __init__(
        ignore_pcg_hits: bool = False,
        ignore_self_hits: bool = False,
        collision_channel: CollisionChannel = CollisionChannel.
    ECC_WORLD_STATIC,
        trace_complex: bool = False,
        actor_tag_filter: PCGWorldQueryFilterByTag = PCGWorldQueryFilterByTag.
    NO_TAG_FILTER,
        actor_tags_list: str = "",
        select_landscape_hits:
    PCGWorldQuerySelectLandscapeHits = PCGWorldQuerySelectLandscapeHits.
    EXCLUDE,
        get_reference_to_actor_hit: bool = False,
        get_reference_to_physical_material: bool = False,
        ignore_backface_hits: bool = False,
        get_impact: bool = False,
        get_impact_point: bool = False,
        get_impact_normal: bool = False,
        get_reflection: bool = False,
        get_distance: bool = False,
        get_local_impact_point: bool = False,
        get_reference_to_render_material: bool = False,
        get_reference_to_static_mesh: bool = False,
        get_face_index: bool = False,
        get_uv_coords: bool = False,
        get_element_index: bool = False,
        apply_metadata_from_landscape: bool = False,
        render_material_index: int = 0,
        uv_channel: int = 0,
        override_default_params: bool = False,
        ray_origin: Vector = [0.000000, 0.000000, 0.000000],
        ray_direction: Vector = [0.000000, 0.000000, 0.000000],
        ray_length: float = 0.000000) -> None
```

<a id="unreal.PCGWorldRayHitQueryParams.override_default_params"></a>

#### override_default_params

```python
@property
def override_default_params() -> bool
```

(bool):  [Read-Write] Set ray parameters including origin, direction and length explicitly rather than deriving these from the generating actor bounds.

<a id="unreal.PCGWorldRayHitQueryParams.override_default_params"></a>

#### override_default_params

```python
@override_default_params.setter
def override_default_params(value: bool) -> None
```

<a id="unreal.PCGWorldRayHitQueryParams.ray_origin"></a>

#### ray_origin

```python
@property
def ray_origin() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGWorldRayHitQueryParams.ray_origin"></a>

#### ray_origin

```python
@ray_origin.setter
def ray_origin(value: Vector) -> None
```

<a id="unreal.PCGWorldRayHitQueryParams.ray_direction"></a>

#### ray_direction

```python
@property
def ray_direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGWorldRayHitQueryParams.ray_direction"></a>

#### ray_direction

```python
@ray_direction.setter
def ray_direction(value: Vector) -> None
```

<a id="unreal.PCGWorldRayHitQueryParams.ray_length"></a>

#### ray_length

```python
@property
def ray_length() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGWorldRayHitQueryParams.ray_length"></a>

#### ray_length

```python
@ray_length.setter
def ray_length(value: float) -> None
```

<a id="unreal.PCGActorSelectorSettings"></a>