## SkyCreatorWeatherFXSettings Objects

```python
class SkyCreatorWeatherFXSettings(StructBase)
```

Sky Creator Weather FXSettings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_lightnings`` (bool):  [Read-Write] Whether to enable Lightnings.
- ``lightning_bolt_curve_frequency`` (float):  [Read-Write] Frequency of a Lightning Bolt curvature.
- ``lightning_bolt_curve_strength_max`` (float):  [Read-Write] Maximum strength of a Lightning Bolt curvature.
- ``lightning_bolt_curve_strength_min`` (float):  [Read-Write] Minimum strength of a Lightning Bolt curvature.
- ``lightning_bolt_jitter_strength`` (float):  [Read-Write] Jitter strength of a Lightning Bolt.
- ``lightning_bolt_length_max`` (float):  [Read-Write] Maximum length of a Lightning Bolt (in kilometers).
- ``lightning_bolt_length_min`` (float):  [Read-Write] Minimum length of a Lightning Bolt (in kilometers).
- ``lightning_bolt_spawn_chance`` (float):  [Read-Write] Chance of spawning a Lightning Bolt when spawning a Lightning.
- ``lightning_bolt_width_max`` (float):  [Read-Write] Maximum width of a Lightning Bolt.
- ``lightning_bolt_width_min`` (float):  [Read-Write] Minimum width of a Lightning Bolt.
- ``lightning_branch_scale_max`` (float):  [Read-Write] Maximum scale of a Lightning Branch.
- ``lightning_branch_scale_min`` (float):  [Read-Write] Minimum scale of a Lightning Branch.
- ``lightning_branch_spawn_chance`` (float):  [Read-Write] Chance of spawning a Lightning Branch when spawning a Lightning Bolt.
- ``lightning_color_max`` (LinearColor):  [Read-Write] Maximum Lightning color.
- ``lightning_color_min`` (LinearColor):  [Read-Write] Minimum Lightning color.
- ``lightning_lifetime`` (float):  [Read-Write] Lightning lifetime in seconds.
- ``lightning_spawn_interval_max`` (float):  [Read-Write] Maximum interval to randomly spawn Lightning in seconds.
- ``lightning_spawn_interval_min`` (float):  [Read-Write] Minimum interval to randomly spawn Lightning in seconds.
- ``rain_amount`` (float):  [Read-Write] Rain Precipitation Amount.
- ``rain_color`` (LinearColor):  [Read-Write] Rain Color.
- ``rain_gravity`` (float):  [Read-Write] Gravity of a biggest sized raindrop.
- ``rain_lifetime_max`` (float):  [Read-Write] Maximum lifetime of a single raindrop. Can affect the performance.
- ``rain_lifetime_min`` (float):  [Read-Write] Minimum lifetime of a single raindrop. Can affect the performance.
- ``rain_size_max`` (float):  [Read-Write] Maximum size of a single raindrop.
- ``rain_size_min`` (float):  [Read-Write] Minimum size of a single raindrop.
- ``rain_splash_lifetime_max`` (float):  [Read-Write] Maximum lifetime of a single rain splash. Can affect the performance.
- ``rain_splash_lifetime_min`` (float):  [Read-Write] Minimum lifetime of a single rain splash. Can affect the performance.
- ``rain_splash_size_max`` (Vector2D):  [Read-Write] Maximum size of a rain splash.
- ``rain_splash_size_min`` (Vector2D):  [Read-Write] Minimum size of a rain splash.
- ``rainbow_amount`` (float):  [Read-Write] Rainbow Amount.
- ``rainbow_color`` (LinearColor):  [Read-Write] Rainbow Tint Color.
- ``rainbow_radius`` (float):  [Read-Write] Radius of the Rainbow.
- ``rainbow_thickness`` (float):  [Read-Write] Thickness of the Rainbow.
- ``secondary_rainbow_color`` (LinearColor):  [Read-Write] Secondary Rainbow Tint Color.
- ``secondary_rainbow_radius`` (float):  [Read-Write] Radius of the Secondary Rainbow.
- ``secondary_rainbow_thickness`` (float):  [Read-Write] Thickness of the Secondary Rainbow.
- ``snow_amount`` (float):  [Read-Write] Snow Precipitation Amount.
- ``snow_color`` (LinearColor):  [Read-Write] Snow Color.
- ``snow_gravity`` (float):  [Read-Write] Gravity of a biggest sized snowflake.
- ``snow_lifetime_max`` (float):  [Read-Write] Maximum lifetime of a single snowflake. Can affect the performance.
- ``snow_lifetime_min`` (float):  [Read-Write] Minimum lifetime of a single snowflake. Can affect the performance.
- ``snow_size_max`` (float):  [Read-Write] Maximum size of a single snowflake.
- ``snow_size_min`` (float):  [Read-Write] Minimum size of a single snowflake.
- ``snow_turbulence`` (float):  [Read-Write] Snow turbulence.

<a id="unreal.SkyCreatorWeatherFXSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rain_amount: float = 0.000000,
             rain_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             rain_gravity: float = 0.000000,
             rain_lifetime_min: float = 0.000000,
             rain_lifetime_max: float = 0.000000,
             rain_size_min: float = 0.000000,
             rain_size_max: float = 0.000000,
             rain_splash_lifetime_min: float = 0.000000,
             rain_splash_lifetime_max: float = 0.000000,
             rain_splash_size_min: Vector2D = [0.000000, 0.000000],
             rain_splash_size_max: Vector2D = [0.000000, 0.000000],
             snow_amount: float = 0.000000,
             snow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             snow_gravity: float = 0.000000,
             snow_turbulence: float = 0.000000,
             snow_lifetime_min: float = 0.000000,
             snow_lifetime_max: float = 0.000000,
             snow_size_min: float = 0.000000,
             snow_size_max: float = 0.000000,
             enable_lightnings: bool = False,
             lightning_spawn_interval_min: float = 0.000000,
             lightning_spawn_interval_max: float = 0.000000,
             lightning_color_min: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             lightning_color_max: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             lightning_lifetime: float = 0.000000,
             lightning_bolt_spawn_chance: float = 0.000000,
             lightning_bolt_width_min: float = 0.000000,
             lightning_bolt_width_max: float = 0.000000,
             lightning_bolt_length_min: float = 0.000000,
             lightning_bolt_length_max: float = 0.000000,
             lightning_bolt_curve_frequency: float = 0.000000,
             lightning_bolt_curve_strength_min: float = 0.000000,
             lightning_bolt_curve_strength_max: float = 0.000000,
             lightning_bolt_jitter_strength: float = 0.000000,
             lightning_branch_spawn_chance: float = 0.000000,
             lightning_branch_scale_min: float = 0.000000,
             lightning_branch_scale_max: float = 0.000000,
             rainbow_amount: float = 0.000000,
             rainbow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             rainbow_radius: float = 0.000000,
             rainbow_thickness: float = 0.000000,
             secondary_rainbow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             secondary_rainbow_radius: float = 0.000000,
             secondary_rainbow_thickness: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_amount"></a>

#### rain\_amount

```python
@property
def rain_amount() -> float
```

(float):  [Read-Write] Rain Precipitation Amount.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_amount"></a>

#### rain\_amount

```python
@rain_amount.setter
def rain_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_color"></a>

#### rain\_color

```python
@property
def rain_color() -> LinearColor
```

(LinearColor):  [Read-Write] Rain Color.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_color"></a>

#### rain\_color

```python
@rain_color.setter
def rain_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_gravity"></a>

#### rain\_gravity

```python
@property
def rain_gravity() -> float
```

(float):  [Read-Write] Gravity of a biggest sized raindrop.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_gravity"></a>

#### rain\_gravity

```python
@rain_gravity.setter
def rain_gravity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_lifetime_min"></a>

#### rain\_lifetime\_min

```python
@property
def rain_lifetime_min() -> float
```

(float):  [Read-Write] Minimum lifetime of a single raindrop. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_lifetime_min"></a>

#### rain\_lifetime\_min

```python
@rain_lifetime_min.setter
def rain_lifetime_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_lifetime_max"></a>

#### rain\_lifetime\_max

```python
@property
def rain_lifetime_max() -> float
```

(float):  [Read-Write] Maximum lifetime of a single raindrop. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_lifetime_max"></a>

#### rain\_lifetime\_max

