## DMMaterialStageFunction Objects

```python
class DMMaterialStageFunction(DMMaterialStageThroughput)
```

Represents a material function which can be added directly to a stage.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStageFunction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_nested_inputs`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``input_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``input_required`` (bool):  [Read-Only]
- ``material_function`` (MaterialFunctionInterface):  [Read-Write]
- ``name`` (Text):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]

<a id="unreal.DMMaterialStageFunction.material_function"></a>

#### material_function

```python
@property
def material_function() -> MaterialFunctionInterface
```

(MaterialFunctionInterface):  [Read-Write]

<a id="unreal.DMMaterialStageFunction.material_function"></a>

#### material_function

```python
@material_function.setter
def material_function(value: MaterialFunctionInterface) -> None
```

<a id="unreal.DMMaterialStageFunction.set_material_function"></a>

#### set_material_function

```python
def set_material_function(
        material_function: MaterialFunctionInterface) -> None
```

x.set_material_function(material_function) -> None
Set Material Function

Args:
    material_function (MaterialFunctionInterface):

<a id="unreal.DMMaterialStageFunction.get_material_function"></a>

#### get_material_function

```python
def get_material_function() -> MaterialFunctionInterface
```

x.get_material_function() -> MaterialFunctionInterface
Get Material Function

Returns:
    MaterialFunctionInterface:

<a id="unreal.DMMaterialStageFunction.get_input_values"></a>

#### get_input_values

```python
def get_input_values() -> Array[DMMaterialValue]
```

x.get_input_values() -> Array[DMMaterialValue]
Get Input Values

Returns:
    Array[DMMaterialValue]:

<a id="unreal.DMMaterialStageFunction.get_input_value"></a>

#### get_input_value

```python
def get_input_value(index: int) -> DMMaterialValue
```

x.get_input_value(index) -> DMMaterialValue
Get Input Value

Args:
    index (int32): 

Returns:
    DMMaterialValue:

<a id="unreal.DMMaterialStageFunction.change_stage_source_function"></a>

#### change_stage_source_function

```python
@classmethod
def change_stage_source_function(
        cls, stage: DMMaterialStage,
        material_function: MaterialFunctionInterface
) -> DMMaterialStageFunction
```

X.change_stage_source_function(stage, material_function) -> DMMaterialStageFunction
Change Stage Source Function

Args:
    stage (DMMaterialStage): 
    material_function (MaterialFunctionInterface): 

Returns:
    DMMaterialStageFunction:

<a id="unreal.DMMaterialStageGradient"></a>