## PCGWorldRaycastQueryParams Objects

```python
class PCGWorldRaycastQueryParams(PCGWorldCommonQueryParams)
```

PCGWorld Raycast Query Params

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
- ``render_material_index`` (int32):  [Read-Write] The index of the render material when it is queried from the hit.
- ``select_landscape_hits`` (PCGWorldQuerySelectLandscapeHits):  [Read-Write]
- ``trace_complex`` (bool):  [Read-Write] Queries against complex collision if enabled, performance warning
- ``uv_channel`` (int32):  [Read-Write] This UV Channel will be selected when retrieving UV Coordinates from a raycast query.

<a id="unreal.PCGWorldRaycastQueryParams.__init__"></a>

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
        uv_channel: int = 0) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.ignore_backface_hits"></a>

#### ignore_backface_hits

```python
@property
def ignore_backface_hits() -> bool
```

(bool):  [Read-Write] Ignore rays that hit backfaces.

<a id="unreal.PCGWorldRaycastQueryParams.ignore_backface_hits"></a>

#### ignore_backface_hits

```python
@ignore_backface_hits.setter
def ignore_backface_hits(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_impact"></a>

#### get_impact

```python
@property
def get_impact() -> bool
```

(bool):  [Read-Write] Create an attribute for whether the raycast resulted in a hit.

<a id="unreal.PCGWorldRaycastQueryParams.get_impact"></a>

#### get_impact

```python
@get_impact.setter
def get_impact(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_impact_point"></a>

#### get_impact_point

```python
@property
def get_impact_point() -> bool
```

(bool):  [Read-Write] Create an attribute for the impact location in world space.

<a id="unreal.PCGWorldRaycastQueryParams.get_impact_point"></a>

#### get_impact_point

```python
@get_impact_point.setter
def get_impact_point(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_impact_normal"></a>

#### get_impact_normal

```python
@property
def get_impact_normal() -> bool
```

(bool):  [Read-Write] Create an attribute for the impact normal.

<a id="unreal.PCGWorldRaycastQueryParams.get_impact_normal"></a>

#### get_impact_normal

```python
@get_impact_normal.setter
def get_impact_normal(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_reflection"></a>

#### get_reflection

```python
@property
def get_reflection() -> bool
```

(bool):  [Read-Write] Create an attribute for the reflection vector based on the ray incoming direction and the impact normal.

<a id="unreal.PCGWorldRaycastQueryParams.get_reflection"></a>

#### get_reflection

```python
@get_reflection.setter
def get_reflection(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_distance"></a>

#### get_distance

```python
@property
def get_distance() -> bool
```

(bool):  [Read-Write] Create an attribute for the distance between the ray origin and the impact point.

<a id="unreal.PCGWorldRaycastQueryParams.get_distance"></a>

#### get_distance

```python
@get_distance.setter
def get_distance(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_local_impact_point"></a>

#### get_local_impact_point

```python
@property
def get_local_impact_point() -> bool
```

(bool):  [Read-Write] Create an attribute for the impact point in the hit object's local space.

<a id="unreal.PCGWorldRaycastQueryParams.get_local_impact_point"></a>

#### get_local_impact_point

```python
@get_local_impact_point.setter
def get_local_impact_point(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_reference_to_render_material"></a>

#### get_reference_to_render_material

```python
@property
def get_reference_to_render_material() -> bool
```

(bool):  [Read-Write] Create an attribute for the render material.

<a id="unreal.PCGWorldRaycastQueryParams.get_reference_to_render_material"></a>

#### get_reference_to_render_material

```python
@get_reference_to_render_material.setter
def get_reference_to_render_material(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_reference_to_static_mesh"></a>

#### get_reference_to_static_mesh

```python
@property
def get_reference_to_static_mesh() -> bool
```

(bool):  [Read-Write] Create an attribute for the static mesh.

<a id="unreal.PCGWorldRaycastQueryParams.get_reference_to_static_mesh"></a>

#### get_reference_to_static_mesh

```python
@get_reference_to_static_mesh.setter
def get_reference_to_static_mesh(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_face_index"></a>

#### get_face_index

```python
@property
def get_face_index() -> bool
```

(bool):  [Read-Write] Create an attribute for index of the hit face. Note: Will only work in complex traces.

<a id="unreal.PCGWorldRaycastQueryParams.get_face_index"></a>

#### get_face_index

```python
@get_face_index.setter
def get_face_index(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_uv_coords"></a>

#### get_uv_coords

```python
@property
def get_uv_coords() -> bool
```

(bool):  [Read-Write] Create an attribute for UV Coordinates of the surface hit. Note: Will only work in complex traces and must have 'Project Settings->Physics->Support UV From Hit Results' set to true.

<a id="unreal.PCGWorldRaycastQueryParams.get_uv_coords"></a>

#### get_uv_coords

```python
@get_uv_coords.setter
def get_uv_coords(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.get_element_index"></a>

#### get_element_index

```python
@property
def get_element_index() -> bool
```

(bool):  [Read-Write] Create an attribute for the index of the element hit. Unique to the hit primitive.

<a id="unreal.PCGWorldRaycastQueryParams.get_element_index"></a>

#### get_element_index

```python
@get_element_index.setter
def get_element_index(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.apply_metadata_from_landscape"></a>

#### apply_metadata_from_landscape

```python
@property
def apply_metadata_from_landscape() -> bool
```

(bool):  [Read-Write] Will apply landscape layers and their values at the impact point.

<a id="unreal.PCGWorldRaycastQueryParams.apply_metadata_from_landscape"></a>

#### apply_metadata_from_landscape

```python
@apply_metadata_from_landscape.setter
def apply_metadata_from_landscape(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.render_material_index"></a>

#### render_material_index

```python
@property
def render_material_index() -> int
```

(int32):  [Read-Write] The index of the render material when it is queried from the hit.

<a id="unreal.PCGWorldRaycastQueryParams.render_material_index"></a>

#### render_material_index

```python
@render_material_index.setter
def render_material_index(value: int) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams.uv_channel"></a>

#### uv_channel

```python
@property
def uv_channel() -> int
```

(int32):  [Read-Write] This UV Channel will be selected when retrieving UV Coordinates from a raycast query.

<a id="unreal.PCGWorldRaycastQueryParams.uv_channel"></a>

#### uv_channel

```python
@uv_channel.setter
def uv_channel(value: int) -> None
```

<a id="unreal.PCGWorldVolumetricQueryParams"></a>