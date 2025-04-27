## PCGMetadataAccessorHelpers Objects

```python
class PCGMetadataAccessorHelpers(BlueprintFunctionLibrary)
```

PCGMetadata Accessor Helpers

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMetadataAccessor.h

<a id="unreal.PCGMetadataAccessorHelpers.set_vector_attribute_by_metadata_key"></a>

#### set_vector_attribute_by_metadata_key

```python
@classmethod
def set_vector_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                         attribute_name: Name,
                                         value: Vector) -> int
```

X.set_vector_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Vector Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_vector_attribute"></a>

#### set_vector_attribute

```python
@classmethod
def set_vector_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                         attribute_name: Name, value: Vector) -> PCGPoint
```

X.set_vector_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Vector Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_vector4_attribute_by_metadata_key"></a>

#### set_vector4_attribute_by_metadata_key

```python
@classmethod
def set_vector4_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                          attribute_name: Name,
                                          value: Vector4) -> int
```

X.set_vector4_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Vector 4Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector4): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_vector4_attribute"></a>

#### set_vector4_attribute

```python
@classmethod
def set_vector4_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                          attribute_name: Name, value: Vector4) -> PCGPoint
```

X.set_vector4_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Vector 4Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector4): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_vector2_attribute_by_metadata_key"></a>

#### set_vector2_attribute_by_metadata_key

```python
@classmethod
def set_vector2_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                          attribute_name: Name,
                                          value: Vector2D) -> int
```

X.set_vector2_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Vector 2Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector2D): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_vector2_attribute"></a>

#### set_vector2_attribute

```python
@classmethod
def set_vector2_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                          attribute_name: Name, value: Vector2D) -> PCGPoint
```

X.set_vector2_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Vector 2Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Vector2D): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_transform_attribute_by_metadata_key"></a>

#### set_transform_attribute_by_metadata_key

```python
@classmethod
def set_transform_attribute_by_metadata_key(cls, key: int,
                                            metadata: PCGMetadata,
                                            attribute_name: Name,
                                            value: Transform) -> int
```

X.set_transform_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Transform Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Transform): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_transform_attribute"></a>

#### set_transform_attribute

```python
@classmethod
def set_transform_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                            attribute_name: Name,
                            value: Transform) -> PCGPoint
```

X.set_transform_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Transform Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Transform): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_string_attribute_by_metadata_key"></a>

#### set_string_attribute_by_metadata_key

```python
@classmethod
def set_string_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                         attribute_name: Name,
                                         value: str) -> int
```

X.set_string_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set String Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (str): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_string_attribute"></a>

#### set_string_attribute

```python
@classmethod
def set_string_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                         attribute_name: Name, value: str) -> PCGPoint
```

X.set_string_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set String Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (str): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_soft_object_path_attribute_by_metadata_key"></a>

#### set_soft_object_path_attribute_by_metadata_key

```python
@classmethod
def set_soft_object_path_attribute_by_metadata_key(
        cls, key: int, metadata: PCGMetadata, attribute_name: Name,
        value: SoftObjectPath) -> int
```

X.set_soft_object_path_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Soft Object Path Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (SoftObjectPath): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_soft_object_path_attribute"></a>

#### set_soft_object_path_attribute

```python
@classmethod
def set_soft_object_path_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                                   attribute_name: Name,
                                   value: SoftObjectPath) -> PCGPoint
```

X.set_soft_object_path_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Soft Object Path Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (SoftObjectPath): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_soft_class_path_attribute_by_metadata_key"></a>

#### set_soft_class_path_attribute_by_metadata_key

```python
@classmethod
def set_soft_class_path_attribute_by_metadata_key(cls, key: int,
                                                  metadata: PCGMetadata,
                                                  attribute_name: Name,
                                                  value: SoftClassPath) -> int
```

X.set_soft_class_path_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Soft Class Path Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (SoftClassPath): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_soft_class_path_attribute"></a>

#### set_soft_class_path_attribute

```python
@classmethod
def set_soft_class_path_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                                  attribute_name: Name,
                                  value: SoftClassPath) -> PCGPoint
```

X.set_soft_class_path_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Soft Class Path Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (SoftClassPath): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_rotator_attribute_by_metadata_key"></a>

#### set_rotator_attribute_by_metadata_key

