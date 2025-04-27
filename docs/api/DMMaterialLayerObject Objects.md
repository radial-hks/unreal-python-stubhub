## DMMaterialLayerObject Objects

```python
class DMMaterialLayerObject(DMMaterialComponent)
```

A collection of stages.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``effect_stack`` (DMMaterialEffectStack):  [Read-Only]
- ``enabled`` (bool):  [Read-Only]
- ``layer_name`` (Text):  [Read-Only]
- ``linked_u_vs`` (bool):  [Read-Only]
- ``material_property`` (DMMaterialPropertyType):  [Read-Only]
- ``stages`` (Array[DMMaterialStage]):  [Read-Only]

<a id="unreal.DMMaterialLayerObject.material_property"></a>

#### material_property

```python
@property
def material_property() -> DMMaterialPropertyType
```

(DMMaterialPropertyType):  [Read-Only]

<a id="unreal.DMMaterialLayerObject.layer_name"></a>

#### layer_name

```python
@property
def layer_name() -> Text
```

(Text):  [Read-Only]

<a id="unreal.DMMaterialLayerObject.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialLayerObject.stages"></a>

#### stages

```python
@property
def stages() -> Array[DMMaterialStage]
```

(Array[DMMaterialStage]):  [Read-Only]

<a id="unreal.DMMaterialLayerObject.effect_stack"></a>

#### effect_stack

```python
@property
def effect_stack() -> DMMaterialEffectStack
```

(DMMaterialEffectStack):  [Read-Only]

<a id="unreal.DMMaterialLayerObject.linked_u_vs"></a>

#### linked_u_vs

```python
@property
def linked_u_vs() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialLayerObject.toggle_texture_uv_link_enabled"></a>

#### toggle_texture_uv_link_enabled

```python
def toggle_texture_uv_link_enabled() -> bool
```

x.toggle_texture_uv_link_enabled() -> bool
Texture UV Link means that all stages use the same Texture UV from the base stage, if available.

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.set_texture_uv_link_enabled"></a>

#### set_texture_uv_link_enabled

```python
def set_texture_uv_link_enabled(value: bool) -> bool
```

x.set_texture_uv_link_enabled(value) -> bool
Texture UV Link means that all stages use the same Texture UV from the base stage, if available.

Args:
    value (bool): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.set_stage"></a>

#### set_stage

```python
def set_stage(stage_type: DMMaterialLayerStage,
              stage: DMMaterialStage) -> bool
```

x.set_stage(stage_type, stage) -> bool
Replace the specified stage.

Args:
    stage_type (DMMaterialLayerStage): 
    stage (DMMaterialStage): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.set_material_property"></a>

#### set_material_property

```python
def set_material_property(material_property: DMMaterialPropertyType) -> bool
```

x.set_material_property(material_property) -> bool
Set Material Property

Args:
    material_property (DMMaterialPropertyType): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.set_layer_name"></a>

#### set_layer_name

```python
def set_layer_name(name: Text) -> None
```

x.set_layer_name(name) -> None
Set Layer Name

Args:
    name (Text):

<a id="unreal.DMMaterialLayerObject.set_enabled"></a>

#### set_enabled

```python
def set_enabled(is_enabled: bool) -> bool
```

x.set_enabled(is_enabled) -> bool
Set Enabled

Args:
    is_enabled (bool): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.is_texture_uv_link_enabled"></a>

#### is_texture_uv_link_enabled

```python
def is_texture_uv_link_enabled() -> bool
```

x.is_texture_uv_link_enabled() -> bool
Texture UV Link means that all stages use the same Texture UV from the base stage, if available.

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.is_stage_enabled"></a>

#### is_stage_enabled

```python
def is_stage_enabled(
        stage_scope: DMMaterialLayerStage = DMMaterialLayerStage.ALL) -> bool
```

x.is_stage_enabled(stage_scope=DMMaterialLayerStage.ALL) -> bool
Is Stage Enabled

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
Is Enabled

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.has_valid_stage_of_type"></a>

#### has_valid_stage_of_type

```python
def has_valid_stage_of_type(
        stage_scope: DMMaterialLayerStage = DMMaterialLayerStage.ALL) -> bool
```

x.has_valid_stage_of_type(stage_scope=DMMaterialLayerStage.ALL) -> bool
Has Valid Stage Of Type

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.has_valid_stage"></a>

#### has_valid_stage

```python
def has_valid_stage(stage: DMMaterialStage) -> bool
```

x.has_valid_stage(stage) -> bool
Has Valid Stage

Args:
    stage (DMMaterialStage): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.get_stage_type"></a>

#### get_stage_type

```python
def get_stage_type(stage: DMMaterialStage) -> DMMaterialLayerStage
```

x.get_stage_type(stage) -> DMMaterialLayerStage
Get Stage Type

Args:
    stage (DMMaterialStage): 

Returns:
    DMMaterialLayerStage:

<a id="unreal.DMMaterialLayerObject.get_stages"></a>

#### get_stages

```python
def get_stages(stage_type: DMMaterialLayerStage = DMMaterialLayerStage.ALL,
               check_enabled: bool = False) -> Array[DMMaterialStage]
```

x.get_stages(stage_type=DMMaterialLayerStage.ALL, check_enabled=False) -> Array[DMMaterialStage]
Get Stages

Args:
    stage_type (DMMaterialLayerStage): 
    check_enabled (bool): 

Returns:
    Array[DMMaterialStage]:

<a id="unreal.DMMaterialLayerObject.get_stage"></a>

#### get_stage

```python
def get_stage(stage_type: DMMaterialLayerStage = DMMaterialLayerStage.ALL,
              check_enabled: bool = False) -> DMMaterialStage
