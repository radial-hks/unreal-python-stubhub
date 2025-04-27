## InputDeviceState Objects

```python
class InputDeviceState(StructBase)
```

Current state of physical input devices at a point in time.
Assumption is that the state refers to a single physical input device,
ie InputDevice field is a single value of EInputDevices and not a combination.

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InputState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alt_key_down`` (bool):  [Read-Write] Is they keyboard ALT modifier key currently pressed down
- ``cmd_key_down`` (bool):  [Read-Write] Is they keyboard CMD modifier key currently pressed down (only on Apple devices)
- ``ctrl_key_down`` (bool):  [Read-Write] Is they keyboard CTRL modifier key currently pressed down
- ``input_device`` (InputDevices):  [Read-Write] Which InputDevice member is valid in this state
- ``keyboard`` (KeyboardInputDeviceState):  [Read-Write] Current state of Keyboard device, if InputDevice == EInputDevices::Keyboard
- ``mouse`` (MouseInputDeviceState):  [Read-Write] Current state of Mouse device, if InputDevice == EInputDevices::Mouse
- ``shift_key_down`` (bool):  [Read-Write] Is they keyboard SHIFT modifier key currently pressed down

<a id="unreal.InputDeviceState.__init__"></a>

#### __init__

```python
def __init__(
    input_device: InputDevices = InputDevices.NONE,
    shift_key_down: bool = False,
    alt_key_down: bool = False,
    ctrl_key_down: bool = False,
    cmd_key_down: bool = False,
    keyboard: KeyboardInputDeviceState = [[[], False, False, False, False]],
    mouse: MouseInputDeviceState = [[[], False, False, False, False],
                                    [[], False, False, False, False],
                                    [[], False, False, False, False], 0.000000,
                                    [0.000000, 0.000000], [0.000000, 0.000000],
                                    [[0.000000, 0.000000, 0.000000],
                                     [0.000000, 0.000000, 1.000000]]]
) -> None
```

<a id="unreal.InputDeviceState.input_device"></a>

#### input_device

```python
@property
def input_device() -> InputDevices
```

(InputDevices):  [Read-Write] Which InputDevice member is valid in this state

<a id="unreal.InputDeviceState.input_device"></a>

#### input_device

```python
@input_device.setter
def input_device(value: InputDevices) -> None
```

<a id="unreal.InputDeviceState.shift_key_down"></a>

#### shift_key_down

```python
@property
def shift_key_down() -> bool
```

(bool):  [Read-Write] Is they keyboard SHIFT modifier key currently pressed down

<a id="unreal.InputDeviceState.shift_key_down"></a>

#### shift_key_down

```python
@shift_key_down.setter
def shift_key_down(value: bool) -> None
```

<a id="unreal.InputDeviceState.alt_key_down"></a>

#### alt_key_down

```python
@property
def alt_key_down() -> bool
```

(bool):  [Read-Write] Is they keyboard ALT modifier key currently pressed down

<a id="unreal.InputDeviceState.alt_key_down"></a>

#### alt_key_down

```python
@alt_key_down.setter
def alt_key_down(value: bool) -> None
```

<a id="unreal.InputDeviceState.ctrl_key_down"></a>

#### ctrl_key_down

```python
@property
def ctrl_key_down() -> bool
```

(bool):  [Read-Write] Is they keyboard CTRL modifier key currently pressed down

<a id="unreal.InputDeviceState.ctrl_key_down"></a>

#### ctrl_key_down

```python
@ctrl_key_down.setter
def ctrl_key_down(value: bool) -> None
```

<a id="unreal.InputDeviceState.cmd_key_down"></a>

#### cmd_key_down

```python
@property
def cmd_key_down() -> bool
```

(bool):  [Read-Write] Is they keyboard CMD modifier key currently pressed down (only on Apple devices)

<a id="unreal.InputDeviceState.cmd_key_down"></a>

#### cmd_key_down

```python
@cmd_key_down.setter
def cmd_key_down(value: bool) -> None
```

<a id="unreal.InputDeviceState.keyboard"></a>

#### keyboard

```python
@property
def keyboard() -> KeyboardInputDeviceState
```

(KeyboardInputDeviceState):  [Read-Write] Current state of Keyboard device, if InputDevice == EInputDevices::Keyboard

<a id="unreal.InputDeviceState.keyboard"></a>

#### keyboard

```python
@keyboard.setter
def keyboard(value: KeyboardInputDeviceState) -> None
```

<a id="unreal.InputDeviceState.mouse"></a>

#### mouse

```python
@property
def mouse() -> MouseInputDeviceState
```

(MouseInputDeviceState):  [Read-Write] Current state of Mouse device, if InputDevice == EInputDevices::Mouse

<a id="unreal.InputDeviceState.mouse"></a>

#### mouse

```python
@mouse.setter
def mouse(value: MouseInputDeviceState) -> None
```

<a id="unreal.InputDeviceRay"></a>