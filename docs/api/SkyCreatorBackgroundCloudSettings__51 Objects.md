## SkyCreatorBackgroundCloudSettings\_51 Objects

```python
class SkyCreatorBackgroundCloudSettings_51(StructBase)
```

卷积云设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_clouds_color_tint`` (LinearColor):  [Read-Write] Color Tint of Background Clouds.
- ``background_clouds_color_tint_curve`` (CurveLinearColor):  [Read-Write]
- ``background_clouds_intensity`` (float):  [Read-Write] Overall intensity of Background Clouds.
- ``background_clouds_intensity_curve`` (CurveFloat):  [Read-Write]
- ``background_clouds_layer_a`` (float):  [Read-Write] Amount of 'Layer A' in Background Clouds.
- ``background_clouds_layer_a_curve`` (CurveFloat):  [Read-Write]
- ``background_clouds_layer_b`` (float):  [Read-Write] Amount of 'Layer B' in Background Clouds.
- ``background_clouds_layer_b_curve`` (CurveFloat):  [Read-Write]
- ``background_clouds_layer_c`` (float):  [Read-Write] Amount of 'Layer C' in Background Clouds.
- ``background_clouds_layer_c_curve`` (CurveFloat):  [Read-Write]
- ``background_clouds_lightning_phase`` (float):  [Read-Write] Amount of Lightning Phase in Background Clouds.
- ``background_clouds_lightning_phase_curve`` (CurveFloat):  [Read-Write]
- ``use_background_clouds_color_tint`` (bool):  [Read-Write]
- ``use_background_clouds_intensity`` (bool):  [Read-Write]
- ``use_background_clouds_layer_a`` (bool):  [Read-Write]
- ``use_background_clouds_layer_b`` (bool):  [Read-Write]
- ``use_background_clouds_layer_c`` (bool):  [Read-Write]
- ``use_background_clouds_lightning_phase`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        use_background_clouds_intensity: bool = False,
        background_clouds_intensity: float = 0.000000,
        background_clouds_intensity_curve: CurveFloat = None,
        use_background_clouds_color_tint: bool = False,
        background_clouds_color_tint: LinearColor = [
            0.000000, 0.000000, 0.000000, 0.000000
        ],
        background_clouds_color_tint_curve: CurveLinearColor = None,
        use_background_clouds_layer_a: bool = False,
        background_clouds_layer_a: float = 0.000000,
        background_clouds_layer_a_curve: CurveFloat = None,
        use_background_clouds_layer_b: bool = False,
        background_clouds_layer_b: float = 0.000000,
        background_clouds_layer_b_curve: CurveFloat = None,
        use_background_clouds_layer_c: bool = False,
        background_clouds_layer_c: float = 0.000000,
        background_clouds_layer_c_curve: CurveFloat = None,
        use_background_clouds_lightning_phase: bool = False,
        background_clouds_lightning_phase: float = 0.000000,
        background_clouds_lightning_phase_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_intensity"></a>

#### use\_background\_clouds\_intensity

```python
@property
def use_background_clouds_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_intensity"></a>

#### use\_background\_clouds\_intensity

```python
@use_background_clouds_intensity.setter
def use_background_clouds_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_intensity"></a>

#### background\_clouds\_intensity

```python
@property
def background_clouds_intensity() -> float
```

(float):  [Read-Write] Overall intensity of Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_intensity"></a>

#### background\_clouds\_intensity

```python
@background_clouds_intensity.setter
def background_clouds_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_intensity_curve"></a>

#### background\_clouds\_intensity\_curve

```python
@property
def background_clouds_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_intensity_curve"></a>

#### background\_clouds\_intensity\_curve

```python
@background_clouds_intensity_curve.setter
def background_clouds_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_color_tint"></a>

#### use\_background\_clouds\_color\_tint

```python
@property
def use_background_clouds_color_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_color_tint"></a>

#### use\_background\_clouds\_color\_tint

```python
@use_background_clouds_color_tint.setter
def use_background_clouds_color_tint(value: bool) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_color_tint"></a>

#### background\_clouds\_color\_tint

