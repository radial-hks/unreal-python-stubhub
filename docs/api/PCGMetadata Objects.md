## PCGMetadata Objects

```python
class PCGMetadata(Object)
```

PCGMetadata

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMetadata.h

<a id="unreal.PCGMetadata.set_point_attributes"></a>

#### set_point_attributes

```python
def set_point_attributes(point: PCGPoint, metadata: PCGMetadata,
                         out_point: PCGPoint) -> PCGPoint
```

x.set_point_attributes(point, metadata, out_point) -> PCGPoint
Set Point Attributes

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    out_point (PCGPoint): 

Returns:
    PCGPoint: 

    out_point (PCGPoint):

<a id="unreal.PCGMetadata.set_attributes_by_key"></a>

#### set_attributes_by_key

```python
def set_attributes_by_key(key: int, metadata: PCGMetadata,
                          target_key: int) -> int
```

x.set_attributes_by_key(key, metadata, target_key) -> int64
Set Attributes by Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    target_key (int64): 

Returns:
    int64: 

    out_key (int64):

<a id="unreal.PCGMetadata.reset_weighted_attributes_by_key"></a>

#### reset_weighted_attributes_by_key

```python
def reset_weighted_attributes_by_key(target_key: int) -> int
```

x.reset_weighted_attributes_by_key(target_key) -> int64
Reset Weighted Attributes by Key

Args:
    target_key (int64): 

Returns:
    int64: 

    out_key (int64):

<a id="unreal.PCGMetadata.reset_point_weighted_attributes"></a>

#### reset_point_weighted_attributes

```python
def reset_point_weighted_attributes() -> PCGPoint
```

x.reset_point_weighted_attributes() -> PCGPoint
Reset Point Weighted Attributes

Returns:
    PCGPoint: 

    out_point (PCGPoint):

<a id="unreal.PCGMetadata.rename_attribute"></a>

#### rename_attribute

```python
def rename_attribute(attribute_to_rename: Name,
                     new_attribute_name: Name) -> bool
```

x.rename_attribute(attribute_to_rename, new_attribute_name) -> bool
Rename attribute

Args:
    attribute_to_rename (Name): 
    new_attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGMetadata.merge_point_attributes"></a>

#### merge_point_attributes

```python
def merge_point_attributes(point_a: PCGPoint, metadata_a: PCGMetadata,
                           point_b: PCGPoint, metadata_b: PCGMetadata,
                           target_point: PCGPoint,
                           op: PCGMetadataOp) -> PCGPoint
```

x.merge_point_attributes(point_a, metadata_a, point_b, metadata_b, target_point, op) -> PCGPoint
Merge Point Attributes

Args:
    point_a (PCGPoint): 
    metadata_a (PCGMetadata): 
    point_b (PCGPoint): 
    metadata_b (PCGMetadata): 
    target_point (PCGPoint): 
    op (PCGMetadataOp): 

Returns:
    PCGPoint: 

    target_point (PCGPoint):

<a id="unreal.PCGMetadata.merge_attributes_by_key"></a>

#### merge_attributes_by_key

```python
def merge_attributes_by_key(key_a: int, metadata_a: PCGMetadata, key_b: int,
                            metadata_b: PCGMetadata, target_key: int,
                            op: PCGMetadataOp) -> int
```

x.merge_attributes_by_key(key_a, metadata_a, key_b, metadata_b, target_key, op) -> int64
Blueprint-friend versions

Args:
    key_a (int64): 
    metadata_a (PCGMetadata): 
    key_b (int64): 
    metadata_b (PCGMetadata): 
    target_key (int64): 
    op (PCGMetadataOp): 

Returns:
    int64: 

    out_key (int64):

<a id="unreal.PCGMetadata.k2_initialize_as_copy_with_attribute_filter"></a>

#### k2_initialize_as_copy_with_attribute_filter

```python
def k2_initialize_as_copy_with_attribute_filter(
    metadata_to_copy: PCGMetadata,
    filtered_attributes: Set[Name],
    optional_entries_to_copy: Array[int],
    filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.
    EXCLUDE_ATTRIBUTES
) -> None
```

