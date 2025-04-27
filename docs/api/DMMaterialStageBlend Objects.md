## DMMaterialStageBlend Objects

```python
class DMMaterialStageBlend(DMMaterialStageThroughput)
```

A node which represents a blend operation.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStageBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``base_channel_override`` (AvaColorChannel):  [Read-Write] Changes the output channel of the base input.
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageBlend.base_channel_override"></a>

#### base_channel_override

```python
@property
def base_channel_override() -> AvaColorChannel
```

(AvaColorChannel):  [Read-Only] Changes the output channel of the base input.

<a id="unreal.DMMaterialStageBlend.set_base_channel_override"></a>

#### set_base_channel_override

```python
def set_base_channel_override(mask_channel: AvaColorChannel) -> None
```

x.set_base_channel_override(mask_channel) -> None
Set Base Channel Override

Args:
    mask_channel (AvaColorChannel):

<a id="unreal.DMMaterialStageBlend.get_base_channel_override"></a>

#### get_base_channel_override

```python
def get_base_channel_override() -> AvaColorChannel
```

x.get_base_channel_override() -> AvaColorChannel
Get Base Channel Override

Returns:
    AvaColorChannel:

<a id="unreal.DMMaterialStageBlendFunction"></a>