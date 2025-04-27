## DMMaterialStageGradient Objects

```python
class DMMaterialStageGradient(DMMaterialStageThroughput)
```

A node which represents UV-based gradient.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStageGradient.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``material_function`` (MaterialFunctionInterface):  [Read-Only]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageGradient.material_function"></a>

#### material_function

```python
@property
def material_function() -> MaterialFunctionInterface
```

(MaterialFunctionInterface):  [Read-Only]

<a id="unreal.DMMaterialStageGradient.create_stage"></a>

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

<a id="unreal.DMMaterialStageGradient.change_stage_source_gradient"></a>

#### change_stage_source_gradient

```python
@classmethod
def change_stage_source_gradient(
        cls, stage: DMMaterialStage,
        gradient_class: Class) -> DMMaterialStageGradient
```

X.change_stage_source_gradient(stage, gradient_class) -> DMMaterialStageGradient
Change Stage Source Gradient

Args:
    stage (DMMaterialStage): 
    gradient_class (type(Class)): 

Returns:
    DMMaterialStageGradient:

<a id="unreal.DMMaterialStageInput"></a>