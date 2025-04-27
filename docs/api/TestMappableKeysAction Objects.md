## TestMappableKeysAction Objects

```python
class TestMappableKeysAction(InputAction)
```

A subclass of UInputAction that will have it's player mappable key settings object set automatically so
we can test re-mappable keys.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: InputEditor
- **File**: InputTestFramework.h

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

<a id="unreal.EnhancedInputUserWidgetValidator"></a>