x.k2_initialize_as_copy_with_attribute_filter(metadata_to_copy, filtered_attributes, optional_entries_to_copy, filter_mode=PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES) -> None
Initializes the metadata from a parent metadata by copy filtered attributes only to it

Args:
    metadata_to_copy (PCGMetadata): Metadata to copy from
    filtered_attributes (Set[Name]): Attributes to keep/exclude, can be empty.
    optional_entries_to_copy (Array[int64]): Optional array that contains the keys to copy over. This array order will be respected, so it can also be used to re-order entries. If empty, copy them all.
    filter_mode (PCGMetadataFilterMode): Filter to know if we should keep or exclude InFilteredAttributes.

<a id="unreal.PCGMetadata.initialize_as_copy_with_attribute_filter"></a>

#### initialize_as_copy_with_attribute_filter

```python
def initialize_as_copy_with_attribute_filter(
    metadata_to_copy: PCGMetadata,
    filtered_attributes: Set[Name],
    optional_entries_to_copy: Array[int],
    filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.
    EXCLUDE_ATTRIBUTES
) -> None
```

deprecated: 'initialize_as_copy_with_attribute_filter' was renamed to 'k2_initialize_as_copy_with_attribute_filter'.

<a id="unreal.PCGMetadata.k2_initialize_as_copy"></a>

#### k2_initialize_as_copy

```python
def k2_initialize_as_copy(metadata_to_copy: PCGMetadata,
                          optional_entries_to_copy: Array[int]) -> None
```

x.k2_initialize_as_copy(metadata_to_copy, optional_entries_to_copy) -> None
Initializes the metadata from a parent metadata by copying all attributes to it.

Args:
    metadata_to_copy (PCGMetadata): Metadata to copy from
    optional_entries_to_copy (Array[int64]): Optional array that contains the keys to copy over. This array order will be respected, so it can also be used to re-order entries. If empty, copy them all.

<a id="unreal.PCGMetadata.initialize_as_copy"></a>

#### initialize_as_copy

```python
def initialize_as_copy(metadata_to_copy: PCGMetadata,
                       optional_entries_to_copy: Array[int]) -> None
```

deprecated: 'initialize_as_copy' was renamed to 'k2_initialize_as_copy'.

<a id="unreal.PCGMetadata.initialize_with_attribute_filter"></a>

#### initialize_with_attribute_filter

```python
def initialize_with_attribute_filter(
    parent: PCGMetadata,
    filtered_attributes: Set[Name],
    filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.
    EXCLUDE_ATTRIBUTES,
    match_operator: PCGStringMatchingOperator = PCGStringMatchingOperator.EQUAL
) -> None
```

x.initialize_with_attribute_filter(parent, filtered_attributes, filter_mode=PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, match_operator=PCGStringMatchingOperator.EQUAL) -> None
Initializes the metadata from a parent metadata. Copies attributes and values.

Args:
    parent (PCGMetadata): The parent metadata to use as a template, if any (can be null).
    filtered_attributes (Set[Name]): Optional list of attributes to exclude or include when adding the attributes from the parent.
    filter_mode (PCGMetadataFilterMode): Defines attribute filter operation.
    match_operator (PCGStringMatchingOperator):

<a id="unreal.PCGMetadata.initialize"></a>

#### initialize

```python
def initialize(parent: PCGMetadata) -> None
```

x.initialize(parent) -> None
Initializes the metadata from a parent metadata, if any (can be null). Copies attributes and values.

Args:
    parent (PCGMetadata):

<a id="unreal.PCGMetadata.has_common_attributes"></a>

#### has_common_attributes

```python
def has_common_attributes(metadata: PCGMetadata) -> bool
```

x.has_common_attributes(metadata) -> bool
Has Common Attributes

Args:
    metadata (PCGMetadata): 

Returns:
    bool:

<a id="unreal.PCGMetadata.has_attribute"></a>

#### has_attribute

```python
def has_attribute(attribute_name: Name) -> bool
```

x.has_attribute(attribute_name) -> bool
Has Attribute

Args:
    attribute_name (Name): 

Returns:
    bool:

