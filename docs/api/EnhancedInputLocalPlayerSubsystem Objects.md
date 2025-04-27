## EnhancedInputLocalPlayerSubsystem Objects

```python
class EnhancedInputLocalPlayerSubsystem(LocalPlayerSubsystem)
```

Per local player input subsystem

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputSubsystems.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_mappings_rebuilt_delegate`` (OnControlMappingsRebuilt):  [Read-Write] Blueprint Event that is called at the end of any frame that Control Mappings have been rebuilt.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.control_mappings_rebuilt_delegate"></a>

#### control_mappings_rebuilt_delegate

```python
@property
def control_mappings_rebuilt_delegate() -> OnControlMappingsRebuilt
```

(OnControlMappingsRebuilt):  [Read-Write] Blueprint Event that is called at the end of any frame that Control Mappings have been rebuilt.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.control_mappings_rebuilt_delegate"></a>

#### control_mappings_rebuilt_delegate

```python
@control_mappings_rebuilt_delegate.setter
def control_mappings_rebuilt_delegate(value: OnControlMappingsRebuilt) -> None
```

<a id="unreal.EnhancedInputLocalPlayerSubsystem.update_value_of_continuous_input_injection_for_player_mapping"></a>

#### update_value_of_continuous_input_injection_for_player_mapping

```python
def update_value_of_continuous_input_injection_for_player_mapping(
        mapping_name: Name, raw_value: InputActionValue) -> None
```

x.update_value_of_continuous_input_injection_for_player_mapping(mapping_name, raw_value) -> None
Update the value of a continuous input injection for the given player mapping name, preserving the state of triggers and modifiers.

Args:
    mapping_name (Name): The name of the player mapping that can be used for look up an associated UInputAction object.
    raw_value (InputActionValue): The value to set the action to (the type will be controlled by the Action)

<a id="unreal.EnhancedInputLocalPlayerSubsystem.update_value_of_continuous_input_injection_for_action"></a>

#### update_value_of_continuous_input_injection_for_action

```python
def update_value_of_continuous_input_injection_for_action(
        action: InputAction, raw_value: InputActionValue) -> None
```

x.update_value_of_continuous_input_injection_for_action(action, raw_value) -> None
Update the value of a continuous input injection, preserving the state of triggers and modifiers.

Args:
    action (InputAction): The Input Action to set inject input for
    raw_value (InputActionValue): The value to set the action to (the type will be controlled by the Action)

<a id="unreal.EnhancedInputLocalPlayerSubsystem.stop_continuous_input_injection_for_player_mapping"></a>

#### stop_continuous_input_injection_for_player_mapping

```python
def stop_continuous_input_injection_for_player_mapping(
        mapping_name: Name) -> None
```

x.stop_continuous_input_injection_for_player_mapping(mapping_name) -> None
Stops continuous input injection for the given player mapping name.

Args:
    mapping_name (Name): The name of the player mapping that can be used for look up an associated UInputAction object.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.stop_continuous_input_injection_for_action"></a>

#### stop_continuous_input_injection_for_action

```python
def stop_continuous_input_injection_for_action(action: InputAction) -> None
```

x.stop_continuous_input_injection_for_action(action) -> None
Stops continuous input injection for the given action.

Args:
    action (InputAction): The action to stop injecting input for

<a id="unreal.EnhancedInputLocalPlayerSubsystem.start_continuous_input_injection_for_player_mapping"></a>

#### start_continuous_input_injection_for_player_mapping

```python
def start_continuous_input_injection_for_player_mapping(
        mapping_name: Name, raw_value: InputActionValue,
        modifiers: Array[InputModifier],
        triggers: Array[InputTrigger]) -> None
```

x.start_continuous_input_injection_for_player_mapping(mapping_name, raw_value, modifiers, triggers) -> None
Starts simulation of input via injection. This injects the given input every tick until it is stopped with StopContinuousInputInjectionForAction.

Args:
    mapping_name (Name): The name of the player mapping that can be used for look up an associated UInputAction object.
    raw_value (InputActionValue): The value to set the action to (the type will be controlled by the Action)
    modifiers (Array[InputModifier]): The modifiers to apply to the injected input.
    triggers (Array[InputTrigger]): The triggers to apply to the injected input.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.start_continuous_input_injection_for_action"></a>

#### start_continuous_input_injection_for_action

```python
def start_continuous_input_injection_for_action(
        action: InputAction, raw_value: InputActionValue,
        modifiers: Array[InputModifier],
        triggers: Array[InputTrigger]) -> None
```

x.start_continuous_input_injection_for_action(action, raw_value, modifiers, triggers) -> None
Starts simulation of input via injection. This injects the given input every tick until it is stopped with StopContinuousInputInjectionForAction.

