## PlatformInputDeviceState Objects

```python
class PlatformInputDeviceState(StructBase)
```

Data about an input device's current state

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``connection_state`` (InputDeviceConnectionState):  [Read-Only] The connection state of this input device
- ``owning_platform_user`` (PlatformUserId):  [Read-Only] The platform user that this input device belongs to

<a id="unreal.PlatformInputDeviceState.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    owning_platform_user: PlatformUserId = [],
    connection_state: InputDeviceConnectionState = InputDeviceConnectionState.
    INVALID
) -> None
```

<a id="unreal.PlatformInputDeviceState.owning_platform_user"></a>

#### owning\_platform\_user

```python
@property
def owning_platform_user() -> PlatformUserId
```

(PlatformUserId):  [Read-Only] The platform user that this input device belongs to

<a id="unreal.PlatformInputDeviceState.connection_state"></a>

#### connection\_state

```python
@property
def connection_state() -> InputDeviceConnectionState
```

(InputDeviceConnectionState):  [Read-Only] The connection state of this input device

<a id="unreal.PlatformUserId"></a>