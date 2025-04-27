## DMMaterialStageInputValue Objects

```python
class DMMaterialStageInputValue(DMMaterialStageInput)
```

DMMaterial Stage Input Value

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSIValue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``value`` (DMMaterialValue):  [Read-Only]

<a id="unreal.DMMaterialStageInputValue.value"></a>

#### value

```python
@property
def value() -> DMMaterialValue
```

(DMMaterialValue):  [Read-Only]

<a id="unreal.DMMaterialStageInputValue.set_value"></a>

#### set_value

```python
def set_value(value: DMMaterialValue) -> None
```

x.set_value(value) -> None
Set Value

Args:
    value (DMMaterialValue):

<a id="unreal.DMMaterialStageInputValue.get_value"></a>

#### get_value

```python
def get_value() -> DMMaterialValue
```

x.get_value() -> DMMaterialValue
Get Value

Returns:
    DMMaterialValue:

<a id="unreal.DMMaterialStageInputValue.create_stage"></a>

#### create_stage

```python
@classmethod
def create_stage(cls,
                 value: DMMaterialValue,
                 layer: DMMaterialLayerObject = None) -> DMMaterialStage
```

X.create_stage(value, layer=None) -> DMMaterialStage
Create Stage

Args:
    value (DMMaterialValue): 
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStageInputValue.change_stage_source_value"></a>

#### change_stage_source_value

```python
@classmethod
def change_stage_source_value(
        cls, stage: DMMaterialStage,
        value: DMMaterialValue) -> DMMaterialStageInputValue
```

X.change_stage_source_value(stage, value) -> DMMaterialStageInputValue
Change Stage Source Value

Args:
    stage (DMMaterialStage): 
    value (DMMaterialValue): 

Returns:
    DMMaterialStageInputValue:

<a id="unreal.DMMaterialStageInputValue.change_stage_source_new_value"></a>

#### change_stage_source_new_value

```python
@classmethod
def change_stage_source_new_value(
        cls, stage: DMMaterialStage,
        value_class: Class) -> DMMaterialStageInputValue
```

X.change_stage_source_new_value(stage, value_class) -> DMMaterialStageInputValue
Change Stage Source New Value

Args:
    stage (DMMaterialStage): 
    value_class (type(Class)): 

Returns:
    DMMaterialStageInputValue:

<a id="unreal.DMMaterialStageInputValue.change_stage_source_new_local_value"></a>

#### change_stage_source_new_local_value

```python
@classmethod
def change_stage_source_new_local_value(
        cls, stage: DMMaterialStage,
        value_class: Class) -> DMMaterialStageInputValue
```

X.change_stage_source_new_local_value(stage, value_class) -> DMMaterialStageInputValue
Change Stage Source New Local Value

Args:
    stage (DMMaterialStage): 
    value_class (type(Class)): 

Returns:
    DMMaterialStageInputValue:

<a id="unreal.DMMaterialStageInputValue.change_stage_input_value"></a>

#### change_stage_input_value

```python
@classmethod
def change_stage_input_value(cls, stage: DMMaterialStage, input_idx: int,
                             input_channel: int, value: DMMaterialValue,
                             output_channel: int) -> DMMaterialStageInputValue
```

X.change_stage_input_value(stage, input_idx, input_channel, value, output_channel) -> DMMaterialStageInputValue
Change Stage Input Value

Args:
    stage (DMMaterialStage): 
    input_idx (int32): 
    input_channel (int32): 
    value (DMMaterialValue): 
    output_channel (int32): 

Returns:
    DMMaterialStageInputValue:

<a id="unreal.DMMaterialStageInputValue.change_stage_input_new_value"></a>

#### change_stage_input_new_value

```python
@classmethod
def change_stage_input_new_value(
        cls, stage: DMMaterialStage, input_idx: int, input_channel: int,
        value_class: Class, output_channel: int) -> DMMaterialStageInputValue
```

X.change_stage_input_new_value(stage, input_idx, input_channel, value_class, output_channel) -> DMMaterialStageInputValue
Change Stage Input New Value

Args:
    stage (DMMaterialStage): 
    input_idx (int32): 
    input_channel (int32): 
    value_class (type(Class)): 
    output_channel (int32): 

Returns:
    DMMaterialStageInputValue:

<a id="unreal.DMMaterialStageInputValue.change_stage_input_new_local_value"></a>

#### change_stage_input_new_local_value

```python
@classmethod
def change_stage_input_new_local_value(
        cls, stage: DMMaterialStage, input_idx: int, input_channel: int,
        value_class: Class, output_channel: int) -> DMMaterialStageInputValue
```

X.change_stage_input_new_local_value(stage, input_idx, input_channel, value_class, output_channel) -> DMMaterialStageInputValue
Change Stage Input New Local Value

Args:
    stage (DMMaterialStage): 
    input_idx (int32): 
    input_channel (int32): 
    value_class (type(Class)): 
    output_channel (int32): 

Returns:
    DMMaterialStageInputValue:

<a id="unreal.DynamicMaterialEditorSettings"></a>