## PCGSelfPruningParameters Objects

```python
class PCGSelfPruningParameters(StructBase)
```

PCGSelf Pruning Parameters

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSelfPruning.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Specifies to use the collision from a given mesh instead of the point; note that this will be ignored in the Remove Duplicates mode.
- ``collision_query_flag`` (PCGCollisionQueryFlag):  [Read-Write] Controls whether queries will be done against complex collisions or not. If enabled, performance warning.
- ``comparison_source`` (PCGAttributePropertyInputSelector):  [Read-Write] By default, it will prune according to the extents of each point, but you can provide another comparison like Density, or a dynamic attribute. Only support numeric values or vector (vector will be reduced to its squared length).
- ``pruning_type`` (PCGSelfPruningType):  [Read-Write]
- ``radius_similarity_factor`` (float):  [Read-Write] Similarity factor to consider 2 points "equal". (For example, if a point extents squared length is 10 and factor is 0.25, all points between 7.5 and 12.5 will be considered "the same").
- ``randomized_pruning`` (bool):  [Read-Write]
- ``use_collision_attribute`` (bool):  [Read-Write]

<a id="unreal.PCGSelfPruningParameters.__init__"></a>

#### __init__

```python
def __init__(
    pruning_type: PCGSelfPruningType = PCGSelfPruningType.LARGE_TO_SMALL,
    comparison_source: PCGAttributePropertyInputSelector = [],
    radius_similarity_factor: float = 0.000000,
    randomized_pruning: bool = False,
    use_collision_attribute: bool = False,
    collision_attribute: PCGAttributePropertyInputSelector = [],
    collision_query_flag: PCGCollisionQueryFlag = PCGCollisionQueryFlag.SIMPLE
) -> None
```

<a id="unreal.PCGSelfPruningParameters.pruning_type"></a>

#### pruning_type

```python
@property
def pruning_type() -> PCGSelfPruningType
```

(PCGSelfPruningType):  [Read-Write]

<a id="unreal.PCGSelfPruningParameters.pruning_type"></a>

#### pruning_type

```python
@pruning_type.setter
def pruning_type(value: PCGSelfPruningType) -> None
```

<a id="unreal.PCGSelfPruningParameters.comparison_source"></a>

#### comparison_source

```python
@property
def comparison_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] By default, it will prune according to the extents of each point, but you can provide another comparison like Density, or a dynamic attribute. Only support numeric values or vector (vector will be reduced to its squared length).

<a id="unreal.PCGSelfPruningParameters.comparison_source"></a>

#### comparison_source

```python
@comparison_source.setter
def comparison_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSelfPruningParameters.radius_similarity_factor"></a>

#### radius_similarity_factor

```python
@property
def radius_similarity_factor() -> float
```

(float):  [Read-Write] Similarity factor to consider 2 points "equal". (For example, if a point extents squared length is 10 and factor is 0.25, all points between 7.5 and 12.5 will be considered "the same").

<a id="unreal.PCGSelfPruningParameters.radius_similarity_factor"></a>

#### radius_similarity_factor

```python
@radius_similarity_factor.setter
def radius_similarity_factor(value: float) -> None
```

<a id="unreal.PCGSelfPruningParameters.randomized_pruning"></a>

#### randomized_pruning

```python
@property
def randomized_pruning() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSelfPruningParameters.randomized_pruning"></a>

#### randomized_pruning

```python
@randomized_pruning.setter
def randomized_pruning(value: bool) -> None
```

<a id="unreal.PCGSelfPruningParameters.use_collision_attribute"></a>

#### use_collision_attribute

```python
@property
def use_collision_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSelfPruningParameters.use_collision_attribute"></a>

#### use_collision_attribute

```python
@use_collision_attribute.setter
def use_collision_attribute(value: bool) -> None
```

<a id="unreal.PCGSelfPruningParameters.collision_attribute"></a>

#### collision_attribute

```python
@property
def collision_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Specifies to use the collision from a given mesh instead of the point; note that this will be ignored in the Remove Duplicates mode.

<a id="unreal.PCGSelfPruningParameters.collision_attribute"></a>

#### collision_attribute

```python
@collision_attribute.setter
def collision_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSelfPruningParameters.collision_query_flag"></a>

#### collision_query_flag

```python
@property
def collision_query_flag() -> PCGCollisionQueryFlag
```

(PCGCollisionQueryFlag):  [Read-Write] Controls whether queries will be done against complex collisions or not. If enabled, performance warning.

<a id="unreal.PCGSelfPruningParameters.collision_query_flag"></a>

#### collision_query_flag

```python
@collision_query_flag.setter
def collision_query_flag(value: PCGCollisionQueryFlag) -> None
```

<a id="unreal.PCGSplineMeshParams"></a>