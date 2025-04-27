## PCGWorldCommonQueryParams Objects

```python
class PCGWorldCommonQueryParams(StructBase)
```

PCGWorld Common Query Params

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
- ``select_landscape_hits`` (PCGWorldQuerySelectLandscapeHits):  [Read-Write]
- ``trace_complex`` (bool):  [Read-Write] Queries against complex collision if enabled, performance warning

<a id="unreal.PCGWorldCommonQueryParams.__init__"></a>

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
        get_reference_to_physical_material: bool = False) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.ignore_pcg_hits"></a>

#### ignore_pcg_hits

```python
@property
def ignore_pcg_hits() -> bool
```

(bool):  [Read-Write] If true, will ignore hits/overlaps on content created from PCG.

<a id="unreal.PCGWorldCommonQueryParams.ignore_pcg_hits"></a>

#### ignore_pcg_hits

```python
@ignore_pcg_hits.setter
def ignore_pcg_hits(value: bool) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.ignore_self_hits"></a>

#### ignore_self_hits

```python
@property
def ignore_self_hits() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGWorldCommonQueryParams.ignore_self_hits"></a>

#### ignore_self_hits

```python
@ignore_self_hits.setter
def ignore_self_hits(value: bool) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.collision_channel"></a>

#### collision_channel

```python
@property
def collision_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write]

<a id="unreal.PCGWorldCommonQueryParams.collision_channel"></a>

#### collision_channel

```python
@collision_channel.setter
def collision_channel(value: CollisionChannel) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.trace_complex"></a>

#### trace_complex

```python
@property
def trace_complex() -> bool
```

(bool):  [Read-Write] Queries against complex collision if enabled, performance warning

<a id="unreal.PCGWorldCommonQueryParams.trace_complex"></a>

#### trace_complex

```python
@trace_complex.setter
def trace_complex(value: bool) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.actor_tag_filter"></a>

#### actor_tag_filter

```python
@property
def actor_tag_filter() -> PCGWorldQueryFilterByTag
```

(PCGWorldQueryFilterByTag):  [Read-Write]

<a id="unreal.PCGWorldCommonQueryParams.actor_tag_filter"></a>

#### actor_tag_filter

```python
@actor_tag_filter.setter
def actor_tag_filter(value: PCGWorldQueryFilterByTag) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.actor_tags_list"></a>

#### actor_tags_list

```python
@property
def actor_tags_list() -> str
```

(str):  [Read-Write]

<a id="unreal.PCGWorldCommonQueryParams.actor_tags_list"></a>

#### actor_tags_list

```python
@actor_tags_list.setter
def actor_tags_list(value: str) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.select_landscape_hits"></a>

#### select_landscape_hits

```python
@property
def select_landscape_hits() -> PCGWorldQuerySelectLandscapeHits
```

(PCGWorldQuerySelectLandscapeHits):  [Read-Write]

<a id="unreal.PCGWorldCommonQueryParams.select_landscape_hits"></a>

#### select_landscape_hits

```python
@select_landscape_hits.setter
def select_landscape_hits(value: PCGWorldQuerySelectLandscapeHits) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.ignore_landscape_hits"></a>

#### ignore_landscape_hits

```python
@property
def ignore_landscape_hits() -> bool
```

(bool):  [Read-Write]
deprecated: IgnoreLandscapeHits has been deprecated in favor of SelectLandscapeHits

<a id="unreal.PCGWorldCommonQueryParams.ignore_landscape_hits"></a>

#### ignore_landscape_hits

```python
@ignore_landscape_hits.setter
def ignore_landscape_hits(value: bool) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.get_reference_to_actor_hit"></a>

#### get_reference_to_actor_hit

```python
@property
def get_reference_to_actor_hit() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGWorldCommonQueryParams.get_reference_to_actor_hit"></a>

#### get_reference_to_actor_hit

```python
@get_reference_to_actor_hit.setter
def get_reference_to_actor_hit(value: bool) -> None
```

<a id="unreal.PCGWorldCommonQueryParams.get_reference_to_physical_material"></a>

#### get_reference_to_physical_material

```python
@property
def get_reference_to_physical_material() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGWorldCommonQueryParams.get_reference_to_physical_material"></a>

#### get_reference_to_physical_material

```python
@get_reference_to_physical_material.setter
def get_reference_to_physical_material(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastQueryParams"></a>