## SkyCreatorWeatherFXSettings\_51 Objects

```python
class SkyCreatorWeatherFXSettings_51(StructBase)
```

天气特效设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_lightnings`` (bool):  [Read-Write] Whether to enable Lightnings.
- ``fog_amount`` (float):  [Read-Write] Rain Precipitation Amount.
- ``fog_amount_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_curve_frequency`` (float):  [Read-Write] Frequency of a Lightning Bolt curvature.
- ``lightning_bolt_curve_frequency_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_curve_strength_max`` (float):  [Read-Write] Maximum strength of a Lightning Bolt curvature.
- ``lightning_bolt_curve_strength_max_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_curve_strength_min`` (float):  [Read-Write] Minimum strength of a Lightning Bolt curvature.
- ``lightning_bolt_curve_strength_min_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_jitter_strength`` (float):  [Read-Write] Jitter strength of a Lightning Bolt.
- ``lightning_bolt_jitter_strength_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_length_max`` (float):  [Read-Write] Maximum length of a Lightning Bolt (in kilometers).
- ``lightning_bolt_length_max_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_length_min`` (float):  [Read-Write] Minimum length of a Lightning Bolt (in kilometers).
- ``lightning_bolt_length_min_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_spawn_chance`` (float):  [Read-Write] Chance of spawning a Lightning Bolt when spawning a Lightning.
- ``lightning_bolt_spawn_chance_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_width_max`` (float):  [Read-Write] Maximum width of a Lightning Bolt.
- ``lightning_bolt_width_max_curve`` (CurveFloat):  [Read-Write]
- ``lightning_bolt_width_min`` (float):  [Read-Write] Minimum width of a Lightning Bolt.
- ``lightning_bolt_width_min_curve`` (CurveFloat):  [Read-Write]
- ``lightning_branch_scale_max`` (float):  [Read-Write] Maximum scale of a Lightning Branch.
- ``lightning_branch_scale_max_curve`` (CurveFloat):  [Read-Write]
- ``lightning_branch_scale_min`` (float):  [Read-Write] Minimum scale of a Lightning Branch.
- ``lightning_branch_scale_min_curve`` (CurveFloat):  [Read-Write]
- ``lightning_branch_spawn_chance`` (float):  [Read-Write] Chance of spawning a Lightning Branch when spawning a Lightning Bolt.
- ``lightning_branch_spawn_chance_curve`` (CurveFloat):  [Read-Write]
- ``lightning_color_max`` (LinearColor):  [Read-Write] Maximum Lightning color.
- ``lightning_color_max_curve`` (CurveLinearColor):  [Read-Write]
- ``lightning_color_min`` (LinearColor):  [Read-Write] Minimum Lightning color.
- ``lightning_color_min_curve`` (CurveLinearColor):  [Read-Write]
- ``lightning_lifetime`` (float):  [Read-Write] Lightning lifetime in seconds.
- ``lightning_lifetime_curve`` (CurveFloat):  [Read-Write]
- ``lightning_spawn_interval_max`` (float):  [Read-Write] Maximum interval to randomly spawn Lightning in seconds.
- ``lightning_spawn_interval_max_curve`` (CurveFloat):  [Read-Write]
- ``lightning_spawn_interval_min`` (float):  [Read-Write] Minimum interval to randomly spawn Lightning in seconds.
- ``lightning_spawn_interval_min_curve`` (CurveFloat):  [Read-Write]
- ``rain_amount`` (float):  [Read-Write] Rain Precipitation Amount.
- ``rain_amount_curve`` (CurveFloat):  [Read-Write]
- ``rain_color`` (LinearColor):  [Read-Write] Rain Color.
- ``rain_color_curve`` (CurveLinearColor):  [Read-Write]
- ``rain_emissive`` (float):  [Read-Write] Rain Precipitation Amount.
- ``rain_emissive_curve`` (CurveFloat):  [Read-Write]
- ``rain_gravity`` (float):  [Read-Write] Gravity of a biggest sized raindrop.
- ``rain_gravity_curve`` (CurveFloat):  [Read-Write]
- ``rain_lifetime_max`` (float):  [Read-Write] Maximum lifetime of a single raindrop. Can affect the performance.
- ``rain_lifetime_max_curve`` (CurveFloat):  [Read-Write]
- ``rain_lifetime_min`` (float):  [Read-Write] Minimum lifetime of a single raindrop. Can affect the performance.
- ``rain_lifetime_min_curve`` (CurveFloat):  [Read-Write]
- ``rain_size_max`` (float):  [Read-Write] Maximum size of a single raindrop.
- ``rain_size_max_curve`` (CurveFloat):  [Read-Write]
- ``rain_size_min`` (float):  [Read-Write] Minimum size of a single raindrop.
- ``rain_size_min_curve`` (CurveFloat):  [Read-Write]
- ``rain_splash_lifetime_max`` (float):  [Read-Write] Maximum lifetime of a single rain splash. Can affect the performance.
- ``rain_splash_lifetime_max_curve`` (CurveFloat):  [Read-Write]
- ``rain_splash_lifetime_min`` (float):  [Read-Write] Minimum lifetime of a single rain splash. Can affect the performance.
- ``rain_splash_lifetime_min_curve`` (CurveFloat):  [Read-Write]
- ``rain_splash_size_max`` (Vector2D):  [Read-Write] Maximum size of a rain splash.
- ``rain_splash_size_max_curve`` (CurveVector):  [Read-Write]
- ``rain_splash_size_min`` (Vector2D):  [Read-Write] Minimum size of a rain splash.
- ``rain_splash_size_min_curve`` (CurveVector):  [Read-Write]
- ``rainbow_amount`` (float):  [Read-Write] Rainbow Amount.
- ``rainbow_amount_curve`` (CurveFloat):  [Read-Write]
- ``rainbow_color`` (LinearColor):  [Read-Write] Rainbow Tint Color.
- ``rainbow_color_curve`` (CurveLinearColor):  [Read-Write]
- ``rainbow_radius`` (float):  [Read-Write] Radius of the Rainbow.
- ``rainbow_radius_curve`` (CurveFloat):  [Read-Write]
- ``rainbow_thickness`` (float):  [Read-Write] Thickness of the Rainbow.
- ``rainbow_thickness_curve`` (CurveFloat):  [Read-Write]
- ``secondary_rainbow_color`` (LinearColor):  [Read-Write] Secondary Rainbow Tint Color.
- ``secondary_rainbow_color_curve`` (CurveLinearColor):  [Read-Write]
- ``secondary_rainbow_radius`` (float):  [Read-Write] Radius of the Secondary Rainbow.
- ``secondary_rainbow_radius_curve`` (CurveFloat):  [Read-Write]
- ``secondary_rainbow_thickness`` (float):  [Read-Write] Thickness of the Secondary Rainbow.
- ``secondary_rainbow_thickness_curve`` (CurveFloat):  [Read-Write]
- ``snow_amount`` (float):  [Read-Write] Snow Precipitation Amount.
- ``snow_amount_curve`` (CurveFloat):  [Read-Write]
- ``snow_color`` (LinearColor):  [Read-Write] Snow Color.
- ``snow_color_curve`` (CurveLinearColor):  [Read-Write]
- ``snow_emissive`` (float):  [Read-Write] Rain Precipitation Amount.
- ``snow_emissive_curve`` (CurveFloat):  [Read-Write]
- ``snow_gravity`` (float):  [Read-Write] Gravity of a biggest sized snowflake.
- ``snow_gravity_curve`` (CurveFloat):  [Read-Write]
- ``snow_lifetime_max`` (float):  [Read-Write] Maximum lifetime of a single snowflake. Can affect the performance.
- ``snow_lifetime_max_curve`` (CurveFloat):  [Read-Write]
- ``snow_lifetime_min`` (float):  [Read-Write] Minimum lifetime of a single snowflake. Can affect the performance.
- ``snow_lifetime_min_curve`` (CurveFloat):  [Read-Write]
- ``snow_size_max`` (float):  [Read-Write] Maximum size of a single snowflake.
- ``snow_size_max_curve`` (CurveFloat):  [Read-Write]
- ``snow_size_min`` (float):  [Read-Write] Minimum size of a single snowflake.
- ``snow_size_min_curve`` (CurveFloat):  [Read-Write]
- ``snow_turbulence`` (float):  [Read-Write] Snow turbulence.
- ``snow_turbulence_curve`` (CurveFloat):  [Read-Write]
- ``use_fog_amount`` (bool):  [Read-Write]
- ``use_lightning_bolt_curve_frequency`` (bool):  [Read-Write]
- ``use_lightning_bolt_curve_strength_max`` (bool):  [Read-Write]
- ``use_lightning_bolt_curve_strength_min`` (bool):  [Read-Write]
- ``use_lightning_bolt_jitter_strength`` (bool):  [Read-Write]
- ``use_lightning_bolt_length_max`` (bool):  [Read-Write]
- ``use_lightning_bolt_length_min`` (bool):  [Read-Write]
- ``use_lightning_bolt_spawn_chance`` (bool):  [Read-Write]
- ``use_lightning_bolt_width_max`` (bool):  [Read-Write]
- ``use_lightning_bolt_width_min`` (bool):  [Read-Write]
- ``use_lightning_branch_scale_max`` (bool):  [Read-Write]
- ``use_lightning_branch_scale_min`` (bool):  [Read-Write]
- ``use_lightning_branch_spawn_chance`` (bool):  [Read-Write]
- ``use_lightning_color_max`` (bool):  [Read-Write]
- ``use_lightning_color_min`` (bool):  [Read-Write]
- ``use_lightning_lifetime`` (bool):  [Read-Write]
- ``use_lightning_spawn_interval_max`` (bool):  [Read-Write]
- ``use_lightning_spawn_interval_min`` (bool):  [Read-Write]
- ``use_rain_amount`` (bool):  [Read-Write]
- ``use_rain_color`` (bool):  [Read-Write]
- ``use_rain_emissive`` (bool):  [Read-Write]
- ``use_rain_gravity`` (bool):  [Read-Write]
- ``use_rain_lifetime_max`` (bool):  [Read-Write]
- ``use_rain_lifetime_min`` (bool):  [Read-Write]
- ``use_rain_size_max`` (bool):  [Read-Write]
- ``use_rain_size_min`` (bool):  [Read-Write]
- ``use_rain_splash_lifetime_max`` (bool):  [Read-Write]
- ``use_rain_splash_lifetime_min`` (bool):  [Read-Write]
- ``use_rain_splash_size_max`` (bool):  [Read-Write]
- ``use_rain_splash_size_min`` (bool):  [Read-Write]
- ``use_rainbow_amount`` (bool):  [Read-Write]
- ``use_rainbow_color`` (bool):  [Read-Write]
- ``use_rainbow_radius`` (bool):  [Read-Write]
- ``use_rainbow_thickness`` (bool):  [Read-Write]
- ``use_secondary_rainbow_color`` (bool):  [Read-Write]
- ``use_secondary_rainbow_radius`` (bool):  [Read-Write]
- ``use_secondary_rainbow_thickness`` (bool):  [Read-Write]
- ``use_snow_amount`` (bool):  [Read-Write]
- ``use_snow_color`` (bool):  [Read-Write]
- ``use_snow_emissive`` (bool):  [Read-Write]
- ``use_snow_gravity`` (bool):  [Read-Write]
- ``use_snow_lifetime_max`` (bool):  [Read-Write]
- ``use_snow_lifetime_min`` (bool):  [Read-Write]
- ``use_snow_size_max`` (bool):  [Read-Write]
- ``use_snow_size_min`` (bool):  [Read-Write]
- ``use_snow_turbulence`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_rain_amount: bool = False,
             rain_amount: float = 0.000000,
             rain_amount_curve: CurveFloat = None,
             use_rain_color: bool = False,
             rain_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             rain_color_curve: CurveLinearColor = None,
             use_rain_gravity: bool = False,
             rain_gravity: float = 0.000000,
             rain_gravity_curve: CurveFloat = None,
             use_rain_lifetime_min: bool = False,
             rain_lifetime_min: float = 0.000000,
             rain_lifetime_min_curve: CurveFloat = None,
             use_rain_lifetime_max: bool = False,
             rain_lifetime_max: float = 0.000000,
             rain_lifetime_max_curve: CurveFloat = None,
             use_rain_size_min: bool = False,
             rain_size_min: float = 0.000000,
             rain_size_min_curve: CurveFloat = None,
             use_rain_size_max: bool = False,
             rain_size_max: float = 0.000000,
             rain_size_max_curve: CurveFloat = None,
             use_rain_emissive: bool = False,
             rain_emissive: float = 0.000000,
             rain_emissive_curve: CurveFloat = None,
             use_rain_splash_lifetime_min: bool = False,
             rain_splash_lifetime_min: float = 0.000000,
             rain_splash_lifetime_min_curve: CurveFloat = None,
             use_rain_splash_lifetime_max: bool = False,
             rain_splash_lifetime_max: float = 0.000000,
             rain_splash_lifetime_max_curve: CurveFloat = None,
             use_rain_splash_size_min: bool = False,
             rain_splash_size_min: Vector2D = [0.000000, 0.000000],
             rain_splash_size_min_curve: CurveVector = None,
             use_rain_splash_size_max: bool = False,
             rain_splash_size_max: Vector2D = [0.000000, 0.000000],
             rain_splash_size_max_curve: CurveVector = None,
             use_snow_amount: bool = False,
             snow_amount: float = 0.000000,
             snow_amount_curve: CurveFloat = None,
             use_snow_color: bool = False,
             snow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             snow_color_curve: CurveLinearColor = None,
             use_snow_gravity: bool = False,
             snow_gravity: float = 0.000000,
             snow_gravity_curve: CurveFloat = None,
             use_snow_turbulence: bool = False,
             snow_turbulence: float = 0.000000,
             snow_turbulence_curve: CurveFloat = None,
             use_snow_lifetime_min: bool = False,
             snow_lifetime_min: float = 0.000000,
             snow_lifetime_min_curve: CurveFloat = None,
             use_snow_lifetime_max: bool = False,
             snow_lifetime_max: float = 0.000000,
             snow_lifetime_max_curve: CurveFloat = None,
             use_snow_size_min: bool = False,
             snow_size_min: float = 0.000000,
             snow_size_min_curve: CurveFloat = None,
             use_snow_size_max: bool = False,
             snow_size_max: float = 0.000000,
             snow_size_max_curve: CurveFloat = None,
             use_snow_emissive: bool = False,
             snow_emissive: float = 0.000000,
             snow_emissive_curve: CurveFloat = None,
             use_fog_amount: bool = False,
             fog_amount: float = 0.000000,
             fog_amount_curve: CurveFloat = None,
             enable_lightnings: bool = False,
             use_lightning_spawn_interval_min: bool = False,
             lightning_spawn_interval_min: float = 0.000000,
             lightning_spawn_interval_min_curve: CurveFloat = None,
             use_lightning_spawn_interval_max: bool = False,
             lightning_spawn_interval_max: float = 0.000000,
             lightning_spawn_interval_max_curve: CurveFloat = None,
             use_lightning_color_min: bool = False,
             lightning_color_min: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             lightning_color_min_curve: CurveLinearColor = None,
             use_lightning_color_max: bool = False,
             lightning_color_max: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             lightning_color_max_curve: CurveLinearColor = None,
             use_lightning_lifetime: bool = False,
             lightning_lifetime: float = 0.000000,
             lightning_lifetime_curve: CurveFloat = None,
             use_lightning_bolt_spawn_chance: bool = False,
             lightning_bolt_spawn_chance: float = 0.000000,
             lightning_bolt_spawn_chance_curve: CurveFloat = None,
             use_lightning_bolt_width_min: bool = False,
             lightning_bolt_width_min: float = 0.000000,
             lightning_bolt_width_min_curve: CurveFloat = None,
             use_lightning_bolt_width_max: bool = False,
             lightning_bolt_width_max: float = 0.000000,
             lightning_bolt_width_max_curve: CurveFloat = None,
             use_lightning_bolt_length_min: bool = False,
             lightning_bolt_length_min: float = 0.000000,
             lightning_bolt_length_min_curve: CurveFloat = None,
             use_lightning_bolt_length_max: bool = False,
             lightning_bolt_length_max: float = 0.000000,
             lightning_bolt_length_max_curve: CurveFloat = None,
             use_lightning_bolt_curve_frequency: bool = False,
             lightning_bolt_curve_frequency: float = 0.000000,
             lightning_bolt_curve_frequency_curve: CurveFloat = None,
             use_lightning_bolt_curve_strength_min: bool = False,
             lightning_bolt_curve_strength_min: float = 0.000000,
             lightning_bolt_curve_strength_min_curve: CurveFloat = None,
             use_lightning_bolt_curve_strength_max: bool = False,
             lightning_bolt_curve_strength_max: float = 0.000000,
             lightning_bolt_curve_strength_max_curve: CurveFloat = None,
             use_lightning_bolt_jitter_strength: bool = False,
             lightning_bolt_jitter_strength: float = 0.000000,
             lightning_bolt_jitter_strength_curve: CurveFloat = None,
             use_lightning_branch_spawn_chance: bool = False,
             lightning_branch_spawn_chance: float = 0.000000,
             lightning_branch_spawn_chance_curve: CurveFloat = None,
             use_lightning_branch_scale_min: bool = False,
             lightning_branch_scale_min: float = 0.000000,
             lightning_branch_scale_min_curve: CurveFloat = None,
             use_lightning_branch_scale_max: bool = False,
             lightning_branch_scale_max: float = 0.000000,
             lightning_branch_scale_max_curve: CurveFloat = None,
             use_rainbow_amount: bool = False,
             rainbow_amount: float = 0.000000,
             rainbow_amount_curve: CurveFloat = None,
             use_rainbow_color: bool = False,
             rainbow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             rainbow_color_curve: CurveLinearColor = None,
             use_rainbow_radius: bool = False,
             rainbow_radius: float = 0.000000,
             rainbow_radius_curve: CurveFloat = None,
             use_rainbow_thickness: bool = False,
             rainbow_thickness: float = 0.000000,
             rainbow_thickness_curve: CurveFloat = None,
             use_secondary_rainbow_color: bool = False,
             secondary_rainbow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             secondary_rainbow_color_curve: CurveLinearColor = None,
             use_secondary_rainbow_radius: bool = False,
             secondary_rainbow_radius: float = 0.000000,
             secondary_rainbow_radius_curve: CurveFloat = None,
             use_secondary_rainbow_thickness: bool = False,
             secondary_rainbow_thickness: float = 0.000000,
             secondary_rainbow_thickness_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_amount"></a>

#### use\_rain\_amount

```python
@property
def use_rain_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_amount"></a>

