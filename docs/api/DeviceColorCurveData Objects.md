## DeviceColorCurveData Objects

```python
class DeviceColorCurveData(StructBase)
```

Data required for setting the Input Device Color

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_color_curve`` (CurveLinearColor):  [Read-Write] The color the device light should be
- ``enable`` (bool):  [Read-Write] True if the light should be enabled at all
- ``reset_after_completion`` (bool):  [Read-Write] If true, the light color will be reset to "off" after the curve values are finished evaluating.

<a id="unreal.DeviceColorCurveData.__init__"></a>

#### __init__

```python
def __init__(enable: bool = False,
             reset_after_completion: bool = False,
             device_color_curve: CurveLinearColor = None) -> None
```

<a id="unreal.DeviceColorCurveData.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] True if the light should be enabled at all

<a id="unreal.DeviceColorCurveData.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DeviceColorCurveData.reset_after_completion"></a>

#### reset_after_completion

```python
@property
def reset_after_completion() -> bool
```

(bool):  [Read-Write] If true, the light color will be reset to "off" after the curve values are finished evaluating.

<a id="unreal.DeviceColorCurveData.reset_after_completion"></a>

#### reset_after_completion

```python
@reset_after_completion.setter
def reset_after_completion(value: bool) -> None
```

<a id="unreal.DeviceColorCurveData.device_color_curve"></a>

#### device_color_curve

```python
@property
def device_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] The color the device light should be

<a id="unreal.DeviceColorCurveData.device_color_curve"></a>

#### device_color_curve

```python
@device_color_curve.setter
def device_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.DeviceTriggerBaseData"></a>