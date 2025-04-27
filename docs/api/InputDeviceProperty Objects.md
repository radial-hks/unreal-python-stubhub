## InputDeviceProperty Objects

```python
class InputDeviceProperty(Object)
```

Base class that represents a single Input Device Property. An Input Device Property
represents a feature that can be set on an input device. Things like what color a
light is, advanced rumble patterns, or trigger haptics.

This top level object can then be evaluated at a specific time to create a lower level
FInputDeviceProperty, which the IInputInterface implementation can interpret however it desires.

The behavior of device properties can vary depending on the current platform. Some platforms may not
support certain device properties. An older gamepad may not have any advanced trigger haptics for
example.

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``property_duration`` (float):  [Read-Only] The duration that this device property should last. Override this if your property has any dynamic curves
  to be the max time range.

  A duration of 0 means that the device property will be treated as a "One Shot" effect, being applied once
  before being removed by the Input Device Subsystem.

<a id="unreal.InputDeviceProperty.property_duration"></a>

#### property_duration

```python
@property
def property_duration() -> float
```

(float):  [Read-Only] The duration that this device property should last. Override this if your property has any dynamic curves
to be the max time range.

A duration of 0 means that the device property will be treated as a "One Shot" effect, being applied once
before being removed by the Input Device Subsystem.

<a id="unreal.InputDeviceProperty.reset_device_property"></a>

#### reset_device_property

```python
def reset_device_property(platform_user: PlatformUserId,
                          device_id: InputDeviceId, force_reset: bool) -> None
```

x.reset_device_property(platform_user, device_id, force_reset) -> None
Reset the current device property. Provides an opportunity to reset device state after evaluation is complete.
If overriding in Blueprints, make sure to call the parent function!

Args:
    platform_user (PlatformUserId): The platform user that should receive this device property change
    device_id (InputDeviceId): 
    force_reset (bool):

<a id="unreal.InputDeviceProperty.evaluate_device_property"></a>

#### evaluate_device_property

```python
def evaluate_device_property(platform_user: PlatformUserId,
                             device_id: InputDeviceId, delta_time: float,
                             duration: float) -> None
```

x.evaluate_device_property(platform_user, device_id, delta_time, duration) -> None
Evaluate this device property for a given duration.
If overriding in Blueprints, make sure to call the parent function!

Args:
    platform_user (PlatformUserId): The platform user that should receive this device property change
    device_id (InputDeviceId): 
    delta_time (float): Delta time
    duration (float): The number of seconds that this property has been active. Use this to get things like curve data over time.

<a id="unreal.ColorInputDeviceProperty"></a>