```python
@classmethod
def set_rotator_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                          attribute_name: Name,
                                          value: Rotator) -> int
```

X.set_rotator_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Rotator Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Rotator): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_rotator_attribute"></a>

#### set_rotator_attribute

```python
@classmethod
def set_rotator_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                          attribute_name: Name, value: Rotator) -> PCGPoint
```

X.set_rotator_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Rotator Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Rotator): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_quat_attribute_by_metadata_key"></a>

#### set_quat_attribute_by_metadata_key

```python
@classmethod
def set_quat_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                       attribute_name: Name,
                                       value: Quat) -> int
```

X.set_quat_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Quat Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Quat): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_quat_attribute"></a>

#### set_quat_attribute

```python
@classmethod
def set_quat_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                       attribute_name: Name, value: Quat) -> PCGPoint
```

X.set_quat_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Quat Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Quat): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_name_attribute"></a>

#### set_name_attribute

```python
@classmethod
def set_name_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                       attribute_name: Name, value: Name) -> PCGPoint
```

X.set_name_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Name Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (Name): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_integer64_attribute_by_metadata_key"></a>

#### set_integer64_attribute_by_metadata_key

```python
@classmethod
def set_integer64_attribute_by_metadata_key(cls, key: int,
                                            metadata: PCGMetadata,
                                            attribute_name: Name,
                                            value: int) -> int
```

X.set_integer64_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Integer 64Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (int64): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_integer64_attribute"></a>

#### set_integer64_attribute

```python
@classmethod
def set_integer64_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                            attribute_name: Name, value: int) -> PCGPoint
```

X.set_integer64_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Integer 64Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (int64): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_integer32_attribute_by_metadata_key"></a>

#### set_integer32_attribute_by_metadata_key

```python
@classmethod
def set_integer32_attribute_by_metadata_key(cls, key: int,
                                            metadata: PCGMetadata,
                                            attribute_name: Name,
                                            value: int) -> int
```

X.set_integer32_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Integer 32Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (int32): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_integer32_attribute"></a>

#### set_integer32_attribute

```python
@classmethod
def set_integer32_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                            attribute_name: Name, value: int) -> PCGPoint
```

X.set_integer32_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Integer 32Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (int32): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_float_attribute_by_metadata_key"></a>

#### set_float_attribute_by_metadata_key

```python
@classmethod
def set_float_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                        attribute_name: Name,
                                        value: float) -> int
```

X.set_float_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Float Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (float): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_float_attribute"></a>

#### set_float_attribute

```python
@classmethod
def set_float_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                        attribute_name: Name, value: float) -> PCGPoint
```

X.set_float_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Float Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (float): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_double_attribute_by_metadata_key"></a>

#### set_double_attribute_by_metadata_key

```python
@classmethod
def set_double_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                         attribute_name: Name,
                                         value: float) -> int
```

X.set_double_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Double Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (double): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_double_attribute"></a>

#### set_double_attribute

```python
@classmethod
def set_double_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                         attribute_name: Name, value: float) -> PCGPoint
```

X.set_double_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Double Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (double): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_bool_attribute_by_metadata_key"></a>

#### set_bool_attribute_by_metadata_key

```python
@classmethod
def set_bool_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                       attribute_name: Name,
                                       value: bool) -> int
```

X.set_bool_attribute_by_metadata_key(key, metadata, attribute_name, value) -> int64
Set Bool Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (bool): 

Returns:
    int64: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.set_bool_attribute"></a>

#### set_bool_attribute

```python
@classmethod
def set_bool_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                       attribute_name: Name, value: bool) -> PCGPoint
```

X.set_bool_attribute(point, metadata, attribute_name, value) -> PCGPoint
Set Bool Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    value (bool): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.set_attribute_from_property_by_metadata_key"></a>

#### set_attribute_from_property_by_metadata_key

```python
@classmethod
def set_attribute_from_property_by_metadata_key(
        cls, key: int, metadata: PCGMetadata, attribute_name: Name,
        object: Object, property_name: Name) -> Optional[int]
```

X.set_attribute_from_property_by_metadata_key(key, metadata, attribute_name, object, property_name) -> int64 or None
Set Attribute from Property by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 
    object (Object): 
    property_name (Name): 

Returns:
    int64 or None: 

    key (int64):

