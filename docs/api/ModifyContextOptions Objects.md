## ModifyContextOptions Objects

```python
class ModifyContextOptions(StructBase)
```

Passed in as params for Adding/Remove input contexts

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputSubsystemInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``force_immediately`` (bool):  [Read-Write] The mapping changes will be applied synchronously, rather than at the end of the frame,
  making them available to the input system on the same frame.

  This is not recommended to be set to true if you are adding multiple mapping contexts
  as it will have poor performance.

  Default: False
- ``ignore_all_pressed_keys_until_release`` (bool):  [Read-Write] If true, then any keys that are "down" or "pressed" during the rebuild of control mappings will
  not be processed by Enhanced Input until after they are "released".

  For example, if you are adding a mapping context with a key mapping to "X",
  and the player is holding down "X" while that IMC is added,
  there will not be a "Triggered" event until the player releases "X" and presses it again.

  If this is set to false for the above example, then the "Triggered" would fire immediately
  as soon as the IMC is finished being added.

  Default: True

  Note: This will only do something for keys bound to boolean Input Action types.
  Note: This includes all keys that the player has pressed, not just the keys that are previously mapped in Enhanced Input before
  the call to RebuildControlMappings.
- ``notify_user_settings`` (bool):  [Read-Write] If true, then this Mapping Context will be registered or unregistered with the
  Enhanced Input User Settings on this subsystem, if they exist.

  Default: False

  Note: You need to enable and configure your UEnhancedInputUserSettings class in the project
  settings for this to do anything.

<a id="unreal.ModifyContextOptions.__init__"></a>

#### __init__

```python
def __init__(ignore_all_pressed_keys_until_release: bool = False,
             force_immediately: bool = False,
             notify_user_settings: bool = False) -> None
```

<a id="unreal.ModifyContextOptions.ignore_all_pressed_keys_until_release"></a>

#### ignore_all_pressed_keys_until_release

```python
@property
def ignore_all_pressed_keys_until_release() -> bool
```

(bool):  [Read-Write] If true, then any keys that are "down" or "pressed" during the rebuild of control mappings will
not be processed by Enhanced Input until after they are "released".

For example, if you are adding a mapping context with a key mapping to "X",
and the player is holding down "X" while that IMC is added,
there will not be a "Triggered" event until the player releases "X" and presses it again.

If this is set to false for the above example, then the "Triggered" would fire immediately
as soon as the IMC is finished being added.

Default: True

Note: This will only do something for keys bound to boolean Input Action types.
Note: This includes all keys that the player has pressed, not just the keys that are previously mapped in Enhanced Input before
the call to RebuildControlMappings.

<a id="unreal.ModifyContextOptions.ignore_all_pressed_keys_until_release"></a>

#### ignore_all_pressed_keys_until_release

```python
@ignore_all_pressed_keys_until_release.setter
def ignore_all_pressed_keys_until_release(value: bool) -> None
```

<a id="unreal.ModifyContextOptions.force_immediately"></a>

#### force_immediately

```python
@property
def force_immediately() -> bool
```

(bool):  [Read-Write] The mapping changes will be applied synchronously, rather than at the end of the frame,
making them available to the input system on the same frame.

This is not recommended to be set to true if you are adding multiple mapping contexts
as it will have poor performance.

Default: False

<a id="unreal.ModifyContextOptions.force_immediately"></a>

#### force_immediately

```python
@force_immediately.setter
def force_immediately(value: bool) -> None
```

<a id="unreal.ModifyContextOptions.notify_user_settings"></a>

#### notify_user_settings

```python
@property
def notify_user_settings() -> bool
```

(bool):  [Read-Write] If true, then this Mapping Context will be registered or unregistered with the
Enhanced Input User Settings on this subsystem, if they exist.

Default: False

Note: You need to enable and configure your UEnhancedInputUserSettings class in the project
settings for this to do anything.

<a id="unreal.ModifyContextOptions.notify_user_settings"></a>

#### notify_user_settings

```python
@notify_user_settings.setter
def notify_user_settings(value: bool) -> None
```

<a id="unreal.InputActionInstance"></a>