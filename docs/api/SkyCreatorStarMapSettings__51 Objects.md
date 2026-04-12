## SkyCreatorStarMapSettings\_51 Objects

```python
class SkyCreatorStarMapSettings_51(StructBase)
```

星光贴图

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``night_horizon_color`` (LinearColor):  [Read-Write] Color tint of the horizon.
- ``night_horizon_color_curve`` (CurveLinearColor):  [Read-Write] FLinearColor(0.039463f, 0.050910f, 0.072917f)
- ``night_zenith_color`` (LinearColor):  [Read-Write] Color tint of the zenith.
- ``night_zenith_color_curve`` (CurveLinearColor):  [Read-Write] FLinearColor(0.003460f, 0.005858f, 0.01f)
- ``star_map_atmosphere_threshold`` (float):  [Read-Write] Indicates how strong the star map can be faded into atmosphere.
  Lower values cause more stars appear at brighter points in atmosphere, e.g. at daytime.
- ``star_map_atmosphere_threshold_curve`` (CurveFloat):  [Read-Write]
- ``star_map_color_tint`` (LinearColor):  [Read-Write] Overall color tint of the Star Map.
- ``star_map_color_tint_curve`` (CurveLinearColor):  [Read-Write]
- ``star_map_horizon_threshold`` (float):  [Read-Write] Indicates how strong the star map can be faded into horizon.
  Lower values cause more stars appear at horizon.
- ``star_map_horizon_threshold_curve`` (CurveFloat):  [Read-Write]
- ``star_map_intensity`` (float):  [Read-Write] Overall brightness of the Star Map.
- ``star_map_intensity_curve`` (CurveFloat):  [Read-Write]
- ``star_map_twinkle_intensity`` (float):  [Read-Write] Intensity of twinkling stars.
- ``star_map_twinkle_intensity_curve`` (CurveFloat):  [Read-Write]
- ``star_map_twinkle_saturation`` (float):  [Read-Write] Saturation of twinkling stars.
- ``star_map_twinkle_saturation_curve`` (CurveFloat):  [Read-Write]
- ``star_map_twinkle_speed`` (float):  [Read-Write] Twinkle speed of stars.
- ``star_map_twinkle_speed_curve`` (CurveFloat):  [Read-Write]
- ``use_night_horizon_color`` (bool):  [Read-Write]
- ``use_night_zenith_color`` (bool):  [Read-Write]
- ``use_star_map_atmosphere_threshold`` (bool):  [Read-Write]
- ``use_star_map_color_tint`` (bool):  [Read-Write]
- ``use_star_map_horizon_threshold`` (bool):  [Read-Write]
- ``use_star_map_intensity`` (bool):  [Read-Write]
- ``use_star_map_twinkle_intensity`` (bool):  [Read-Write]
- ``use_star_map_twinkle_saturation`` (bool):  [Read-Write]
- ``use_star_map_twinkle_speed`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_star_map_intensity: bool = False,
             star_map_intensity: float = 0.000000,
             star_map_intensity_curve: CurveFloat = None,
             use_star_map_color_tint: bool = False,
             star_map_color_tint: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             star_map_color_tint_curve: CurveLinearColor = None,
             use_star_map_twinkle_intensity: bool = False,
             star_map_twinkle_intensity: float = 0.000000,
             star_map_twinkle_intensity_curve: CurveFloat = None,
             use_star_map_twinkle_saturation: bool = False,
             star_map_twinkle_saturation: float = 0.000000,
             star_map_twinkle_saturation_curve: CurveFloat = None,
             use_star_map_twinkle_speed: bool = False,
             star_map_twinkle_speed: float = 0.000000,
             star_map_twinkle_speed_curve: CurveFloat = None,
             use_star_map_horizon_threshold: bool = False,
             star_map_horizon_threshold: float = 0.000000,
             star_map_horizon_threshold_curve: CurveFloat = None,
             use_star_map_atmosphere_threshold: bool = False,
             star_map_atmosphere_threshold: float = 0.000000,
             star_map_atmosphere_threshold_curve: CurveFloat = None,
             use_night_horizon_color: bool = False,
             night_horizon_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             night_horizon_color_curve: CurveLinearColor = None,
             use_night_zenith_color: bool = False,
             night_zenith_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             night_zenith_color_curve: CurveLinearColor = None) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_intensity"></a>

#### use\_star\_map\_intensity

```python
@property
def use_star_map_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_intensity"></a>