```python
@property
def background_clouds_color_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Color Tint of Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_color_tint"></a>

#### background\_clouds\_color\_tint

```python
@background_clouds_color_tint.setter
def background_clouds_color_tint(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_color_tint_curve"></a>

#### background\_clouds\_color\_tint\_curve

```python
@property
def background_clouds_color_tint_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_color_tint_curve"></a>

#### background\_clouds\_color\_tint\_curve

```python
@background_clouds_color_tint_curve.setter
def background_clouds_color_tint_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_a"></a>

#### use\_background\_clouds\_layer\_a

```python
@property
def use_background_clouds_layer_a() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_a"></a>

#### use\_background\_clouds\_layer\_a

```python
@use_background_clouds_layer_a.setter
def use_background_clouds_layer_a(value: bool) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_a"></a>

#### background\_clouds\_layer\_a

```python
@property
def background_clouds_layer_a() -> float
```

(float):  [Read-Write] Amount of 'Layer A' in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_a"></a>

#### background\_clouds\_layer\_a

```python
@background_clouds_layer_a.setter
def background_clouds_layer_a(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_a_curve"></a>

#### background\_clouds\_layer\_a\_curve

```python
@property
def background_clouds_layer_a_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_a_curve"></a>

#### background\_clouds\_layer\_a\_curve

```python
@background_clouds_layer_a_curve.setter
def background_clouds_layer_a_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_b"></a>

#### use\_background\_clouds\_layer\_b

```python
@property
def use_background_clouds_layer_b() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_b"></a>

#### use\_background\_clouds\_layer\_b

```python
@use_background_clouds_layer_b.setter
def use_background_clouds_layer_b(value: bool) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_b"></a>

#### background\_clouds\_layer\_b

```python
@property
def background_clouds_layer_b() -> float
```

(float):  [Read-Write] Amount of 'Layer B' in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_b"></a>

#### background\_clouds\_layer\_b

```python
@background_clouds_layer_b.setter
def background_clouds_layer_b(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_b_curve"></a>

#### background\_clouds\_layer\_b\_curve

```python
@property
def background_clouds_layer_b_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_b_curve"></a>

#### background\_clouds\_layer\_b\_curve

```python
@background_clouds_layer_b_curve.setter
def background_clouds_layer_b_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_c"></a>

#### use\_background\_clouds\_layer\_c

```python
@property
def use_background_clouds_layer_c() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_layer_c"></a>

#### use\_background\_clouds\_layer\_c

```python
@use_background_clouds_layer_c.setter
def use_background_clouds_layer_c(value: bool) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_c"></a>

#### background\_clouds\_layer\_c

```python
@property
def background_clouds_layer_c() -> float
```

(float):  [Read-Write] Amount of 'Layer C' in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_c"></a>

#### background\_clouds\_layer\_c

```python
@background_clouds_layer_c.setter
def background_clouds_layer_c(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_c_curve"></a>

#### background\_clouds\_layer\_c\_curve

```python
@property
def background_clouds_layer_c_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_layer_c_curve"></a>

#### background\_clouds\_layer\_c\_curve

```python
@background_clouds_layer_c_curve.setter
def background_clouds_layer_c_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_lightning_phase"></a>

#### use\_background\_clouds\_lightning\_phase

```python
@property
def use_background_clouds_lightning_phase() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.use_background_clouds_lightning_phase"></a>

#### use\_background\_clouds\_lightning\_phase

```python
@use_background_clouds_lightning_phase.setter
def use_background_clouds_lightning_phase(value: bool) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_lightning_phase"></a>

#### background\_clouds\_lightning\_phase

```python
@property
def background_clouds_lightning_phase() -> float
```

(float):  [Read-Write] Amount of Lightning Phase in Background Clouds.

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_lightning_phase"></a>

#### background\_clouds\_lightning\_phase

```python
@background_clouds_lightning_phase.setter
def background_clouds_lightning_phase(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_lightning_phase_curve"></a>

#### background\_clouds\_lightning\_phase\_curve

```python
@property
def background_clouds_lightning_phase_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorBackgroundCloudSettings_51.background_clouds_lightning_phase_curve"></a>

#### background\_clouds\_lightning\_phase\_curve

```python
@background_clouds_lightning_phase_curve.setter
def background_clouds_lightning_phase_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51"></a>