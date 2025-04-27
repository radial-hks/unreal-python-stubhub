## DisplayClusterConfigurationViewport_ColorGradingMiscSettings Objects

```python
class DisplayClusterConfigurationViewport_ColorGradingMiscSettings(StructBase)
```

Display Cluster Configuration Viewport Color Grading Misc Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blue_correction`` (float):  [Read-Write] Correct for artifacts with "electric" blues due to the ACEScg color space. Bright blue desaturates instead of going to violet.
- ``expand_gamut`` (float):  [Read-Write] Expand bright saturated colors outside the sRGB gamut to fake wide gamut rendering.
- ``override_blue_correction`` (bool):  [Read-Write]
- ``override_expand_gamut`` (bool):  [Read-Write]
- ``override_scene_color_tint`` (bool):  [Read-Write]
- ``scene_color_tint`` (LinearColor):  [Read-Write] Scene tint color

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.__init__"></a>

#### __init__

```python
def __init__(
    override_blue_correction: bool = False,
    override_expand_gamut: bool = False,
    override_scene_color_tint: bool = False,
    blue_correction: float = 0.000000,
    expand_gamut: float = 0.000000,
    scene_color_tint: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.override_blue_correction"></a>

#### override_blue_correction

```python
@property
def override_blue_correction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.override_blue_correction"></a>

#### override_blue_correction

```python
@override_blue_correction.setter
def override_blue_correction(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.override_expand_gamut"></a>

#### override_expand_gamut

```python
@property
def override_expand_gamut() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.override_expand_gamut"></a>

#### override_expand_gamut

```python
@override_expand_gamut.setter
def override_expand_gamut(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.override_scene_color_tint"></a>

#### override_scene_color_tint

```python
@property
def override_scene_color_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.override_scene_color_tint"></a>

#### override_scene_color_tint

```python
@override_scene_color_tint.setter
def override_scene_color_tint(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.blue_correction"></a>

#### blue_correction

```python
@property
def blue_correction() -> float
```

(float):  [Read-Write] Correct for artifacts with "electric" blues due to the ACEScg color space. Bright blue desaturates instead of going to violet.

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.blue_correction"></a>

#### blue_correction

```python
@blue_correction.setter
def blue_correction(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.expand_gamut"></a>

#### expand_gamut

```python
@property
def expand_gamut() -> float
```

(float):  [Read-Write] Expand bright saturated colors outside the sRGB gamut to fake wide gamut rendering.

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.expand_gamut"></a>

#### expand_gamut

```python
@expand_gamut.setter
def expand_gamut(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.scene_color_tint"></a>

#### scene_color_tint

```python
@property
def scene_color_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Scene tint color

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings.scene_color_tint"></a>

#### scene_color_tint

```python
@scene_color_tint.setter
def scene_color_tint(value: LinearColor) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingSettings"></a>