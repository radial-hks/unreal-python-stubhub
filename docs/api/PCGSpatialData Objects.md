## PCGSpatialData Objects

```python
class PCGSpatialData(PCGData)
```

"Concrete" data base class for PCG generation
This will be the base class for data classes that actually represent
concrete evidence of spatial data - points, surfaces, splines, etc.
In opposition to settings/control type of data.

Conceptually, any concrete data can be decayed into points (potentially through transformations)
which hold metadata and a transform, and this is the basic currency of the PCG framework.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSpatialData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGSpatialData.target_actor"></a>

#### target_actor

```python
@property
def target_actor() -> Actor
```

(Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGSpatialData.target_actor"></a>

#### target_actor

```python
@target_actor.setter
def target_actor(value: Actor) -> None
```

<a id="unreal.PCGSpatialData.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@property
def keep_zero_density_points() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSpatialData.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@keep_zero_density_points.setter
def keep_zero_density_points(value: bool) -> None
```

<a id="unreal.PCGSpatialData.to_point_data_with_context"></a>

#### to_point_data_with_context

```python
def to_point_data_with_context(
        context: PCGContext) -> Tuple[PCGPointData, PCGContext]
```

x.to_point_data_with_context(context) -> (PCGPointData, context=PCGContext)
To Point Data with Context

Args:
    context (PCGContext): 

Returns:
    PCGContext: 

    context (PCGContext):

<a id="unreal.PCGSpatialData.to_point_data"></a>

#### to_point_data

```python
def to_point_data() -> PCGPointData
```

x.to_point_data() -> PCGPointData
Discretizes the data into points
deprecated: The To Point Data function is deprecated - use To Point Data With Context instead.

Returns:
    PCGPointData:

<a id="unreal.PCGSpatialData.mutable_metadata"></a>

#### mutable_metadata

```python
def mutable_metadata() -> PCGMetadata
```

x.mutable_metadata() -> PCGMetadata
Mutable Metadata

Returns:
    PCGMetadata:

<a id="unreal.PCGSpatialData.k2_union_with"></a>

#### k2_union_with

```python
def k2_union_with(other: PCGSpatialData) -> PCGUnionData
```

x.k2_union_with(other) -> PCGUnionData
Returns a specialized data to union this with another data

Args:
    other (PCGSpatialData): 

Returns:
    PCGUnionData:

<a id="unreal.PCGSpatialData.union_with"></a>

#### union_with

```python
def union_with(other: PCGSpatialData) -> PCGUnionData
```

deprecated: 'union_with' was renamed to 'k2_union_with'.

<a id="unreal.PCGSpatialData.k2_subtract"></a>

#### k2_subtract

```python
def k2_subtract(other: PCGSpatialData) -> PCGDifferenceData
```

x.k2_subtract(other) -> PCGDifferenceData
K2 Subtract

Args:
    other (PCGSpatialData): 

Returns:
    PCGDifferenceData:

<a id="unreal.PCGSpatialData.subtract"></a>

#### subtract

```python
def subtract(other: PCGSpatialData) -> PCGDifferenceData
```

deprecated: 'subtract' was renamed to 'k2_subtract'.

<a id="unreal.PCGSpatialData.k2_sample_point"></a>

#### k2_sample_point

```python
def k2_sample_point(transform: Transform, bounds: Box,
                    out_metadata: PCGMetadata) -> Optional[PCGPoint]
```

x.k2_sample_point(transform, bounds, out_metadata) -> PCGPoint or None
Sample rotation, scale and other attributes from this data at the query position. Returns true if Transform location and Bounds overlaps this data.

Args:
    transform (Transform): 
    bounds (Box): 
    out_metadata (PCGMetadata): 

Returns:
    PCGPoint or None: 

    out_point (PCGPoint):

<a id="unreal.PCGSpatialData.sample_point"></a>

#### sample_point

```python
def sample_point(transform: Transform, bounds: Box,
                 out_metadata: PCGMetadata) -> Optional[PCGPoint]
```

deprecated: 'sample_point' was renamed to 'k2_sample_point'.

<a id="unreal.PCGSpatialData.k2_project_point"></a>

#### k2_project_point

```python
def k2_project_point(transform: Transform, bounds: Box,
                     params: PCGProjectionParams,
                     out_metadata: PCGMetadata) -> Optional[PCGPoint]
```

x.k2_project_point(transform, bounds, params, out_metadata) -> PCGPoint or None
K2 Project Point

Args:
    transform (Transform): 
    bounds (Box): 
    params (PCGProjectionParams): 
    out_metadata (PCGMetadata): 

Returns:
    PCGPoint or None: 

    out_point (PCGPoint):

<a id="unreal.PCGSpatialData.project_point"></a>

#### project_point

```python
def project_point(transform: Transform, bounds: Box,
                  params: PCGProjectionParams,
                  out_metadata: PCGMetadata) -> Optional[PCGPoint]
```

deprecated: 'project_point' was renamed to 'k2_project_point'.

<a id="unreal.PCGSpatialData.k2_project_on"></a>

#### k2_project_on

```python
def k2_project_on(
    other: PCGSpatialData,
    params: PCGProjectionParams = [
        True, True, False, PCGProjectionColorBlendMode.SOURCE_VALUE, "",
        PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, PCGMetadataOp.TARGET_VALUE,
        PCGProjectionTagMergeMode.SOURCE
    ]
) -> PCGSpatialData
```

x.k2_project_on(other, params=[True, True, False, PCGProjectionColorBlendMode.SOURCE_VALUE, "", PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, PCGMetadataOp.TARGET_VALUE, PCGProjectionTagMergeMode.SOURCE]) -> PCGSpatialData
Returns a specialized data to project this on another data of equal or higher dimension. Returns copy of this data if projection fails.

Args:
    other (PCGSpatialData): 
    params (PCGProjectionParams): 

Returns:
    PCGSpatialData:

<a id="unreal.PCGSpatialData.project_on"></a>

#### project_on

```python
def project_on(
    other: PCGSpatialData,
    params: PCGProjectionParams = [
        True, True, False, PCGProjectionColorBlendMode.SOURCE_VALUE, "",
        PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, PCGMetadataOp.TARGET_VALUE,
        PCGProjectionTagMergeMode.SOURCE
    ]
) -> PCGSpatialData
```

deprecated: 'project_on' was renamed to 'k2_project_on'.

<a id="unreal.PCGSpatialData.k2_intersect_with"></a>

#### k2_intersect_with

```python
def k2_intersect_with(other: PCGSpatialData) -> PCGIntersectionData
```

x.k2_intersect_with(other) -> PCGIntersectionData
Returns a specialized data to intersect with another data

Args:
    other (PCGSpatialData): 

Returns:
    PCGIntersectionData:

<a id="unreal.PCGSpatialData.intersect_with"></a>

#### intersect_with

```python
def intersect_with(other: PCGSpatialData) -> PCGIntersectionData
```

deprecated: 'intersect_with' was renamed to 'k2_intersect_with'.

<a id="unreal.PCGSpatialData.initialize_from_data"></a>

#### initialize_from_data

```python
def initialize_from_data(source: PCGSpatialData,
                         metadata_parent_override: PCGMetadata = None,
                         inherit_metadata: bool = True,
                         inherit_attributes: bool = True) -> None
```

x.initialize_from_data(source, metadata_parent_override=None, inherit_metadata=True, inherit_attributes=True) -> None
Initialize from Data

Args:
    source (PCGSpatialData): 
    metadata_parent_override (PCGMetadata): 
    inherit_metadata (bool): 
    inherit_attributes (bool):

<a id="unreal.PCGSpatialData.has_non_trivial_transform"></a>

#### has_non_trivial_transform

```python
def has_non_trivial_transform() -> bool
```

x.has_non_trivial_transform() -> bool
Returns true if the data has a non-trivial transform

Returns:
    bool:

<a id="unreal.PCGSpatialData.get_strict_bounds"></a>

#### get_strict_bounds

```python
def get_strict_bounds() -> Box
```

x.get_strict_bounds() -> Box
Returns the bounds in which the density is always 1

Returns:
    Box:

<a id="unreal.PCGSpatialData.get_normal"></a>

#### get_normal

```python
def get_normal() -> Vector
```

x.get_normal() -> Vector
Returns the expected data normal (for surfaces) or eventual projection axis (for volumes)

Returns:
    Vector:

<a id="unreal.PCGSpatialData.get_dimension"></a>

#### get_dimension

```python
def get_dimension() -> int
```

x.get_dimension() -> int32
Returns the dimension of the data type, which has nothing to do with the dimension of its points

Returns:
    int32:

<a id="unreal.PCGSpatialData.get_density_at_position"></a>

#### get_density_at_position

```python
def get_density_at_position(position: Vector) -> float
```

x.get_density_at_position(position) -> float
Computes the density at a given location

Args:
    position (Vector): 

Returns:
    float:

<a id="unreal.PCGSpatialData.get_bounds"></a>

#### get_bounds

```python
def get_bounds() -> Box
```

x.get_bounds() -> Box
Returns the full bounds (including density fall-off) of the data

Returns:
    Box:

<a id="unreal.PCGSpatialData.create_empty_metadata"></a>

#### create_empty_metadata

```python
def create_empty_metadata() -> PCGMetadata
```

x.create_empty_metadata() -> PCGMetadata
Create Empty Metadata
deprecated: The Create Empty Metadata function is not needed anymore - it can safely be removed

Returns:
    PCGMetadata:

<a id="unreal.PCGSpatialData.const_metadata"></a>

#### const_metadata

```python
def const_metadata() -> PCGMetadata
```

x.const_metadata() -> PCGMetadata
Const Metadata

Returns:
    PCGMetadata:

<a id="unreal.PCGSpatialDataWithPointCache"></a>