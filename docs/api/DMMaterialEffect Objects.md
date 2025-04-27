## DMMaterialEffect Objects

```python
class DMMaterialEffect(DMMaterialComponent)
```

DMMaterial Effect

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``effect_target`` (DMMaterialEffectTarget):  [Read-Only]
- ``enabled`` (bool):  [Read-Only]

<a id="unreal.DMMaterialEffect.effect_target"></a>

#### effect_target

```python
@property
def effect_target() -> DMMaterialEffectTarget
```

(DMMaterialEffectTarget):  [Read-Only]

<a id="unreal.DMMaterialEffect.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialEffect.stage_type_to_effect_type"></a>

#### stage_type_to_effect_type

```python
@classmethod
def stage_type_to_effect_type(
        cls, stage_type: DMMaterialLayerStage) -> DMMaterialEffectTarget
```

X.stage_type_to_effect_type(stage_type) -> DMMaterialEffectTarget
Stage Type to Effect Type

Args:
    stage_type (DMMaterialLayerStage): 

Returns:
    DMMaterialEffectTarget:

<a id="unreal.DMMaterialEffect.set_enabled"></a>

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

<a id="unreal.DMMaterialEffect.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
Is Enabled

Returns:
    bool:

<a id="unreal.DMMaterialEffect.get_effect_target"></a>

#### get_effect_target

```python
def get_effect_target() -> DMMaterialEffectTarget
```

x.get_effect_target() -> DMMaterialEffectTarget
Returns the type of nodes which this effect targets.

Returns:
    DMMaterialEffectTarget:

<a id="unreal.DMMaterialEffect.get_effect_stack"></a>

#### get_effect_stack

```python
def get_effect_stack() -> DMMaterialEffectStack
```

x.get_effect_stack() -> DMMaterialEffectStack
Get Effect Stack

Returns:
    DMMaterialEffectStack:

<a id="unreal.DMMaterialEffect.get_effect_name"></a>

#### get_effect_name

```python
def get_effect_name() -> Text
```

x.get_effect_name() -> Text
Get Effect Name

Returns:
    Text:

<a id="unreal.DMMaterialEffect.get_effect_description"></a>

#### get_effect_description

```python
def get_effect_description() -> Text
```

x.get_effect_description() -> Text
Get Effect Description

Returns:
    Text:

<a id="unreal.DMMaterialEffect.find_index"></a>

#### find_index

```python
def find_index() -> int
```

x.find_index() -> int32
Retrieves the index of this effect in the effect stack.

Returns:
    int32:

<a id="unreal.DMMaterialEffect.create_effect"></a>

#### create_effect

```python
@classmethod
def create_effect(cls, effect_stack: DMMaterialEffectStack,
                  effect_class: Class) -> DMMaterialEffect
```

X.create_effect(effect_stack, effect_class) -> DMMaterialEffect
Create Effect

Args:
    effect_stack (DMMaterialEffectStack): 
    effect_class (type(Class)): 

Returns:
    DMMaterialEffect:

<a id="unreal.DMMaterialEffectFunction"></a>