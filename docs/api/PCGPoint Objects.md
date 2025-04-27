## PCGPoint Objects

```python
class PCGPoint(StructBase)
```

PCGPoint

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPoint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_max`` (Vector):  [Read-Write]
- ``bounds_min`` (Vector):  [Read-Write]
- ``color`` (Vector4):  [Read-Write]
- ``density`` (float):  [Read-Write]
- ``metadata_entry`` (int64):  [Read-Only]
- ``seed`` (int32):  [Read-Write]
- ``steepness`` (float):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.PCGPoint.__init__"></a>

#### __init__

```python
def __init__(transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             density: float = 0.000000,
             bounds_min: Vector = [0.000000, 0.000000, 0.000000],
             bounds_max: Vector = [0.000000, 0.000000, 0.000000],
             color: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
             steepness: float = 0.000000,
             seed: int = 0,
             metadata_entry: int = 0) -> None
```

<a id="unreal.PCGPoint.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.PCGPoint.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.PCGPoint.density"></a>

#### density

```python
@property
def density() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGPoint.density"></a>

#### density

```python
@density.setter
def density(value: float) -> None
```

<a id="unreal.PCGPoint.bounds_min"></a>

#### bounds_min

```python
@property
def bounds_min() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGPoint.bounds_min"></a>

#### bounds_min

```python
@bounds_min.setter
def bounds_min(value: Vector) -> None
```

<a id="unreal.PCGPoint.bounds_max"></a>

#### bounds_max

```python
@property
def bounds_max() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGPoint.bounds_max"></a>

#### bounds_max

```python
@bounds_max.setter
def bounds_max(value: Vector) -> None
```

<a id="unreal.PCGPoint.color"></a>

#### color

```python
@property
def color() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.PCGPoint.color"></a>

#### color

```python
@color.setter
def color(value: Vector4) -> None
```

<a id="unreal.PCGPoint.steepness"></a>

#### steepness

```python
@property
def steepness() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGPoint.steepness"></a>

#### steepness

```python
@steepness.setter
def steepness(value: float) -> None
```

<a id="unreal.PCGPoint.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGPoint.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.PCGPoint.metadata_entry"></a>

#### metadata_entry

```python
@property
def metadata_entry() -> int
```

(int64):  [Read-Only]

<a id="unreal.PCGPoint.set_local_center"></a>

#### set_local_center

```python
def set_local_center(local_center: Vector) -> None
```

x.set_local_center(local_center) -> None
Set Local Center

Args:
    local_center (Vector):

<a id="unreal.PCGPoint.set_extents"></a>

#### set_extents

```python
def set_extents(extents: Vector) -> None
```

x.set_extents(extents) -> None
Set Extents

Args:
    extents (Vector):

<a id="unreal.PCGPoint.get_transformed_bounds"></a>

#### get_transformed_bounds

```python
def get_transformed_bounds() -> Box
```

x.get_transformed_bounds() -> Box
Get Transformed Bounds

Returns:
    Box:

<a id="unreal.PCGPoint.get_random_stream_from_two_points"></a>

#### get_random_stream_from_two_points

```python
def get_random_stream_from_two_points(
        point_b: PCGPoint,
        optional_settings: PCGSettings = None,
        optional_component: PCGComponent = None) -> RandomStream
```

x.get_random_stream_from_two_points(point_b, optional_settings=None, optional_component=None) -> RandomStream
Creates a random stream from using the random seeds from two points, as well as settings/component's seed (optional)

Args:
    point_b (PCGPoint): 
    optional_settings (PCGSettings): 
    optional_component (PCGComponent): 

Returns:
    RandomStream:

<a id="unreal.PCGPoint.get_random_stream_from_point"></a>

#### get_random_stream_from_point

```python
def get_random_stream_from_point(
        optional_settings: PCGSettings = None,
        optional_component: PCGComponent = None) -> RandomStream
