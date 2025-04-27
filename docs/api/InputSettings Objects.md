## InputSettings Objects

```python
class InputSettings(Object)
```

Project wide settings for input handling
see: https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

**C++ Source:**

- **Module**: Engine
- **File**: InputSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action_mappings`` (Array[InputActionKeyMapping]):  [Read-Write] List of Action Mappings
- ``alt_enter_toggles_fullscreen`` (bool):  [Read-Write]
- ``always_show_touch_interface`` (bool):  [Read-Write] Should the touch input interface be shown always, or only when the platform has a touch screen?
- ``axis_config`` (Array[InputAxisConfigEntry]):  [Read-Write] List of Axis Properties
- ``axis_mappings`` (Array[InputAxisKeyMapping]):  [Read-Write] List of Axis Mappings
- ``capture_mouse_on_launch`` (bool):  [Read-Write] Controls if the viewport will capture the mouse on Launch of the application
- ``console_keys`` (Array[Key]):  [Read-Write] The keys which open the console.
- ``default_input_component_class`` (Class):  [Read-Write] Default class type for pawn input components.
- ``default_player_input_class`` (Class):  [Read-Write] Default class type for player input object. May be overridden by player controller.
- ``default_touch_interface`` (SoftObjectPath):  [Read-Write] The default on-screen touch input interface for the game (can be null to disable the onscreen interface)
- ``default_viewport_mouse_capture_mode`` (MouseCaptureMode):  [Read-Write] The default mouse capture mode for the game viewport
- ``default_viewport_mouse_lock_mode`` (MouseLockMode):  [Read-Write] The default mouse lock state behavior when the viewport acquires capture
- ``double_click_time`` (float):  [Read-Write] If a key is pressed twice in this amount of time it is considered a "double click"
- ``enable_dynamic_component_input_binding`` (bool):  [Read-Write] Should components that are dynamically added via the 'AddComponent' function at runtime have input delegates bound to them?
  see: AActor::FinishAddComponent
- ``enable_fov_scaling`` (bool):  [Read-Write] Scale the mouse based on the player camera manager's field of view
- ``enable_gesture_recognizer`` (bool):  [Read-Write] Whether or not to use the gesture recognition system to convert touches in to gestures that can be bound and queried
- ``enable_input_device_subsystem`` (bool):  [Read-Write]
  deprecated: bEnableInputDeviceSubsystem is deprecated, ths input device subsystem will now always be created.
- ``enable_legacy_input_scales`` (bool):  [Read-Write] Enable the use of legacy input scales on the player controller (InputYawScale, InputPitchScale, and InputRollScale)
- ``enable_motion_controls`` (bool):  [Read-Write] If set to false, then the player controller's InputMotion function will never be called.
  This will effectively disable any motion input (tilt, rotation, acceleration, etc) on
  the GameViewportClient.
  see: GameViewportClient::InputMotion
- ``enable_mouse_smoothing`` (bool):  [Read-Write] Mouse smoothing control
- ``excluded_autocorrect_cultures`` (Array[str]):  [Read-Write] Disables autocorrect for these cultures, even if autocorrect is turned on. These should be ISO-compliant language and country codes, such as "en" or "en-US".
- ``excluded_autocorrect_device_models`` (Array[str]):  [Read-Write] Disables autocorrect for these device models, even if autocorrect is turned in. Model IDs listed here will match against the start of the device's
  model (e.g., "SM-" will match all device model IDs that start with "SM-"). This is currently only supported on Android devices.
- ``excluded_autocorrect_os`` (Array[str]):  [Read-Write] Disables autocorrect for these operating systems, even if autocorrect is enabled. Use the format "[platform] [osversion]"
  (e.g., "iOS 11.2" or "Android 6"). More specific versions will disable autocorrect for fewer devices ("iOS 11" will disable
  autocorrect for all devices running iOS 11, but "iOS 11.2.2" will not disable autocorrect for devices running 11.2.1).
- ``f11_toggles_fullscreen`` (bool):  [Read-Write]
- ``filter_input_by_platform_user`` (bool):  [Read-Write] If true, then the PlayerController::InputKey function will only process an input event if it
  came from an input device that is owned by the PlayerController's Platform User.
- ``fov_scale`` (float):  [Read-Write] The scaling value to multiply the field of view by
- ``platform_settings`` (PerPlatformSettings):  [Read-Write] Platform specific settings for Input.
  see: UInputPlatformSettings
- ``should_flush_pressed_keys_on_viewport_focus_lost`` (bool):  [Read-Write] If true, then the Player Controller will have it's Pressed Keys flushed when the input mode is changed
  to Game and UI mode or the game viewport loses focus. The default behavior is true.
  see: UGameViewportClient::LostFocus
  see: APlayerController::ShouldFlushKeysWhenViewportFocusChanges
- ``show_console_on_four_finger_tap`` (bool):  [Read-Write] Whether or not to show the console on 4 finger tap, on mobile platforms
- ``speech_mappings`` (Array[InputActionSpeechMapping]):  [Read-Write] List of Speech Mappings
- ``use_autocorrect`` (bool):  [Read-Write] If enabled, virtual keyboards will have autocorrect enabled. Currently only supported on mobile devices.
- ``use_mouse_for_touch`` (bool):  [Read-Write] Allow mouse to be used for touch

