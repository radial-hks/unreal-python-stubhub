## InputDeviceAudioBasedVibrationProperty Objects

```python
class InputDeviceAudioBasedVibrationProperty(InputDeviceProperty)
```

Plays a sound to an input device's speaker. On platforms that support it, this sound will be played
in the form of a vibration where the left and right audio channels represent the left and right side
of the controller.

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data`` (AudioBasedVibrationData):  [Read-Write]
- ``device_override_data`` (Map[Name, AudioBasedVibrationData]):  [Read-Write] A map of device specific color data. If no overrides are specified, the Default hardware data will be used
- ``property_duration`` (float):  [Read-Only] The duration that this device property should last. Override this if your property has any dynamic curves
  to be the max time range.

  A duration of 0 means that the device property will be treated as a "One Shot" effect, being applied once
  before being removed by the Input Device Subsystem.

<a id="unreal.InputDeviceAudioBasedVibrationProperty.data"></a>

#### data

```python
@property
def data() -> AudioBasedVibrationData
```

(AudioBasedVibrationData):  [Read-Write]

<a id="unreal.InputDeviceAudioBasedVibrationProperty.data"></a>

#### data

```python
@data.setter
def data(value: AudioBasedVibrationData) -> None
```

<a id="unreal.InputDeviceAudioBasedVibrationProperty.device_override_data"></a>

#### device_override_data

```python
@property
def device_override_data() -> Map[Name, AudioBasedVibrationData]
```

(Map[Name, AudioBasedVibrationData]):  [Read-Write] A map of device specific color data. If no overrides are specified, the Default hardware data will be used

<a id="unreal.InputDeviceAudioBasedVibrationProperty.device_override_data"></a>

#### device_override_data

```python
@device_override_data.setter
def device_override_data(value: Map[Name, AudioBasedVibrationData]) -> None
```

<a id="unreal.InputDeviceSubsystem"></a>