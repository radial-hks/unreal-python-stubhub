## DeviceButtonState Objects

```python
class DeviceButtonState(StructBase)
```

Current State of a physical device button (mouse, key, etc) at a point in time.
Each "click" of a button should involve at minimum two separate state
events, one where bPressed=true and one where bReleased=true.
Each of these states should occur only once.
In addition there may be additional frames where the button is
held down and bDown=true and bPressed=false.

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InputState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``button`` (Key):  [Read-Write] Button identifier
- ``double_clicked`` (bool):  [Read-Write] Was the button double clicked this frame. This should happen only once per "double click"
- ``down`` (bool):  [Read-Write] Is the button currently pressed down. This should be true every frame the button is pressed.
- ``pressed`` (bool):  [Read-Write] Was the button pressed down this frame. This should happen once per "click"
- ``released`` (bool):  [Read-Write] Was the button released this frame. This should happen once per "click"

<a id="unreal.DeviceButtonState.__init__"></a>

#### __init__

```python
def __init__(button: Key = [],
             pressed: bool = False,
             down: bool = False,
             released: bool = False,
             double_clicked: bool = False) -> None
```

<a id="unreal.DeviceButtonState.button"></a>

#### button

```python
@property
def button() -> Key
```

(Key):  [Read-Write] Button identifier

<a id="unreal.DeviceButtonState.button"></a>

#### button

```python
@button.setter
def button(value: Key) -> None
```

<a id="unreal.DeviceButtonState.pressed"></a>

#### pressed

```python
@property
def pressed() -> bool
```

(bool):  [Read-Write] Was the button pressed down this frame. This should happen once per "click"

<a id="unreal.DeviceButtonState.pressed"></a>

#### pressed

```python
@pressed.setter
def pressed(value: bool) -> None
```

<a id="unreal.DeviceButtonState.down"></a>

#### down

```python
@property
def down() -> bool
```

(bool):  [Read-Write] Is the button currently pressed down. This should be true every frame the button is pressed.

<a id="unreal.DeviceButtonState.down"></a>

#### down

```python
@down.setter
def down(value: bool) -> None
```

<a id="unreal.DeviceButtonState.released"></a>

#### released

```python
@property
def released() -> bool
```

(bool):  [Read-Write] Was the button released this frame. This should happen once per "click"

<a id="unreal.DeviceButtonState.released"></a>

#### released

```python
@released.setter
def released(value: bool) -> None
```

<a id="unreal.DeviceButtonState.double_clicked"></a>

#### double_clicked

```python
@property
def double_clicked() -> bool
```

(bool):  [Read-Write] Was the button double clicked this frame. This should happen only once per "double click"

<a id="unreal.DeviceButtonState.double_clicked"></a>

#### double_clicked

```python
@double_clicked.setter
def double_clicked(value: bool) -> None
```

<a id="unreal.KeyboardInputDeviceState"></a>