<a id="unreal.InputSettings.enable_input_device_subsystem"></a>

#### enable_input_device_subsystem

```python
@property
def enable_input_device_subsystem() -> bool
```

(bool):  [Read-Write]
deprecated: bEnableInputDeviceSubsystem is deprecated, ths input device subsystem will now always be created.

<a id="unreal.InputSettings.enable_input_device_subsystem"></a>

#### enable_input_device_subsystem

```python
@enable_input_device_subsystem.setter
def enable_input_device_subsystem(value: bool) -> None
```

<a id="unreal.InputSettings.save_key_mappings"></a>

#### save_key_mappings

```python
def save_key_mappings() -> None
```

x.save_key_mappings() -> None
Flush the current mapping values to the config file

<a id="unreal.InputSettings.remove_axis_mapping"></a>

#### remove_axis_mapping

```python
def remove_axis_mapping(key_mapping: InputAxisKeyMapping,
                        force_rebuild_keymaps: bool = True) -> None
```

x.remove_axis_mapping(key_mapping, force_rebuild_keymaps=True) -> None
Programmatically remove an axis mapping to the project defaults

Args:
    key_mapping (InputAxisKeyMapping): 
    force_rebuild_keymaps (bool):

<a id="unreal.InputSettings.remove_action_mapping"></a>

#### remove_action_mapping

```python
def remove_action_mapping(key_mapping: InputActionKeyMapping,
                          force_rebuild_keymaps: bool = True) -> None
```

x.remove_action_mapping(key_mapping, force_rebuild_keymaps=True) -> None
Programmatically remove an action mapping to the project defaults

Args:
    key_mapping (InputActionKeyMapping): 
    force_rebuild_keymaps (bool):

<a id="unreal.InputSettings.get_input_settings"></a>

#### get_input_settings

```python
@classmethod
def get_input_settings(cls) -> InputSettings
```

X.get_input_settings() -> InputSettings
Returns the game local input settings (action mappings, axis mappings, etc...)

Returns:
    InputSettings:

<a id="unreal.InputSettings.get_axis_names"></a>

#### get_axis_names

```python
def get_axis_names() -> Array[Name]
```

x.get_axis_names() -> Array[Name]
Populate a list of all defined axis names

Returns:
    Array[Name]: 

    axis_names (Array[Name]):

<a id="unreal.InputSettings.get_axis_mapping_by_name"></a>

#### get_axis_mapping_by_name

```python
def get_axis_mapping_by_name(axis_name: Name) -> Array[InputAxisKeyMapping]
```

x.get_axis_mapping_by_name(axis_name) -> Array[InputAxisKeyMapping]
Retrieve all axis mappings by a certain name.

Args:
    axis_name (Name): 

Returns:
    Array[InputAxisKeyMapping]: 

    out_mappings (Array[InputAxisKeyMapping]):

<a id="unreal.InputSettings.get_action_names"></a>

#### get_action_names

```python
def get_action_names() -> Array[Name]
```

x.get_action_names() -> Array[Name]
Populate a list of all defined action names

Returns:
    Array[Name]: 

    action_names (Array[Name]):

<a id="unreal.InputSettings.get_action_mapping_by_name"></a>

#### get_action_mapping_by_name

```python
def get_action_mapping_by_name(
        action_name: Name) -> Array[InputActionKeyMapping]
```

x.get_action_mapping_by_name(action_name) -> Array[InputActionKeyMapping]
Get Action Mapping by Name

Args:
    action_name (Name): 

Returns:
    Array[InputActionKeyMapping]: 

    out_mappings (Array[InputActionKeyMapping]):

<a id="unreal.InputSettings.force_rebuild_keymaps"></a>

#### force_rebuild_keymaps

```python
def force_rebuild_keymaps() -> None
```

x.force_rebuild_keymaps() -> None
When changes are made to the default mappings, push those changes out to PlayerInput key maps

<a id="unreal.InputSettings.add_axis_mapping"></a>

#### add_axis_mapping

```python
def add_axis_mapping(key_mapping: InputAxisKeyMapping,
                     force_rebuild_keymaps: bool = True) -> None
```

x.add_axis_mapping(key_mapping, force_rebuild_keymaps=True) -> None
Programmatically add an axis mapping to the project defaults

Args:
    key_mapping (InputAxisKeyMapping): 
    force_rebuild_keymaps (bool):

<a id="unreal.InputSettings.add_action_mapping"></a>

#### add_action_mapping

```python
def add_action_mapping(key_mapping: InputActionKeyMapping,
                       force_rebuild_keymaps: bool = True) -> None
```

x.add_action_mapping(key_mapping, force_rebuild_keymaps=True) -> None
Programmatically add an action mapping to the project defaults

Args:
    key_mapping (InputActionKeyMapping): 
    force_rebuild_keymaps (bool):

<a id="unreal.PlayerInput"></a>