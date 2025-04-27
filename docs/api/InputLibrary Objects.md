## InputLibrary Objects

```python
class InputLibrary(BlueprintFunctionLibrary)
```

Kismet Input Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetInputLibrary.h

<a id="unreal.InputLibrary.pointer_event_is_touch_event"></a>

#### pointer_event_is_touch_event

```python
@classmethod
def pointer_event_is_touch_event(cls, input: PointerEvent) -> bool
```

X.pointer_event_is_touch_event(input) -> bool
Returns true if this event a result from a touch (as opposed to a mouse)

Args:
    input (PointerEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.pointer_event_is_mouse_button_down"></a>

#### pointer_event_is_mouse_button_down

```python
@classmethod
def pointer_event_is_mouse_button_down(cls, input: PointerEvent,
                                       mouse_button: Key) -> bool
```

X.pointer_event_is_mouse_button_down(input, mouse_button) -> bool
Mouse buttons that are currently pressed

Args:
    input (PointerEvent): 
    mouse_button (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.pointer_event_get_wheel_delta"></a>

#### pointer_event_get_wheel_delta

```python
@classmethod
def pointer_event_get_wheel_delta(cls, input: PointerEvent) -> float
```

X.pointer_event_get_wheel_delta(input) -> float
How much did the mouse wheel turn since the last mouse event

Args:
    input (PointerEvent): 

Returns:
    float:

<a id="unreal.InputLibrary.pointer_event_get_user_index"></a>

#### pointer_event_get_user_index

```python
@classmethod
def pointer_event_get_user_index(cls, input: PointerEvent) -> int
```

X.pointer_event_get_user_index(input) -> int32
Returns the index of the user that caused the event

Args:
    input (PointerEvent): 

Returns:
    int32:

<a id="unreal.InputLibrary.pointer_event_get_touchpad_index"></a>

#### pointer_event_get_touchpad_index

```python
@classmethod
def pointer_event_get_touchpad_index(cls, input: PointerEvent) -> int
```

X.pointer_event_get_touchpad_index(input) -> int32
Returns the index of the touch pad that generated this event (for platforms with multiple touch pads per user)

Args:
    input (PointerEvent): 

Returns:
    int32:

<a id="unreal.InputLibrary.pointer_event_get_screen_space_position"></a>

#### pointer_event_get_screen_space_position

```python
@classmethod
def pointer_event_get_screen_space_position(cls,
                                            input: PointerEvent) -> Vector2D
```

X.pointer_event_get_screen_space_position(input) -> Vector2D
Returns The position of the cursor in screen space

Args:
    input (PointerEvent): 

Returns:
    Vector2D:

<a id="unreal.InputLibrary.pointer_event_get_pointer_index"></a>

#### pointer_event_get_pointer_index

```python
@classmethod
def pointer_event_get_pointer_index(cls, input: PointerEvent) -> int
```

X.pointer_event_get_pointer_index(input) -> int32
Returns the unique identifier of the pointer (e.g., finger index)

Args:
    input (PointerEvent): 

Returns:
    int32:

<a id="unreal.InputLibrary.pointer_event_get_last_screen_space_position"></a>

#### pointer_event_get_last_screen_space_position

```python
@classmethod
def pointer_event_get_last_screen_space_position(
        cls, input: PointerEvent) -> Vector2D
```

X.pointer_event_get_last_screen_space_position(input) -> Vector2D
Returns the position of the cursor in screen space last time we handled an input event

Args:
    input (PointerEvent): 

Returns:
    Vector2D:

<a id="unreal.InputLibrary.pointer_event_get_gesture_type"></a>

#### pointer_event_get_gesture_type

```python
@classmethod
def pointer_event_get_gesture_type(cls, input: PointerEvent) -> SlateGesture
```

X.pointer_event_get_gesture_type(input) -> SlateGesture
Returns the type of touch gesture

Args:
    input (PointerEvent): 

Returns:
    SlateGesture:

<a id="unreal.InputLibrary.pointer_event_get_gesture_delta"></a>

#### pointer_event_get_gesture_delta

```python
@classmethod
def pointer_event_get_gesture_delta(cls, input: PointerEvent) -> Vector2D
```

X.pointer_event_get_gesture_delta(input) -> Vector2D
Returns the change in gesture value since the last gesture event of the same type.

Args:
    input (PointerEvent): 

Returns:
    Vector2D:

<a id="unreal.InputLibrary.pointer_event_get_effecting_button"></a>

#### pointer_event_get_effecting_button

```python
@classmethod
def pointer_event_get_effecting_button(cls, input: PointerEvent) -> Key
```

X.pointer_event_get_effecting_button(input) -> Key
Mouse button that caused this event to be raised (possibly FKey::Invalid)

Args:
    input (PointerEvent): 

Returns:
    Key:

<a id="unreal.InputLibrary.pointer_event_get_cursor_delta"></a>

#### pointer_event_get_cursor_delta

```python
@classmethod
def pointer_event_get_cursor_delta(cls, input: PointerEvent) -> Vector2D
```

X.pointer_event_get_cursor_delta(input) -> Vector2D
Returns the distance the mouse traveled since the last event was handled.

Args:
    input (PointerEvent): 

Returns:
    Vector2D:

<a id="unreal.InputLibrary.modifier_keys_state_is_shift_down"></a>

#### modifier_keys_state_is_shift_down

```python
@classmethod
def modifier_keys_state_is_shift_down(
        cls, keys_state: SlateModifierKeysState) -> bool
```

X.modifier_keys_state_is_shift_down(keys_state) -> bool
Returns true if either shift key was down when the key state was captured

Args:
    keys_state (SlateModifierKeysState): 

Returns:
    bool:

<a id="unreal.InputLibrary.modifier_keys_state_is_control_down"></a>

#### modifier_keys_state_is_control_down

```python
@classmethod
def modifier_keys_state_is_control_down(
        cls, keys_state: SlateModifierKeysState) -> bool
```

X.modifier_keys_state_is_control_down(keys_state) -> bool
Returns true if either control key was down when the key state was captured

Args:
    keys_state (SlateModifierKeysState): 

Returns:
    bool:

<a id="unreal.InputLibrary.modifier_keys_state_is_command_down"></a>

#### modifier_keys_state_is_command_down

```python
@classmethod
def modifier_keys_state_is_command_down(
        cls, keys_state: SlateModifierKeysState) -> bool
```

X.modifier_keys_state_is_command_down(keys_state) -> bool
Returns true if either command key was down when the key state was captured

Args:
    keys_state (SlateModifierKeysState): 

Returns:
    bool:

<a id="unreal.InputLibrary.modifier_keys_state_is_alt_down"></a>

#### modifier_keys_state_is_alt_down

```python
@classmethod
def modifier_keys_state_is_alt_down(
        cls, keys_state: SlateModifierKeysState) -> bool
```

X.modifier_keys_state_is_alt_down(keys_state) -> bool
Returns true if either alt key was down when the key state was captured

Args:
    keys_state (SlateModifierKeysState): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_vector_axis"></a>

#### key_is_vector_axis

```python
@classmethod
def key_is_vector_axis(cls, key: Key) -> bool
```

X.key_is_vector_axis(key) -> bool
Returns true if the key is a vector axis
deprecated: Use Is Axis 2D/3D instead.
note: Deprecated. Use Is Axis 2D/3D instead.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_valid"></a>

#### key_is_valid

```python
@classmethod
def key_is_valid(cls, key: Key) -> bool
```

X.key_is_valid(key) -> bool
Returns true if this is a valid key.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_mouse_button"></a>

#### key_is_mouse_button

```python
@classmethod
def key_is_mouse_button(cls, key: Key) -> bool
```

X.key_is_mouse_button(key) -> bool
Returns true if the key is a mouse button

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_modifier_key"></a>

#### key_is_modifier_key

```python
@classmethod
def key_is_modifier_key(cls, key: Key) -> bool
```

X.key_is_modifier_key(key) -> bool
Returns true if the key is a modifier key: Ctrl, Command, Alt, Shift

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_keyboard_key"></a>

#### key_is_keyboard_key

```python
@classmethod
def key_is_keyboard_key(cls, key: Key) -> bool
```

X.key_is_keyboard_key(key) -> bool
Returns true if the key is a keyboard button

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_gamepad_key"></a>

#### key_is_gamepad_key

```python
@classmethod
def key_is_gamepad_key(cls, key: Key) -> bool
```

X.key_is_gamepad_key(key) -> bool
Returns true if the key is a gamepad button

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_digital"></a>

#### key_is_digital

```python
@classmethod
def key_is_digital(cls, key: Key) -> bool
```

X.key_is_digital(key) -> bool
Returns true if the key is a digital button press

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_button_axis"></a>

#### key_is_button_axis

```python
@classmethod
def key_is_button_axis(cls, key: Key) -> bool
```

X.key_is_button_axis(key) -> bool
Returns true if the key is a 1D axis emulating a digital button press.

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_axis3d"></a>

#### key_is_axis3d

```python
@classmethod
def key_is_axis3d(cls, key: Key) -> bool
```

X.key_is_axis3d(key) -> bool
Returns true if the key is a 3D (vector) axis

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_axis2d"></a>

#### key_is_axis2d

```python
@classmethod
def key_is_axis2d(cls, key: Key) -> bool
```

X.key_is_axis2d(key) -> bool
Returns true if the key is a 2D (vector) axis

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_axis1d"></a>

#### key_is_axis1d

```python
@classmethod
def key_is_axis1d(cls, key: Key) -> bool
```

X.key_is_axis1d(key) -> bool
Returns true if the key is a 1D (float) axis

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_is_float_axis"></a>

#### key_is_float_axis

```python
@classmethod
def key_is_float_axis(cls, key: Key) -> bool
```

deprecated: 'key_is_float_axis' was renamed to 'key_is_axis1d'.

<a id="unreal.InputLibrary.key_is_analog"></a>

#### key_is_analog

```python
@classmethod
def key_is_analog(cls, key: Key) -> bool
```

X.key_is_analog(key) -> bool
Returns true if the key is an analog axis

Args:
    key (Key): 

Returns:
    bool:

<a id="unreal.InputLibrary.key_get_navigation_direction_from_key"></a>

#### key_get_navigation_direction_from_key

```python
@classmethod
def key_get_navigation_direction_from_key(cls,
                                          key_event: KeyEvent) -> UINavigation
```

X.key_get_navigation_direction_from_key(key_event) -> UINavigation
Returns the navigation action corresponding to this key, or Invalid if not found

Args:
    key_event (KeyEvent): 

Returns:
    UINavigation:

<a id="unreal.InputLibrary.key_get_navigation_direction_from_analog"></a>

#### key_get_navigation_direction_from_analog

```python
@classmethod
def key_get_navigation_direction_from_analog(
        cls, analog_event: AnalogInputEvent) -> UINavigation
```

X.key_get_navigation_direction_from_analog(analog_event) -> UINavigation
Returns the navigation action corresponding to this key, or Invalid if not found

Args:
    analog_event (AnalogInputEvent): 

Returns:
    UINavigation:

<a id="unreal.InputLibrary.key_get_navigation_action_from_key"></a>

#### key_get_navigation_action_from_key

```python
@classmethod
def key_get_navigation_action_from_key(
        cls, key_event: KeyEvent) -> UINavigationAction
```

X.key_get_navigation_action_from_key(key_event) -> UINavigationAction
Returns the navigation action corresponding to this key, or Invalid if not found

Args:
    key_event (KeyEvent): 

Returns:
    UINavigationAction:

<a id="unreal.InputLibrary.key_get_navigation_action"></a>

#### key_get_navigation_action

```python
@classmethod
def key_get_navigation_action(cls, key: Key) -> UINavigationAction
```

X.key_get_navigation_action(key) -> UINavigationAction
Key Get Navigation Action
deprecated: Use Get Key Event Navigation Action instead

Args:
    key (Key): 

Returns:
    UINavigationAction:

<a id="unreal.InputLibrary.key_get_display_name"></a>

#### key_get_display_name

```python
@classmethod
def key_get_display_name(cls,
                         key: Key,
                         long_display_name: bool = True) -> Text
```

X.key_get_display_name(key, long_display_name=True) -> Text
Returns the display name of the key.

Args:
    key (Key): 
    long_display_name (bool): 

Returns:
    Text:

<a id="unreal.InputLibrary.input_event_is_shift_down"></a>

#### input_event_is_shift_down

```python
@classmethod
def input_event_is_shift_down(cls, input: InputEvent) -> bool
```

X.input_event_is_shift_down(input) -> bool
Returns true if either shift key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_right_shift_down"></a>

#### input_event_is_right_shift_down

```python
@classmethod
def input_event_is_right_shift_down(cls, input: InputEvent) -> bool
```

X.input_event_is_right_shift_down(input) -> bool
Returns true if right shift key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_right_control_down"></a>

#### input_event_is_right_control_down

```python
@classmethod
def input_event_is_right_control_down(cls, input: InputEvent) -> bool
```

X.input_event_is_right_control_down(input) -> bool
Returns true if left control key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_right_command_down"></a>

#### input_event_is_right_command_down

```python
@classmethod
def input_event_is_right_command_down(cls, input: InputEvent) -> bool
```

X.input_event_is_right_command_down(input) -> bool
Returns true if right command key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_right_alt_down"></a>

#### input_event_is_right_alt_down

```python
@classmethod
def input_event_is_right_alt_down(cls, input: InputEvent) -> bool
```

X.input_event_is_right_alt_down(input) -> bool
Returns true if right alt key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_repeat"></a>

#### input_event_is_repeat

```python
@classmethod
def input_event_is_repeat(cls, input: InputEvent) -> bool
```

X.input_event_is_repeat(input) -> bool
Returns whether or not this character is an auto-repeated keystroke

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_left_shift_down"></a>

#### input_event_is_left_shift_down

```python
@classmethod
def input_event_is_left_shift_down(cls, input: InputEvent) -> bool
```

X.input_event_is_left_shift_down(input) -> bool
Returns true if left shift key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_left_control_down"></a>

#### input_event_is_left_control_down

```python
@classmethod
def input_event_is_left_control_down(cls, input: InputEvent) -> bool
```

X.input_event_is_left_control_down(input) -> bool
Returns true if left control key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_left_command_down"></a>

#### input_event_is_left_command_down

```python
@classmethod
def input_event_is_left_command_down(cls, input: InputEvent) -> bool
```

X.input_event_is_left_command_down(input) -> bool
Returns true if left command key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_left_alt_down"></a>

#### input_event_is_left_alt_down

```python
@classmethod
def input_event_is_left_alt_down(cls, input: InputEvent) -> bool
```

X.input_event_is_left_alt_down(input) -> bool
Returns true if left alt key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_control_down"></a>

#### input_event_is_control_down

```python
@classmethod
def input_event_is_control_down(cls, input: InputEvent) -> bool
```

X.input_event_is_control_down(input) -> bool
Returns true if either control key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_command_down"></a>

#### input_event_is_command_down

```python
@classmethod
def input_event_is_command_down(cls, input: InputEvent) -> bool
```

X.input_event_is_command_down(input) -> bool
Returns true if either command key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_event_is_alt_down"></a>

#### input_event_is_alt_down

```python
@classmethod
def input_event_is_alt_down(cls, input: InputEvent) -> bool
```

X.input_event_is_alt_down(input) -> bool
Returns true if either alt key was down when this event occurred

Args:
    input (InputEvent): 

Returns:
    bool:

<a id="unreal.InputLibrary.input_chord_get_display_name"></a>

#### input_chord_get_display_name

```python
@classmethod
def input_chord_get_display_name(cls, key: InputChord) -> Text
```

X.input_chord_get_display_name(key) -> Text


Args:
    key (InputChord): 

Returns:
    Text: The display name of the input chord

<a id="unreal.InputLibrary.get_user_index"></a>

#### get_user_index

```python
@classmethod
def get_user_index(cls, input: KeyEvent) -> int
```

X.get_user_index(input) -> int32
Get User Index

Args:
    input (KeyEvent): 

Returns:
    int32:

<a id="unreal.InputLibrary.get_modifier_keys_state"></a>

#### get_modifier_keys_state

```python
@classmethod
def get_modifier_keys_state(cls) -> SlateModifierKeysState
```

X.get_modifier_keys_state() -> SlateModifierKeysState
Returns a snapshot of the cached modifier-keys state for the application.

Returns:
    SlateModifierKeysState:

<a id="unreal.InputLibrary.get_key"></a>

#### get_key

```python
@classmethod
def get_key(cls, input: KeyEvent) -> Key
```

X.get_key(input) -> Key
Returns the key for this event.

Args:
    input (KeyEvent): 

Returns:
    Key: Key name

<a id="unreal.InputLibrary.get_analog_value"></a>

#### get_analog_value

```python
@classmethod
def get_analog_value(cls, input: AnalogInputEvent) -> float
```

X.get_analog_value(input) -> float
Get Analog Value

Args:
    input (AnalogInputEvent): 

Returns:
    float:

<a id="unreal.InputLibrary.equal_equal_key_key"></a>

#### equal_equal_key_key

```python
@classmethod
def equal_equal_key_key(cls, a: Key, b: Key) -> bool
```

X.equal_equal_key_key(a, b) -> bool
Test if the input key are equal (A == B)

Args:
    a (Key): The key to compare against
    b (Key): The key to compare Returns true if the key are equal, false otherwise

Returns:
    bool:

<a id="unreal.InputLibrary.equal_equal_input_chord_input_chord"></a>

#### equal_equal_input_chord_input_chord

```python
@classmethod
def equal_equal_input_chord_input_chord(cls, a: InputChord,
                                        b: InputChord) -> bool
```

X.equal_equal_input_chord_input_chord(a, b) -> bool
Test if the input chords are equal (A == B)

Args:
    a (InputChord): The chord to compare against
    b (InputChord): The chord to compare Returns true if the chords are equal, false otherwise

Returns:
    bool:

<a id="unreal.InputLibrary.calibrate_tilt"></a>

#### calibrate_tilt

```python
@classmethod
def calibrate_tilt(cls) -> None
```

X.calibrate_tilt() -> None
Calibrate the tilt for the input device

<a id="unreal.InternationalizationLibrary"></a>