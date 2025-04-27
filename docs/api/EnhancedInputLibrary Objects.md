## EnhancedInputLibrary Objects

```python
class EnhancedInputLibrary(BlueprintFunctionLibrary)
```

Enhanced Input Library

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputLibrary.h

<a id="unreal.EnhancedInputLibrary.request_rebuild_control_mappings_using_context"></a>

#### request_rebuild_control_mappings_using_context

```python
@classmethod
def request_rebuild_control_mappings_using_context(
        cls,
        context: InputMappingContext,
        force_immediately: bool = False) -> None
```

X.request_rebuild_control_mappings_using_context(context, force_immediately=False) -> None
Flag all enhanced input subsystems making use of the mapping context for reapplication of all control mappings at the end of this frame.

Args:
    context (InputMappingContext): Mappings will be rebuilt for all subsystems utilizing this context.
    force_immediately (bool): The mapping changes will be applied synchronously, rather than at the end of the frame, making them available to the input system on the same frame.

<a id="unreal.EnhancedInputLibrary.is_action_key_mapping_player_mappable"></a>

#### is_action_key_mapping_player_mappable

```python
@classmethod
def is_action_key_mapping_player_mappable(
        cls, action_key_mapping: EnhancedActionKeyMapping) -> bool
```

X.is_action_key_mapping_player_mappable(action_key_mapping) -> bool
Returns true if this Action Key Mapping either holds a Player Mappable Key Settings or is set bIsPlayerMappable.

Args:
    action_key_mapping (EnhancedActionKeyMapping): 

Returns:
    bool:

<a id="unreal.EnhancedInputLibrary.get_third_player_mappable_key_slot"></a>

#### get_third_player_mappable_key_slot

```python
@classmethod
def get_third_player_mappable_key_slot(cls) -> PlayerMappableKeySlotData
```

X.get_third_player_mappable_key_slot() -> PlayerMappableKeySlotData
Get Third Player Mappable Key Slot
deprecated: FPlayerMappableKeyOptions has been deprecated. Please use UPlayerMappableKeySettings instead.

Returns:
    PlayerMappableKeySlotData:

<a id="unreal.EnhancedInputLibrary.get_second_player_mappable_key_slot"></a>

#### get_second_player_mappable_key_slot

```python
@classmethod
def get_second_player_mappable_key_slot(cls) -> PlayerMappableKeySlotData
```

X.get_second_player_mappable_key_slot() -> PlayerMappableKeySlotData
Get Second Player Mappable Key Slot
deprecated: FPlayerMappableKeyOptions has been deprecated. Please use UPlayerMappableKeySettings instead.

Returns:
    PlayerMappableKeySlotData:

<a id="unreal.EnhancedInputLibrary.get_player_mappable_key_settings"></a>

#### get_player_mappable_key_settings

```python
@classmethod
def get_player_mappable_key_settings(
        cls, action_key_mapping: EnhancedActionKeyMapping
) -> PlayerMappableKeySettings
```

X.get_player_mappable_key_settings(action_key_mapping) -> PlayerMappableKeySettings
Returns the Player Mappable Key Settings owned by the Action Key Mapping or by the referenced Input Action, or nothing based of the Setting Behavior.

Args:
    action_key_mapping (EnhancedActionKeyMapping): 

Returns:
    PlayerMappableKeySettings:

<a id="unreal.EnhancedInputLibrary.get_mapping_name"></a>

#### get_mapping_name

```python
@classmethod
def get_mapping_name(cls,
                     action_key_mapping: EnhancedActionKeyMapping) -> Name
```

X.get_mapping_name(action_key_mapping) -> Name
Returns the name of the mapping based on setting behavior used. If no name is found in the Mappable Key Settings it will return the name set in Player Mappable Options if bIsPlayerMappable is true.

Args:
    action_key_mapping (EnhancedActionKeyMapping): 

Returns:
    Name:

<a id="unreal.EnhancedInputLibrary.get_fourth_player_mappable_key_slot"></a>

#### get_fourth_player_mappable_key_slot

```python
@classmethod
def get_fourth_player_mappable_key_slot(cls) -> PlayerMappableKeySlotData
```

X.get_fourth_player_mappable_key_slot() -> PlayerMappableKeySlotData
Get Fourth Player Mappable Key Slot
deprecated: FPlayerMappableKeyOptions has been deprecated. Please use UPlayerMappableKeySettings instead.

Returns:
    PlayerMappableKeySlotData:

<a id="unreal.EnhancedInputLibrary.get_first_player_mappable_key_slot"></a>

#### get_first_player_mappable_key_slot

```python
@classmethod
def get_first_player_mappable_key_slot(cls) -> PlayerMappableKeySlotData
```

X.get_first_player_mappable_key_slot() -> PlayerMappableKeySlotData
Get First Player Mappable Key Slot
deprecated: FPlayerMappableKeyOptions has been deprecated. Please use UPlayerMappableKeySettings instead.

Returns:
    PlayerMappableKeySlotData:

<a id="unreal.EnhancedInputLibrary.flush_player_input"></a>

#### flush_player_input

```python
@classmethod
def flush_player_input(cls, player_controller: PlayerController) -> None
```

X.flush_player_input(player_controller) -> None
Flushes the player controller's pressed keys
see: APlayerController::FlushPressedKeys

Args:
    player_controller (PlayerController):

<a id="unreal.EnhancedInputLibrary.conv_trigger_event_value_to_string"></a>

#### conv_trigger_event_value_to_string

```python
@classmethod
def conv_trigger_event_value_to_string(cls,
                                       trigger_event: TriggerEvent) -> str
```

X.conv_trigger_event_value_to_string(trigger_event) -> str
Converts an ETriggerEvent to a string

Args:
    trigger_event (TriggerEvent): 

Returns:
    str:

<a id="unreal.EnhancedInputLibrary.conv_input_action_value_to_string"></a>

#### conv_input_action_value_to_string

```python
@classmethod
def conv_input_action_value_to_string(cls,
                                      action_value: InputActionValue) -> str
```

X.conv_input_action_value_to_string(action_value) -> str
Converts a FInputActionValue to a string

Args:
    action_value (InputActionValue): 

Returns:
    str:

<a id="unreal.EnhancedInputPlatformData"></a>