<a id="unreal.PCGMetadataAccessorHelpers.initialize_metadata"></a>

#### initialize_metadata

```python
@classmethod
def initialize_metadata(cls,
                        point: PCGPoint,
                        metadata: PCGMetadata,
                        parent_point: PCGPoint,
                        parent_metadata: PCGMetadata = None) -> PCGPoint
```

X.initialize_metadata(point, metadata, parent_point, parent_metadata=None) -> PCGPoint
Assigns a metadata entry key and will copy attribute values if from an unrelated metadata. Note: a null ParentMetadata assumes this is the same as Metadata

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    parent_point (PCGPoint): 
    parent_metadata (PCGMetadata): 

Returns:
    PCGPoint: 

    point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers.has_attribute_set_by_metadata_key"></a>

#### has_attribute_set_by_metadata_key

```python
@classmethod
def has_attribute_set_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                      attribute_name: Name) -> bool
```

X.has_attribute_set_by_metadata_key(key, metadata, attribute_name) -> bool
Has Attribute Set by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGMetadataAccessorHelpers.has_attribute_set"></a>

#### has_attribute_set

```python
@classmethod
def has_attribute_set(cls, point: PCGPoint, metadata: PCGMetadata,
                      attribute_name: Name) -> bool
```

X.has_attribute_set(point, metadata, attribute_name) -> bool
Has Attribute Set

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGMetadataAccessorHelpers.get_vector_attribute_by_metadata_key"></a>

#### get_vector_attribute_by_metadata_key

```python
@classmethod
def get_vector_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                         attribute_name: Name) -> Vector
```

X.get_vector_attribute_by_metadata_key(key, metadata, attribute_name) -> Vector
Get Vector Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector:

<a id="unreal.PCGMetadataAccessorHelpers.get_vector_attribute"></a>

#### get_vector_attribute

```python
@classmethod
def get_vector_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                         attribute_name: Name) -> Vector
```

X.get_vector_attribute(point, metadata, attribute_name) -> Vector
Get Vector Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector:

<a id="unreal.PCGMetadataAccessorHelpers.get_vector4_attribute_by_metadata_key"></a>

#### get_vector4_attribute_by_metadata_key

```python
@classmethod
def get_vector4_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                          attribute_name: Name) -> Vector4
```

X.get_vector4_attribute_by_metadata_key(key, metadata, attribute_name) -> Vector4
Get Vector 4Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector4:

<a id="unreal.PCGMetadataAccessorHelpers.get_vector4_attribute"></a>

#### get_vector4_attribute

```python
@classmethod
def get_vector4_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                          attribute_name: Name) -> Vector4
```

X.get_vector4_attribute(point, metadata, attribute_name) -> Vector4
Get Vector 4Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector4:

<a id="unreal.PCGMetadataAccessorHelpers.get_vector2_attribute_by_metadata_key"></a>

#### get_vector2_attribute_by_metadata_key

```python
@classmethod
def get_vector2_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                          attribute_name: Name) -> Vector2D
```

X.get_vector2_attribute_by_metadata_key(key, metadata, attribute_name) -> Vector2D
Get Vector 2Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector2D:

<a id="unreal.PCGMetadataAccessorHelpers.get_vector2_attribute"></a>

#### get_vector2_attribute

```python
@classmethod
def get_vector2_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                          attribute_name: Name) -> Vector2D
```

X.get_vector2_attribute(point, metadata, attribute_name) -> Vector2D
Get Vector 2Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Vector2D:

<a id="unreal.PCGMetadataAccessorHelpers.get_transform_attribute_by_metadata_key"></a>

#### get_transform_attribute_by_metadata_key

```python
@classmethod
def get_transform_attribute_by_metadata_key(cls, key: int,
                                            metadata: PCGMetadata,
                                            attribute_name: Name) -> Transform
```

X.get_transform_attribute_by_metadata_key(key, metadata, attribute_name) -> Transform
Get Transform Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Transform:

<a id="unreal.PCGMetadataAccessorHelpers.get_transform_attribute"></a>

#### get_transform_attribute

```python
@classmethod
def get_transform_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                            attribute_name: Name) -> Transform
```

X.get_transform_attribute(point, metadata, attribute_name) -> Transform
Get Transform Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Transform:

