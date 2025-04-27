## InterchangeSourceNode Objects

```python
class InterchangeSourceNode(InterchangeBaseNode)
```

This class allows a translator to add general source data that describes the whole source. Pipelines can use this information.

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeSourceNode.h

<a id="unreal.InterchangeSourceNode.set_extra_information"></a>

#### set_extra_information

```python
def set_extra_information(name: str, value: str) -> bool
```

x.set_extra_information(name, value) -> bool
Set Extra Information that we want to show in the Config Panel (such as File Information).

Args:
    name (str): 
    value (str): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_source_timeline_start"></a>

#### set_custom_source_timeline_start

```python
def set_custom_source_timeline_start(attribute_value: float) -> bool
```

x.set_custom_source_timeline_start(attribute_value) -> bool
Set the start of the source timeline.

Args:
    attribute_value (double): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_source_timeline_end"></a>

#### set_custom_source_timeline_end

```python
def set_custom_source_timeline_end(attribute_value: float) -> bool
```

x.set_custom_source_timeline_end(attribute_value) -> bool
Set the end of the source timeline.

Args:
    attribute_value (double): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_source_frame_rate_numerator"></a>

#### set_custom_source_frame_rate_numerator

```python
def set_custom_source_frame_rate_numerator(attribute_value: int) -> bool
```

x.set_custom_source_frame_rate_numerator(attribute_value) -> bool
Set the source frame rate numerator.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_source_frame_rate_denominator"></a>

#### set_custom_source_frame_rate_denominator

```python
def set_custom_source_frame_rate_denominator(attribute_value: int) -> bool
```

x.set_custom_source_frame_rate_denominator(attribute_value) -> bool
Set the source frame rate denominator.

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_import_unused_material"></a>

#### set_custom_import_unused_material

```python
def set_custom_import_unused_material(attribute_value: bool) -> bool
```

x.set_custom_import_unused_material(attribute_value) -> bool
Set whether to import materials that aren't used.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_axis_conversion_inverse_transform"></a>

#### set_custom_axis_conversion_inverse_transform

```python
def set_custom_axis_conversion_inverse_transform(
        axis_conversion_inverse_transform: Transform) -> bool
```

x.set_custom_axis_conversion_inverse_transform(axis_conversion_inverse_transform) -> bool
Set the Axis Conversion Inverse Transform (Primarily used for Socket transform calculations.).

Args:
    axis_conversion_inverse_transform (Transform): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_animated_time_start"></a>

#### set_custom_animated_time_start

```python
def set_custom_animated_time_start(attribute_value: float) -> bool
```

x.set_custom_animated_time_start(attribute_value) -> bool
Set the start of the source animated time.

Args:
    attribute_value (double): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.set_custom_animated_time_end"></a>

#### set_custom_animated_time_end

```python
def set_custom_animated_time_end(attribute_value: float) -> bool
```

x.set_custom_animated_time_end(attribute_value) -> bool
Set the end of the source animated time.

Args:
    attribute_value (double): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.remove_extra_information"></a>

#### remove_extra_information

```python
def remove_extra_information(name: str) -> bool
```

x.remove_extra_information(name) -> bool
Remove Extra Information that we dont want to show in the Config Panel.

Args:
    name (str): 

Returns:
    bool:

<a id="unreal.InterchangeSourceNode.initialize_source_node"></a>

#### initialize_source_node

```python
def initialize_source_node(unique_id: str, display_label: str) -> None
```

x.initialize_source_node(unique_id, display_label) -> None
Initialize the base data of the node.

Args:
    unique_id (str): The unique ID for this node.
    display_label (str): The name of the node.

<a id="unreal.InterchangeSourceNode.get_extra_information"></a>

#### get_extra_information

```python
def get_extra_information() -> Map[str, str]
```

x.get_extra_information() -> Map[str, str]
Get Extra Information that we want to show in the Config Panel (such as File Information).

Returns:
    Map[str, str]: 

    out_extra_information (Map[str, str]):

<a id="unreal.InterchangeSourceNode.get_custom_source_timeline_start"></a>

#### get_custom_source_timeline_start

```python
def get_custom_source_timeline_start() -> Optional[float]
```

x.get_custom_source_timeline_start() -> double or None
Query the start of the source timeline.

Returns:
    double or None: 

    attribute_value (double):

<a id="unreal.InterchangeSourceNode.get_custom_source_timeline_end"></a>

#### get_custom_source_timeline_end

```python
def get_custom_source_timeline_end() -> Optional[float]
```

x.get_custom_source_timeline_end() -> double or None
Query the end of the source timeline.

Returns:
    double or None: 

    attribute_value (double):

<a id="unreal.InterchangeSourceNode.get_custom_source_frame_rate_numerator"></a>

#### get_custom_source_frame_rate_numerator

```python
def get_custom_source_frame_rate_numerator() -> Optional[int]
```

x.get_custom_source_frame_rate_numerator() -> int32 or None
Query the source frame rate numerator.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeSourceNode.get_custom_source_frame_rate_denominator"></a>

#### get_custom_source_frame_rate_denominator

```python
def get_custom_source_frame_rate_denominator() -> Optional[int]
```

x.get_custom_source_frame_rate_denominator() -> int32 or None
Query the source frame rate denominator.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeSourceNode.get_custom_import_unused_material"></a>

#### get_custom_import_unused_material

```python
def get_custom_import_unused_material() -> Optional[bool]
```

x.get_custom_import_unused_material() -> bool or None
Query whether to import materials that aren't used.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeSourceNode.get_custom_axis_conversion_inverse_transform"></a>

#### get_custom_axis_conversion_inverse_transform

```python
def get_custom_axis_conversion_inverse_transform() -> Optional[Transform]
```

x.get_custom_axis_conversion_inverse_transform() -> Transform or None
Query Axis Conversion Inverse Transform (Primarily used for Socket transform calculations.).

Returns:
    Transform or None: 

    axis_conversion_inverse_transform (Transform):

<a id="unreal.InterchangeSourceNode.get_custom_animated_time_start"></a>

#### get_custom_animated_time_start

```python
def get_custom_animated_time_start() -> Optional[float]
```

x.get_custom_animated_time_start() -> double or None
Query the start of the source animated time.

Returns:
    double or None: 

    attribute_value (double):

<a id="unreal.InterchangeSourceNode.get_custom_animated_time_end"></a>

#### get_custom_animated_time_end

```python
def get_custom_animated_time_end() -> Optional[float]
```

x.get_custom_animated_time_end() -> double or None
Query the end of the source animated time.

Returns:
    double or None: 

    attribute_value (double):

<a id="unreal.InterchangeUserDefinedAttributesAPI"></a>