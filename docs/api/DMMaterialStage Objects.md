## DMMaterialStage Objects

```python
class DMMaterialStage(DMMaterialComponent)
```

A component which wraps a source and its inputs.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialStage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_change_source`` (bool):  [Read-Only]
- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``enabled`` (bool):  [Read-Only]
- ``input_connection_map`` (Array[DMMaterialStageConnection]):  [Read-Only] How our inputs connect to the inputs of this stage's source
- ``inputs`` (Array[DMMaterialStageInput]):  [Read-Only]
- ``source`` (DMMaterialStageSource):  [Read-Only]

<a id="unreal.DMMaterialStage.source"></a>

#### source

```python
@property
def source() -> DMMaterialStageSource
```

(DMMaterialStageSource):  [Read-Only]

<a id="unreal.DMMaterialStage.inputs"></a>

#### inputs

```python
@property
def inputs() -> Array[DMMaterialStageInput]
```

(Array[DMMaterialStageInput]):  [Read-Only]

<a id="unreal.DMMaterialStage.input_connection_map"></a>

#### input_connection_map

```python
@property
def input_connection_map() -> Array[DMMaterialStageConnection]
```

(Array[DMMaterialStageConnection]):  [Read-Only] How our inputs connect to the inputs of this stage's source

<a id="unreal.DMMaterialStage.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialStage.can_change_source"></a>

#### can_change_source

```python
@property
def can_change_source() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialStage.verify_input_map"></a>

#### verify_input_map

```python
def verify_input_map(input_idx: int) -> bool
```

x.verify_input_map(input_idx) -> bool
Returns true if any changes were made

Args:
    input_idx (int32): 

Returns:
    bool:

<a id="unreal.DMMaterialStage.verify_all_input_maps"></a>

#### verify_all_input_maps

```python
def verify_all_input_maps() -> bool
```

x.verify_all_input_maps() -> bool
Returns true if any changes were made

Returns:
    bool:

<a id="unreal.DMMaterialStage.set_source"></a>

#### set_source

```python
def set_source(source: DMMaterialStageSource) -> None
```

x.set_source(source) -> None
Set Source

Args:
    source (DMMaterialStageSource):

<a id="unreal.DMMaterialStage.set_enabled"></a>

#### set_enabled

```python
def set_enabled(enabled: bool) -> bool
```

x.set_enabled(enabled) -> bool
Set Enabled

Args:
    enabled (bool): 

Returns:
    bool:

<a id="unreal.DMMaterialStage.set_can_change_source"></a>

#### set_can_change_source

```python
def set_can_change_source(can_change_source: bool) -> None
```

x.set_can_change_source(can_change_source) -> None
Set Can Change Source

Args:
    can_change_source (bool):

<a id="unreal.DMMaterialStage.reset_input_connection_map"></a>

#### reset_input_connection_map

```python
def reset_input_connection_map() -> None
```

x.reset_input_connection_map() -> None
Verifies the entire input connection map.

<a id="unreal.DMMaterialStage.remove_unused_inputs"></a>

#### remove_unused_inputs

```python
def remove_unused_inputs() -> None
```

x.remove_unused_inputs() -> None
Remove Unused Inputs

<a id="unreal.DMMaterialStage.remove_input"></a>

#### remove_input

```python
def remove_input(input: DMMaterialStageInput) -> None
```

x.remove_input(input) -> None
Remove Input

Args:
    input (DMMaterialStageInput):

<a id="unreal.DMMaterialStage.remove_all_inputs"></a>

#### remove_all_inputs

```python
def remove_all_inputs() -> None
```

x.remove_all_inputs() -> None
Remove All Inputs

<a id="unreal.DMMaterialStage.is_input_mapped"></a>

#### is_input_mapped

```python
def is_input_mapped(input_index: int) -> bool
```

x.is_input_mapped(input_index) -> bool
Returns true if the given source's input is mapped to an input (or the previous stage).

Args:
    input_index (int32): 

Returns:
    bool:

<a id="unreal.DMMaterialStage.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
Is Enabled

Returns:
    bool:

<a id="unreal.DMMaterialStage.is_compatible_with_previous_stage"></a>

#### is_compatible_with_previous_stage

```python
def is_compatible_with_previous_stage(previous_stage: DMMaterialStage) -> bool
```

x.is_compatible_with_previous_stage(previous_stage) -> bool
Returns true if the output of the previous stage can connect to this stage.
It is now up to the user to sort this particular problem out because it would do more harm than good
to force correctness in "transition states" while the user is changing settings.

Args:
    previous_stage (DMMaterialStage): 

Returns:
    bool:

<a id="unreal.DMMaterialStage.is_compatible_with_next_stage"></a>

#### is_compatible_with_next_stage

```python
def is_compatible_with_next_stage(next_stage: DMMaterialStage) -> bool
```

x.is_compatible_with_next_stage(next_stage) -> bool

see: IsCompatibleWithPreviousStage

Args:
    next_stage (DMMaterialStage): 

Returns:
    bool:

<a id="unreal.DMMaterialStage.get_source_type"></a>

#### get_source_type

```python
def get_source_type(channel: DMMaterialStageConnectorChannel) -> DMValueType
```

x.get_source_type(channel) -> DMValueType
Get Source Type

Args:
    channel (DMMaterialStageConnectorChannel): 

Returns:
    DMValueType:

<a id="unreal.DMMaterialStage.get_source"></a>

#### get_source

```python
def get_source() -> DMMaterialStageSource
```

x.get_source() -> DMMaterialStageSource
Get Source

Returns:
    DMMaterialStageSource:

<a id="unreal.DMMaterialStage.get_previous_stage"></a>

#### get_previous_stage

```python
def get_previous_stage() -> DMMaterialStage
```

x.get_previous_stage() -> DMMaterialStage
Get Previous Stage

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStage.get_next_stage"></a>

#### get_next_stage

```python
def get_next_stage() -> DMMaterialStage
```

x.get_next_stage() -> DMMaterialStage
Get Next Stage

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStage.get_layer"></a>

#### get_layer

```python
def get_layer() -> DMMaterialLayerObject
```

x.get_layer() -> DMMaterialLayerObject
Get Layer

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialStage.get_inputs"></a>

#### get_inputs

```python
def get_inputs() -> Array[DMMaterialStageInput]
```

x.get_inputs() -> Array[DMMaterialStageInput]
Get Inputs

Returns:
    Array[DMMaterialStageInput]:

<a id="unreal.DMMaterialStage.get_input_connection_map"></a>

#### get_input_connection_map

```python
def get_input_connection_map() -> Array[DMMaterialStageConnection]
```

x.get_input_connection_map() -> Array[DMMaterialStageConnection]
Determines what connects to what on this stage's Source.

Returns:
    Array[DMMaterialStageConnection]:

<a id="unreal.DMMaterialStage.generate_preview_material"></a>

#### generate_preview_material

```python
def generate_preview_material(preview_material: Material) -> None
```

x.generate_preview_material(preview_material) -> None
Generate Preview Material

Args:
    preview_material (Material):

<a id="unreal.DMMaterialStage.find_index"></a>

#### find_index

```python
def find_index() -> int
```

x.find_index() -> int32
Returns the index of this stage in the layer.

Returns:
    int32:

<a id="unreal.DMMaterialStage.create_material_stage"></a>

#### create_material_stage

```python
@classmethod
def create_material_stage(cls,
                          layer: DMMaterialLayerObject = None
                          ) -> DMMaterialStage
