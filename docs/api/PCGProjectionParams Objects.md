## PCGProjectionParams Objects

```python
class PCGProjectionParams(StructBase)
```

Parameters that control projection behaviour.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGProjectionParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_list`` (str):  [Read-Write] Attributes to either explicitly exclude or include in the projection operation, depending on the Attribute Mode setting. Leave empty to gather all attributes and their values. Format is comma separated list like: Attribute1,Attribute2 .
- ``attribute_merge_operation`` (PCGMetadataOp):  [Read-Write] Operation to use to combine attributes that reside on both source and target data.
- ``attribute_mode`` (PCGMetadataFilterMode):  [Read-Write] How the attribute list is used. Exclude Attributes will ignore these attributes and their values on the projection target.
- ``color_blend_mode`` (PCGProjectionColorBlendMode):  [Read-Write] The blend mode for colors during the projection
- ``project_colors`` (bool):  [Read-Write]
  deprecated: Property 'bProjectColors' is deprecated.
- ``project_positions`` (bool):  [Read-Write] Project positions.
- ``project_rotations`` (bool):  [Read-Write] Project rotations.
- ``project_scales`` (bool):  [Read-Write] Project scales.
- ``tag_merge_operation`` (PCGProjectionTagMergeMode):  [Read-Write] Controls whether the data tags are taken from the source, the target or both.

<a id="unreal.PCGProjectionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    project_positions: bool = False,
    project_rotations: bool = False,
    project_scales: bool = False,
    color_blend_mode: PCGProjectionColorBlendMode = PCGProjectionColorBlendMode
    .SOURCE_VALUE,
    attribute_list: str = "",
    attribute_mode: PCGMetadataFilterMode = PCGMetadataFilterMode.
    EXCLUDE_ATTRIBUTES,
    attribute_merge_operation: PCGMetadataOp = PCGMetadataOp.MIN,
    tag_merge_operation: PCGProjectionTagMergeMode = PCGProjectionTagMergeMode.
    SOURCE
) -> None
```

<a id="unreal.PCGProjectionParams.project_positions"></a>

#### project\_positions

```python
@property
def project_positions() -> bool
```

(bool):  [Read-Write] Project positions.

<a id="unreal.PCGProjectionParams.project_positions"></a>

#### project\_positions

```python
@project_positions.setter
def project_positions(value: bool) -> None
```

<a id="unreal.PCGProjectionParams.project_rotations"></a>

#### project\_rotations

```python
@property
def project_rotations() -> bool
```

(bool):  [Read-Write] Project rotations.

<a id="unreal.PCGProjectionParams.project_rotations"></a>

#### project\_rotations

```python
@project_rotations.setter
def project_rotations(value: bool) -> None
```

<a id="unreal.PCGProjectionParams.project_scales"></a>

#### project\_scales

```python
@property
def project_scales() -> bool
```

(bool):  [Read-Write] Project scales.

<a id="unreal.PCGProjectionParams.project_scales"></a>

#### project\_scales

```python
@project_scales.setter
def project_scales(value: bool) -> None
```

<a id="unreal.PCGProjectionParams.color_blend_mode"></a>

#### color\_blend\_mode

```python
@property
def color_blend_mode() -> PCGProjectionColorBlendMode
```

(PCGProjectionColorBlendMode):  [Read-Write] The blend mode for colors during the projection

<a id="unreal.PCGProjectionParams.color_blend_mode"></a>

#### color\_blend\_mode

```python
@color_blend_mode.setter
def color_blend_mode(value: PCGProjectionColorBlendMode) -> None
```

<a id="unreal.PCGProjectionParams.attribute_list"></a>

#### attribute\_list

```python
@property
def attribute_list() -> str
```

(str):  [Read-Write] Attributes to either explicitly exclude or include in the projection operation, depending on the Attribute Mode setting. Leave empty to gather all attributes and their values. Format is comma separated list like: Attribute1,Attribute2 .

<a id="unreal.PCGProjectionParams.attribute_list"></a>

#### attribute\_list

```python
@attribute_list.setter
def attribute_list(value: str) -> None
```

<a id="unreal.PCGProjectionParams.attribute_mode"></a>

#### attribute\_mode

```python
@property
def attribute_mode() -> PCGMetadataFilterMode
```

(PCGMetadataFilterMode):  [Read-Write] How the attribute list is used. Exclude Attributes will ignore these attributes and their values on the projection target.

<a id="unreal.PCGProjectionParams.attribute_mode"></a>

#### attribute\_mode

```python
@attribute_mode.setter
def attribute_mode(value: PCGMetadataFilterMode) -> None
```

<a id="unreal.PCGProjectionParams.attribute_merge_operation"></a>

#### attribute\_merge\_operation

```python
@property
def attribute_merge_operation() -> PCGMetadataOp
```

(PCGMetadataOp):  [Read-Write] Operation to use to combine attributes that reside on both source and target data.

<a id="unreal.PCGProjectionParams.attribute_merge_operation"></a>

#### attribute\_merge\_operation

```python
@attribute_merge_operation.setter
def attribute_merge_operation(value: PCGMetadataOp) -> None
```

<a id="unreal.PCGProjectionParams.tag_merge_operation"></a>

#### tag\_merge\_operation

```python
@property
def tag_merge_operation() -> PCGProjectionTagMergeMode
```

(PCGProjectionTagMergeMode):  [Read-Write] Controls whether the data tags are taken from the source, the target or both.

<a id="unreal.PCGProjectionParams.tag_merge_operation"></a>

#### tag\_merge\_operation

```python
@tag_merge_operation.setter
def tag_merge_operation(value: PCGProjectionTagMergeMode) -> None
```

<a id="unreal.PCGProjectionParams.project_colors"></a>

#### project\_colors

```python
@property
def project_colors() -> bool
```

(bool):  [Read-Write]
deprecated: Property 'bProjectColors' is deprecated.

<a id="unreal.PCGProjectionParams.project_colors"></a>

#### project\_colors

```python
@project_colors.setter
def project_colors(value: bool) -> None
```

<a id="unreal.PCGSelectGrammarCriterion"></a>