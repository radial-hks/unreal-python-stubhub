## DeviceColorData Objects

```python
class DeviceColorData(StructBase)
```

Data required for setting the Input Device Color

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable`` (bool):  [Read-Write] True if the light should be enabled at all
- ``light_color`` (Color):  [Read-Write] The color to set the light on
- ``reset_after_completion`` (bool):  [Read-Write] If true, the light color will be reset to "off" after this property has been evaluated.

<a id="unreal.DeviceColorData.__init__"></a>

#### __init__

```python
def __init__(enable: bool = False,
             reset_after_completion: bool = False,
             light_color: Color = [0, 0, 0, 0]) -> None
```

<a id="unreal.DeviceColorData.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] True if the light should be enabled at all

<a id="unreal.DeviceColorData.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DeviceColorData.reset_after_completion"></a>

#### reset_after_completion

```python
@property
def reset_after_completion() -> bool
```

(bool):  [Read-Write] If true, the light color will be reset to "off" after this property has been evaluated.

<a id="unreal.DeviceColorData.reset_after_completion"></a>

#### reset_after_completion

```python
@reset_after_completion.setter
def reset_after_completion(value: bool) -> None
```

<a id="unreal.DeviceColorData.light_color"></a>

#### light_color

```python
@property
def light_color() -> Color
```

(Color):  [Read-Write] The color to set the light on

<a id="unreal.DeviceColorData.light_color"></a>

#### light_color

```python
@light_color.setter
def light_color(value: Color) -> None
```

<a id="unreal.DeviceColorCurveData"></a>