<a id="unreal.PCGMetadata.get_item_count_for_child"></a>

#### get_item_count_for_child

```python
def get_item_count_for_child() -> int
```

x.get_item_count_for_child() -> int64
Return the number of entries in metadata including the parent entries.

Returns:
    int64:

<a id="unreal.PCGMetadata.get_attributes"></a>

#### get_attributes

```python
def get_attributes() -> Tuple[Array[Name], Array[PCGMetadataTypes]]
```

x.get_attributes() -> (attribute_names=Array[Name], attribute_types=Array[PCGMetadataTypes])
Get Attributes

Returns:
    tuple: 

    attribute_names (Array[Name]): 

    attribute_types (Array[PCGMetadataTypes]):

<a id="unreal.PCGMetadata.get_attribute_count"></a>

#### get_attribute_count

```python
def get_attribute_count() -> int
```

x.get_attribute_count() -> int32
Return the number of attributes in this metadata.

Returns:
    int32:

<a id="unreal.PCGMetadata.flatten"></a>

#### flatten

```python
def flatten() -> None
```

x.flatten() -> None
Unparents current metadata by flattening the attributes (values, entries, etc.) and potentially compress the data to remove unused values.

<a id="unreal.PCGMetadata.delete_attribute"></a>

#### delete_attribute

```python
def delete_attribute(attribute_name: Name) -> None
```

x.delete_attribute(attribute_name) -> None
Delete/Hide attribute // Due to stream inheriting, we might want to consider "hiding" parent stream and deleting local streams only

Args:
    attribute_name (Name):

<a id="unreal.PCGMetadata.create_vector_attribute"></a>

#### create_vector_attribute

```python
def create_vector_attribute(attribute_name: Name,
                            default_value: Vector,
                            allows_interpolation: bool,
                            override_parent: bool = True) -> PCGMetadata
```

x.create_vector_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Vector Attribute

Args:
    attribute_name (Name): 
    default_value (Vector): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_vector4_attribute"></a>

#### create_vector4_attribute

```python
def create_vector4_attribute(attribute_name: Name,
                             default_value: Vector4,
                             allows_interpolation: bool,
                             override_parent: bool = True) -> PCGMetadata
```

x.create_vector4_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Vector 4Attribute

Args:
    attribute_name (Name): 
    default_value (Vector4): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_vector2_attribute"></a>

#### create_vector2_attribute

```python
def create_vector2_attribute(attribute_name: Name,
                             default_value: Vector2D,
                             allows_interpolation: bool,
                             override_parent: bool = True) -> PCGMetadata
```

x.create_vector2_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Vector 2Attribute

Args:
    attribute_name (Name): 
    default_value (Vector2D): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_transform_attribute"></a>

#### create_transform_attribute

```python
def create_transform_attribute(attribute_name: Name,
                               default_value: Transform,
                               allows_interpolation: bool,
                               override_parent: bool = True) -> PCGMetadata
```

x.create_transform_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Transform Attribute

Args:
    attribute_name (Name): 
    default_value (Transform): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_string_attribute"></a>

#### create_string_attribute

```python
def create_string_attribute(attribute_name: Name,
                            default_value: str,
                            allows_interpolation: bool,
                            override_parent: bool = True) -> PCGMetadata
```

x.create_string_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create String Attribute

Args:
    attribute_name (Name): 
    default_value (str): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_soft_object_path_attribute"></a>

#### create_soft_object_path_attribute

```python
def create_soft_object_path_attribute(
        attribute_name: Name,
        default_value: SoftObjectPath,
        allows_interpolation: bool,
        override_parent: bool = True) -> PCGMetadata
```

x.create_soft_object_path_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Soft Object Path Attribute

Args:
    attribute_name (Name): 
    default_value (SoftObjectPath): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_soft_class_path_attribute"></a>

#### create_soft_class_path_attribute

```python
def create_soft_class_path_attribute(
        attribute_name: Name,
        default_value: SoftClassPath,
        allows_interpolation: bool,
        override_parent: bool = True) -> PCGMetadata
```

x.create_soft_class_path_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Soft Class Path Attribute