```

x.get_random_stream_from_point(optional_settings=None, optional_component=None) -> RandomStream
Creates a random stream from a point's seed and settings/component's seed (optional)

Args:
    optional_settings (PCGSettings): 
    optional_component (PCGComponent): 

Returns:
    RandomStream:

<a id="unreal.PCGPoint.get_random_stream"></a>

#### get_random_stream

```python
def get_random_stream(optional_settings: PCGSettings = None,
                      optional_component: PCGComponent = None) -> RandomStream
```

deprecated: 'get_random_stream' was renamed to 'get_random_stream_from_point'.

<a id="unreal.PCGPoint.get_local_center"></a>

#### get_local_center

```python
def get_local_center() -> Vector
```

x.get_local_center() -> Vector
Get Local Center

Returns:
    Vector:

<a id="unreal.PCGPoint.get_extents"></a>

#### get_extents

```python
def get_extents() -> Vector
```

x.get_extents() -> Vector
Get Extents

Returns:
    Vector:

<a id="unreal.PCGPoint.set_vector_attribute"></a>

#### set_vector_attribute

```python
def set_vector_attribute(metadata: PCGMetadata, attribute_name: Name,
                         value: Vector) -> None
```

x.set_vector_attribute(metadata, attribute_name, value) -> None
Set Vector Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector):

<a id="unreal.PCGPoint.set_vector4_attribute"></a>

#### set_vector4_attribute

```python
def set_vector4_attribute(metadata: PCGMetadata, attribute_name: Name,
                          value: Vector4) -> None
```

x.set_vector4_attribute(metadata, attribute_name, value) -> None
Set Vector 4Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector4):

<a id="unreal.PCGPoint.set_vector2_attribute"></a>

#### set_vector2_attribute

```python
def set_vector2_attribute(metadata: PCGMetadata, attribute_name: Name,
                          value: Vector2D) -> None
```

x.set_vector2_attribute(metadata, attribute_name, value) -> None
Set Vector 2Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector2D):

<a id="unreal.PCGPoint.set_transform_attribute"></a>

#### set_transform_attribute

```python
def set_transform_attribute(metadata: PCGMetadata, attribute_name: Name,
                            value: Transform) -> None
```

x.set_transform_attribute(metadata, attribute_name, value) -> None
Set Transform Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Transform):

<a id="unreal.PCGPoint.set_string_attribute"></a>

#### set_string_attribute

```python
def set_string_attribute(metadata: PCGMetadata, attribute_name: Name,
                         value: str) -> None
```

x.set_string_attribute(metadata, attribute_name, value) -> None
Set String Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (str):

<a id="unreal.PCGPoint.set_soft_object_path_attribute"></a>

#### set_soft_object_path_attribute

```python
def set_soft_object_path_attribute(metadata: PCGMetadata, attribute_name: Name,
                                   value: SoftObjectPath) -> None
```

x.set_soft_object_path_attribute(metadata, attribute_name, value) -> None
Set Soft Object Path Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (SoftObjectPath):

<a id="unreal.PCGPoint.set_soft_class_path_attribute"></a>

#### set_soft_class_path_attribute

```python
def set_soft_class_path_attribute(metadata: PCGMetadata, attribute_name: Name,
                                  value: SoftClassPath) -> None
```

x.set_soft_class_path_attribute(metadata, attribute_name, value) -> None
Set Soft Class Path Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (SoftClassPath):

<a id="unreal.PCGPoint.set_rotator_attribute"></a>

#### set_rotator_attribute

```python
def set_rotator_attribute(metadata: PCGMetadata, attribute_name: Name,
                          value: Rotator) -> None
```

x.set_rotator_attribute(metadata, attribute_name, value) -> None
Set Rotator Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Rotator):

<a id="unreal.PCGPoint.set_quat_attribute"></a>

#### set_quat_attribute

```python
def set_quat_attribute(metadata: PCGMetadata, attribute_name: Name,
                       value: Quat) -> None
```

x.set_quat_attribute(metadata, attribute_name, value) -> None
Set Quat Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Quat):

<a id="unreal.PCGPoint.set_name_attribute"></a>

#### set_name_attribute

```python
def set_name_attribute(metadata: PCGMetadata, attribute_name: Name,
                       value: Name) -> None
