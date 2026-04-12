## KeyboardInputDeviceState Objects

```python
class KeyboardInputDeviceState(StructBase)
```

Current state of active keyboard key at a point in time
todo: would be useful to track set of active keys

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InputState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_key`` (DeviceButtonState):  [Read-Write] state of active key that was modified (ie press or release)

<a id="unreal.KeyboardInputDeviceState.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        active_key: DeviceButtonState = [[], False, False, False,
                                         False]) -> None
```

<a id="unreal.KeyboardInputDeviceState.active_key"></a>

#### active\_key

```python
@property
def active_key() -> DeviceButtonState
```

(DeviceButtonState):  [Read-Write] state of active key that was modified (ie press or release)

<a id="unreal.KeyboardInputDeviceState.active_key"></a>

#### active\_key

```python
@active_key.setter
def active_key(value: DeviceButtonState) -> None
```

<a id="unreal.MouseInputDeviceState"></a>