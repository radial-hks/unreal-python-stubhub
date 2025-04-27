## DMMaterialStageConnectorChannel Objects

```python
class DMMaterialStageConnectorChannel(StructBase)
```

An individual component of a connector (e.g. G from RGB.)

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_property`` (DMMaterialPropertyType):  [Read-Only] When using previous stages, this is the material property the previous stage is using
- ``output_channel`` (int32):  [Read-Only] This can be used to break down float2/3/4 into single pieces of data
  A value of 0 will be the original output. A bitmask (1,2,4,8) will reference (and combine) the specific channels.
- ``output_index`` (int32):  [Read-Only] The index of the output connector of the given stage.
- ``source_index`` (int32):  [Read-Only] The index of the source of this channel
  Index 0 is the previous stage, 1+ are the other inputs required by the current stage (e.g. textures, uvs, etc.)

<a id="unreal.DMMaterialStageConnectorChannel.__init__"></a>

#### __init__

```python
def __init__(source_index: int = 0,
             material_property: DMMaterialPropertyType = DMMaterialPropertyType
             .NONE,
             output_index: int = 0,
             output_channel: int = 0) -> None
```

<a id="unreal.DMMaterialStageConnectorChannel.source_index"></a>

#### source_index

```python
@property
def source_index() -> int
```

(int32):  [Read-Only] The index of the source of this channel
Index 0 is the previous stage, 1+ are the other inputs required by the current stage (e.g. textures, uvs, etc.)

<a id="unreal.DMMaterialStageConnectorChannel.material_property"></a>

#### material_property

```python
@property
def material_property() -> DMMaterialPropertyType
```

(DMMaterialPropertyType):  [Read-Only] When using previous stages, this is the material property the previous stage is using

<a id="unreal.DMMaterialStageConnectorChannel.output_index"></a>

#### output_index

```python
@property
def output_index() -> int
```

(int32):  [Read-Only] The index of the output connector of the given stage.

<a id="unreal.DMMaterialStageConnectorChannel.output_channel"></a>

#### output_channel

```python
@property
def output_channel() -> int
```

(int32):  [Read-Only] This can be used to break down float2/3/4 into single pieces of data
A value of 0 will be the original output. A bitmask (1,2,4,8) will reference (and combine) the specific channels.

<a id="unreal.DMValueDefinition"></a>