```python
@rain_lifetime_max.setter
def rain_lifetime_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_size_min"></a>

#### rain\_size\_min

```python
@property
def rain_size_min() -> float
```

(float):  [Read-Write] Minimum size of a single raindrop.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_size_min"></a>

#### rain\_size\_min

```python
@rain_size_min.setter
def rain_size_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_size_max"></a>

#### rain\_size\_max

```python
@property
def rain_size_max() -> float
```

(float):  [Read-Write] Maximum size of a single raindrop.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_size_max"></a>

#### rain\_size\_max

```python
@rain_size_max.setter
def rain_size_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_lifetime_min"></a>

#### rain\_splash\_lifetime\_min

```python
@property
def rain_splash_lifetime_min() -> float
```

(float):  [Read-Write] Minimum lifetime of a single rain splash. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_lifetime_min"></a>

#### rain\_splash\_lifetime\_min

```python
@rain_splash_lifetime_min.setter
def rain_splash_lifetime_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_lifetime_max"></a>

#### rain\_splash\_lifetime\_max

```python
@property
def rain_splash_lifetime_max() -> float
```

(float):  [Read-Write] Maximum lifetime of a single rain splash. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_lifetime_max"></a>

#### rain\_splash\_lifetime\_max

```python
@rain_splash_lifetime_max.setter
def rain_splash_lifetime_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_size_min"></a>

#### rain\_splash\_size\_min

```python
@property
def rain_splash_size_min() -> Vector2D
```

(Vector2D):  [Read-Write] Minimum size of a rain splash.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_size_min"></a>

#### rain\_splash\_size\_min

```python
@rain_splash_size_min.setter
def rain_splash_size_min(value: Vector2D) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_size_max"></a>

#### rain\_splash\_size\_max

```python
@property
def rain_splash_size_max() -> Vector2D
```

(Vector2D):  [Read-Write] Maximum size of a rain splash.

<a id="unreal.SkyCreatorWeatherFXSettings.rain_splash_size_max"></a>

#### rain\_splash\_size\_max

```python
@rain_splash_size_max.setter
def rain_splash_size_max(value: Vector2D) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_amount"></a>

#### snow\_amount

```python
@property
def snow_amount() -> float
```

(float):  [Read-Write] Snow Precipitation Amount.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_amount"></a>

#### snow\_amount

```python
@snow_amount.setter
def snow_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_color"></a>

#### snow\_color

```python
@property
def snow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Snow Color.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_color"></a>

#### snow\_color

```python
@snow_color.setter
def snow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_gravity"></a>

#### snow\_gravity

```python
@property
def snow_gravity() -> float
```

(float):  [Read-Write] Gravity of a biggest sized snowflake.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_gravity"></a>

#### snow\_gravity

