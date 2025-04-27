## DMMaterialStageInputSlot Objects

```python
class DMMaterialStageInputSlot(DMMaterialStageInput)
```

DMMaterial Stage Input Slot

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMSISlot.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``material_property`` (DMMaterialPropertyType):  [Read-Only]
- ``output_connectors`` (Array[DMMaterialStageConnector]):  [Read-Only]
- ``slot`` (DMMaterialSlot):  [Read-Only]

<a id="unreal.DMMaterialStageInputSlot.slot"></a>

#### slot

```python
@property
def slot() -> DMMaterialSlot
```

(DMMaterialSlot):  [Read-Only]

<a id="unreal.DMMaterialStageInputSlot.material_property"></a>

#### material_property

```python
@property
def material_property() -> DMMaterialPropertyType
```

(DMMaterialPropertyType):  [Read-Only]

<a id="unreal.DMMaterialStageInputSlot.set_slot"></a>

#### set_slot

```python
def set_slot(slot: DMMaterialSlot) -> None
```

x.set_slot(slot) -> None
Set Slot

Args:
    slot (DMMaterialSlot):

<a id="unreal.DMMaterialStageInputSlot.set_material_property"></a>

#### set_material_property

```python
def set_material_property(material_property: DMMaterialPropertyType) -> None
```

x.set_material_property(material_property) -> None
Set Material Property

Args:
    material_property (DMMaterialPropertyType):

<a id="unreal.DMMaterialStageInputSlot.get_slot"></a>

#### get_slot

```python
def get_slot() -> DMMaterialSlot
```

x.get_slot() -> DMMaterialSlot
Get Slot

Returns:
    DMMaterialSlot:

<a id="unreal.DMMaterialStageInputSlot.get_material_property"></a>

#### get_material_property

```python
def get_material_property() -> DMMaterialPropertyType
```

x.get_material_property() -> DMMaterialPropertyType
Get Material Property

Returns:
    DMMaterialPropertyType:

<a id="unreal.DMMaterialStageInputSlot.create_stage"></a>

#### create_stage

```python
@classmethod
def create_stage(cls,
                 source_slot: DMMaterialSlot,
                 material_property: DMMaterialPropertyType,
                 layer: DMMaterialLayerObject = None) -> DMMaterialStage
```

X.create_stage(source_slot, material_property, layer=None) -> DMMaterialStage
Create Stage

Args:
    source_slot (DMMaterialSlot): 
    material_property (DMMaterialPropertyType): 
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialStageInputSlot.change_stage_source_slot"></a>

#### change_stage_source_slot

```python
@classmethod
def change_stage_source_slot(
        cls, stage: DMMaterialStage, slot: DMMaterialSlot,
        property_: DMMaterialPropertyType) -> DMMaterialStageInputSlot
```

X.change_stage_source_slot(stage, slot, property_) -> DMMaterialStageInputSlot
Change Stage Source Slot

Args:
    stage (DMMaterialStage): 
    slot (DMMaterialSlot): 
    property_ (DMMaterialPropertyType): 

Returns:
    DMMaterialStageInputSlot:

<a id="unreal.DMMaterialStageInputSlot.change_stage_input_slot"></a>

#### change_stage_input_slot

```python
@classmethod
def change_stage_input_slot(cls, stage: DMMaterialStage, input_idx: int,
                            input_channel: int, slot: DMMaterialSlot,
                            property_: DMMaterialPropertyType, output_idx: int,
                            output_channel: int) -> DMMaterialStageInputSlot
```

X.change_stage_input_slot(stage, input_idx, input_channel, slot, property_, output_idx, output_channel) -> DMMaterialStageInputSlot
Change the input type of an input on a stage to the output of another slot.

Args:
    stage (DMMaterialStage): 
    input_idx (int32): Index of the source input.
    input_channel (int32): The channel of the input that the input connects to.
    slot (DMMaterialSlot): 
    property_ (DMMaterialPropertyType): The property of the slot to use.
    output_idx (int32): The output index of the new input.
    output_channel (int32): The channel of the output to connect.

Returns:
    DMMaterialStageInputSlot:

<a id="unreal.DMMaterialStageInputTextureUV"></a>