Args:
    attribute_name (Name): 
    default_value (SoftClassPath): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_rotator_attribute"></a>

#### create_rotator_attribute

```python
def create_rotator_attribute(attribute_name: Name,
                             default_value: Rotator,
                             allows_interpolation: bool,
                             override_parent: bool = True) -> PCGMetadata
```

x.create_rotator_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Rotator Attribute

Args:
    attribute_name (Name): 
    default_value (Rotator): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_quat_attribute"></a>

#### create_quat_attribute

```python
def create_quat_attribute(attribute_name: Name,
                          default_value: Quat,
                          allows_interpolation: bool,
                          override_parent: bool = True) -> PCGMetadata
```

x.create_quat_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Quat Attribute

Args:
    attribute_name (Name): 
    default_value (Quat): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_name_attribute"></a>

#### create_name_attribute

```python
def create_name_attribute(attribute_name: Name,
                          default_value: Name,
                          allows_interpolation: bool,
                          override_parent: bool = True) -> PCGMetadata
```

x.create_name_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Name Attribute

Args:
    attribute_name (Name): 
    default_value (Name): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_integer64_attribute"></a>

#### create_integer64_attribute

```python
def create_integer64_attribute(attribute_name: Name,
                               default_value: int,
                               allows_interpolation: bool,
                               override_parent: bool = True) -> PCGMetadata
```

x.create_integer64_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Integer 64Attribute

Args:
    attribute_name (Name): 
    default_value (int64): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_integer32_attribute"></a>

#### create_integer32_attribute

```python
def create_integer32_attribute(attribute_name: Name,
                               default_value: int,
                               allows_interpolation: bool,
                               override_parent: bool = True) -> PCGMetadata
```

x.create_integer32_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Integer 32Attribute

Args:
    attribute_name (Name): 
    default_value (int32): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_float_attribute"></a>

#### create_float_attribute

```python
def create_float_attribute(attribute_name: Name,
                           default_value: float,
                           allows_interpolation: bool,
                           override_parent: bool = True) -> PCGMetadata
```

x.create_float_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Float Attribute

Args:
    attribute_name (Name): 
    default_value (float): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_double_attribute"></a>

#### create_double_attribute

```python
def create_double_attribute(attribute_name: Name,
                            default_value: float,
                            allows_interpolation: bool,
                            override_parent: bool = True) -> PCGMetadata
```

x.create_double_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Double Attribute

Args:
    attribute_name (Name): 
    default_value (double): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.create_bool_attribute"></a>

#### create_bool_attribute

```python
def create_bool_attribute(attribute_name: Name,
                          default_value: bool,
                          allows_interpolation: bool,
                          override_parent: bool = True) -> PCGMetadata
```

x.create_bool_attribute(attribute_name, default_value, allows_interpolation, override_parent=True) -> PCGMetadata
Create Bool Attribute

Args:
    attribute_name (Name): 
    default_value (bool): 
    allows_interpolation (bool): 
    override_parent (bool): 

Returns:
    PCGMetadata:

<a id="unreal.PCGMetadata.copy_existing_attribute"></a>

#### copy_existing_attribute

```python
def copy_existing_attribute(attribute_to_copy: Name,
                            new_attribute_name: Name,
                            keep_parent: bool = True) -> bool
```

x.copy_existing_attribute(attribute_to_copy, new_attribute_name, keep_parent=True) -> bool
Copy attribute

Args:
    attribute_to_copy (Name): 
    new_attribute_name (Name): 
    keep_parent (bool): 

Returns:
    bool:

<a id="unreal.PCGMetadata.copy_attributes"></a>

#### copy_attributes

```python
def copy_attributes(other: PCGMetadata) -> None
```

x.copy_attributes(other) -> None
Copies attributes from another metadata, including entries & values. Warning: this is intended when dealing with the same data set

Args:
    other (PCGMetadata):

<a id="unreal.PCGMetadata.copy_attribute"></a>

#### copy_attribute

```python
def copy_attribute(other: PCGMetadata, attribute_to_copy: Name,
                   new_attribute_name: Name) -> None
```

