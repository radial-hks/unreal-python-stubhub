## DMMaterialStageThroughputLayerBlend Objects

```python
class DMMaterialStageThroughputLayerBlend(DMMaterialStageThroughput)
```

Used as the source for mask stages.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStageThroughputLayerBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``is_alpha_only_blend`` (bool):  [Read-Write]
- ``mask_channel_override`` (AvaColorChannel):  [Read-Write] Changes the output channel of the mask input.
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``premultiply_alpha`` (bool):  [Read-Write] Additionally multiplies the output of the RGB Stage by the output from this Stage.

<a id="unreal.DMMaterialStageThroughputLayerBlend.mask_channel_override"></a>

#### mask_channel_override

```python
@property
def mask_channel_override() -> AvaColorChannel
```

(AvaColorChannel):  [Read-Only] Changes the output channel of the mask input.

<a id="unreal.DMMaterialStageThroughputLayerBlend.premultiply_alpha"></a>

#### premultiply_alpha

```python
@property
def premultiply_alpha() -> bool
```

(bool):  [Read-Only] Additionally multiplies the output of the RGB Stage by the output from this Stage.

<a id="unreal.DMMaterialStageThroughputLayerBlend.is_alpha_only_blend"></a>

#### is_alpha_only_blend

```python
@property
def is_alpha_only_blend() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialStageThroughputLayerBlend.use_premultiply_alpha"></a>

#### use_premultiply_alpha

```python
def use_premultiply_alpha() -> bool
```

x.use_premultiply_alpha() -> bool
When true, the base stage's output will be multiplied by this stage (darkening it where it is translucent).

Returns:
    bool:

<a id="unreal.DMMaterialStageThroughputLayerBlend.set_premultiply_alpha"></a>

#### set_premultiply_alpha

```python
def set_premultiply_alpha(value: bool) -> None
```

x.set_premultiply_alpha(value) -> None
When true, the base stage's output will be multiplied by this stage (darkening it where it is translucent).

Args:
    value (bool):

<a id="unreal.DMMaterialStageThroughputLayerBlend.set_mask_channel_override"></a>

#### set_mask_channel_override

```python
def set_mask_channel_override(mask_channel: AvaColorChannel) -> None
```

x.set_mask_channel_override(mask_channel) -> None
Filters the output of the mask input node with the given channel.

Args:
    mask_channel (AvaColorChannel):

<a id="unreal.DMMaterialStageThroughputLayerBlend.get_mask_channel_override"></a>

#### get_mask_channel_override

```python
def get_mask_channel_override() -> AvaColorChannel
```

x.get_mask_channel_override() -> AvaColorChannel
Filters the output of the mask input node with the given channel.

Returns:
    AvaColorChannel:

<a id="unreal.DMMaterialStageThroughputLayerBlend.get_input_mask"></a>

#### get_input_mask

```python
def get_input_mask() -> DMMaterialStageInput
```

x.get_input_mask() -> DMMaterialStageInput
Returns the input connected to the Mask input.

Returns:
    DMMaterialStageInput:

<a id="unreal.DMMaterialStageThroughputLayerBlend.create_stage"></a>

#### create_stage

```python
@classmethod
def create_stage(cls, layer: DMMaterialLayerObject = None) -> DMMaterialStage
```

X.create_stage(layer=None) -> DMMaterialStage
Create Stage

Args:
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialSubStage"></a>