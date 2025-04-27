## DeviceTriggerTriggerVibrationData Objects

```python
class DeviceTriggerTriggerVibrationData(StructBase)
```

UInputDeviceTriggerVibrationProperty

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``trigger_position_curve`` (CurveFloat):  [Read-Write] What position on the trigger that the feedback should be applied to over time (1-9)
- ``vibration_amplitude_curve`` (CurveFloat):  [Read-Write] The amplitude of the vibration
- ``vibration_frequency_curve`` (CurveFloat):  [Read-Write] The frequency of the vibration

<a id="unreal.DeviceTriggerTriggerVibrationData.__init__"></a>

#### __init__

```python
def __init__(trigger_position_curve: CurveFloat = None,
             vibration_frequency_curve: CurveFloat = None,
             vibration_amplitude_curve: CurveFloat = None) -> None
```

<a id="unreal.DeviceTriggerTriggerVibrationData.trigger_position_curve"></a>

#### trigger_position_curve

```python
@property
def trigger_position_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] What position on the trigger that the feedback should be applied to over time (1-9)

<a id="unreal.DeviceTriggerTriggerVibrationData.trigger_position_curve"></a>

#### trigger_position_curve

```python
@trigger_position_curve.setter
def trigger_position_curve(value: CurveFloat) -> None
```

<a id="unreal.DeviceTriggerTriggerVibrationData.vibration_frequency_curve"></a>

#### vibration_frequency_curve

```python
@property
def vibration_frequency_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] The frequency of the vibration

<a id="unreal.DeviceTriggerTriggerVibrationData.vibration_frequency_curve"></a>

#### vibration_frequency_curve

```python
@vibration_frequency_curve.setter
def vibration_frequency_curve(value: CurveFloat) -> None
```

<a id="unreal.DeviceTriggerTriggerVibrationData.vibration_amplitude_curve"></a>

#### vibration_amplitude_curve

```python
@property
def vibration_amplitude_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] The amplitude of the vibration

<a id="unreal.DeviceTriggerTriggerVibrationData.vibration_amplitude_curve"></a>

#### vibration_amplitude_curve

```python
@vibration_amplitude_curve.setter
def vibration_amplitude_curve(value: CurveFloat) -> None
```

<a id="unreal.AudioBasedVibrationData"></a>