```

X.create_material_stage(layer=None) -> DMMaterialStage
Create Material Stage

Args:
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStage.change_source"></a>

#### change_source

```python
def change_source(source_class: Class) -> DMMaterialStageSource
```

x.change_source(source_class) -> DMMaterialStageSource
Change Source

Args:
    source_class (type(Class)): 

Returns:
    DMMaterialStageSource:

<a id="unreal.DMMaterialStage.change_input_previous_stage"></a>

#### change_input_previous_stage

```python
def change_input_previous_stage(
        input_idx: int, input_channel: int,
        previous_stage_property: DMMaterialPropertyType, output_idx: int,
        output_channel: int) -> DMMaterialStageSource
```

x.change_input_previous_stage(input_idx, input_channel, previous_stage_property, output_idx, output_channel) -> DMMaterialStageSource
Changes the input of the given input index to the output of the previous stage with the given material property.

Args:
    input_idx (int32): 
    input_channel (int32): 
    previous_stage_property (DMMaterialPropertyType): 
    output_idx (int32): 
    output_channel (int32): 

Returns:
    DMMaterialStageSource:

<a id="unreal.DMMaterialStage.change_input"></a>

#### change_input

```python
def change_input(input_class: Class, input_idx: int, input_channel: int,
                 output_idx: int, output_channel: int) -> DMMaterialStageInput
```

x.change_input(input_class, input_idx, input_channel, output_idx, output_channel) -> DMMaterialStageInput
Change Input

Args:
    input_class (type(Class)): 
    input_idx (int32): 
    input_channel (int32): 
    output_idx (int32): 
    output_channel (int32): 

Returns:
    DMMaterialStageInput:

<a id="unreal.DMMaterialStage.can_change_source"></a>

#### can_change_source

```python
def can_change_source() -> bool
```

x.can_change_source() -> bool
Can Change Source

Returns:
    bool:

<a id="unreal.DMMaterialStage.add_input"></a>

#### add_input

```python
def add_input(new_input: DMMaterialStageInput) -> None
```

x.add_input(new_input) -> None
Add Input

Args:
    new_input (DMMaterialStageInput):

<a id="unreal.DMMaterialStageSource"></a>