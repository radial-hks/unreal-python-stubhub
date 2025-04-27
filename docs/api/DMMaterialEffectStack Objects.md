## DMMaterialEffectStack Objects

```python
class DMMaterialEffectStack(DMMaterialComponent)
```

Container for effects. Effects can be applied to either layers (on a per stage basis) or to slots.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialEffectStack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``effects`` (Array[DMMaterialEffect]):  [Read-Only]
- ``enabled`` (bool):  [Read-Only]

<a id="unreal.DMMaterialEffectStack.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialEffectStack.effects"></a>

#### effects

```python
@property
def effects() -> Array[DMMaterialEffect]
```

(Array[DMMaterialEffect]):  [Read-Only]

<a id="unreal.DMMaterialEffectStack.set_enabled"></a>

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

<a id="unreal.DMMaterialEffectStack.set_effect"></a>

#### set_effect

```python
def set_effect(index: int, effect: DMMaterialEffect) -> DMMaterialEffect
```

x.set_effect(index, effect) -> DMMaterialEffect
Set Effect

Args:
    index (int32): 
    effect (DMMaterialEffect): 

Returns:
    DMMaterialEffect:

<a id="unreal.DMMaterialEffectStack.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
Is Enabled

Returns:
    bool:

<a id="unreal.DMMaterialEffectStack.has_effect"></a>

#### has_effect

```python
def has_effect(effect: DMMaterialEffect) -> bool
```

x.has_effect(effect) -> bool
Has Effect

Args:
    effect (DMMaterialEffect): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectStack.get_slot"></a>

#### get_slot

```python
def get_slot() -> DMMaterialSlot
```

x.get_slot() -> DMMaterialSlot
Get Slot

Returns:
    DMMaterialSlot:

<a id="unreal.DMMaterialEffectStack.get_layer"></a>

#### get_layer

```python
def get_layer() -> DMMaterialLayerObject
```

x.get_layer() -> DMMaterialLayerObject
Get Layer

Returns:
    DMMaterialLayerObject:

<a id="unreal.DMMaterialEffectStack.get_effect"></a>

#### get_effect

```python
def get_effect(index: int) -> DMMaterialEffect
```

x.get_effect(index) -> DMMaterialEffect
Get Effect

Args:
    index (int32): 

Returns:
    DMMaterialEffect:

<a id="unreal.DMMaterialEffectStack.create_preset"></a>

#### create_preset

```python
def create_preset() -> DMMaterialEffectStackJson
```

x.create_preset() -> DMMaterialEffectStackJson
Creates a preset based on the current stage.

Returns:
    DMMaterialEffectStackJson:

<a id="unreal.DMMaterialEffectStack.create_effect_stack_for_slot"></a>

#### create_effect_stack_for_slot

```python
@classmethod
def create_effect_stack_for_slot(
        cls, slot: DMMaterialSlot) -> DMMaterialEffectStack
```

X.create_effect_stack_for_slot(slot) -> DMMaterialEffectStack
Create Effect Stack for Slot

Args:
    slot (DMMaterialSlot): 

Returns:
    DMMaterialEffectStack:

<a id="unreal.DMMaterialEffectStack.create_effect_stack_for_layer"></a>

#### create_effect_stack_for_layer

```python
@classmethod
def create_effect_stack_for_layer(
        cls, layer: DMMaterialLayerObject) -> DMMaterialEffectStack
```

X.create_effect_stack_for_layer(layer) -> DMMaterialEffectStack
Create Effect Stack for Layer

Args:
    layer (DMMaterialLayerObject): 

Returns:
    DMMaterialEffectStack:

<a id="unreal.DMMaterialEffectStack.bp_remove_effect_by_value"></a>

#### bp_remove_effect_by_value

```python
def bp_remove_effect_by_value(effect: DMMaterialEffect) -> bool
```

x.bp_remove_effect_by_value(effect) -> bool
BP Remove Effect by Value

Args:
    effect (DMMaterialEffect): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectStack.bp_remove_effect_by_index"></a>

#### bp_remove_effect_by_index

```python
def bp_remove_effect_by_index(index: int) -> DMMaterialEffect
```

x.bp_remove_effect_by_index(index) -> DMMaterialEffect
BP Remove Effect by Index

Args:
    index (int32): 

Returns:
    DMMaterialEffect:

<a id="unreal.DMMaterialEffectStack.bp_move_effect_by_value"></a>

#### bp_move_effect_by_value

```python
def bp_move_effect_by_value(effect: DMMaterialEffect, new_index: int) -> bool
```

x.bp_move_effect_by_value(effect, new_index) -> bool
BP Move Effect by Value

Args:
    effect (DMMaterialEffect): 
    new_index (int32): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectStack.bp_move_effect_by_index"></a>

#### bp_move_effect_by_index

```python
def bp_move_effect_by_index(index: int, new_index: int) -> bool
```

x.bp_move_effect_by_index(index, new_index) -> bool
BP Move Effect by Index

Args:
    index (int32): 
    new_index (int32): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectStack.bp_get_effects"></a>

#### bp_get_effects

```python
def bp_get_effects() -> Array[DMMaterialEffect]
```

x.bp_get_effects() -> Array[DMMaterialEffect]
BP Get Effects

Returns:
    Array[DMMaterialEffect]:

<a id="unreal.DMMaterialEffectStack.apply_preset"></a>

#### apply_preset

```python
def apply_preset(preset: DMMaterialEffectStackJson) -> None
```

x.apply_preset(preset) -> None
Apply the given preset to this stack. Does not remove old effects.

Args:
    preset (DMMaterialEffectStackJson):

<a id="unreal.DMMaterialEffectStack.add_effect"></a>

#### add_effect

```python
def add_effect(effect: DMMaterialEffect) -> bool
```

x.add_effect(effect) -> bool
Add Effect

Args:
    effect (DMMaterialEffect): 

Returns:
    bool:

<a id="unreal.DMMaterialEffectStackPresetSubsystem"></a>