Args:
    action (InputAction): The Input Action to set inject input for
    raw_value (InputActionValue): The value to set the action to (the type will be controlled by the Action)
    modifiers (Array[InputModifier]): The modifiers to apply to the injected input.
    triggers (Array[InputTrigger]): The triggers to apply to the injected input.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.request_rebuild_control_mappings"></a>

#### request_rebuild_control_mappings

```python
def request_rebuild_control_mappings(
    options: ModifyContextOptions = [True, False, False],
    rebuild_type: InputMappingRebuildType = InputMappingRebuildType.REBUILD
) -> None
```

x.request_rebuild_control_mappings(options=[True, False, False], rebuild_type=InputMappingRebuildType.REBUILD) -> None
Flag player for reapplication of all mapping contexts at the end of this frame.
This is called automatically when adding or removing mappings contexts.

Args:
    options (ModifyContextOptions): Options to consider when removing this input mapping context
    rebuild_type (InputMappingRebuildType):

<a id="unreal.EnhancedInputLocalPlayerSubsystem.remove_mapping_context"></a>

#### remove_mapping_context

```python
def remove_mapping_context(
        mapping_context: InputMappingContext,
        options: ModifyContextOptions = [True, False, False]) -> None
```

x.remove_mapping_context(mapping_context, options=[True, False, False]) -> None
Remove a specific control context.
This is safe to call even if the context is not applied.

Args:
    mapping_context (InputMappingContext): Context to remove from the player
    options (ModifyContextOptions): Options to consider when removing this input mapping context

<a id="unreal.EnhancedInputLocalPlayerSubsystem.query_map_key_in_context_set"></a>

#### query_map_key_in_context_set

```python
def query_map_key_in_context_set(
    prioritized_active_contexts: Array[InputMappingContext],
    input_context: InputMappingContext, action: InputAction, key: Key,
    blocking_issues: MappingQueryIssueFlag
) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
```

x.query_map_key_in_context_set(prioritized_active_contexts, input_context, action, key, blocking_issues) -> (MappingQueryResult, out_issues=Array[MappingQueryIssue])
= DefaultMappingIssues::StandardFatal

Args:
    prioritized_active_contexts (Array[InputMappingContext]): 
    input_context (InputMappingContext): 
    action (InputAction): 
    key (Key): 
    blocking_issues (MappingQueryIssueFlag): 

Returns:
    Array[MappingQueryIssue]: 

    out_issues (Array[MappingQueryIssue]):

<a id="unreal.EnhancedInputLocalPlayerSubsystem.query_map_key_in_active_context_set"></a>

#### query_map_key_in_active_context_set

```python
def query_map_key_in_active_context_set(
    input_context: InputMappingContext, action: InputAction, key: Key,
    blocking_issues: MappingQueryIssueFlag
) -> Tuple[MappingQueryResult, Array[MappingQueryIssue]]
```

x.query_map_key_in_active_context_set(input_context, action, key, blocking_issues) -> (MappingQueryResult, out_issues=Array[MappingQueryIssue])
= DefaultMappingIssues::StandardFatal

Args:
    input_context (InputMappingContext): 
    action (InputAction): 
    key (Key): 
    blocking_issues (MappingQueryIssueFlag): 

Returns:
    Array[MappingQueryIssue]: 

    out_issues (Array[MappingQueryIssue]):

<a id="unreal.EnhancedInputLocalPlayerSubsystem.query_keys_mapped_to_action"></a>

#### query_keys_mapped_to_action

```python
def query_keys_mapped_to_action(action: InputAction) -> Array[Key]
```

x.query_keys_mapped_to_action(action) -> Array[Key]
Returns the keys mapped to the given action in the active input mapping contexts.

Args:
    action (InputAction): 

Returns:
    Array[Key]:

<a id="unreal.EnhancedInputLocalPlayerSubsystem.inject_input_vector_for_player_mapping"></a>

#### inject_input_vector_for_player_mapping

```python
def inject_input_vector_for_player_mapping(
        mapping_name: Name, value: Vector, modifiers: Array[InputModifier],
        triggers: Array[InputTrigger]) -> None
```

x.inject_input_vector_for_player_mapping(mapping_name, value, modifiers, triggers) -> None
Input simulation via injection. Runs modifiers and triggers delegates as if the input had come through the underlying input system as FKeys.
Applies action modifiers and triggers on top.

Args:
    mapping_name (Name): The name of the player mapping that can be used for look up an associated UInputAction object.
    value (Vector): The value to set the action to (the type will be controlled by the Action)
    modifiers (Array[InputModifier]): The modifiers to apply to the injected input.
    triggers (Array[InputTrigger]): The triggers to apply to the injected input.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.inject_input_vector_for_action"></a>

