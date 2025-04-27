## DisplayClusterConfigurationViewport_ColorGradingRenderingSettings Objects

```python
class DisplayClusterConfigurationViewport_ColorGradingRenderingSettings(
        StructBase)
```

Display Cluster Configuration Viewport Color Grading Rendering Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Postprocess.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_exposure_bias`` (float):  [Read-Write] Exposure compensation
- ``color_correction_highlights_max`` (float):  [Read-Write]
- ``color_correction_highlights_min`` (float):  [Read-Write]
- ``color_correction_shadows_max`` (float):  [Read-Write]
- ``global_`` (DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Global color grading
- ``highlights`` (DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Highlights color grading
- ``midtones`` (DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Midtones color grading
- ``misc`` (DisplayClusterConfigurationViewport_ColorGradingMiscSettings):  [Read-Write] Highlights color grading misc settings
- ``override_auto_exposure_bias`` (bool):  [Read-Write]
- ``override_color_correction_highlights_max`` (bool):  [Read-Write]
- ``override_color_correction_highlights_min`` (bool):  [Read-Write]
- ``override_color_correction_shadows_max`` (bool):  [Read-Write]
- ``shadows`` (DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Shadows color grading
- ``white_balance`` (DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings):  [Read-Write] White balance

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.__init__"></a>

#### __init__

```python
def __init__(
    override_auto_exposure_bias: bool = False,
    override_color_correction_highlights_min: bool = False,
    override_color_correction_highlights_max: bool = False,
    override_color_correction_shadows_max: bool = False,
    auto_exposure_bias: float = 0.000000,
    white_balance:
    DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings = [
        False, False, False, TemperatureMethod.TEMP_WHITE_BALANCE, 6500.000000,
        0.000000
    ],
    global_: DisplayClusterConfigurationViewport_ColorGradingSettings = [
        False, False, False, False, False,
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [0.000000, 0.000000, 0.000000, 0.000000]
    ],
    shadows: DisplayClusterConfigurationViewport_ColorGradingSettings = [
        False, False, False, False, False,
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [0.000000, 0.000000, 0.000000, 0.000000]
    ],
    color_correction_shadows_max: float = 0.000000,
    midtones: DisplayClusterConfigurationViewport_ColorGradingSettings = [
        False, False, False, False, False,
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [0.000000, 0.000000, 0.000000, 0.000000]
    ],
    highlights: DisplayClusterConfigurationViewport_ColorGradingSettings = [
        False, False, False, False, False,
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [0.000000, 0.000000, 0.000000, 0.000000]
    ],
    color_correction_highlights_min: float = 0.000000,
    color_correction_highlights_max: float = 0.000000,
    misc: DisplayClusterConfigurationViewport_ColorGradingMiscSettings = [
        False, False, False, 0.000000, 0.000000,
        [0.000000, 0.000000, 0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_auto_exposure_bias"></a>

#### override_auto_exposure_bias

```python
@property
def override_auto_exposure_bias() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_auto_exposure_bias"></a>

#### override_auto_exposure_bias

```python
@override_auto_exposure_bias.setter
def override_auto_exposure_bias(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_color_correction_highlights_min"></a>

#### override_color_correction_highlights_min

```python
@property
def override_color_correction_highlights_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_color_correction_highlights_min"></a>

#### override_color_correction_highlights_min

```python
@override_color_correction_highlights_min.setter
def override_color_correction_highlights_min(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_color_correction_highlights_max"></a>

#### override_color_correction_highlights_max

```python
@property
def override_color_correction_highlights_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_color_correction_highlights_max"></a>

#### override_color_correction_highlights_max

```python
@override_color_correction_highlights_max.setter
def override_color_correction_highlights_max(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_color_correction_shadows_max"></a>

#### override_color_correction_shadows_max

```python
@property
def override_color_correction_shadows_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.override_color_correction_shadows_max"></a>

#### override_color_correction_shadows_max

```python
@override_color_correction_shadows_max.setter
def override_color_correction_shadows_max(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.auto_exposure_bias"></a>

#### auto_exposure_bias

```python
@property
def auto_exposure_bias() -> float
```

(float):  [Read-Write] Exposure compensation

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.auto_exposure_bias"></a>

#### auto_exposure_bias

```python
@auto_exposure_bias.setter
def auto_exposure_bias(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.white_balance"></a>

#### white_balance

```python
@property
def white_balance(
) -> DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings
```

(DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings):  [Read-Write] White balance

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.white_balance"></a>

#### white_balance

```python
@white_balance.setter
def white_balance(
    value: DisplayClusterConfigurationViewport_ColorGradingWhiteBalanceSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.global_"></a>

#### global_

```python
@property
def global_() -> DisplayClusterConfigurationViewport_ColorGradingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Global color grading

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.global_"></a>

#### global_

```python
@global_.setter
def global_(
        value: DisplayClusterConfigurationViewport_ColorGradingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.shadows"></a>

#### shadows

```python
@property
def shadows() -> DisplayClusterConfigurationViewport_ColorGradingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Shadows color grading

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.shadows"></a>

#### shadows

```python
@shadows.setter
def shadows(
        value: DisplayClusterConfigurationViewport_ColorGradingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.color_correction_shadows_max"></a>

#### color_correction_shadows_max

```python
@property
def color_correction_shadows_max() -> float
```

(float):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.color_correction_shadows_max"></a>

#### color_correction_shadows_max

```python
@color_correction_shadows_max.setter
def color_correction_shadows_max(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.midtones"></a>

#### midtones

```python
@property
def midtones() -> DisplayClusterConfigurationViewport_ColorGradingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Midtones color grading

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.midtones"></a>

#### midtones

```python
@midtones.setter
def midtones(
        value: DisplayClusterConfigurationViewport_ColorGradingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.highlights"></a>

#### highlights

```python
@property
def highlights() -> DisplayClusterConfigurationViewport_ColorGradingSettings
```

(DisplayClusterConfigurationViewport_ColorGradingSettings):  [Read-Write] Highlights color grading

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.highlights"></a>

#### highlights

```python
@highlights.setter
def highlights(
        value: DisplayClusterConfigurationViewport_ColorGradingSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.color_correction_highlights_min"></a>

#### color_correction_highlights_min

```python
@property
def color_correction_highlights_min() -> float
```

(float):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.color_correction_highlights_min"></a>

#### color_correction_highlights_min

```python
@color_correction_highlights_min.setter
def color_correction_highlights_min(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.color_correction_highlights_max"></a>

#### color_correction_highlights_max

```python
@property
def color_correction_highlights_max() -> float
```

(float):  [Read-Write]

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.color_correction_highlights_max"></a>

#### color_correction_highlights_max

```python
@color_correction_highlights_max.setter
def color_correction_highlights_max(value: float) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.misc"></a>

#### misc

```python
@property
def misc() -> DisplayClusterConfigurationViewport_ColorGradingMiscSettings
```

(DisplayClusterConfigurationViewport_ColorGradingMiscSettings):  [Read-Write] Highlights color grading misc settings

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingRenderingSettings.misc"></a>

#### misc

```python
@misc.setter
def misc(
    value: DisplayClusterConfigurationViewport_ColorGradingMiscSettings
) -> None
```

<a id="unreal.DisplayClusterConfigurationViewport_ColorGradingMiscSettings"></a>