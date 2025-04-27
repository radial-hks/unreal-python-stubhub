## ActivateDevicePropertyParams Objects

```python
class ActivateDevicePropertyParams(StructBase)
```

Parameters for the UInputDeviceSubsystem::ActivateDeviceProperty function

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_id`` (InputDeviceId):  [Read-Write] The Input Device that should receive the device property. If nothing is specified here,
  then the Platform User's default input device will be used.

  The default input device is obtained from IPlatformInputDeviceMapper::GetPrimaryInputDeviceForUser
- ``ignore_time_dilation`` (bool):  [Read-Write] If true, then this device property will ignore dilated delta time and use the Applications delta time instead
- ``looping`` (bool):  [Read-Write] If true, then the input device property will not be removed after it's evaluation time has completed.
  Instead, it will remain active until manually removed with a RemoveDeviceProperty call.
- ``play_while_paused`` (bool):  [Read-Write] If true, then this device property will be played even if the game world is paused.
- ``user_id`` (PlatformUserId):  [Read-Write] The Platform User whose device's should receive the device property

<a id="unreal.ActivateDevicePropertyParams.__init__"></a>

#### __init__

```python
def __init__(user_id: PlatformUserId = [],
             device_id: InputDeviceId = [],
             looping: bool = False,
             ignore_time_dilation: bool = False,
             play_while_paused: bool = False) -> None
```

<a id="unreal.ActivateDevicePropertyParams.user_id"></a>

#### user_id

```python
@property
def user_id() -> PlatformUserId
```

(PlatformUserId):  [Read-Write] The Platform User whose device's should receive the device property

<a id="unreal.ActivateDevicePropertyParams.user_id"></a>

#### user_id

```python
@user_id.setter
def user_id(value: PlatformUserId) -> None
```

<a id="unreal.ActivateDevicePropertyParams.device_id"></a>

#### device_id

```python
@property
def device_id() -> InputDeviceId
```

(InputDeviceId):  [Read-Write] The Input Device that should receive the device property. If nothing is specified here,
then the Platform User's default input device will be used.

The default input device is obtained from IPlatformInputDeviceMapper::GetPrimaryInputDeviceForUser

<a id="unreal.ActivateDevicePropertyParams.device_id"></a>

#### device_id

```python
@device_id.setter
def device_id(value: InputDeviceId) -> None
```

<a id="unreal.ActivateDevicePropertyParams.looping"></a>

#### looping

```python
@property
def looping() -> bool
```

(bool):  [Read-Write] If true, then the input device property will not be removed after it's evaluation time has completed.
Instead, it will remain active until manually removed with a RemoveDeviceProperty call.

<a id="unreal.ActivateDevicePropertyParams.looping"></a>

#### looping

```python
@looping.setter
def looping(value: bool) -> None
```

<a id="unreal.ActivateDevicePropertyParams.ignore_time_dilation"></a>

#### ignore_time_dilation

```python
@property
def ignore_time_dilation() -> bool
```

(bool):  [Read-Write] If true, then this device property will ignore dilated delta time and use the Applications delta time instead

<a id="unreal.ActivateDevicePropertyParams.ignore_time_dilation"></a>

#### ignore_time_dilation

```python
@ignore_time_dilation.setter
def ignore_time_dilation(value: bool) -> None
```

<a id="unreal.ActivateDevicePropertyParams.play_while_paused"></a>

#### play_while_paused

```python
@property
def play_while_paused() -> bool
```

(bool):  [Read-Write] If true, then this device property will be played even if the game world is paused.

<a id="unreal.ActivateDevicePropertyParams.play_while_paused"></a>

#### play_while_paused

```python
@play_while_paused.setter
def play_while_paused(value: bool) -> None
```

<a id="unreal.SetDevicePropertyParams"></a>