x.copy_attribute(other, attribute_to_copy, new_attribute_name) -> None
Copies an attribute from another metadata, including entries & values. Warning: this is intended when dealing with the same data set

Args:
    other (PCGMetadata): 
    attribute_to_copy (Name): 
    new_attribute_name (Name):

<a id="unreal.PCGMetadata.clear_attribute"></a>

#### clear_attribute

```python
def clear_attribute(attribute_to_clear: Name) -> None
```

x.clear_attribute(attribute_to_clear) -> None
Clear/Reinit attribute

Args:
    attribute_to_clear (Name):

<a id="unreal.PCGMetadata.add_entry"></a>

#### add_entry

```python
def add_entry(parent_entry_key: int = -1) -> int
```

x.add_entry(parent_entry_key=-1) -> int64
Adds a unique entry key to the metadata

Args:
    parent_entry_key (int64): 

Returns:
    int64:

<a id="unreal.PCGMetadata.add_attributes_filtered"></a>

#### add_attributes_filtered

```python
def add_attributes_filtered(
    other: PCGMetadata,
    filtered_attributes: Set[Name],
    filter_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.
    EXCLUDE_ATTRIBUTES,
    match_operator: PCGStringMatchingOperator = PCGStringMatchingOperator.EQUAL
) -> None
```

x.add_attributes_filtered(other, filtered_attributes, filter_mode=PCGMetadataFilterMode.EXCLUDE_ATTRIBUTES, match_operator=PCGStringMatchingOperator.EQUAL) -> None
Creates missing attributes from another metadata if they are not currently present - note that this does not copy values.

Args:
    other (PCGMetadata): The other metadata to obtain a list of attributes from.
    filtered_attributes (Set[Name]): Optional list of attributes to exclude or include when adding the attributes.
    filter_mode (PCGMetadataFilterMode): Defines attribute filter operation.
    match_operator (PCGStringMatchingOperator):

<a id="unreal.PCGMetadata.add_attributes"></a>

#### add_attributes

```python
def add_attributes(other: PCGMetadata) -> None
```

x.add_attributes(other) -> None
Creates missing attributes from another metadata if they are not currently present - note that this does not copy values

Args:
    other (PCGMetadata):

<a id="unreal.PCGMetadata.add_attribute"></a>

#### add_attribute

```python
def add_attribute(other: PCGMetadata, attribute_name: Name) -> None
```

x.add_attribute(other, attribute_name) -> None
Creates missing attribute from another metadata if it is not currently present - note that this does not copy values

Args:
    other (PCGMetadata): 
    attribute_name (Name):

<a id="unreal.PCGMetadata.accumulate_weighted_attributes_by_key"></a>

#### accumulate_weighted_attributes_by_key

```python
def accumulate_weighted_attributes_by_key(
        key: int, metadata: PCGMetadata, weight: float,
        set_non_interpolable_attributes: bool, target_key: int) -> int
```

x.accumulate_weighted_attributes_by_key(key, metadata, weight, set_non_interpolable_attributes, target_key) -> int64
Accumulate Weighted Attributes by Key

Args:
    key (int64): 
    metadata (PCGMetadata): 
    weight (float): 
    set_non_interpolable_attributes (bool): 
    target_key (int64): 

Returns:
    int64: 

    out_key (int64):

<a id="unreal.PCGMetadata.accumulate_point_weighted_attributes"></a>

#### accumulate_point_weighted_attributes

```python
def accumulate_point_weighted_attributes(point: PCGPoint,
                                         metadata: PCGMetadata, weight: float,
                                         set_non_interpolable_attributes: bool,
                                         out_point: PCGPoint) -> PCGPoint
```

x.accumulate_point_weighted_attributes(point, metadata, weight, set_non_interpolable_attributes, out_point) -> PCGPoint
Accumulate Point Weighted Attributes

Args:
    point (PCGPoint): 
    metadata (PCGMetadata): 
    weight (float): 
    set_non_interpolable_attributes (bool): 
    out_point (PCGPoint): 

Returns:
    PCGPoint: 

    out_point (PCGPoint):

<a id="unreal.PCGMetadataAccessorHelpers"></a>