## SkyCreatorSkyLightSettings\_51 Objects

```python
class SkyCreatorSkyLightSettings_51(StructBase)
```

天光设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cloud_ambient_occlusion_strength`` (float):  [Read-Write] The strength of the ambient occlusion, higher value will block more light.
- ``cloud_ambient_occlusion_strength_curve`` (CurveFloat):  [Read-Write]
- ``intensity`` (float):  [Read-Write] Total energy that the light emits.
- ``intensity_curve`` (CurveFloat):  [Read-Write]
- ``light_color`` (LinearColor):  [Read-Write] Filter color of the light.
  Note that this can change the light's effective intensity.
- ``light_color_curve`` (CurveLinearColor):  [Read-Write]
- ``lower_hemisphere_color`` (LinearColor):  [Read-Write] Lower Hemisphere Color.
- ``lower_hemisphere_color_curve`` (CurveLinearColor):  [Read-Write]
- ``night_intensity`` (float):  [Read-Write] Energy that the light emits in the nights.
- ``night_intensity_curve`` (CurveFloat):  [Read-Write]
- ``use_cloud_ambient_occlusion_strength`` (bool):  [Read-Write]
- ``use_intensity`` (bool):  [Read-Write]
- ``use_light_color`` (bool):  [Read-Write]
- ``use_lower_hemisphere_color`` (bool):  [Read-Write]
- ``use_night_intensity`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        use_intensity: bool = False,
        intensity: float = 0.000000,
        intensity_curve: CurveFloat = None,
        use_night_intensity: bool = False,
        night_intensity: float = 0.000000,
        night_intensity_curve: CurveFloat = None,
        use_light_color: bool = False,
        light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        light_color_curve: CurveLinearColor = None,
        use_lower_hemisphere_color: bool = False,
        lower_hemisphere_color: LinearColor = [
            0.000000, 0.000000, 0.000000, 0.000000
        ],
        lower_hemisphere_color_curve: CurveLinearColor = None,
        use_cloud_ambient_occlusion_strength: bool = False,
        cloud_ambient_occlusion_strength: float = 0.000000,
        cloud_ambient_occlusion_strength_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.use_intensity"></a>

#### use\_intensity

```python
@property
def use_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.use_intensity"></a>

#### use\_intensity

```python
@use_intensity.setter
def use_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Write] Total energy that the light emits.

<a id="unreal.SkyCreatorSkyLightSettings_51.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.intensity_curve"></a>

#### intensity\_curve

```python
@property
def intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.intensity_curve"></a>

#### intensity\_curve

```python
@intensity_curve.setter
def intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.use_night_intensity"></a>

#### use\_night\_intensity

```python
@property
def use_night_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.use_night_intensity"></a>

#### use\_night\_intensity

```python
@use_night_intensity.setter
def use_night_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.night_intensity"></a>

#### night\_intensity

```python
@property
def night_intensity() -> float
```

(float):  [Read-Write] Energy that the light emits in the nights.

<a id="unreal.SkyCreatorSkyLightSettings_51.night_intensity"></a>

#### night\_intensity

```python
@night_intensity.setter
def night_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.night_intensity_curve"></a>

#### night\_intensity\_curve

```python
@property
def night_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.night_intensity_curve"></a>

#### night\_intensity\_curve

```python
@night_intensity_curve.setter
def night_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.use_light_color"></a>

#### use\_light\_color

```python
@property
def use_light_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.use_light_color"></a>

#### use\_light\_color

```python
@use_light_color.setter
def use_light_color(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.light_color"></a>

#### light\_color

```python
@property
def light_color() -> LinearColor
```

(LinearColor):  [Read-Write] Filter color of the light.
Note that this can change the light's effective intensity.

<a id="unreal.SkyCreatorSkyLightSettings_51.light_color"></a>

#### light\_color

```python
@light_color.setter
def light_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.light_color_curve"></a>

#### light\_color\_curve

```python
@property
def light_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.light_color_curve"></a>

#### light\_color\_curve

```python
@light_color_curve.setter
def light_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.use_lower_hemisphere_color"></a>

#### use\_lower\_hemisphere\_color

```python
@property
def use_lower_hemisphere_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.use_lower_hemisphere_color"></a>

#### use\_lower\_hemisphere\_color

```python
@use_lower_hemisphere_color.setter
def use_lower_hemisphere_color(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.lower_hemisphere_color"></a>

#### lower\_hemisphere\_color

```python
@property
def lower_hemisphere_color() -> LinearColor
```

(LinearColor):  [Read-Write] Lower Hemisphere Color.

<a id="unreal.SkyCreatorSkyLightSettings_51.lower_hemisphere_color"></a>

#### lower\_hemisphere\_color

```python
@lower_hemisphere_color.setter
def lower_hemisphere_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.lower_hemisphere_color_curve"></a>

#### lower\_hemisphere\_color\_curve

```python
@property
def lower_hemisphere_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.lower_hemisphere_color_curve"></a>

#### lower\_hemisphere\_color\_curve

```python
@lower_hemisphere_color_curve.setter
def lower_hemisphere_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.use_cloud_ambient_occlusion_strength"></a>

#### use\_cloud\_ambient\_occlusion\_strength

```python
@property
def use_cloud_ambient_occlusion_strength() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.use_cloud_ambient_occlusion_strength"></a>

#### use\_cloud\_ambient\_occlusion\_strength

```python
@use_cloud_ambient_occlusion_strength.setter
def use_cloud_ambient_occlusion_strength(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.cloud_ambient_occlusion_strength"></a>

#### cloud\_ambient\_occlusion\_strength

```python
@property
def cloud_ambient_occlusion_strength() -> float
```

(float):  [Read-Write] The strength of the ambient occlusion, higher value will block more light.

<a id="unreal.SkyCreatorSkyLightSettings_51.cloud_ambient_occlusion_strength"></a>

#### cloud\_ambient\_occlusion\_strength

```python
@cloud_ambient_occlusion_strength.setter
def cloud_ambient_occlusion_strength(value: float) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings_51.cloud_ambient_occlusion_strength_curve"></a>

#### cloud\_ambient\_occlusion\_strength\_curve

```python
@property
def cloud_ambient_occlusion_strength_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorSkyLightSettings_51.cloud_ambient_occlusion_strength_curve"></a>

#### cloud\_ambient\_occlusion\_strength\_curve

```python
@cloud_ambient_occlusion_strength_curve.setter
def cloud_ambient_occlusion_strength_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51"></a>