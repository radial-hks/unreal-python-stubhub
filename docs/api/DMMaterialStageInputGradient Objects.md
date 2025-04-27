## DMMaterialStageInputGradient Objects

```python
class DMMaterialStageInputGradient(DMMaterialStageInputThroughput)
```

DMMaterial Stage Input Gradient

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSIGradient.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``sub_stage`` (DMMaterialSubStage):  [Read-Only]

<a id="unreal.DMMaterialStageInputGradient.set_material_stage_gradient_class"></a>

#### set_material_stage_gradient_class

```python
def set_material_stage_gradient_class(
        material_stage_gradient_class: Class) -> None
```

x.set_material_stage_gradient_class(material_stage_gradient_class) -> None
Set Material Stage Gradient Class

Args:
    material_stage_gradient_class (type(Class)):

<a id="unreal.DMMaterialStageInputGradient.get_material_stage_gradient_class"></a>

#### get_material_stage_gradient_class

```python
def get_material_stage_gradient_class() -> Class
```

x.get_material_stage_gradient_class() -> type(Class)
Get Material Stage Gradient Class

Returns:
    type(Class):

<a id="unreal.DMMaterialStageInputGradient.get_material_stage_gradient"></a>

#### get_material_stage_gradient

```python
def get_material_stage_gradient() -> DMMaterialStageGradient
```

x.get_material_stage_gradient() -> DMMaterialStageGradient
Get Material Stage Gradient

Returns:
    DMMaterialStageGradient:

<a id="unreal.DMMaterialStageInputGradient.create_stage"></a>

#### create_stage

```python
@classmethod
def create_stage(cls,
                 material_stage_gradient_class: Class,
                 layer: DMMaterialLayerObject = None) -> DMMaterialStage
```

X.create_stage(material_stage_gradient_class, layer=None) -> DMMaterialStage
Create Stage

Args:
    material_stage_gradient_class (type(Class)): 
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStageInputGradient.change_stage_source_gradient"></a>

#### change_stage_source_gradient

```python
@classmethod
def change_stage_source_gradient(
        cls, stage: DMMaterialStage,
        gradient_class: Class) -> DMMaterialStageInputGradient
```

X.change_stage_source_gradient(stage, gradient_class) -> DMMaterialStageInputGradient
Change Stage Source Gradient

Args:
    stage (DMMaterialStage): 
    gradient_class (type(Class)): 

Returns:
    DMMaterialStageInputGradient:

<a id="unreal.DMMaterialStageInputGradient.change_stage_input_gradient"></a>

#### change_stage_input_gradient

```python
@classmethod
def change_stage_input_gradient(
        cls, stage: DMMaterialStage, gradient_class: Class, input_idx: int,
        input_channel: int,
        output_channel: int) -> DMMaterialStageInputGradient
```

X.change_stage_input_gradient(stage, gradient_class, input_idx, input_channel, output_channel) -> DMMaterialStageInputGradient
Change the input type of an input on a stage to a gradient.

Args:
    stage (DMMaterialStage): 
    gradient_class (type(Class)): 
    input_idx (int32): Index of the source input.
    input_channel (int32): The channel of the input that the input connects to.
    output_channel (int32): The channel of the output to connect.

Returns:
    DMMaterialStageInputGradient:

<a id="unreal.DMMaterialStageInputSlot"></a>