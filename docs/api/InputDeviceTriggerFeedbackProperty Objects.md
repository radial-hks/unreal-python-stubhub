## InputDeviceTriggerFeedbackProperty Objects

```python
class InputDeviceTriggerFeedbackProperty(InputDeviceTriggerEffect)
```

Sets simple trigger feedback

NOTE: This property has platform specific implementations and may behave differently per platform.
See the docs for more details on each platform.

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_trigger_data`` (DeviceTriggerBaseData):  [Read-Write]
- ``device_override_data`` (Map[Name, DeviceTriggerFeedbackData]):  [Read-Write] A map of device specific color data. If no overrides are specified, the Default hardware data will be used
- ``property_duration`` (float):  [Read-Only] The duration that this device property should last. Override this if your property has any dynamic curves
  to be the max time range.

  A duration of 0 means that the device property will be treated as a "One Shot" effect, being applied once
  before being removed by the Input Device Subsystem.
- ``trigger_data`` (DeviceTriggerFeedbackData):  [Read-Write] What position on the trigger that the feedback should be applied to over time (1-9)

<a id="unreal.InputDeviceTriggerFeedbackProperty.trigger_data"></a>

#### trigger_data

```python
@property
def trigger_data() -> DeviceTriggerFeedbackData
```

(DeviceTriggerFeedbackData):  [Read-Write] What position on the trigger that the feedback should be applied to over time (1-9)

<a id="unreal.InputDeviceTriggerFeedbackProperty.trigger_data"></a>

#### trigger_data

```python
@trigger_data.setter
def trigger_data(value: DeviceTriggerFeedbackData) -> None
```

<a id="unreal.InputDeviceTriggerFeedbackProperty.device_override_data"></a>

#### device_override_data

```python
@property
def device_override_data() -> Map[Name, DeviceTriggerFeedbackData]
```

(Map[Name, DeviceTriggerFeedbackData]):  [Read-Write] A map of device specific color data. If no overrides are specified, the Default hardware data will be used

<a id="unreal.InputDeviceTriggerFeedbackProperty.device_override_data"></a>

#### device_override_data

```python
@device_override_data.setter
def device_override_data(value: Map[Name, DeviceTriggerFeedbackData]) -> None
```

<a id="unreal.InputDeviceTriggerResistanceProperty"></a>