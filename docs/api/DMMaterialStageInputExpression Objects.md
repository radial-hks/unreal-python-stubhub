## DMMaterialStageInputExpression Objects

```python
class DMMaterialStageInputExpression(DMMaterialStageInputThroughput)
```

DMMaterial Stage Input Expression

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSIExpression.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``sub_stage`` (DMMaterialSubStage):  [Read-Only]

<a id="unreal.DMMaterialStageInputExpression.set_material_stage_expression_class"></a>

#### set_material_stage_expression_class

```python
def set_material_stage_expression_class(
        material_stage_expression_class: Class) -> None
```

x.set_material_stage_expression_class(material_stage_expression_class) -> None
Set Material Stage Expression Class

Args:
    material_stage_expression_class (type(Class)):

<a id="unreal.DMMaterialStageInputExpression.get_material_stage_expression_class"></a>

#### get_material_stage_expression_class

```python
def get_material_stage_expression_class() -> Class
```

x.get_material_stage_expression_class() -> type(Class)
Get Material Stage Expression Class

Returns:
    type(Class):

<a id="unreal.DMMaterialStageInputExpression.get_material_stage_expression"></a>

#### get_material_stage_expression

```python
def get_material_stage_expression() -> DMMaterialStageExpression
```

x.get_material_stage_expression() -> DMMaterialStageExpression
Get Material Stage Expression

Returns:
    DMMaterialStageExpression:

<a id="unreal.DMMaterialStageInputExpression.create_stage"></a>

#### create_stage

```python
@classmethod
def create_stage(cls,
                 material_stage_expression_class: Class,
                 layer: DMMaterialLayerObject = None) -> DMMaterialStage
```

X.create_stage(material_stage_expression_class, layer=None) -> DMMaterialStage
Create Stage

Args:
    material_stage_expression_class (type(Class)): 
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStageInputExpression.change_stage_source_expression"></a>

#### change_stage_source_expression

```python
@classmethod
def change_stage_source_expression(
        cls, stage: DMMaterialStage,
        expression_class: Class) -> DMMaterialStageInputExpression
```

X.change_stage_source_expression(stage, expression_class) -> DMMaterialStageInputExpression
Change Stage Source Expression

Args:
    stage (DMMaterialStage): 
    expression_class (type(Class)): 

Returns:
    DMMaterialStageInputExpression:

<a id="unreal.DMMaterialStageInputExpression.change_stage_input_expression"></a>

#### change_stage_input_expression

```python
@classmethod
def change_stage_input_expression(
        cls, stage: DMMaterialStage, expression_class: Class, input_idx: int,
        input_channel: int, output_idx: int,
        output_channel: int) -> DMMaterialStageInputExpression
```

X.change_stage_input_expression(stage, expression_class, input_idx, input_channel, output_idx, output_channel) -> DMMaterialStageInputExpression
Change the input type of an input on a stage to an expression.

Args:
    stage (DMMaterialStage): 
    expression_class (type(Class)): 
    input_idx (int32): Index of the source input.
    input_channel (int32): The channel of the input that the input connects to.
    output_idx (int32): The output index of the new input.
    output_channel (int32): The channel of the output to connect.

Returns:
    DMMaterialStageInputExpression:

<a id="unreal.DMMaterialStageInputFunction"></a>