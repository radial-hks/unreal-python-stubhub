## EnhancedActionKeyMapping Objects

```python
class EnhancedActionKeyMapping(StructBase)
```

Defines a mapping between a key activation and the resulting enhanced action
An key could be a button press, joystick axis movement, etc.
An enhanced action could be MoveForward, Jump, Fire, etc.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedActionKeyMapping.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action`` (InputAction):  [Read-Write] Action to be affected by the key
- ``is_player_mappable`` (bool):  [Read-Write]
  deprecated: bIsPlayerMappable has been deprecated, please use the SettingBehavior instead
- ``key`` (Key):  [Read-Write] Key that affect the action.
- ``modifiers`` (Array[InputModifier]):  [Read-Write] Modifiers applied to the raw key value.
  These are applied sequentially in array order.

  Note: Modifiers defined in individual key mappings will be applied before those defined in the Input Action asset.
  Modifiers will not override any that are defined on the Input Action asset, they will be combined together during evaluation.
- ``player_mappable_key_settings`` (PlayerMappableKeySettings):  [Read-Write] Used to expose this mapping or to opt-out of settings completely.
- ``player_mappable_options`` (PlayerMappableKeyOptions):  [Read-Write]
  deprecated: PlayerMappableOptions has been deprecated, please use the PlayerMappableKeySettings instead
- ``setting_behavior`` (PlayerMappableKeySettingBehaviors):  [Read-Write] Defines which Player Mappable Key Setting to use for a Action Key Mapping.
- ``triggers`` (Array[InputTrigger]):  [Read-Write] Trigger qualifiers. If any trigger qualifiers exist the mapping will not trigger unless:
  If there are any Explicit triggers in this list at least one of them must be met.
  All Implicit triggers in this list must be met.

<a id="unreal.EnhancedActionKeyMapping.__init__"></a>

#### __init__

```python
def __init__(triggers: Array[InputTrigger] = [],
             modifiers: Array[InputModifier] = [],
             action: InputAction = None,
             key: Key = []) -> None
```

<a id="unreal.EnhancedActionKeyMapping.player_mappable_options"></a>

#### player_mappable_options

```python
@property
def player_mappable_options() -> PlayerMappableKeyOptions
```

(PlayerMappableKeyOptions):  [Read-Write]
deprecated: PlayerMappableOptions has been deprecated, please use the PlayerMappableKeySettings instead

<a id="unreal.EnhancedActionKeyMapping.player_mappable_options"></a>

#### player_mappable_options

```python
@player_mappable_options.setter
def player_mappable_options(value: PlayerMappableKeyOptions) -> None
```

<a id="unreal.EnhancedActionKeyMapping.triggers"></a>

#### triggers

```python
@property
def triggers() -> Array[InputTrigger]
```

(Array[InputTrigger]):  [Read-Write] Trigger qualifiers. If any trigger qualifiers exist the mapping will not trigger unless:
If there are any Explicit triggers in this list at least one of them must be met.
All Implicit triggers in this list must be met.

<a id="unreal.EnhancedActionKeyMapping.triggers"></a>

#### triggers

```python
@triggers.setter
def triggers(value: Array[InputTrigger]) -> None
```

<a id="unreal.EnhancedActionKeyMapping.modifiers"></a>

#### modifiers

```python
@property
def modifiers() -> Array[InputModifier]
```

(Array[InputModifier]):  [Read-Write] Modifiers applied to the raw key value.
These are applied sequentially in array order.

Note: Modifiers defined in individual key mappings will be applied before those defined in the Input Action asset.
Modifiers will not override any that are defined on the Input Action asset, they will be combined together during evaluation.

<a id="unreal.EnhancedActionKeyMapping.modifiers"></a>

#### modifiers

```python
@modifiers.setter
def modifiers(value: Array[InputModifier]) -> None
```

<a id="unreal.EnhancedActionKeyMapping.action"></a>

#### action

```python
@property
def action() -> InputAction
```

(InputAction):  [Read-Write] Action to be affected by the key

<a id="unreal.EnhancedActionKeyMapping.action"></a>

#### action

```python
@action.setter
def action(value: InputAction) -> None
```

<a id="unreal.EnhancedActionKeyMapping.key"></a>

#### key

```python
@property
def key() -> Key
```

(Key):  [Read-Write] Key that affect the action.

<a id="unreal.EnhancedActionKeyMapping.key"></a>

#### key

```python
@key.setter
def key(value: Key) -> None
```

<a id="unreal.EnhancedActionKeyMapping.is_player_mappable"></a>

#### is_player_mappable

```python
@property
def is_player_mappable() -> bool
```

(bool):  [Read-Write]
deprecated: bIsPlayerMappable has been deprecated, please use the SettingBehavior instead

<a id="unreal.EnhancedActionKeyMapping.is_player_mappable"></a>

#### is_player_mappable

```python
@is_player_mappable.setter
def is_player_mappable(value: bool) -> None
```

<a id="unreal.ModifyContextOptions"></a>