#### inject_input_vector_for_action

```python
def inject_input_vector_for_action(action: InputAction, value: Vector,
                                   modifiers: Array[InputModifier],
                                   triggers: Array[InputTrigger]) -> None
```

x.inject_input_vector_for_action(action, value, modifiers, triggers) -> None
Input simulation via injection. Runs modifiers and triggers delegates as if the input had come through the underlying input system as FKeys.
Applies action modifiers and triggers on top.

Args:
    action (InputAction): The Input Action to set inject input for
    value (Vector): The value to set the action to (the type will be controlled by the Action)
    modifiers (Array[InputModifier]): The modifiers to apply to the injected input.
    triggers (Array[InputTrigger]): The triggers to apply to the injected input.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.inject_input_for_player_mapping"></a>

#### inject_input_for_player_mapping

```python
def inject_input_for_player_mapping(mapping_name: Name,
                                    raw_value: InputActionValue,
                                    modifiers: Array[InputModifier],
                                    triggers: Array[InputTrigger]) -> None
```

x.inject_input_for_player_mapping(mapping_name, raw_value, modifiers, triggers) -> None
Input simulation via injection. Runs modifiers and triggers delegates as if the input had come through the underlying input system as FKeys.
Applies action modifiers and triggers on top.

Args:
    mapping_name (Name): The name of the player mapping that can be used for look up an associated UInputAction object.
    raw_value (InputActionValue): The value to set the action to
    modifiers (Array[InputModifier]): The modifiers to apply to the injected input.
    triggers (Array[InputTrigger]): The triggers to apply to the injected input.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.inject_input_for_action"></a>

#### inject_input_for_action

```python
def inject_input_for_action(action: InputAction, raw_value: InputActionValue,
                            modifiers: Array[InputModifier],
                            triggers: Array[InputTrigger]) -> None
```

x.inject_input_for_action(action, raw_value, modifiers, triggers) -> None
Input simulation via injection. Runs modifiers and triggers delegates as if the input had come through the underlying input system as FKeys.
Applies action modifiers and triggers on top.

Args:
    action (InputAction): The Input Action to set inject input for
    raw_value (InputActionValue): The value to set the action to
    modifiers (Array[InputModifier]): The modifiers to apply to the injected input.
    triggers (Array[InputTrigger]): The triggers to apply to the injected input.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.has_mapping_context"></a>

#### has_mapping_context

```python
def has_mapping_context(mapping_context: InputMappingContext) -> Optional[int]
```

x.has_mapping_context(mapping_context) -> int32 or None
Check if a mapping context is applied to this subsystem's owner.

Args:
    mapping_context (InputMappingContext): The mapping context to search for on the subsystem's owner.

Returns:
    int32 or None: True if the mapping context is applied

    out_found_priority (int32): The priority of the mapping context if it is applied. -1 if the context is not applied

<a id="unreal.EnhancedInputLocalPlayerSubsystem.get_user_settings"></a>

#### get_user_settings

```python
def get_user_settings() -> EnhancedInputUserSettings
```

x.get_user_settings() -> EnhancedInputUserSettings
Get User Settings

Returns:
    EnhancedInputUserSettings:

<a id="unreal.EnhancedInputLocalPlayerSubsystem.get_all_player_mappable_action_key_mappings"></a>

#### get_all_player_mappable_action_key_mappings

```python
def get_all_player_mappable_action_key_mappings(
) -> Array[EnhancedActionKeyMapping]
```

x.get_all_player_mappable_action_key_mappings() -> Array[EnhancedActionKeyMapping]
Get an array of the currently applied key mappings that are marked as Player Mappable.

Returns:
    Array[EnhancedActionKeyMapping]:

<a id="unreal.EnhancedInputLocalPlayerSubsystem.clear_all_mappings"></a>

#### clear_all_mappings

```python
def clear_all_mappings() -> None
```

x.clear_all_mappings() -> None
Remove all applied mapping contexts.

<a id="unreal.EnhancedInputLocalPlayerSubsystem.add_mapping_context"></a>

#### add_mapping_context

```python
def add_mapping_context(
        mapping_context: InputMappingContext,
        priority: int,
        options: ModifyContextOptions = [True, False, False]) -> None
```

x.add_mapping_context(mapping_context, priority, options=[True, False, False]) -> None
Add a control mapping context.

Args:
    mapping_context (InputMappingContext): A set of key to action mappings to apply to this player
    priority (int32): Higher priority mappings will be applied first and, if they consume input, will block lower priority mappings.
    options (ModifyContextOptions): Options to consider when adding this mapping context.

<a id="unreal.EnhancedInputWorldSubsystem"></a>