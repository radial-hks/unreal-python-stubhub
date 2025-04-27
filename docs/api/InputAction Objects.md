## InputAction Objects

```python
class InputAction(DataAsset)
```

An Input Action is a logical representation of something the user can do, such as "Jump" or "Crouch".
These are what your gameplay code binds to in order to listen for input state changes. For most scenarios
your gameplay code should be listening for the "Triggered" event on an input action. This will allow
for the most scalable and customizable input configuration because you can add different triggers
for each key mapping in the Input Mapping Context.

They are the conceptual equivalent to "Action" and "Axis" mapping names from the Legacy Input System.

Note: These are instanced per player (via FInputActionInstance)

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputAction.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulation_behavior`` (InputActionAccumulationBehavior):  [Read-Write] This defines how the value of this input action will be calcuated in the case that there are multiple key mappings to the same input action.

  When TakeHighestAbsoluteValue is selected, then the key mapping with the highest absolutle value will be utilized. (Default)
  When Cumulative is selected, then each key mapping will be added together to get the key value.
  see: UEnhancedPlayerInput::ProcessActionMappingEvent, where this property is read from.
- ``action_description`` (Text):  [Read-Write] A localized descriptor of this input action
- ``consume_input`` (bool):  [Read-Write] Should this action swallow any inputs bound to it or allow them to pass through to affect lower priority bound actions?
- ``consumes_action_and_axis_mappings`` (bool):  [Read-Write] Should this Input Action consume any legacy Action and Axis key mappings?
  If true, then any key mapping to this input action will consume(aka block) the legacy key
  mapping from firing delegates.
- ``modifiers`` (Array[InputModifier]):  [Read-Write] Modifiers are applied to the final action value.
  These are applied sequentially in array order.
  They are applied on top of any FEnhancedActionKeyMapping modifiers that drove the initial input

  Note: Modifiers defined in the Input Action asset will be applied AFTER any modifiers defined in individual key mappings in the Input Mapping Context asset.
- ``player_mappable_key_settings`` (PlayerMappableKeySettings):  [Read-Write] Holds setting information about this Action Input for setting screen and save purposes.
- ``reserve_all_mappings`` (bool):  [Read-Write] This action's mappings are not intended to be automatically overridden by higher priority context mappings. Users must explicitly remove the mapping first. NOTE: It is the responsibility of the author of the mapping code to enforce this!
- ``trigger_events_that_consume_legacy_keys`` (int32):  [Read-Write] A bitmask of trigger events that, when reached, will consume any FKeys mapped to this input action.
- ``trigger_when_paused`` (bool):  [Read-Write] Should this action be able to trigger whilst the game is paused - Replaces bExecuteWhenPaused
- ``triggers`` (Array[InputTrigger]):  [Read-Write] Trigger qualifiers. If any trigger qualifiers exist the action will not trigger unless:
  At least one Explicit trigger in this list has been met.
  All Implicit triggers in this list are met.
- ``value_type`` (InputActionValueType):  [Read-Write] The type that this action returns from a GetActionValue query or action event

<a id="unreal.InputAction.action_description"></a>

#### action_description

```python
@property
def action_description() -> Text
```

(Text):  [Read-Only] A localized descriptor of this input action

<a id="unreal.InputAction.trigger_when_paused"></a>

#### trigger_when_paused

```python
@property
def trigger_when_paused() -> bool
```

(bool):  [Read-Only] Should this action be able to trigger whilst the game is paused - Replaces bExecuteWhenPaused

<a id="unreal.InputAction.consume_input"></a>

#### consume_input

```python
@property
def consume_input() -> bool
```

(bool):  [Read-Write] Should this action swallow any inputs bound to it or allow them to pass through to affect lower priority bound actions?

<a id="unreal.InputAction.consume_input"></a>

#### consume_input

```python
@consume_input.setter
def consume_input(value: bool) -> None
```

<a id="unreal.InputAction.consumes_action_and_axis_mappings"></a>

#### consumes_action_and_axis_mappings