#### use\_star\_map\_intensity

```python
@use_star_map_intensity.setter
def use_star_map_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_intensity"></a>

#### star\_map\_intensity

```python
@property
def star_map_intensity() -> float
```

(float):  [Read-Write] Overall brightness of the Star Map.

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_intensity"></a>

#### star\_map\_intensity

```python
@star_map_intensity.setter
def star_map_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_intensity_curve"></a>

#### star\_map\_intensity\_curve

```python
@property
def star_map_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_intensity_curve"></a>

#### star\_map\_intensity\_curve

```python
@star_map_intensity_curve.setter
def star_map_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_color_tint"></a>

#### use\_star\_map\_color\_tint

```python
@property
def use_star_map_color_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_color_tint"></a>

#### use\_star\_map\_color\_tint

```python
@use_star_map_color_tint.setter
def use_star_map_color_tint(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_color_tint"></a>

#### star\_map\_color\_tint

```python
@property
def star_map_color_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Overall color tint of the Star Map.

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_color_tint"></a>

#### star\_map\_color\_tint

```python
@star_map_color_tint.setter
def star_map_color_tint(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_color_tint_curve"></a>

#### star\_map\_color\_tint\_curve

```python
@property
def star_map_color_tint_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_color_tint_curve"></a>

#### star\_map\_color\_tint\_curve

```python
@star_map_color_tint_curve.setter
def star_map_color_tint_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_intensity"></a>

#### use\_star\_map\_twinkle\_intensity

```python
@property
def use_star_map_twinkle_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_intensity"></a>

#### use\_star\_map\_twinkle\_intensity

```python
@use_star_map_twinkle_intensity.setter
def use_star_map_twinkle_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_intensity"></a>

#### star\_map\_twinkle\_intensity

```python
@property
def star_map_twinkle_intensity() -> float
```

(float):  [Read-Write] Intensity of twinkling stars.

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_intensity"></a>

#### star\_map\_twinkle\_intensity

```python
@star_map_twinkle_intensity.setter
def star_map_twinkle_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_intensity_curve"></a>

#### star\_map\_twinkle\_intensity\_curve

```python
@property
def star_map_twinkle_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_intensity_curve"></a>

#### star\_map\_twinkle\_intensity\_curve

```python
@star_map_twinkle_intensity_curve.setter
def star_map_twinkle_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_saturation"></a>

#### use\_star\_map\_twinkle\_saturation

```python
@property
def use_star_map_twinkle_saturation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_saturation"></a>

#### use\_star\_map\_twinkle\_saturation

```python
@use_star_map_twinkle_saturation.setter
def use_star_map_twinkle_saturation(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_saturation"></a>

#### star\_map\_twinkle\_saturation

```python
@property
def star_map_twinkle_saturation() -> float
```

(float):  [Read-Write] Saturation of twinkling stars.

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_saturation"></a>

#### star\_map\_twinkle\_saturation

```python
@star_map_twinkle_saturation.setter
def star_map_twinkle_saturation(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_saturation_curve"></a>

#### star\_map\_twinkle\_saturation\_curve

```python
@property
def star_map_twinkle_saturation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_saturation_curve"></a>

#### star\_map\_twinkle\_saturation\_curve

```python
@star_map_twinkle_saturation_curve.setter
def star_map_twinkle_saturation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_speed"></a>

#### use\_star\_map\_twinkle\_speed

```python
@property
def use_star_map_twinkle_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_twinkle_speed"></a>

#### use\_star\_map\_twinkle\_speed

```python
@use_star_map_twinkle_speed.setter
def use_star_map_twinkle_speed(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_speed"></a>

#### star\_map\_twinkle\_speed

```python
@property
def star_map_twinkle_speed() -> float
```

(float):  [Read-Write] Twinkle speed of stars.

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_speed"></a>

#### star\_map\_twinkle\_speed

```python
@star_map_twinkle_speed.setter
def star_map_twinkle_speed(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_speed_curve"></a>

#### star\_map\_twinkle\_speed\_curve

```python
@property
def star_map_twinkle_speed_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_twinkle_speed_curve"></a>

#### star\_map\_twinkle\_speed\_curve

```python
@star_map_twinkle_speed_curve.setter
def star_map_twinkle_speed_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_horizon_threshold"></a>

#### use\_star\_map\_horizon\_threshold

```python
@property
def use_star_map_horizon_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_horizon_threshold"></a>

#### use\_star\_map\_horizon\_threshold

```python
@use_star_map_horizon_threshold.setter
def use_star_map_horizon_threshold(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_horizon_threshold"></a>

#### star\_map\_horizon\_threshold

```python
@property
def star_map_horizon_threshold() -> float
```

(float):  [Read-Write] Indicates how strong the star map can be faded into horizon.
Lower values cause more stars appear at horizon.

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_horizon_threshold"></a>

#### star\_map\_horizon\_threshold

```python
@star_map_horizon_threshold.setter
def star_map_horizon_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_horizon_threshold_curve"></a>

#### star\_map\_horizon\_threshold\_curve

```python
@property
def star_map_horizon_threshold_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_horizon_threshold_curve"></a>

#### star\_map\_horizon\_threshold\_curve

```python
@star_map_horizon_threshold_curve.setter
def star_map_horizon_threshold_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_atmosphere_threshold"></a>

#### use\_star\_map\_atmosphere\_threshold

```python
@property
def use_star_map_atmosphere_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_star_map_atmosphere_threshold"></a>

#### use\_star\_map\_atmosphere\_threshold

```python
@use_star_map_atmosphere_threshold.setter
def use_star_map_atmosphere_threshold(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_atmosphere_threshold"></a>

#### star\_map\_atmosphere\_threshold

```python
@property
def star_map_atmosphere_threshold() -> float
```

(float):  [Read-Write] Indicates how strong the star map can be faded into atmosphere.
Lower values cause more stars appear at brighter points in atmosphere, e.g. at daytime.

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_atmosphere_threshold"></a>

#### star\_map\_atmosphere\_threshold

```python
@star_map_atmosphere_threshold.setter
def star_map_atmosphere_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_atmosphere_threshold_curve"></a>

#### star\_map\_atmosphere\_threshold\_curve

```python
@property
def star_map_atmosphere_threshold_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.star_map_atmosphere_threshold_curve"></a>

#### star\_map\_atmosphere\_threshold\_curve

```python
@star_map_atmosphere_threshold_curve.setter
def star_map_atmosphere_threshold_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_night_horizon_color"></a>

#### use\_night\_horizon\_color

```python
@property
def use_night_horizon_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_night_horizon_color"></a>

#### use\_night\_horizon\_color

```python
@use_night_horizon_color.setter
def use_night_horizon_color(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.night_horizon_color"></a>

#### night\_horizon\_color

```python
@property
def night_horizon_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color tint of the horizon.

<a id="unreal.SkyCreatorStarMapSettings_51.night_horizon_color"></a>

#### night\_horizon\_color

```python
@night_horizon_color.setter
def night_horizon_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.night_horizon_color_curve"></a>

#### night\_horizon\_color\_curve

```python
@property
def night_horizon_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] FLinearColor(0.039463f, 0.050910f, 0.072917f)

<a id="unreal.SkyCreatorStarMapSettings_51.night_horizon_color_curve"></a>

#### night\_horizon\_color\_curve

```python
@night_horizon_color_curve.setter
def night_horizon_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.use_night_zenith_color"></a>

#### use\_night\_zenith\_color

```python
@property
def use_night_zenith_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorStarMapSettings_51.use_night_zenith_color"></a>

#### use\_night\_zenith\_color

```python
@use_night_zenith_color.setter
def use_night_zenith_color(value: bool) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.night_zenith_color"></a>

#### night\_zenith\_color

```python
@property
def night_zenith_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color tint of the zenith.

<a id="unreal.SkyCreatorStarMapSettings_51.night_zenith_color"></a>

#### night\_zenith\_color

```python
@night_zenith_color.setter
def night_zenith_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorStarMapSettings_51.night_zenith_color_curve"></a>

#### night\_zenith\_color\_curve

```python
@property
def night_zenith_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] FLinearColor(0.003460f, 0.005858f, 0.01f)

<a id="unreal.SkyCreatorStarMapSettings_51.night_zenith_color_curve"></a>

#### night\_zenith\_color\_curve

```python
@night_zenith_color_curve.setter
def night_zenith_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51"></a>