<a id="unreal.PCGMetadataAccessorHelpers.get_string_attribute_by_metadata_key"></a>

#### get_string_attribute_by_metadata_key

```python
@classmethod
def get_string_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                         attribute_name: Name) -> str
```

X.get_string_attribute_by_metadata_key(key, metadata, attribute_name) -> str
Get String Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    str:

<a id="unreal.PCGMetadataAccessorHelpers.get_string_attribute"></a>

#### get_string_attribute

```python
@classmethod
def get_string_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                         attribute_name: Name) -> str
```

X.get_string_attribute(point, metadata, attribute_name) -> str
Get String Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    str:

<a id="unreal.PCGMetadataAccessorHelpers.get_soft_object_path_attribute_by_metadata_key"></a>

#### get_soft_object_path_attribute_by_metadata_key

```python
@classmethod
def get_soft_object_path_attribute_by_metadata_key(
        cls, key: int, metadata: PCGMetadata,
        attribute_name: Name) -> SoftObjectPath
```

X.get_soft_object_path_attribute_by_metadata_key(key, metadata, attribute_name) -> SoftObjectPath
Get Soft Object Path Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    SoftObjectPath:

<a id="unreal.PCGMetadataAccessorHelpers.get_soft_object_path_attribute"></a>

#### get_soft_object_path_attribute

```python
@classmethod
def get_soft_object_path_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                                   attribute_name: Name) -> SoftObjectPath
```

X.get_soft_object_path_attribute(point, metadata, attribute_name) -> SoftObjectPath
Get Soft Object Path Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    SoftObjectPath:

<a id="unreal.PCGMetadataAccessorHelpers.get_soft_class_path_attribute_by_metadata_key"></a>

#### get_soft_class_path_attribute_by_metadata_key

```python
@classmethod
def get_soft_class_path_attribute_by_metadata_key(
        cls, key: int, metadata: PCGMetadata,
        attribute_name: Name) -> SoftClassPath
```

X.get_soft_class_path_attribute_by_metadata_key(key, metadata, attribute_name) -> SoftClassPath
Get Soft Class Path Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    SoftClassPath:

<a id="unreal.PCGMetadataAccessorHelpers.get_soft_class_path_attribute"></a>

#### get_soft_class_path_attribute

```python
@classmethod
def get_soft_class_path_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                                  attribute_name: Name) -> SoftClassPath
```

X.get_soft_class_path_attribute(point, metadata, attribute_name) -> SoftClassPath
Get Soft Class Path Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    SoftClassPath:

<a id="unreal.PCGMetadataAccessorHelpers.get_rotator_attribute_by_metadata_key"></a>

#### get_rotator_attribute_by_metadata_key

```python
@classmethod
def get_rotator_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                          attribute_name: Name) -> Rotator
```

X.get_rotator_attribute_by_metadata_key(key, metadata, attribute_name) -> Rotator
Get Rotator Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Rotator:

<a id="unreal.PCGMetadataAccessorHelpers.get_rotator_attribute"></a>

#### get_rotator_attribute

```python
@classmethod
def get_rotator_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                          attribute_name: Name) -> Rotator
```

X.get_rotator_attribute(point, metadata, attribute_name) -> Rotator
Get Rotator Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Rotator:

<a id="unreal.PCGMetadataAccessorHelpers.get_quat_attribute_by_metadata_key"></a>

#### get_quat_attribute_by_metadata_key

```python
@classmethod
def get_quat_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                       attribute_name: Name) -> Quat
```

X.get_quat_attribute_by_metadata_key(key, metadata, attribute_name) -> Quat
Get Quat Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Quat:

<a id="unreal.PCGMetadataAccessorHelpers.get_quat_attribute"></a>

#### get_quat_attribute

```python
@classmethod
def get_quat_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                       attribute_name: Name) -> Quat
```

X.get_quat_attribute(point, metadata, attribute_name) -> Quat
Get Quat Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Quat:

<a id="unreal.PCGMetadataAccessorHelpers.get_name_attribute"></a>

#### get_name_attribute

```python
@classmethod
def get_name_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                       attribute_name: Name) -> Name
```

X.get_name_attribute(point, metadata, attribute_name) -> Name
Get Name Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    Name:

<a id="unreal.PCGMetadataAccessorHelpers.get_integer64_attribute_by_metadata_key"></a>