```python
@snow_gravity.setter
def snow_gravity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_turbulence"></a>

#### snow\_turbulence

```python
@property
def snow_turbulence() -> float
```

(float):  [Read-Write] Snow turbulence.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_turbulence"></a>

#### snow\_turbulence

```python
@snow_turbulence.setter
def snow_turbulence(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_lifetime_min"></a>

#### snow\_lifetime\_min

```python
@property
def snow_lifetime_min() -> float
```

(float):  [Read-Write] Minimum lifetime of a single snowflake. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_lifetime_min"></a>

#### snow\_lifetime\_min

```python
@snow_lifetime_min.setter
def snow_lifetime_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_lifetime_max"></a>

#### snow\_lifetime\_max

```python
@property
def snow_lifetime_max() -> float
```

(float):  [Read-Write] Maximum lifetime of a single snowflake. Can affect the performance.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_lifetime_max"></a>

#### snow\_lifetime\_max

```python
@snow_lifetime_max.setter
def snow_lifetime_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_size_min"></a>

#### snow\_size\_min

```python
@property
def snow_size_min() -> float
```

(float):  [Read-Write] Minimum size of a single snowflake.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_size_min"></a>

#### snow\_size\_min

```python
@snow_size_min.setter
def snow_size_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.snow_size_max"></a>

#### snow\_size\_max

```python
@property
def snow_size_max() -> float
```

(float):  [Read-Write] Maximum size of a single snowflake.

<a id="unreal.SkyCreatorWeatherFXSettings.snow_size_max"></a>

#### snow\_size\_max

```python
@snow_size_max.setter
def snow_size_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.enable_lightnings"></a>

#### enable\_lightnings

```python
@property
def enable_lightnings() -> bool
```

(bool):  [Read-Write] Whether to enable Lightnings.

<a id="unreal.SkyCreatorWeatherFXSettings.enable_lightnings"></a>

#### enable\_lightnings

```python
@enable_lightnings.setter
def enable_lightnings(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_spawn_interval_min"></a>

#### lightning\_spawn\_interval\_min

```python
@property
def lightning_spawn_interval_min() -> float
```

(float):  [Read-Write] Minimum interval to randomly spawn Lightning in seconds.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_spawn_interval_min"></a>

#### lightning\_spawn\_interval\_min

```python
@lightning_spawn_interval_min.setter
def lightning_spawn_interval_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_spawn_interval_max"></a>

#### lightning\_spawn\_interval\_max

```python
@property
def lightning_spawn_interval_max() -> float
```

(float):  [Read-Write] Maximum interval to randomly spawn Lightning in seconds.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_spawn_interval_max"></a>

#### lightning\_spawn\_interval\_max

```python
@lightning_spawn_interval_max.setter
def lightning_spawn_interval_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_color_min"></a>

#### lightning\_color\_min

```python
@property
def lightning_color_min() -> LinearColor
```

(LinearColor):  [Read-Write] Minimum Lightning color.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_color_min"></a>

#### lightning\_color\_min

```python
@lightning_color_min.setter
def lightning_color_min(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_color_max"></a>

#### lightning\_color\_max

```python
@property
def lightning_color_max() -> LinearColor
```

(LinearColor):  [Read-Write] Maximum Lightning color.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_color_max"></a>

#### lightning\_color\_max

```python
@lightning_color_max.setter
def lightning_color_max(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_lifetime"></a>

#### lightning\_lifetime

```python
@property
def lightning_lifetime() -> float
```

(float):  [Read-Write] Lightning lifetime in seconds.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_lifetime"></a>

#### lightning\_lifetime

```python
@lightning_lifetime.setter
def lightning_lifetime(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_spawn_chance"></a>

#### lightning\_bolt\_spawn\_chance

```python
@property
def lightning_bolt_spawn_chance() -> float
```

(float):  [Read-Write] Chance of spawning a Lightning Bolt when spawning a Lightning.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_spawn_chance"></a>

#### lightning\_bolt\_spawn\_chance

```python
@lightning_bolt_spawn_chance.setter
def lightning_bolt_spawn_chance(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_width_min"></a>

#### lightning\_bolt\_width\_min

```python
@property
def lightning_bolt_width_min() -> float
```

(float):  [Read-Write] Minimum width of a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_width_min"></a>

#### lightning\_bolt\_width\_min

```python
@lightning_bolt_width_min.setter
def lightning_bolt_width_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_width_max"></a>

#### lightning\_bolt\_width\_max

```python
@property
def lightning_bolt_width_max() -> float
```

(float):  [Read-Write] Maximum width of a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_width_max"></a>

#### lightning\_bolt\_width\_max

```python
@lightning_bolt_width_max.setter
def lightning_bolt_width_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_length_min"></a>

#### lightning\_bolt\_length\_min

```python
@property
def lightning_bolt_length_min() -> float
```

(float):  [Read-Write] Minimum length of a Lightning Bolt (in kilometers).

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_length_min"></a>

#### lightning\_bolt\_length\_min

```python
@lightning_bolt_length_min.setter
def lightning_bolt_length_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_length_max"></a>

#### lightning\_bolt\_length\_max

```python
@property
def lightning_bolt_length_max() -> float
```

(float):  [Read-Write] Maximum length of a Lightning Bolt (in kilometers).

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_length_max"></a>

#### lightning\_bolt\_length\_max

```python
@lightning_bolt_length_max.setter
def lightning_bolt_length_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_frequency"></a>

#### lightning\_bolt\_curve\_frequency

```python
@property
def lightning_bolt_curve_frequency() -> float
```

(float):  [Read-Write] Frequency of a Lightning Bolt curvature.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_frequency"></a>

#### lightning\_bolt\_curve\_frequency

```python
@lightning_bolt_curve_frequency.setter
def lightning_bolt_curve_frequency(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_strength_min"></a>

#### lightning\_bolt\_curve\_strength\_min

```python
@property
def lightning_bolt_curve_strength_min() -> float
```

(float):  [Read-Write] Minimum strength of a Lightning Bolt curvature.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_strength_min"></a>

#### lightning\_bolt\_curve\_strength\_min

```python
@lightning_bolt_curve_strength_min.setter
def lightning_bolt_curve_strength_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_strength_max"></a>

#### lightning\_bolt\_curve\_strength\_max

```python
@property
def lightning_bolt_curve_strength_max() -> float
```

(float):  [Read-Write] Maximum strength of a Lightning Bolt curvature.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_curve_strength_max"></a>

#### lightning\_bolt\_curve\_strength\_max

```python
@lightning_bolt_curve_strength_max.setter
def lightning_bolt_curve_strength_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_jitter_strength"></a>

#### lightning\_bolt\_jitter\_strength

```python
@property
def lightning_bolt_jitter_strength() -> float
```

(float):  [Read-Write] Jitter strength of a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_bolt_jitter_strength"></a>

#### lightning\_bolt\_jitter\_strength

```python
@lightning_bolt_jitter_strength.setter
def lightning_bolt_jitter_strength(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_branch_spawn_chance"></a>

#### lightning\_branch\_spawn\_chance

```python
@property
def lightning_branch_spawn_chance() -> float
```

(float):  [Read-Write] Chance of spawning a Lightning Branch when spawning a Lightning Bolt.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_branch_spawn_chance"></a>

#### lightning\_branch\_spawn\_chance

```python
@lightning_branch_spawn_chance.setter
def lightning_branch_spawn_chance(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_branch_scale_min"></a>

#### lightning\_branch\_scale\_min

```python
@property
def lightning_branch_scale_min() -> float
```

(float):  [Read-Write] Minimum scale of a Lightning Branch.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_branch_scale_min"></a>

#### lightning\_branch\_scale\_min

```python
@lightning_branch_scale_min.setter
def lightning_branch_scale_min(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_branch_scale_max"></a>

#### lightning\_branch\_scale\_max

```python
@property
def lightning_branch_scale_max() -> float
```

(float):  [Read-Write] Maximum scale of a Lightning Branch.

<a id="unreal.SkyCreatorWeatherFXSettings.lightning_branch_scale_max"></a>

#### lightning\_branch\_scale\_max

```python
@lightning_branch_scale_max.setter
def lightning_branch_scale_max(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_amount"></a>

#### rainbow\_amount

```python
@property
def rainbow_amount() -> float
```

(float):  [Read-Write] Rainbow Amount.

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_amount"></a>

#### rainbow\_amount

```python
@rainbow_amount.setter
def rainbow_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_color"></a>

#### rainbow\_color

```python
@property
def rainbow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Rainbow Tint Color.

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_color"></a>

#### rainbow\_color

```python
@rainbow_color.setter
def rainbow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_radius"></a>

#### rainbow\_radius

```python
@property
def rainbow_radius() -> float
```

(float):  [Read-Write] Radius of the Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_radius"></a>

#### rainbow\_radius

```python
@rainbow_radius.setter
def rainbow_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_thickness"></a>

#### rainbow\_thickness

```python
@property
def rainbow_thickness() -> float
```

(float):  [Read-Write] Thickness of the Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings.rainbow_thickness"></a>

#### rainbow\_thickness

```python
@rainbow_thickness.setter
def rainbow_thickness(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_color"></a>

#### secondary\_rainbow\_color

```python
@property
def secondary_rainbow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Secondary Rainbow Tint Color.

<a id="unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_color"></a>

#### secondary\_rainbow\_color

```python
@secondary_rainbow_color.setter
def secondary_rainbow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_radius"></a>

#### secondary\_rainbow\_radius

```python
@property
def secondary_rainbow_radius() -> float
```

(float):  [Read-Write] Radius of the Secondary Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_radius"></a>

#### secondary\_rainbow\_radius

```python
@secondary_rainbow_radius.setter
def secondary_rainbow_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_thickness"></a>

#### secondary\_rainbow\_thickness

```python
@property
def secondary_rainbow_thickness() -> float
```

(float):  [Read-Write] Thickness of the Secondary Rainbow.

<a id="unreal.SkyCreatorWeatherFXSettings.secondary_rainbow_thickness"></a>

#### secondary\_rainbow\_thickness

```python
@secondary_rainbow_thickness.setter
def secondary_rainbow_thickness(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings"></a>