```

x.set_name_attribute(metadata, attribute_name, value) -> None
Set Name Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Name):

<a id="unreal.PCGPoint.set_integer64_attribute"></a>

#### set_integer64_attribute

```python
def set_integer64_attribute(metadata: PCGMetadata, attribute_name: Name,
                            value: int) -> None
```

x.set_integer64_attribute(metadata, attribute_name, value) -> None
Set Integer 64Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (int64):

<a id="unreal.PCGPoint.set_integer32_attribute"></a>

#### set_integer32_attribute

```python
def set_integer32_attribute(metadata: PCGMetadata, attribute_name: Name,
                            value: int) -> None
```

x.set_integer32_attribute(metadata, attribute_name, value) -> None
Set Integer 32Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (int32):

<a id="unreal.PCGPoint.set_float_attribute"></a>

#### set_float_attribute

```python
def set_float_attribute(metadata: PCGMetadata, attribute_name: Name,
                        value: float) -> None
```

x.set_float_attribute(metadata, attribute_name, value) -> None
Set Float Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (float):

<a id="unreal.PCGPoint.set_double_attribute"></a>

#### set_double_attribute

```python
def set_double_attribute(metadata: PCGMetadata, attribute_name: Name,
                         value: float) -> None
```

x.set_double_attribute(metadata, attribute_name, value) -> None
Set Double Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (double):

<a id="unreal.PCGPoint.set_bool_attribute"></a>

#### set_bool_attribute

```python
def set_bool_attribute(metadata: PCGMetadata, attribute_name: Name,
                       value: bool) -> None
```

x.set_bool_attribute(metadata, attribute_name, value) -> None
Set Bool Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (bool):

<a id="unreal.PCGPoint.initialize_metadata"></a>

#### initialize_metadata

```python
def initialize_metadata(metadata: PCGMetadata,
                        parent_point: PCGPoint,
                        parent_metadata: PCGMetadata = None) -> None
```

x.initialize_metadata(metadata, parent_point, parent_metadata=None) -> None
Assigns a metadata entry key and will copy attribute values if from an unrelated metadata. Note: a null ParentMetadata assumes this is the same as Metadata

Args:
    metadata (PCGMetadata): 
    parent_point (PCGPoint): 
    parent_metadata (PCGMetadata):

<a id="unreal.PCGPoint.has_attribute_set"></a>

#### has_attribute_set

```python
def has_attribute_set(metadata: PCGMetadata, attribute_name: Name) -> bool
```

x.has_attribute_set(metadata, attribute_name) -> bool
Has Attribute Set

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGPoint.get_vector_attribute"></a>

#### get_vector_attribute

```python
def get_vector_attribute(metadata: PCGMetadata,
                         attribute_name: Name) -> Vector
```

x.get_vector_attribute(metadata, attribute_name) -> Vector
Get Vector Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector:

<a id="unreal.PCGPoint.get_vector4_attribute"></a>

#### get_vector4_attribute

```python
def get_vector4_attribute(metadata: PCGMetadata,
                          attribute_name: Name) -> Vector4
```

x.get_vector4_attribute(metadata, attribute_name) -> Vector4
Get Vector 4Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector4:

<a id="unreal.PCGPoint.get_vector2_attribute"></a>

#### get_vector2_attribute

```python
def get_vector2_attribute(metadata: PCGMetadata,
                          attribute_name: Name) -> Vector2D
```

x.get_vector2_attribute(metadata, attribute_name) -> Vector2D
Get Vector 2Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector2D:

<a id="unreal.PCGPoint.get_transform_attribute"></a>

#### get_transform_attribute

```python
def get_transform_attribute(metadata: PCGMetadata,
                            attribute_name: Name) -> Transform
