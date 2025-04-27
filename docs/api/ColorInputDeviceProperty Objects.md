## ColorInputDeviceProperty Objects

```python
class ColorInputDeviceProperty(InputDeviceProperty)
```

Set the color of an Input Device to a static color. This will NOT reset the device color when the property
is done evaluating. You can think of this as a "One Shot" effect, where you set the device property color.

NOTE: This property has platform specific implementations and may behave differently per platform.
See the docs for more details on each platform.

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_data`` (DeviceColorData):  [Read-Write] Default color data that will be used by default. Device Specific overrides will be used when the current input device matches
- ``device_override_data`` (Map[Name, DeviceColorData]):  [Read-Write] A map of device specific color data. If no overrides are specified, the Default hardware data will be used
- ``property_duration`` (float):  [Read-Only] The duration that this device property should last. Override this if your property has any dynamic curves
  to be the max time range.

  A duration of 0 means that the device property will be treated as a "One Shot" effect, being applied once
  before being removed by the Input Device Subsystem.

<a id="unreal.ColorInputDeviceProperty.color_data"></a>

#### color_data

```python
@property
def color_data() -> DeviceColorData
```

(DeviceColorData):  [Read-Write] Default color data that will be used by default. Device Specific overrides will be used when the current input device matches

<a id="unreal.ColorInputDeviceProperty.color_data"></a>

#### color_data

```python
@color_data.setter
def color_data(value: DeviceColorData) -> None
```

<a id="unreal.ColorInputDeviceProperty.device_override_data"></a>

#### device_override_data

```python
@property
def device_override_data() -> Map[Name, DeviceColorData]
```

(Map[Name, DeviceColorData]):  [Read-Write] A map of device specific color data. If no overrides are specified, the Default hardware data will be used

<a id="unreal.ColorInputDeviceProperty.device_override_data"></a>

#### device_override_data

```python
@device_override_data.setter
def device_override_data(value: Map[Name, DeviceColorData]) -> None
```

<a id="unreal.ColorInputDeviceCurveProperty"></a>