#### use\_rain\_amount

```python
@use_rain_amount.setter
def use_rain_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_amount"></a>

#### rain\_amount

```python
@property
def rain_amount() -> float
```

(float):  [Read-Write] Rain Precipitation Amount.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_amount"></a>

#### rain\_amount

```python
@rain_amount.setter
def rain_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_amount_curve"></a>

#### rain\_amount\_curve

```python
@property
def rain_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_amount_curve"></a>

#### rain\_amount\_curve

```python
@rain_amount_curve.setter
def rain_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_color"></a>

#### use\_rain\_color

```python
@property
def use_rain_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_color"></a>

#### use\_rain\_color

```python
@use_rain_color.setter
def use_rain_color(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_color"></a>

#### rain\_color

```python
@property
def rain_color() -> LinearColor
```

(LinearColor):  [Read-Write] Rain Color.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_color"></a>

#### rain\_color

```python
@rain_color.setter
def rain_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_color_curve"></a>

#### rain\_color\_curve

```python
@property
def rain_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_color_curve"></a>

#### rain\_color\_curve

```python
@rain_color_curve.setter
def rain_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_gravity"></a>

#### use\_rain\_gravity

```python
@property
def use_rain_gravity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_gravity"></a>

#### use\_rain\_gravity

```python
@use_rain_gravity.setter
def use_rain_gravity(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_gravity"></a>

#### rain\_gravity

```python
@property
def rain_gravity() -> float
```

(float):  [Read-Write] Gravity of a biggest sized raindrop.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_gravity"></a>

#### rain\_gravity

```python
@rain_gravity.setter
def rain_gravity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_gravity_curve"></a>

#### rain\_gravity\_curve

```python
@property
def rain_gravity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_gravity_curve"></a>

#### rain\_gravity\_curve

```python
@rain_gravity_curve.setter
def rain_gravity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_lifetime_min"></a>

#### use\_rain\_lifetime\_min

```python
@property
def use_rain_lifetime_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_lifetime_min"></a>

#### use\_rain\_lifetime\_min

```python
@use_rain_lifetime_min.setter
def use_rain_lifetime_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_min"></a>

#### rain\_lifetime\_min

```python
@property
def rain_lifetime_min() -> float
```

(float):  [Read-Write] Minimum lifetime of a single raindrop. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_min"></a>

#### rain\_lifetime\_min

```python
@rain_lifetime_min.setter
def rain_lifetime_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_min_curve"></a>

#### rain\_lifetime\_min\_curve

```python
@property
def rain_lifetime_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_min_curve"></a>

#### rain\_lifetime\_min\_curve

```python
@rain_lifetime_min_curve.setter
def rain_lifetime_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_lifetime_max"></a>

#### use\_rain\_lifetime\_max

```python
@property
def use_rain_lifetime_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_lifetime_max"></a>

#### use\_rain\_lifetime\_max

```python
@use_rain_lifetime_max.setter
def use_rain_lifetime_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_max"></a>

#### rain\_lifetime\_max

```python
@property
def rain_lifetime_max() -> float
```

(float):  [Read-Write] Maximum lifetime of a single raindrop. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_max"></a>

#### rain\_lifetime\_max

```python
@rain_lifetime_max.setter
def rain_lifetime_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_max_curve"></a>

#### rain\_lifetime\_max\_curve

```python
@property
def rain_lifetime_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_lifetime_max_curve"></a>

#### rain\_lifetime\_max\_curve

```python
@rain_lifetime_max_curve.setter
def rain_lifetime_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_size_min"></a>

#### use\_rain\_size\_min

```python
@property
def use_rain_size_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_size_min"></a>

#### use\_rain\_size\_min

```python
@use_rain_size_min.setter
def use_rain_size_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_min"></a>

#### rain\_size\_min

```python
@property
def rain_size_min() -> float
```

(float):  [Read-Write] Minimum size of a single raindrop.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_min"></a>

#### rain\_size\_min

```python
@rain_size_min.setter
def rain_size_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_min_curve"></a>

#### rain\_size\_min\_curve

```python
@property
def rain_size_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_min_curve"></a>

#### rain\_size\_min\_curve

```python
@rain_size_min_curve.setter
def rain_size_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_size_max"></a>

#### use\_rain\_size\_max

```python
@property
def use_rain_size_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_size_max"></a>

#### use\_rain\_size\_max

```python
@use_rain_size_max.setter
def use_rain_size_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_max"></a>

#### rain\_size\_max

```python
@property
def rain_size_max() -> float
```

(float):  [Read-Write] Maximum size of a single raindrop.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_max"></a>

#### rain\_size\_max

```python
@rain_size_max.setter
def rain_size_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_max_curve"></a>

#### rain\_size\_max\_curve

```python
@property
def rain_size_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_size_max_curve"></a>

#### rain\_size\_max\_curve

```python
@rain_size_max_curve.setter
def rain_size_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_emissive"></a>

#### use\_rain\_emissive

```python
@property
def use_rain_emissive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_emissive"></a>

#### use\_rain\_emissive

```python
@use_rain_emissive.setter
def use_rain_emissive(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_emissive"></a>

#### rain\_emissive

```python
@property
def rain_emissive() -> float
```

(float):  [Read-Write] Rain Precipitation Amount.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_emissive"></a>

#### rain\_emissive

```python
@rain_emissive.setter
def rain_emissive(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_emissive_curve"></a>

#### rain\_emissive\_curve

```python
@property
def rain_emissive_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_emissive_curve"></a>

#### rain\_emissive\_curve

```python
@rain_emissive_curve.setter
def rain_emissive_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_lifetime_min"></a>

#### use\_rain\_splash\_lifetime\_min

```python
@property
def use_rain_splash_lifetime_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_lifetime_min"></a>

#### use\_rain\_splash\_lifetime\_min

```python
@use_rain_splash_lifetime_min.setter
def use_rain_splash_lifetime_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_min"></a>

#### rain\_splash\_lifetime\_min

```python
@property
def rain_splash_lifetime_min() -> float
```

(float):  [Read-Write] Minimum lifetime of a single rain splash. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_min"></a>

#### rain\_splash\_lifetime\_min

```python
@rain_splash_lifetime_min.setter
def rain_splash_lifetime_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_min_curve"></a>

#### rain\_splash\_lifetime\_min\_curve

```python
@property
def rain_splash_lifetime_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_min_curve"></a>

#### rain\_splash\_lifetime\_min\_curve

```python
@rain_splash_lifetime_min_curve.setter
def rain_splash_lifetime_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_lifetime_max"></a>

#### use\_rain\_splash\_lifetime\_max

```python
@property
def use_rain_splash_lifetime_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_lifetime_max"></a>

#### use\_rain\_splash\_lifetime\_max

```python
@use_rain_splash_lifetime_max.setter
def use_rain_splash_lifetime_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_max"></a>

#### rain\_splash\_lifetime\_max

```python
@property
def rain_splash_lifetime_max() -> float
```

(float):  [Read-Write] Maximum lifetime of a single rain splash. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_max"></a>

#### rain\_splash\_lifetime\_max

```python
@rain_splash_lifetime_max.setter
def rain_splash_lifetime_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_max_curve"></a>

#### rain\_splash\_lifetime\_max\_curve

```python
@property
def rain_splash_lifetime_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_lifetime_max_curve"></a>

#### rain\_splash\_lifetime\_max\_curve

```python
@rain_splash_lifetime_max_curve.setter
def rain_splash_lifetime_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_size_min"></a>

#### use\_rain\_splash\_size\_min

```python
@property
def use_rain_splash_size_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_size_min"></a>

#### use\_rain\_splash\_size\_min

```python
@use_rain_splash_size_min.setter
def use_rain_splash_size_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_min"></a>

#### rain\_splash\_size\_min

```python
@property
def rain_splash_size_min() -> Vector2D
```

(Vector2D):  [Read-Write] Minimum size of a rain splash.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_min"></a>

#### rain\_splash\_size\_min

```python
@rain_splash_size_min.setter
def rain_splash_size_min(value: Vector2D) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_min_curve"></a>

#### rain\_splash\_size\_min\_curve

```python
@property
def rain_splash_size_min_curve() -> CurveVector
```

(CurveVector):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_min_curve"></a>

#### rain\_splash\_size\_min\_curve

```python
@rain_splash_size_min_curve.setter
def rain_splash_size_min_curve(value: CurveVector) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_size_max"></a>

#### use\_rain\_splash\_size\_max

```python
@property
def use_rain_splash_size_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rain_splash_size_max"></a>

#### use\_rain\_splash\_size\_max

```python
@use_rain_splash_size_max.setter
def use_rain_splash_size_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_max"></a>

#### rain\_splash\_size\_max

```python
@property
def rain_splash_size_max() -> Vector2D
```

(Vector2D):  [Read-Write] Maximum size of a rain splash.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_max"></a>

#### rain\_splash\_size\_max

```python
@rain_splash_size_max.setter
def rain_splash_size_max(value: Vector2D) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_max_curve"></a>

#### rain\_splash\_size\_max\_curve

```python
@property
def rain_splash_size_max_curve() -> CurveVector
```

(CurveVector):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rain_splash_size_max_curve"></a>

#### rain\_splash\_size\_max\_curve

```python
@rain_splash_size_max_curve.setter
def rain_splash_size_max_curve(value: CurveVector) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_amount"></a>

#### use\_snow\_amount

```python
@property
def use_snow_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_amount"></a>

#### use\_snow\_amount

```python
@use_snow_amount.setter
def use_snow_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_amount"></a>

#### snow\_amount

```python
@property
def snow_amount() -> float
```

(float):  [Read-Write] Snow Precipitation Amount.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_amount"></a>

#### snow\_amount

```python
@snow_amount.setter
def snow_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_amount_curve"></a>

#### snow\_amount\_curve

```python
@property
def snow_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_amount_curve"></a>

#### snow\_amount\_curve

```python
@snow_amount_curve.setter
def snow_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_color"></a>

#### use\_snow\_color

```python
@property
def use_snow_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_color"></a>

#### use\_snow\_color

```python
@use_snow_color.setter
def use_snow_color(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_color"></a>

#### snow\_color

```python
@property
def snow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Snow Color.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_color"></a>

#### snow\_color

```python
@snow_color.setter
def snow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_color_curve"></a>

#### snow\_color\_curve

```python
@property
def snow_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_color_curve"></a>

#### snow\_color\_curve

```python
@snow_color_curve.setter
def snow_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_gravity"></a>

#### use\_snow\_gravity

```python
@property
def use_snow_gravity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_gravity"></a>

#### use\_snow\_gravity

```python
@use_snow_gravity.setter
def use_snow_gravity(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_gravity"></a>

#### snow\_gravity

```python
@property
def snow_gravity() -> float
```

(float):  [Read-Write] Gravity of a biggest sized snowflake.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_gravity"></a>

#### snow\_gravity

```python
@snow_gravity.setter
def snow_gravity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_gravity_curve"></a>

#### snow\_gravity\_curve

```python
@property
def snow_gravity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_gravity_curve"></a>

#### snow\_gravity\_curve

```python
@snow_gravity_curve.setter
def snow_gravity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_turbulence"></a>

#### use\_snow\_turbulence

```python
@property
def use_snow_turbulence() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_turbulence"></a>

#### use\_snow\_turbulence

```python
@use_snow_turbulence.setter
def use_snow_turbulence(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_turbulence"></a>

#### snow\_turbulence

```python
@property
def snow_turbulence() -> float
```

(float):  [Read-Write] Snow turbulence.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_turbulence"></a>

#### snow\_turbulence

```python
@snow_turbulence.setter
def snow_turbulence(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_turbulence_curve"></a>

#### snow\_turbulence\_curve

```python
@property
def snow_turbulence_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_turbulence_curve"></a>

#### snow\_turbulence\_curve

```python
@snow_turbulence_curve.setter
def snow_turbulence_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_lifetime_min"></a>

#### use\_snow\_lifetime\_min

```python
@property
def use_snow_lifetime_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_lifetime_min"></a>

#### use\_snow\_lifetime\_min

```python
@use_snow_lifetime_min.setter
def use_snow_lifetime_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_min"></a>

#### snow\_lifetime\_min

```python
@property
def snow_lifetime_min() -> float
```

(float):  [Read-Write] Minimum lifetime of a single snowflake. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_min"></a>

#### snow\_lifetime\_min

```python
@snow_lifetime_min.setter
def snow_lifetime_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_min_curve"></a>

#### snow\_lifetime\_min\_curve

```python
@property
def snow_lifetime_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_min_curve"></a>

#### snow\_lifetime\_min\_curve

```python
@snow_lifetime_min_curve.setter
def snow_lifetime_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_lifetime_max"></a>

#### use\_snow\_lifetime\_max

```python
@property
def use_snow_lifetime_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_lifetime_max"></a>

#### use\_snow\_lifetime\_max

```python
@use_snow_lifetime_max.setter
def use_snow_lifetime_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_max"></a>

#### snow\_lifetime\_max

```python
@property
def snow_lifetime_max() -> float
```

(float):  [Read-Write] Maximum lifetime of a single snowflake. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_max"></a>

#### snow\_lifetime\_max

```python
@snow_lifetime_max.setter
def snow_lifetime_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_max_curve"></a>

#### snow\_lifetime\_max\_curve

```python
@property
def snow_lifetime_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_lifetime_max_curve"></a>

#### snow\_lifetime\_max\_curve

```python
@snow_lifetime_max_curve.setter
def snow_lifetime_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_size_min"></a>

#### use\_snow\_size\_min

```python
@property
def use_snow_size_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_size_min"></a>

#### use\_snow\_size\_min

```python
@use_snow_size_min.setter
def use_snow_size_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_min"></a>

#### snow\_size\_min

```python
@property
def snow_size_min() -> float
```

(float):  [Read-Write] Minimum size of a single snowflake.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_min"></a>

#### snow\_size\_min

```python
@snow_size_min.setter
def snow_size_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_min_curve"></a>

#### snow\_size\_min\_curve

```python
@property
def snow_size_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_min_curve"></a>

#### snow\_size\_min\_curve

```python
@snow_size_min_curve.setter
def snow_size_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_size_max"></a>

#### use\_snow\_size\_max

```python
@property
def use_snow_size_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_size_max"></a>

#### use\_snow\_size\_max

```python
@use_snow_size_max.setter
def use_snow_size_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_max"></a>

#### snow\_size\_max

```python
@property
def snow_size_max() -> float
```

(float):  [Read-Write] Maximum size of a single snowflake.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_max"></a>

#### snow\_size\_max

```python
@snow_size_max.setter
def snow_size_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_max_curve"></a>

#### snow\_size\_max\_curve

```python
@property
def snow_size_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_size_max_curve"></a>

#### snow\_size\_max\_curve

```python
@snow_size_max_curve.setter
def snow_size_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_emissive"></a>

#### use\_snow\_emissive

```python
@property
def use_snow_emissive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_snow_emissive"></a>

#### use\_snow\_emissive

```python
@use_snow_emissive.setter
def use_snow_emissive(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_emissive"></a>

#### snow\_emissive

```python
@property
def snow_emissive() -> float
```

(float):  [Read-Write] Rain Precipitation Amount.

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_emissive"></a>

#### snow\_emissive

```python
@snow_emissive.setter
def snow_emissive(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_emissive_curve"></a>

#### snow\_emissive\_curve

```python
@property
def snow_emissive_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.snow_emissive_curve"></a>

#### snow\_emissive\_curve

```python
@snow_emissive_curve.setter
def snow_emissive_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_fog_amount"></a>

#### use\_fog\_amount

```python
@property
def use_fog_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_fog_amount"></a>

#### use\_fog\_amount

```python
@use_fog_amount.setter
def use_fog_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.fog_amount"></a>

#### fog\_amount

```python
@property
def fog_amount() -> float
```

(float):  [Read-Write] Rain Precipitation Amount.

<a id="unreal.SkyCreatorWeatherFXSettings_51.fog_amount"></a>

#### fog\_amount

```python
@fog_amount.setter
def fog_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.fog_amount_curve"></a>

#### fog\_amount\_curve

```python
@property
def fog_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.fog_amount_curve"></a>

#### fog\_amount\_curve

```python
@fog_amount_curve.setter
def fog_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.enable_lightnings"></a>

#### enable\_lightnings

```python
@property
def enable_lightnings() -> bool
```

(bool):  [Read-Write] Whether to enable Lightnings.

<a id="unreal.SkyCreatorWeatherFXSettings_51.enable_lightnings"></a>

#### enable\_lightnings

```python
@enable_lightnings.setter
def enable_lightnings(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_spawn_interval_min"></a>

#### use\_lightning\_spawn\_interval\_min

```python
@property
def use_lightning_spawn_interval_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_spawn_interval_min"></a>

#### use\_lightning\_spawn\_interval\_min

```python
@use_lightning_spawn_interval_min.setter
def use_lightning_spawn_interval_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_min"></a>

#### lightning\_spawn\_interval\_min

```python
@property
def lightning_spawn_interval_min() -> float
```

(float):  [Read-Write] Minimum interval to randomly spawn Lightning in seconds.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_min"></a>

#### lightning\_spawn\_interval\_min

```python
@lightning_spawn_interval_min.setter
def lightning_spawn_interval_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_min_curve"></a>

#### lightning\_spawn\_interval\_min\_curve

```python
@property
def lightning_spawn_interval_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_min_curve"></a>

#### lightning\_spawn\_interval\_min\_curve

```python
@lightning_spawn_interval_min_curve.setter
def lightning_spawn_interval_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_spawn_interval_max"></a>

#### use\_lightning\_spawn\_interval\_max

```python
@property
def use_lightning_spawn_interval_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_spawn_interval_max"></a>

#### use\_lightning\_spawn\_interval\_max

```python
@use_lightning_spawn_interval_max.setter
def use_lightning_spawn_interval_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_max"></a>

#### lightning\_spawn\_interval\_max

```python
@property
def lightning_spawn_interval_max() -> float
```

(float):  [Read-Write] Maximum interval to randomly spawn Lightning in seconds.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_max"></a>

#### lightning\_spawn\_interval\_max

```python
@lightning_spawn_interval_max.setter
def lightning_spawn_interval_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_max_curve"></a>

#### lightning\_spawn\_interval\_max\_curve

```python
@property
def lightning_spawn_interval_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_spawn_interval_max_curve"></a>

#### lightning\_spawn\_interval\_max\_curve

```python
@lightning_spawn_interval_max_curve.setter
def lightning_spawn_interval_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_color_min"></a>

#### use\_lightning\_color\_min

```python
@property
def use_lightning_color_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_color_min"></a>

#### use\_lightning\_color\_min

```python
@use_lightning_color_min.setter
def use_lightning_color_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_min"></a>

#### lightning\_color\_min

```python
@property
def lightning_color_min() -> LinearColor
```

(LinearColor):  [Read-Write] Minimum Lightning color.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_min"></a>

#### lightning\_color\_min

```python
@lightning_color_min.setter
def lightning_color_min(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_min_curve"></a>

#### lightning\_color\_min\_curve

```python
@property
def lightning_color_min_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_min_curve"></a>

#### lightning\_color\_min\_curve

```python
@lightning_color_min_curve.setter
def lightning_color_min_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_color_max"></a>

#### use\_lightning\_color\_max

```python
@property
def use_lightning_color_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_color_max"></a>

#### use\_lightning\_color\_max

```python
@use_lightning_color_max.setter
def use_lightning_color_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_max"></a>

#### lightning\_color\_max

```python
@property
def lightning_color_max() -> LinearColor
```

(LinearColor):  [Read-Write] Maximum Lightning color.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_max"></a>

#### lightning\_color\_max

```python
@lightning_color_max.setter
def lightning_color_max(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_max_curve"></a>

#### lightning\_color\_max\_curve

```python
@property
def lightning_color_max_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_color_max_curve"></a>

#### lightning\_color\_max\_curve

```python
@lightning_color_max_curve.setter
def lightning_color_max_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_lifetime"></a>

#### use\_lightning\_lifetime

```python
@property
def use_lightning_lifetime() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_lifetime"></a>

#### use\_lightning\_lifetime

```python
@use_lightning_lifetime.setter
def use_lightning_lifetime(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_lifetime"></a>

#### lightning\_lifetime

```python
@property
def lightning_lifetime() -> float
```

(float):  [Read-Write] Lightning lifetime in seconds.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_lifetime"></a>

#### lightning\_lifetime

```python
@lightning_lifetime.setter
def lightning_lifetime(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_lifetime_curve"></a>

#### lightning\_lifetime\_curve

```python
@property
def lightning_lifetime_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_lifetime_curve"></a>

#### lightning\_lifetime\_curve

```python
@lightning_lifetime_curve.setter
def lightning_lifetime_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_spawn_chance"></a>

#### use\_lightning\_bolt\_spawn\_chance

```python
@property
def use_lightning_bolt_spawn_chance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_spawn_chance"></a>

#### use\_lightning\_bolt\_spawn\_chance

```python
@use_lightning_bolt_spawn_chance.setter
def use_lightning_bolt_spawn_chance(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_spawn_chance"></a>

#### lightning\_bolt\_spawn\_chance

```python
@property
def lightning_bolt_spawn_chance() -> float
```

(float):  [Read-Write] Chance of spawning a Lightning Bolt when spawning a Lightning.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_spawn_chance"></a>

#### lightning\_bolt\_spawn\_chance

```python
@lightning_bolt_spawn_chance.setter
def lightning_bolt_spawn_chance(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_spawn_chance_curve"></a>

#### lightning\_bolt\_spawn\_chance\_curve

```python
@property
def lightning_bolt_spawn_chance_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_spawn_chance_curve"></a>

#### lightning\_bolt\_spawn\_chance\_curve

```python
@lightning_bolt_spawn_chance_curve.setter
def lightning_bolt_spawn_chance_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_width_min"></a>

#### use\_lightning\_bolt\_width\_min

```python
@property
def use_lightning_bolt_width_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_width_min"></a>

#### use\_lightning\_bolt\_width\_min

```python
@use_lightning_bolt_width_min.setter
def use_lightning_bolt_width_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_min"></a>

#### lightning\_bolt\_width\_min

```python
@property
def lightning_bolt_width_min() -> float
```

(float):  [Read-Write] Minimum width of a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_min"></a>

#### lightning\_bolt\_width\_min

```python
@lightning_bolt_width_min.setter
def lightning_bolt_width_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_min_curve"></a>

#### lightning\_bolt\_width\_min\_curve

```python
@property
def lightning_bolt_width_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_min_curve"></a>

#### lightning\_bolt\_width\_min\_curve

```python
@lightning_bolt_width_min_curve.setter
def lightning_bolt_width_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_width_max"></a>

#### use\_lightning\_bolt\_width\_max

```python
@property
def use_lightning_bolt_width_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_width_max"></a>

#### use\_lightning\_bolt\_width\_max

```python
@use_lightning_bolt_width_max.setter
def use_lightning_bolt_width_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_max"></a>

#### lightning\_bolt\_width\_max

```python
@property
def lightning_bolt_width_max() -> float
```

(float):  [Read-Write] Maximum width of a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_max"></a>

#### lightning\_bolt\_width\_max

```python
@lightning_bolt_width_max.setter
def lightning_bolt_width_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_max_curve"></a>

#### lightning\_bolt\_width\_max\_curve

```python
@property
def lightning_bolt_width_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_width_max_curve"></a>

#### lightning\_bolt\_width\_max\_curve

```python
@lightning_bolt_width_max_curve.setter
def lightning_bolt_width_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_length_min"></a>

#### use\_lightning\_bolt\_length\_min

```python
@property
def use_lightning_bolt_length_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_length_min"></a>

#### use\_lightning\_bolt\_length\_min

```python
@use_lightning_bolt_length_min.setter
def use_lightning_bolt_length_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_min"></a>

#### lightning\_bolt\_length\_min

```python
@property
def lightning_bolt_length_min() -> float
```

(float):  [Read-Write] Minimum length of a Lightning Bolt (in kilometers).

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_min"></a>

#### lightning\_bolt\_length\_min

```python
@lightning_bolt_length_min.setter
def lightning_bolt_length_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_min_curve"></a>

#### lightning\_bolt\_length\_min\_curve

```python
@property
def lightning_bolt_length_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_min_curve"></a>

#### lightning\_bolt\_length\_min\_curve

```python
@lightning_bolt_length_min_curve.setter
def lightning_bolt_length_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_length_max"></a>

#### use\_lightning\_bolt\_length\_max

```python
@property
def use_lightning_bolt_length_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_length_max"></a>

#### use\_lightning\_bolt\_length\_max

```python
@use_lightning_bolt_length_max.setter
def use_lightning_bolt_length_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_max"></a>

#### lightning\_bolt\_length\_max

```python
@property
def lightning_bolt_length_max() -> float
```

(float):  [Read-Write] Maximum length of a Lightning Bolt (in kilometers).

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_max"></a>

#### lightning\_bolt\_length\_max

```python
@lightning_bolt_length_max.setter
def lightning_bolt_length_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_max_curve"></a>

#### lightning\_bolt\_length\_max\_curve

```python
@property
def lightning_bolt_length_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_length_max_curve"></a>

#### lightning\_bolt\_length\_max\_curve

```python
@lightning_bolt_length_max_curve.setter
def lightning_bolt_length_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_frequency"></a>

#### use\_lightning\_bolt\_curve\_frequency

```python
@property
def use_lightning_bolt_curve_frequency() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_frequency"></a>

#### use\_lightning\_bolt\_curve\_frequency

```python
@use_lightning_bolt_curve_frequency.setter
def use_lightning_bolt_curve_frequency(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_frequency"></a>

#### lightning\_bolt\_curve\_frequency

```python
@property
def lightning_bolt_curve_frequency() -> float
```

(float):  [Read-Write] Frequency of a Lightning Bolt curvature.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_frequency"></a>

#### lightning\_bolt\_curve\_frequency

```python
@lightning_bolt_curve_frequency.setter
def lightning_bolt_curve_frequency(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_frequency_curve"></a>

#### lightning\_bolt\_curve\_frequency\_curve

```python
@property
def lightning_bolt_curve_frequency_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_frequency_curve"></a>

#### lightning\_bolt\_curve\_frequency\_curve

```python
@lightning_bolt_curve_frequency_curve.setter
def lightning_bolt_curve_frequency_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_strength_min"></a>

#### use\_lightning\_bolt\_curve\_strength\_min

```python
@property
def use_lightning_bolt_curve_strength_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_strength_min"></a>

#### use\_lightning\_bolt\_curve\_strength\_min

```python
@use_lightning_bolt_curve_strength_min.setter
def use_lightning_bolt_curve_strength_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_min"></a>

#### lightning\_bolt\_curve\_strength\_min

```python
@property
def lightning_bolt_curve_strength_min() -> float
```

(float):  [Read-Write] Minimum strength of a Lightning Bolt curvature.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_min"></a>

#### lightning\_bolt\_curve\_strength\_min

```python
@lightning_bolt_curve_strength_min.setter
def lightning_bolt_curve_strength_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_min_curve"></a>

#### lightning\_bolt\_curve\_strength\_min\_curve

```python
@property
def lightning_bolt_curve_strength_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_min_curve"></a>

#### lightning\_bolt\_curve\_strength\_min\_curve

```python
@lightning_bolt_curve_strength_min_curve.setter
def lightning_bolt_curve_strength_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_strength_max"></a>

#### use\_lightning\_bolt\_curve\_strength\_max

```python
@property
def use_lightning_bolt_curve_strength_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_curve_strength_max"></a>

#### use\_lightning\_bolt\_curve\_strength\_max

```python
@use_lightning_bolt_curve_strength_max.setter
def use_lightning_bolt_curve_strength_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_max"></a>

#### lightning\_bolt\_curve\_strength\_max

```python
@property
def lightning_bolt_curve_strength_max() -> float
```

(float):  [Read-Write] Maximum strength of a Lightning Bolt curvature.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_max"></a>

#### lightning\_bolt\_curve\_strength\_max

```python
@lightning_bolt_curve_strength_max.setter
def lightning_bolt_curve_strength_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_max_curve"></a>

#### lightning\_bolt\_curve\_strength\_max\_curve

```python
@property
def lightning_bolt_curve_strength_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_curve_strength_max_curve"></a>

#### lightning\_bolt\_curve\_strength\_max\_curve

```python
@lightning_bolt_curve_strength_max_curve.setter
def lightning_bolt_curve_strength_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_jitter_strength"></a>

#### use\_lightning\_bolt\_jitter\_strength

```python
@property
def use_lightning_bolt_jitter_strength() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_bolt_jitter_strength"></a>

#### use\_lightning\_bolt\_jitter\_strength

```python
@use_lightning_bolt_jitter_strength.setter
def use_lightning_bolt_jitter_strength(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_jitter_strength"></a>

#### lightning\_bolt\_jitter\_strength

```python
@property
def lightning_bolt_jitter_strength() -> float
```

(float):  [Read-Write] Jitter strength of a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_jitter_strength"></a>

#### lightning\_bolt\_jitter\_strength

```python
@lightning_bolt_jitter_strength.setter
def lightning_bolt_jitter_strength(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_jitter_strength_curve"></a>

#### lightning\_bolt\_jitter\_strength\_curve

```python
@property
def lightning_bolt_jitter_strength_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_bolt_jitter_strength_curve"></a>

#### lightning\_bolt\_jitter\_strength\_curve

```python
@lightning_bolt_jitter_strength_curve.setter
def lightning_bolt_jitter_strength_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_spawn_chance"></a>

#### use\_lightning\_branch\_spawn\_chance

```python
@property
def use_lightning_branch_spawn_chance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_spawn_chance"></a>

#### use\_lightning\_branch\_spawn\_chance

```python
@use_lightning_branch_spawn_chance.setter
def use_lightning_branch_spawn_chance(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_spawn_chance"></a>

#### lightning\_branch\_spawn\_chance

```python
@property
def lightning_branch_spawn_chance() -> float
```

(float):  [Read-Write] Chance of spawning a Lightning Branch when spawning a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_spawn_chance"></a>

#### lightning\_branch\_spawn\_chance

```python
@lightning_branch_spawn_chance.setter
def lightning_branch_spawn_chance(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_spawn_chance_curve"></a>

#### lightning\_branch\_spawn\_chance\_curve

```python
@property
def lightning_branch_spawn_chance_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_spawn_chance_curve"></a>

#### lightning\_branch\_spawn\_chance\_curve

```python
@lightning_branch_spawn_chance_curve.setter
def lightning_branch_spawn_chance_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_scale_min"></a>

#### use\_lightning\_branch\_scale\_min

```python
@property
def use_lightning_branch_scale_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_scale_min"></a>

#### use\_lightning\_branch\_scale\_min

```python
@use_lightning_branch_scale_min.setter
def use_lightning_branch_scale_min(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_min"></a>

#### lightning\_branch\_scale\_min

```python
@property
def lightning_branch_scale_min() -> float
```

(float):  [Read-Write] Minimum scale of a Lightning Branch.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_min"></a>

#### lightning\_branch\_scale\_min

```python
@lightning_branch_scale_min.setter
def lightning_branch_scale_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_min_curve"></a>

#### lightning\_branch\_scale\_min\_curve

```python
@property
def lightning_branch_scale_min_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_min_curve"></a>

#### lightning\_branch\_scale\_min\_curve

```python
@lightning_branch_scale_min_curve.setter
def lightning_branch_scale_min_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_scale_max"></a>

#### use\_lightning\_branch\_scale\_max

```python
@property
def use_lightning_branch_scale_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_lightning_branch_scale_max"></a>

#### use\_lightning\_branch\_scale\_max

```python
@use_lightning_branch_scale_max.setter
def use_lightning_branch_scale_max(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_max"></a>

#### lightning\_branch\_scale\_max

```python
@property
def lightning_branch_scale_max() -> float
```

(float):  [Read-Write] Maximum scale of a Lightning Branch.

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_max"></a>

#### lightning\_branch\_scale\_max

```python
@lightning_branch_scale_max.setter
def lightning_branch_scale_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_max_curve"></a>

#### lightning\_branch\_scale\_max\_curve

```python
@property
def lightning_branch_scale_max_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.lightning_branch_scale_max_curve"></a>

#### lightning\_branch\_scale\_max\_curve

```python
@lightning_branch_scale_max_curve.setter
def lightning_branch_scale_max_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_amount"></a>

#### use\_rainbow\_amount

```python
@property
def use_rainbow_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_amount"></a>

#### use\_rainbow\_amount

```python
@use_rainbow_amount.setter
def use_rainbow_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_amount"></a>

#### rainbow\_amount

```python
@property
def rainbow_amount() -> float
```

(float):  [Read-Write] Rainbow Amount.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_amount"></a>

#### rainbow\_amount

```python
@rainbow_amount.setter
def rainbow_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_amount_curve"></a>

#### rainbow\_amount\_curve

```python
@property
def rainbow_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_amount_curve"></a>

#### rainbow\_amount\_curve

```python
@rainbow_amount_curve.setter
def rainbow_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_color"></a>

#### use\_rainbow\_color

```python
@property
def use_rainbow_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_color"></a>

#### use\_rainbow\_color

```python
@use_rainbow_color.setter
def use_rainbow_color(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_color"></a>

#### rainbow\_color

```python
@property
def rainbow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Rainbow Tint Color.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_color"></a>

#### rainbow\_color

```python
@rainbow_color.setter
def rainbow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_color_curve"></a>

#### rainbow\_color\_curve

```python
@property
def rainbow_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_color_curve"></a>

#### rainbow\_color\_curve

```python
@rainbow_color_curve.setter
def rainbow_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_radius"></a>

#### use\_rainbow\_radius

```python
@property
def use_rainbow_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_radius"></a>

#### use\_rainbow\_radius

```python
@use_rainbow_radius.setter
def use_rainbow_radius(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_radius"></a>

#### rainbow\_radius

```python
@property
def rainbow_radius() -> float
```

(float):  [Read-Write] Radius of the Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_radius"></a>

#### rainbow\_radius

```python
@rainbow_radius.setter
def rainbow_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_radius_curve"></a>

#### rainbow\_radius\_curve

```python
@property
def rainbow_radius_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_radius_curve"></a>

#### rainbow\_radius\_curve

```python
@rainbow_radius_curve.setter
def rainbow_radius_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_thickness"></a>

#### use\_rainbow\_thickness

```python
@property
def use_rainbow_thickness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_rainbow_thickness"></a>

#### use\_rainbow\_thickness

```python
@use_rainbow_thickness.setter
def use_rainbow_thickness(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_thickness"></a>

#### rainbow\_thickness

```python
@property
def rainbow_thickness() -> float
```

(float):  [Read-Write] Thickness of the Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_thickness"></a>

#### rainbow\_thickness

```python
@rainbow_thickness.setter
def rainbow_thickness(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_thickness_curve"></a>

#### rainbow\_thickness\_curve

```python
@property
def rainbow_thickness_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.rainbow_thickness_curve"></a>

#### rainbow\_thickness\_curve

```python
@rainbow_thickness_curve.setter
def rainbow_thickness_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_color"></a>

#### use\_secondary\_rainbow\_color

```python
@property
def use_secondary_rainbow_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_color"></a>

#### use\_secondary\_rainbow\_color

```python
@use_secondary_rainbow_color.setter
def use_secondary_rainbow_color(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_color"></a>

#### secondary\_rainbow\_color

```python
@property
def secondary_rainbow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Secondary Rainbow Tint Color.

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_color"></a>

#### secondary\_rainbow\_color

```python
@secondary_rainbow_color.setter
def secondary_rainbow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_color_curve"></a>

#### secondary\_rainbow\_color\_curve

```python
@property
def secondary_rainbow_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_color_curve"></a>

#### secondary\_rainbow\_color\_curve

```python
@secondary_rainbow_color_curve.setter
def secondary_rainbow_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_radius"></a>

#### use\_secondary\_rainbow\_radius

```python
@property
def use_secondary_rainbow_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_radius"></a>

#### use\_secondary\_rainbow\_radius

```python
@use_secondary_rainbow_radius.setter
def use_secondary_rainbow_radius(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_radius"></a>

#### secondary\_rainbow\_radius

```python
@property
def secondary_rainbow_radius() -> float
```

(float):  [Read-Write] Radius of the Secondary Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_radius"></a>

#### secondary\_rainbow\_radius

```python
@secondary_rainbow_radius.setter
def secondary_rainbow_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_radius_curve"></a>

#### secondary\_rainbow\_radius\_curve

```python
@property
def secondary_rainbow_radius_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_radius_curve"></a>

#### secondary\_rainbow\_radius\_curve

```python
@secondary_rainbow_radius_curve.setter
def secondary_rainbow_radius_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_thickness"></a>

#### use\_secondary\_rainbow\_thickness

```python
@property
def use_secondary_rainbow_thickness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.use_secondary_rainbow_thickness"></a>

#### use\_secondary\_rainbow\_thickness

```python
@use_secondary_rainbow_thickness.setter
def use_secondary_rainbow_thickness(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_thickness"></a>

#### secondary\_rainbow\_thickness

```python
@property
def secondary_rainbow_thickness() -> float
```

(float):  [Read-Write] Thickness of the Secondary Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_thickness"></a>

#### secondary\_rainbow\_thickness

```python
@secondary_rainbow_thickness.setter
def secondary_rainbow_thickness(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_thickness_curve"></a>

#### secondary\_rainbow\_thickness\_curve

```python
@property
def secondary_rainbow_thickness_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherFXSettings_51.secondary_rainbow_thickness_curve"></a>

#### secondary\_rainbow\_thickness\_curve

```python
@secondary_rainbow_thickness_curve.setter
def secondary_rainbow_thickness_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51"></a>