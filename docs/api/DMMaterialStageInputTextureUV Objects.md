## DMMaterialStageInputTextureUV Objects

```python
class DMMaterialStageInputTextureUV(DMMaterialStageInput)
```

DMMaterial Stage Input Texture UV

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSITextureUV.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``texture_uv`` (DMTextureUV):  [Read-Write]

<a id="unreal.DMMaterialStageInputTextureUV.texture_uv"></a>

#### texture_uv

```python
@property
def texture_uv() -> DMTextureUV
```

(DMTextureUV):  [Read-Only]

<a id="unreal.DMMaterialStageInputTextureUV.get_texture_uv"></a>

#### get_texture_uv

```python
def get_texture_uv() -> DMTextureUV
```

x.get_texture_uv() -> DMTextureUV
Get Texture UV

Returns:
    DMTextureUV:

<a id="unreal.DMMaterialStageInputTextureUV.create_stage"></a>

#### create_stage

```python
@classmethod
def create_stage(cls,
                 material_model: DynamicMaterialModel,
                 layer: DMMaterialLayerObject = None) -> DMMaterialStage
```

X.create_stage(material_model, layer=None) -> DMMaterialStage
Create Stage

Args:
    material_model (DynamicMaterialModel): 
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStageInputTextureUV.change_stage_source_uv"></a>

#### change_stage_source_uv

```python
@classmethod
def change_stage_source_uv(cls, stage: DMMaterialStage,
                           do_update: bool) -> DMMaterialStageInputTextureUV
```

X.change_stage_source_uv(stage, do_update) -> DMMaterialStageInputTextureUV
Change Stage Source UV

Args:
    stage (DMMaterialStage): 
    do_update (bool): 

Returns:
    DMMaterialStageInputTextureUV:

<a id="unreal.DMMaterialStageInputTextureUV.change_stage_input_uv"></a>

#### change_stage_input_uv

```python
@classmethod
def change_stage_input_uv(
        cls, stage: DMMaterialStage, input_idx: int, input_channel: int,
        output_channel: int) -> DMMaterialStageInputTextureUV
```

X.change_stage_input_uv(stage, input_idx, input_channel, output_channel) -> DMMaterialStageInputTextureUV
Change Stage Input UV

Args:
    stage (DMMaterialStage): 
    input_idx (int32): 
    input_channel (int32): 
    output_channel (int32): 

Returns:
    DMMaterialStageInputTextureUV:

<a id="unreal.DMMaterialStageInputValue"></a>