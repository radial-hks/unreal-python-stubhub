## DisplayClusterConfigurationViewport_ColorGradingSettings Objects

```python
class DisplayClusterConfigurationViewport_ColorGradingSettings(StructBase)
```

Display Cluster Configuration Viewport Color Grading Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``contrast`` (Vector4):  [Read-Write] Contrast
- ``gain`` (Vector4):  [Read-Write] Gain
- ``gamma`` (Vector4):  [Read-Write] Gamma
- ``offset`` (Vector4):  [Read-Write] Offset
- ``override_contrast`` (bool):  [Read-Write]
- ``override_gain`` (bool):  [Read-Write]
- ``override_gamma`` (bool):  [Read-Write]
- ``override_offset`` (bool):  [Read-Write]
- ``override_saturation`` (bool):  [Read-Write]
- ``saturation`` (Vector4):  [Read-Write] Saturation

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.__init__"></a>

#### __init__

```python
def __init__(
        override_saturation: bool = False,
        override_contrast: bool = False,
        override_gamma: bool = False,
        override_gain: bool = False,
        override_offset: bool = False,
        saturation: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        contrast: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        gamma: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        gain: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000],
        offset: Vector4 = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_saturation"></a>

#### override_saturation

```python
@property
def override_saturation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_saturation"></a>

#### override_saturation

```python
@override_saturation.setter
def override_saturation(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_contrast"></a>

#### override_contrast

```python
@property
def override_contrast() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_contrast"></a>

#### override_contrast

```python
@override_contrast.setter
def override_contrast(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_gamma"></a>

#### override_gamma

```python
@property
def override_gamma() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_gamma"></a>

#### override_gamma

```python
@override_gamma.setter
def override_gamma(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_gain"></a>

#### override_gain

```python
@property
def override_gain() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_gain"></a>

#### override_gain

```python
@override_gain.setter
def override_gain(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_offset"></a>

#### override_offset

```python
@property
def override_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.override_offset"></a>

#### override_offset

```python
@override_offset.setter
def override_offset(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.saturation"></a>

#### saturation

```python
@property
def saturation() -> Vector4
```

(Vector4):  [Read-Write] Saturation

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.saturation"></a>

#### saturation

```python
@saturation.setter
def saturation(value: Vector4) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.contrast"></a>

#### contrast

```python
@property
def contrast() -> Vector4
```

(Vector4):  [Read-Write] Contrast

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.contrast"></a>

#### contrast

```python
@contrast.setter
def contrast(value: Vector4) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.gamma"></a>

#### gamma

```python
@property
def gamma() -> Vector4
```

(Vector4):  [Read-Write] Gamma

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.gamma"></a>

#### gamma

```python
@gamma.setter
def gamma(value: Vector4) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.gain"></a>

#### gain

```python
@property
def gain() -> Vector4
```

(Vector4):  [Read-Write] Gain

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.gain"></a>

#### gain

```python
@gain.setter
def gain(value: Vector4) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.offset"></a>

#### offset

```python
@property
def offset() -> Vector4
```

(Vector4):  [Read-Write] Offset

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector4) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings"></a>