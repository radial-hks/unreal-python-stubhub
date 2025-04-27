## PCGWorldVolumetricQueryParams Objects

```python
class PCGWorldVolumetricQueryParams(PCGWorldCommonQueryParams)
```

PCGWorld Volumetric Query Params

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGWorldData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_tag_filter`` (PCGWorldQueryFilterByTag):  [Read-Write]
- ``actor_tags_list`` (str):  [Read-Write]
- ``collision_channel`` (CollisionChannel):  [Read-Write]
- ``get_reference_to_actor_hit`` (bool):  [Read-Write]
- ``get_reference_to_physical_material`` (bool):  [Read-Write]
- ``ignore_landscape_hits`` (bool):  [Read-Write]
  deprecated: IgnoreLandscapeHits has been deprecated in favor of SelectLandscapeHits
- ``ignore_pcg_hits`` (bool):  [Read-Write] If true, will ignore hits/overlaps on content created from PCG.
- ``ignore_self_hits`` (bool):  [Read-Write]
- ``search_for_overlap`` (bool):  [Read-Write] Controls whether we are trying to find an overlap with physical objects (true) or to find empty spaces that do not contain anything (false)
- ``select_landscape_hits`` (PCGWorldQuerySelectLandscapeHits):  [Read-Write]
- ``trace_complex`` (bool):  [Read-Write] Queries against complex collision if enabled, performance warning

<a id="unreal.PCGWorldVolumetricQueryParams.__init__"></a>

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
        search_for_overlap: bool = False) -> None
```

<a id="unreal.PCGWorldVolumetricQueryParams.search_for_overlap"></a>

#### search_for_overlap

```python
@property
def search_for_overlap() -> bool
```

(bool):  [Read-Write] Controls whether we are trying to find an overlap with physical objects (true) or to find empty spaces that do not contain anything (false)

<a id="unreal.PCGWorldVolumetricQueryParams.search_for_overlap"></a>

#### search_for_overlap

```python
@search_for_overlap.setter
def search_for_overlap(value: bool) -> None
```

<a id="unreal.PCGWorldRayHitQueryParams"></a>