```

x.get_stage(stage_type=DMMaterialLayerStage.ALL, check_enabled=False) -> DMMaterialStage
Get Stage

Args:
    stage_type (DMMaterialLayerStage): 
    check_enabled (bool): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialLayerObject.get_slot"></a>

#### get_slot

```python
def get_slot() -> DMMaterialSlot
```

x.get_slot() -> DMMaterialSlot
Get Slot

Returns:
    DMMaterialSlot:

<a id="unreal.DMMaterialLayerObject.get_previous_layer"></a>

#### get_previous_layer

```python
def get_previous_layer(
        using_property: DMMaterialPropertyType,
        search_for: DMMaterialLayerStage) -> DMMaterialLayerObject
```

x.get_previous_layer(using_property, search_for) -> DMMaterialLayerObject
Get Previous Layer

Args:
    using_property (DMMaterialPropertyType): 
    search_for (DMMaterialLayerStage): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialLayerObject.get_next_layer"></a>

#### get_next_layer

```python
def get_next_layer(using_property: DMMaterialPropertyType,
                   search_for: DMMaterialLayerStage) -> DMMaterialLayerObject
```

x.get_next_layer(using_property, search_for) -> DMMaterialLayerObject
Get Next Layer

Args:
    using_property (DMMaterialPropertyType): 
    search_for (DMMaterialLayerStage): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialLayerObject.get_material_property"></a>

#### get_material_property

```python
def get_material_property() -> DMMaterialPropertyType
```

x.get_material_property() -> DMMaterialPropertyType
Get Material Property

Returns:
    DMMaterialPropertyType:

<a id="unreal.DMMaterialLayerObject.get_layer_name"></a>

#### get_layer_name

```python
def get_layer_name() -> Text
```

x.get_layer_name() -> Text
Get Layer Name

Returns:
    Text:

<a id="unreal.DMMaterialLayerObject.get_last_valid_stage"></a>

#### get_last_valid_stage

```python
def get_last_valid_stage(stage_scope: DMMaterialLayerStage) -> DMMaterialStage
```

x.get_last_valid_stage(stage_scope) -> DMMaterialStage
Get Last Valid Stage

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialLayerObject.get_last_enabled_stage"></a>

#### get_last_enabled_stage

```python
def get_last_enabled_stage(
        stage_scope: DMMaterialLayerStage) -> DMMaterialStage
```

x.get_last_enabled_stage(stage_scope) -> DMMaterialStage
Checks for the last enabled and valid stage.

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialLayerObject.get_first_valid_stage"></a>

#### get_first_valid_stage

```python
def get_first_valid_stage(
        stage_scope: DMMaterialLayerStage) -> DMMaterialStage
```

x.get_first_valid_stage(stage_scope) -> DMMaterialStage
Get First Valid Stage

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialLayerObject.get_first_enabled_stage"></a>

#### get_first_enabled_stage

```python
def get_first_enabled_stage(
        stage_scope: DMMaterialLayerStage) -> DMMaterialStage
```

x.get_first_enabled_stage(stage_scope) -> DMMaterialStage
Checks for the first enabled and valid stage.

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    DMMaterialStage:

<a id="unreal.DMMaterialLayerObject.get_effect_stack"></a>

#### get_effect_stack

```python
def get_effect_stack() -> DMMaterialEffectStack
```

x.get_effect_stack() -> DMMaterialEffectStack
Get Effect Stack

Returns:
    DMMaterialEffectStack:

<a id="unreal.DMMaterialLayerObject.find_index"></a>

#### find_index

```python
def find_index() -> int
```

x.find_index() -> int32
Find the index of this layer in the slot.

Returns:
    int32:

<a id="unreal.DMMaterialLayerObject.create_layer"></a>

#### create_layer

```python
@classmethod
def create_layer(cls, slot: DMMaterialSlot,
                 material_property: DMMaterialPropertyType,
                 stages: Array[DMMaterialStage]) -> DMMaterialLayerObject
```

X.create_layer(slot, material_property, stages) -> DMMaterialLayerObject
Create Layer

Args:
    slot (DMMaterialSlot): 
    material_property (DMMaterialPropertyType): 
    stages (Array[DMMaterialStage]): 

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialLayerObject.can_move_layer_below"></a>

#### can_move_layer_below

```python
def can_move_layer_below(layer: DMMaterialLayerObject) -> bool
```

x.can_move_layer_below(layer) -> bool
Can Move Layer Below

Args:
    layer (DMMaterialLayerObject): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.can_move_layer_above"></a>

#### can_move_layer_above

```python
def can_move_layer_above(layer: DMMaterialLayerObject) -> bool
```

x.can_move_layer_above(layer) -> bool
Can Move Layer Above

Args:
    layer (DMMaterialLayerObject): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.are_all_stages_valid"></a>

#### are_all_stages_valid

```python
def are_all_stages_valid(stage_scope: DMMaterialLayerStage) -> bool
```

x.are_all_stages_valid(stage_scope) -> bool
Are All Stages Valid

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    bool:

<a id="unreal.DMMaterialLayerObject.are_all_stages_enabled"></a>

#### are_all_stages_enabled

```python
def are_all_stages_enabled(stage_scope: DMMaterialLayerStage) -> bool
```

x.are_all_stages_enabled(stage_scope) -> bool
Checks if both stages are enabled and valid

Args:
    stage_scope (DMMaterialLayerStage): 

Returns:
    bool:

<a id="unreal.DMMaterialProperty"></a>