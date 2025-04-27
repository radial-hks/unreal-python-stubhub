## InputDeviceTriggerEffect Objects

```python
class InputDeviceTriggerEffect(InputDeviceProperty)
```

A property that effect the triggers on a gamepad

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_trigger_data`` (DeviceTriggerBaseData):  [Read-Write]
- ``property_duration`` (float):  [Read-Only] The duration that this device property should last. Override this if your property has any dynamic curves
  to be the max time range.

  A duration of 0 means that the device property will be treated as a "One Shot" effect, being applied once
  before being removed by the Input Device Subsystem.

<a id="unreal.InputDeviceTriggerEffect.base_trigger_data"></a>

#### base_trigger_data

```python
@property
def base_trigger_data() -> DeviceTriggerBaseData
```

(DeviceTriggerBaseData):  [Read-Write]

<a id="unreal.InputDeviceTriggerEffect.base_trigger_data"></a>

#### base_trigger_data

```python
@base_trigger_data.setter
def base_trigger_data(value: DeviceTriggerBaseData) -> None
```

<a id="unreal.InputDeviceTriggerFeedbackProperty"></a>