```python
@property
def consumes_action_and_axis_mappings() -> bool
```

(bool):  [Read-Write] Should this Input Action consume any legacy Action and Axis key mappings?
If true, then any key mapping to this input action will consume(aka block) the legacy key
mapping from firing delegates.

<a id="unreal.InputAction.consumes_action_and_axis_mappings"></a>

#### consumes_action_and_axis_mappings

```python
@consumes_action_and_axis_mappings.setter
def consumes_action_and_axis_mappings(value: bool) -> None
```

<a id="unreal.InputAction.reserve_all_mappings"></a>

#### reserve_all_mappings

```python
@property
def reserve_all_mappings() -> bool
```

(bool):  [Read-Only] This action's mappings are not intended to be automatically overridden by higher priority context mappings. Users must explicitly remove the mapping first. NOTE: It is the responsibility of the author of the mapping code to enforce this!

<a id="unreal.InputAction.trigger_events_that_consume_legacy_keys"></a>

#### trigger_events_that_consume_legacy_keys

```python
@property
def trigger_events_that_consume_legacy_keys() -> int
```

(int32):  [Read-Write] A bitmask of trigger events that, when reached, will consume any FKeys mapped to this input action.

<a id="unreal.InputAction.trigger_events_that_consume_legacy_keys"></a>

#### trigger_events_that_consume_legacy_keys

```python
@trigger_events_that_consume_legacy_keys.setter
def trigger_events_that_consume_legacy_keys(value: int) -> None
```

<a id="unreal.InputAction.value_type"></a>

#### value_type

```python
@property
def value_type() -> InputActionValueType
```

(InputActionValueType):  [Read-Only] The type that this action returns from a GetActionValue query or action event

<a id="unreal.InputAction.accumulation_behavior"></a>

#### accumulation_behavior

```python
@property
def accumulation_behavior() -> InputActionAccumulationBehavior
```

(InputActionAccumulationBehavior):  [Read-Only] This defines how the value of this input action will be calcuated in the case that there are multiple key mappings to the same input action.

When TakeHighestAbsoluteValue is selected, then the key mapping with the highest absolutle value will be utilized. (Default)
When Cumulative is selected, then each key mapping will be added together to get the key value.
see: UEnhancedPlayerInput::ProcessActionMappingEvent, where this property is read from.

<a id="unreal.InputAction.triggers"></a>

#### triggers

```python
@property
def triggers() -> Array[InputTrigger]
```

(Array[InputTrigger]):  [Read-Write] Trigger qualifiers. If any trigger qualifiers exist the action will not trigger unless:
At least one Explicit trigger in this list has been met.
All Implicit triggers in this list are met.

<a id="unreal.InputAction.triggers"></a>

#### triggers

```python
@triggers.setter
def triggers(value: Array[InputTrigger]) -> None
```

<a id="unreal.InputAction.modifiers"></a>

#### modifiers

```python
@property
def modifiers() -> Array[InputModifier]
```

(Array[InputModifier]):  [Read-Write] Modifiers are applied to the final action value.
These are applied sequentially in array order.
They are applied on top of any FEnhancedActionKeyMapping modifiers that drove the initial input

Note: Modifiers defined in the Input Action asset will be applied AFTER any modifiers defined in individual key mappings in the Input Mapping Context asset.

<a id="unreal.InputAction.modifiers"></a>

#### modifiers

```python
@modifiers.setter
def modifiers(value: Array[InputModifier]) -> None
```

<a id="unreal.InputAction.player_mappable_key_settings"></a>

#### player_mappable_key_settings

```python
@property
def player_mappable_key_settings() -> PlayerMappableKeySettings
```

(PlayerMappableKeySettings):  [Read-Write] Holds setting information about this Action Input for setting screen and save purposes.

<a id="unreal.InputAction.player_mappable_key_settings"></a>

#### player_mappable_key_settings

```python
@player_mappable_key_settings.setter
def player_mappable_key_settings(value: PlayerMappableKeySettings) -> None
```

<a id="unreal.InputMappingContext"></a>