#### get_integer64_attribute_by_metadata_key

```python
@classmethod
def get_integer64_attribute_by_metadata_key(cls, key: int,
                                            metadata: PCGMetadata,
                                            attribute_name: Name) -> int
```

X.get_integer64_attribute_by_metadata_key(key, metadata, attribute_name) -> int64
Get Integer 64Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    int64:

<a id="unreal.PCGMetadataAccessorHelpers.get_integer64_attribute"></a>

#### get_integer64_attribute

```python
@classmethod
def get_integer64_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                            attribute_name: Name) -> int
```

X.get_integer64_attribute(point, metadata, attribute_name) -> int64
Get Integer 64Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    int64:

<a id="unreal.PCGMetadataAccessorHelpers.get_integer32_attribute_by_metadata_key"></a>

#### get_integer32_attribute_by_metadata_key

```python
@classmethod
def get_integer32_attribute_by_metadata_key(cls, key: int,
                                            metadata: PCGMetadata,
                                            attribute_name: Name) -> int
```

X.get_integer32_attribute_by_metadata_key(key, metadata, attribute_name) -> int32
Id-based metadata functions

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    int32:

<a id="unreal.PCGMetadataAccessorHelpers.get_integer32_attribute"></a>

#### get_integer32_attribute

```python
@classmethod
def get_integer32_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                            attribute_name: Name) -> int
```

X.get_integer32_attribute(point, metadata, attribute_name) -> int32
Get Integer 32Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    int32:

<a id="unreal.PCGMetadataAccessorHelpers.get_float_attribute_by_metadata_key"></a>

#### get_float_attribute_by_metadata_key

```python
@classmethod
def get_float_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                        attribute_name: Name) -> float
```

X.get_float_attribute_by_metadata_key(key, metadata, attribute_name) -> float
Get Float Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    float:

<a id="unreal.PCGMetadataAccessorHelpers.get_float_attribute"></a>

#### get_float_attribute

```python
@classmethod
def get_float_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                        attribute_name: Name) -> float
```

X.get_float_attribute(point, metadata, attribute_name) -> float
Get Float Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    float:

<a id="unreal.PCGMetadataAccessorHelpers.get_double_attribute_by_metadata_key"></a>

#### get_double_attribute_by_metadata_key

```python
@classmethod
def get_double_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                         attribute_name: Name) -> float
```

X.get_double_attribute_by_metadata_key(key, metadata, attribute_name) -> double
Get Double Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    double:

<a id="unreal.PCGMetadataAccessorHelpers.get_double_attribute"></a>

#### get_double_attribute

```python
@classmethod
def get_double_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                         attribute_name: Name) -> float
```

X.get_double_attribute(point, metadata, attribute_name) -> double
Get Double Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    double:

<a id="unreal.PCGMetadataAccessorHelpers.get_bool_attribute_by_metadata_key"></a>

#### get_bool_attribute_by_metadata_key

```python
@classmethod
def get_bool_attribute_by_metadata_key(cls, key: int, metadata: PCGMetadata,
                                       attribute_name: Name) -> bool
```

X.get_bool_attribute_by_metadata_key(key, metadata, attribute_name) -> bool
Get Bool Attribute by Metadata Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGMetadataAccessorHelpers.get_bool_attribute"></a>

#### get_bool_attribute

```python
@classmethod
def get_bool_attribute(cls, point: PCGPoint, metadata: PCGMetadata,
                       attribute_name: Name) -> bool
```

X.get_bool_attribute(point, metadata, attribute_name) -> bool
Get Bool Attribute

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGMetadataAccessorHelpers.copy_point"></a>

#### copy_point

```python
@classmethod
def copy_point(cls,
               point: PCGPoint,
               copy_metadata: bool = True,
               metadata: PCGMetadata = None,
               out_metadata: PCGMetadata = None) -> PCGPoint
```

X.copy_point(point, copy_metadata=True, metadata=None, out_metadata=None) -> PCGPoint
Point functions

Args:
    point (PCGPoint): 
    copy_metadata (bool): 
    metadata (PCGMetadata): 
    out_metadata (PCGMetadata): 

Returns:
    PCGPoint: 

    out_point (PCGPoint):

<a id="unreal.PCGDataFunctionLibrary"></a>