```

x.get_transform_attribute(metadata, attribute_name) -> Transform
Get Transform Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Transform:

<a id="unreal.PCGPoint.get_string_attribute"></a>

#### get_string_attribute

```python
def get_string_attribute(metadata: PCGMetadata, attribute_name: Name) -> str
```

x.get_string_attribute(metadata, attribute_name) -> str
Get String Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    str:

<a id="unreal.PCGPoint.get_soft_object_path_attribute"></a>

#### get_soft_object_path_attribute

```python
def get_soft_object_path_attribute(metadata: PCGMetadata,
                                   attribute_name: Name) -> SoftObjectPath
```

x.get_soft_object_path_attribute(metadata, attribute_name) -> SoftObjectPath
Get Soft Object Path Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    SoftObjectPath:

<a id="unreal.PCGPoint.get_soft_class_path_attribute"></a>

#### get_soft_class_path_attribute

```python
def get_soft_class_path_attribute(metadata: PCGMetadata,
                                  attribute_name: Name) -> SoftClassPath
```

x.get_soft_class_path_attribute(metadata, attribute_name) -> SoftClassPath
Get Soft Class Path Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    SoftClassPath:

<a id="unreal.PCGPoint.get_rotator_attribute"></a>

#### get_rotator_attribute

```python
def get_rotator_attribute(metadata: PCGMetadata,
                          attribute_name: Name) -> Rotator
```

x.get_rotator_attribute(metadata, attribute_name) -> Rotator
Get Rotator Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Rotator:

<a id="unreal.PCGPoint.get_quat_attribute"></a>

#### get_quat_attribute

```python
def get_quat_attribute(metadata: PCGMetadata, attribute_name: Name) -> Quat
```

x.get_quat_attribute(metadata, attribute_name) -> Quat
Get Quat Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Quat:

<a id="unreal.PCGPoint.get_name_attribute"></a>

#### get_name_attribute

```python
def get_name_attribute(metadata: PCGMetadata, attribute_name: Name) -> Name
```

x.get_name_attribute(metadata, attribute_name) -> Name
Get Name Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Name:

<a id="unreal.PCGPoint.get_integer64_attribute"></a>

#### get_integer64_attribute

```python
def get_integer64_attribute(metadata: PCGMetadata,
                            attribute_name: Name) -> int
```

x.get_integer64_attribute(metadata, attribute_name) -> int64
Get Integer 64Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    int64:

<a id="unreal.PCGPoint.get_integer32_attribute"></a>

#### get_integer32_attribute

```python
def get_integer32_attribute(metadata: PCGMetadata,
                            attribute_name: Name) -> int
```

x.get_integer32_attribute(metadata, attribute_name) -> int32
Get Integer 32Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    int32:

<a id="unreal.PCGPoint.get_float_attribute"></a>

#### get_float_attribute

```python
def get_float_attribute(metadata: PCGMetadata, attribute_name: Name) -> float
```

x.get_float_attribute(metadata, attribute_name) -> float
Get Float Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    float:

<a id="unreal.PCGPoint.get_double_attribute"></a>

#### get_double_attribute

```python
def get_double_attribute(metadata: PCGMetadata, attribute_name: Name) -> float
```

x.get_double_attribute(metadata, attribute_name) -> double
Get Double Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    double:

<a id="unreal.PCGPoint.get_bool_attribute"></a>

#### get_bool_attribute

```python
def get_bool_attribute(metadata: PCGMetadata, attribute_name: Name) -> bool
```

x.get_bool_attribute(metadata, attribute_name) -> bool
Get Bool Attribute

Args:
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGPoint.copy_point"></a>

#### copy_point

```python
def copy_point(copy_metadata: bool = True,
               metadata: PCGMetadata = None,
               out_metadata: PCGMetadata = None) -> PCGPoint
```

x.copy_point(copy_metadata=True, metadata=None, out_metadata=None) -> PCGPoint
Point functions

Args:
    copy_metadata (bool): 
    metadata (PCGMetadata): 
    out_metadata (PCGMetadata): 

Returns:
    PCGPoint: 

    out_point (PCGPoint):

<a id="unreal.PCGPreConfiguredSettingsInfo"></a>