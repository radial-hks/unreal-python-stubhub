## DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings Objects

```python
class DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings(
        StructBase)
```

Display Cluster Configuration Viewport Color Grading White Balance Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``override_temperature_type`` (bool):  [Read-Write]
- ``override_white_temp`` (bool):  [Read-Write]
- ``override_white_tint`` (bool):  [Read-Write]
- ``temperature_type`` (TemperatureMethod):  [Read-Write] Selects the type of temperature calculation.
  White Balance uses the Temperature value to control the virtual camera's White Balance. This is the default selection.
  Color Temperature uses the Temperature value to adjust the color temperature of the scene, which is the inverse of the White Balance operation.
- ``white_temp`` (float):  [Read-Write] White temperature
- ``white_tint`` (float):  [Read-Write] White tint

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.__init__"></a>

#### __init__

```python
def __init__(override_temperature_type: bool = False,
             override_white_temp: bool = False,
             override_white_tint: bool = False,
             temperature_type: TemperatureMethod = TemperatureMethod.
             TEMP_WHITE_BALANCE,
             white_temp: float = 0.000000,
             white_tint: float = 0.000000) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.override_temperature_type"></a>

#### override_temperature_type

```python
@property
def override_temperature_type() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.override_temperature_type"></a>

#### override_temperature_type

```python
@override_temperature_type.setter
def override_temperature_type(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.override_white_temp"></a>

#### override_white_temp

```python
@property
def override_white_temp() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.override_white_temp"></a>

#### override_white_temp

```python
@override_white_temp.setter
def override_white_temp(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.override_white_tint"></a>

#### override_white_tint

```python
@property
def override_white_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.override_white_tint"></a>

#### override_white_tint

```python
@override_white_tint.setter
def override_white_tint(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.temperature_type"></a>

#### temperature_type

```python
@property
def temperature_type() -> TemperatureMethod
```

(TemperatureMethod):  [Read-Write] Selects the type of temperature calculation.
White Balance uses the Temperature value to control the virtual camera's White Balance. This is the default selection.
Color Temperature uses the Temperature value to adjust the color temperature of the scene, which is the inverse of the White Balance operation.

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.temperature_type"></a>

#### temperature_type

```python
@temperature_type.setter
def temperature_type(value: TemperatureMethod) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.white_temp"></a>

#### white_temp

```python
@property
def white_temp() -> float
```

(float):  [Read-Write] White temperature

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.white_temp"></a>

#### white_temp

```python
@white_temp.setter
def white_temp(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.white_tint"></a>

#### white_tint

```python
@property
def white_tint() -> float
```

(float):  [Read-Write] White tint

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings.white_tint"></a>

#### white_tint

```python
@white_tint.setter
def white_tint(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_AllNodesColorGrading"></a>