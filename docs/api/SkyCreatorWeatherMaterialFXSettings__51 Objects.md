## SkyCreatorWeatherMaterialFXSettings\_51 Objects

```python
class SkyCreatorWeatherMaterialFXSettings_51(StructBase)
```

天气特效材质设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``puddles_amount`` (float):  [Read-Write] Puddles Coverage Amount.
- ``puddles_amount_curve`` (CurveFloat):  [Read-Write]
- ``puddles_color`` (LinearColor):  [Read-Write] Puddles Coverage Color.
- ``puddles_color_curve`` (CurveLinearColor):  [Read-Write]
- ``rain_ripples_amount`` (float):  [Read-Write] Rain Ripples Amount.
- ``rain_ripples_amount_curve`` (CurveFloat):  [Read-Write]
- ``rain_ripples_damping`` (float):  [Read-Write] Damping of Rain Ripples. Higher values are fading Rain Ripples faster.
- ``rain_ripples_damping_curve`` (CurveFloat):  [Read-Write]
- ``rain_ripples_force_max_radius`` (float):  [Read-Write] Max Force Radius to write by the Rain Ripples Solver.
- ``rain_ripples_force_max_radius_curve`` (CurveFloat):  [Read-Write]
- ``rain_ripples_force_min_radius`` (float):  [Read-Write] Min Force Radius to write by the Rain Ripples Solver.
- ``rain_ripples_force_min_radius_curve`` (CurveFloat):  [Read-Write]
- ``rain_ripples_intensity`` (float):  [Read-Write] Rain Ripples normap map intensity.
- ``rain_ripples_intensity_curve`` (CurveFloat):  [Read-Write]
- ``rain_ripples_rings_delay`` (float):  [Read-Write] Delay of Rain Ripples Rings propagation. Number represents Rain Ripples Solver frames to skip.
- ``rain_ripples_rings_delay_curve`` (CurveFloat):  [Read-Write]
- ``rain_ripples_rings_number`` (float):  [Read-Write] Number of Rain Ripples Rings to propagate by a single raindrop.
- ``rain_ripples_rings_number_curve`` (CurveFloat):  [Read-Write]
- ``snow_amount`` (float):  [Read-Write] Snow Coverage Amount.
- ``snow_amount_curve`` (CurveFloat):  [Read-Write]
- ``snow_color`` (LinearColor):  [Read-Write] Snow Coverage Color.
- ``snow_color_curve`` (CurveLinearColor):  [Read-Write]
- ``snow_intensity`` (float):  [Read-Write] Snow normap map intensity.
- ``snow_intensity_curve`` (CurveFloat):  [Read-Write]
- ``snow_sparkles_threshold`` (float):  [Read-Write] Snow Sparkles Threshold. Lower values exposes more sparkles.
- ``snow_sparkles_threshold_curve`` (CurveFloat):  [Read-Write]
- ``use_puddles_amount`` (bool):  [Read-Write]
- ``use_puddles_color`` (bool):  [Read-Write]
- ``use_rain_ripples_amount`` (bool):  [Read-Write]
- ``use_rain_ripples_damping`` (bool):  [Read-Write]
- ``use_rain_ripples_force_max_radius`` (bool):  [Read-Write]
- ``use_rain_ripples_force_min_radius`` (bool):  [Read-Write]
- ``use_rain_ripples_intensity`` (bool):  [Read-Write]
- ``use_rain_ripples_rings_delay`` (bool):  [Read-Write]
- ``use_rain_ripples_rings_number`` (bool):  [Read-Write]
- ``use_snow_amount`` (bool):  [Read-Write]
- ``use_snow_color`` (bool):  [Read-Write]
- ``use_snow_intensity`` (bool):  [Read-Write]
- ``use_snow_sparkles_threshold`` (bool):  [Read-Write]
- ``use_wetness_amount`` (bool):  [Read-Write]
- ``use_wetness_color`` (bool):  [Read-Write]
- ``use_wind_ripples_intensity`` (bool):  [Read-Write]
- ``use_wind_ripples_speed`` (bool):  [Read-Write]
- ``wetness_amount`` (float):  [Read-Write] Wetness Amount.
- ``wetness_amount_curve`` (CurveFloat):  [Read-Write]
- ``wetness_color`` (LinearColor):  [Read-Write] Wetness Color.
- ``wetness_color_curve`` (CurveLinearColor):  [Read-Write]
- ``wind_ripples_intensity`` (float):  [Read-Write] Wind Ripples normap map intensity.
- ``wind_ripples_intensity_curve`` (CurveFloat):  [Read-Write]
- ``wind_ripples_speed`` (float):  [Read-Write] Speed of the Wind Ripples.
- ``wind_ripples_speed_curve`` (CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_wetness_amount: bool = False,
             wetness_amount: float = 0.000000,
             wetness_amount_curve: CurveFloat = None,
             use_wetness_color: bool = False,
             wetness_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             wetness_color_curve: CurveLinearColor = None,
             use_puddles_amount: bool = False,
             puddles_amount: float = 0.000000,
             puddles_amount_curve: CurveFloat = None,
             use_puddles_color: bool = False,
             puddles_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             puddles_color_curve: CurveLinearColor = None,
             use_rain_ripples_amount: bool = False,
             rain_ripples_amount: float = 0.000000,
             rain_ripples_amount_curve: CurveFloat = None,
             use_rain_ripples_intensity: bool = False,
             rain_ripples_intensity: float = 0.000000,
             rain_ripples_intensity_curve: CurveFloat = None,
             use_rain_ripples_force_min_radius: bool = False,
             rain_ripples_force_min_radius: float = 0.000000,
             rain_ripples_force_min_radius_curve: CurveFloat = None,
             use_rain_ripples_force_max_radius: bool = False,
             rain_ripples_force_max_radius: float = 0.000000,
             rain_ripples_force_max_radius_curve: CurveFloat = None,
             use_rain_ripples_rings_number: bool = False,
             rain_ripples_rings_number: float = 0.000000,
             rain_ripples_rings_number_curve: CurveFloat = None,
             use_rain_ripples_rings_delay: bool = False,
             rain_ripples_rings_delay: float = 0.000000,
             rain_ripples_rings_delay_curve: CurveFloat = None,
             use_rain_ripples_damping: bool = False,
             rain_ripples_damping: float = 0.000000,
             rain_ripples_damping_curve: CurveFloat = None,
             use_wind_ripples_intensity: bool = False,
             wind_ripples_intensity: float = 0.000000,
             wind_ripples_intensity_curve: CurveFloat = None,
             use_wind_ripples_speed: bool = False,
             wind_ripples_speed: float = 0.000000,
             wind_ripples_speed_curve: CurveFloat = None,
             use_snow_amount: bool = False,
             snow_amount: float = 0.000000,
             snow_amount_curve: CurveFloat = None,
             use_snow_color: bool = False,
             snow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             snow_color_curve: CurveLinearColor = None,
             use_snow_intensity: bool = False,
             snow_intensity: float = 0.000000,
             snow_intensity_curve: CurveFloat = None,
             use_snow_sparkles_threshold: bool = False,
             snow_sparkles_threshold: float = 0.000000,
             snow_sparkles_threshold_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wetness_amount"></a>

#### use\_wetness\_amount

```python
@property
def use_wetness_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wetness_amount"></a>

#### use\_wetness\_amount

```python
@use_wetness_amount.setter
def use_wetness_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_amount"></a>

#### wetness\_amount

```python
@property
def wetness_amount() -> float
```

(float):  [Read-Write] Wetness Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_amount"></a>

#### wetness\_amount

```python
@wetness_amount.setter
def wetness_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_amount_curve"></a>

#### wetness\_amount\_curve

```python
@property
def wetness_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_amount_curve"></a>

#### wetness\_amount\_curve

```python
@wetness_amount_curve.setter
def wetness_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wetness_color"></a>

#### use\_wetness\_color

```python
@property
def use_wetness_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wetness_color"></a>

#### use\_wetness\_color

```python
@use_wetness_color.setter
def use_wetness_color(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_color"></a>

#### wetness\_color

```python
@property
def wetness_color() -> LinearColor
```

(LinearColor):  [Read-Write] Wetness Color.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_color"></a>

#### wetness\_color

```python
@wetness_color.setter
def wetness_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_color_curve"></a>

#### wetness\_color\_curve

```python
@property
def wetness_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wetness_color_curve"></a>

#### wetness\_color\_curve

```python
@wetness_color_curve.setter
def wetness_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_puddles_amount"></a>

#### use\_puddles\_amount

```python
@property
def use_puddles_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_puddles_amount"></a>

#### use\_puddles\_amount

```python
@use_puddles_amount.setter
def use_puddles_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_amount"></a>

#### puddles\_amount

```python
@property
def puddles_amount() -> float
```

(float):  [Read-Write] Puddles Coverage Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_amount"></a>

#### puddles\_amount

```python
@puddles_amount.setter
def puddles_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_amount_curve"></a>

#### puddles\_amount\_curve

```python
@property
def puddles_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_amount_curve"></a>

#### puddles\_amount\_curve

```python
@puddles_amount_curve.setter
def puddles_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_puddles_color"></a>

#### use\_puddles\_color

```python
@property
def use_puddles_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_puddles_color"></a>

#### use\_puddles\_color

```python
@use_puddles_color.setter
def use_puddles_color(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_color"></a>

#### puddles\_color

```python
@property
def puddles_color() -> LinearColor
```

(LinearColor):  [Read-Write] Puddles Coverage Color.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_color"></a>

#### puddles\_color

```python
@puddles_color.setter
def puddles_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_color_curve"></a>

#### puddles\_color\_curve

```python
@property
def puddles_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.puddles_color_curve"></a>

#### puddles\_color\_curve

```python
@puddles_color_curve.setter
def puddles_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_amount"></a>

#### use\_rain\_ripples\_amount

```python
@property
def use_rain_ripples_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_amount"></a>

#### use\_rain\_ripples\_amount

```python
@use_rain_ripples_amount.setter
def use_rain_ripples_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_amount"></a>

#### rain\_ripples\_amount

```python
@property
def rain_ripples_amount() -> float
```

(float):  [Read-Write] Rain Ripples Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_amount"></a>

#### rain\_ripples\_amount

```python
@rain_ripples_amount.setter
def rain_ripples_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_amount_curve"></a>

#### rain\_ripples\_amount\_curve

```python
@property
def rain_ripples_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_amount_curve"></a>

#### rain\_ripples\_amount\_curve

```python
@rain_ripples_amount_curve.setter
def rain_ripples_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_intensity"></a>

#### use\_rain\_ripples\_intensity

```python
@property
def use_rain_ripples_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_intensity"></a>

#### use\_rain\_ripples\_intensity

```python
@use_rain_ripples_intensity.setter
def use_rain_ripples_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_intensity"></a>

#### rain\_ripples\_intensity

```python
@property
def rain_ripples_intensity() -> float
```

(float):  [Read-Write] Rain Ripples normap map intensity.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_intensity"></a>

#### rain\_ripples\_intensity

```python
@rain_ripples_intensity.setter
def rain_ripples_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_intensity_curve"></a>

#### rain\_ripples\_intensity\_curve

```python
@property
def rain_ripples_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_intensity_curve"></a>

#### rain\_ripples\_intensity\_curve

```python
@rain_ripples_intensity_curve.setter
def rain_ripples_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_force_min_radius"></a>

#### use\_rain\_ripples\_force\_min\_radius

```python
@property
def use_rain_ripples_force_min_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_force_min_radius"></a>

#### use\_rain\_ripples\_force\_min\_radius

```python
@use_rain_ripples_force_min_radius.setter
def use_rain_ripples_force_min_radius(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_min_radius"></a>

#### rain\_ripples\_force\_min\_radius

```python
@property
def rain_ripples_force_min_radius() -> float
```

(float):  [Read-Write] Min Force Radius to write by the Rain Ripples Solver.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_min_radius"></a>

#### rain\_ripples\_force\_min\_radius

```python
@rain_ripples_force_min_radius.setter
def rain_ripples_force_min_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_min_radius_curve"></a>

#### rain\_ripples\_force\_min\_radius\_curve

```python
@property
def rain_ripples_force_min_radius_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_min_radius_curve"></a>

#### rain\_ripples\_force\_min\_radius\_curve

```python
@rain_ripples_force_min_radius_curve.setter
def rain_ripples_force_min_radius_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_force_max_radius"></a>

#### use\_rain\_ripples\_force\_max\_radius

```python
@property
def use_rain_ripples_force_max_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_force_max_radius"></a>

#### use\_rain\_ripples\_force\_max\_radius

```python
@use_rain_ripples_force_max_radius.setter
def use_rain_ripples_force_max_radius(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_max_radius"></a>

#### rain\_ripples\_force\_max\_radius

```python
@property
def rain_ripples_force_max_radius() -> float
```

(float):  [Read-Write] Max Force Radius to write by the Rain Ripples Solver.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_max_radius"></a>

#### rain\_ripples\_force\_max\_radius

```python
@rain_ripples_force_max_radius.setter
def rain_ripples_force_max_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_max_radius_curve"></a>

#### rain\_ripples\_force\_max\_radius\_curve

```python
@property
def rain_ripples_force_max_radius_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_force_max_radius_curve"></a>

#### rain\_ripples\_force\_max\_radius\_curve

```python
@rain_ripples_force_max_radius_curve.setter
def rain_ripples_force_max_radius_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_rings_number"></a>

#### use\_rain\_ripples\_rings\_number

```python
@property
def use_rain_ripples_rings_number() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_rings_number"></a>

#### use\_rain\_ripples\_rings\_number

```python
@use_rain_ripples_rings_number.setter
def use_rain_ripples_rings_number(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_number"></a>

#### rain\_ripples\_rings\_number

```python
@property
def rain_ripples_rings_number() -> float
```

(float):  [Read-Write] Number of Rain Ripples Rings to propagate by a single raindrop.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_number"></a>

#### rain\_ripples\_rings\_number

```python
@rain_ripples_rings_number.setter
def rain_ripples_rings_number(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_number_curve"></a>

#### rain\_ripples\_rings\_number\_curve

```python
@property
def rain_ripples_rings_number_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_number_curve"></a>

#### rain\_ripples\_rings\_number\_curve

```python
@rain_ripples_rings_number_curve.setter
def rain_ripples_rings_number_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_rings_delay"></a>

#### use\_rain\_ripples\_rings\_delay

```python
@property
def use_rain_ripples_rings_delay() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_rings_delay"></a>

#### use\_rain\_ripples\_rings\_delay

```python
@use_rain_ripples_rings_delay.setter
def use_rain_ripples_rings_delay(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_delay"></a>

#### rain\_ripples\_rings\_delay

```python
@property
def rain_ripples_rings_delay() -> float
```

(float):  [Read-Write] Delay of Rain Ripples Rings propagation. Number represents Rain Ripples Solver frames to skip.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_delay"></a>

#### rain\_ripples\_rings\_delay

```python
@rain_ripples_rings_delay.setter
def rain_ripples_rings_delay(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_delay_curve"></a>

#### rain\_ripples\_rings\_delay\_curve

```python
@property
def rain_ripples_rings_delay_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_rings_delay_curve"></a>

#### rain\_ripples\_rings\_delay\_curve

```python
@rain_ripples_rings_delay_curve.setter
def rain_ripples_rings_delay_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_damping"></a>

#### use\_rain\_ripples\_damping

```python
@property
def use_rain_ripples_damping() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_rain_ripples_damping"></a>

#### use\_rain\_ripples\_damping

```python
@use_rain_ripples_damping.setter
def use_rain_ripples_damping(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_damping"></a>

#### rain\_ripples\_damping

```python
@property
def rain_ripples_damping() -> float
```

(float):  [Read-Write] Damping of Rain Ripples. Higher values are fading Rain Ripples faster.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_damping"></a>

#### rain\_ripples\_damping

```python
@rain_ripples_damping.setter
def rain_ripples_damping(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_damping_curve"></a>

#### rain\_ripples\_damping\_curve

```python
@property
def rain_ripples_damping_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.rain_ripples_damping_curve"></a>

#### rain\_ripples\_damping\_curve

```python
@rain_ripples_damping_curve.setter
def rain_ripples_damping_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wind_ripples_intensity"></a>

#### use\_wind\_ripples\_intensity

```python
@property
def use_wind_ripples_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wind_ripples_intensity"></a>

#### use\_wind\_ripples\_intensity

```python
@use_wind_ripples_intensity.setter
def use_wind_ripples_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_intensity"></a>

#### wind\_ripples\_intensity

```python
@property
def wind_ripples_intensity() -> float
```

(float):  [Read-Write] Wind Ripples normap map intensity.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_intensity"></a>

#### wind\_ripples\_intensity

```python
@wind_ripples_intensity.setter
def wind_ripples_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_intensity_curve"></a>

#### wind\_ripples\_intensity\_curve

```python
@property
def wind_ripples_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_intensity_curve"></a>

#### wind\_ripples\_intensity\_curve

```python
@wind_ripples_intensity_curve.setter
def wind_ripples_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wind_ripples_speed"></a>

#### use\_wind\_ripples\_speed

```python
@property
def use_wind_ripples_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_wind_ripples_speed"></a>

#### use\_wind\_ripples\_speed

```python
@use_wind_ripples_speed.setter
def use_wind_ripples_speed(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_speed"></a>

#### wind\_ripples\_speed

```python
@property
def wind_ripples_speed() -> float
```

(float):  [Read-Write] Speed of the Wind Ripples.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_speed"></a>

#### wind\_ripples\_speed

```python
@wind_ripples_speed.setter
def wind_ripples_speed(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_speed_curve"></a>

#### wind\_ripples\_speed\_curve

```python
@property
def wind_ripples_speed_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.wind_ripples_speed_curve"></a>

#### wind\_ripples\_speed\_curve

```python
@wind_ripples_speed_curve.setter
def wind_ripples_speed_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_amount"></a>

#### use\_snow\_amount

```python
@property
def use_snow_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_amount"></a>

#### use\_snow\_amount

```python
@use_snow_amount.setter
def use_snow_amount(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_amount"></a>

#### snow\_amount

```python
@property
def snow_amount() -> float
```

(float):  [Read-Write] Snow Coverage Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_amount"></a>

#### snow\_amount

```python
@snow_amount.setter
def snow_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_amount_curve"></a>

#### snow\_amount\_curve

```python
@property
def snow_amount_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_amount_curve"></a>

#### snow\_amount\_curve

```python
@snow_amount_curve.setter
def snow_amount_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_color"></a>

#### use\_snow\_color

```python
@property
def use_snow_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_color"></a>

#### use\_snow\_color

```python
@use_snow_color.setter
def use_snow_color(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_color"></a>

#### snow\_color

```python
@property
def snow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Snow Coverage Color.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_color"></a>

#### snow\_color

```python
@snow_color.setter
def snow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_color_curve"></a>

#### snow\_color\_curve

```python
@property
def snow_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_color_curve"></a>

#### snow\_color\_curve

```python
@snow_color_curve.setter
def snow_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_intensity"></a>

#### use\_snow\_intensity

```python
@property
def use_snow_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_intensity"></a>

#### use\_snow\_intensity

```python
@use_snow_intensity.setter
def use_snow_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_intensity"></a>

#### snow\_intensity

```python
@property
def snow_intensity() -> float
```

(float):  [Read-Write] Snow normap map intensity.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_intensity"></a>

#### snow\_intensity

```python
@snow_intensity.setter
def snow_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_intensity_curve"></a>

#### snow\_intensity\_curve

```python
@property
def snow_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_intensity_curve"></a>

#### snow\_intensity\_curve

```python
@snow_intensity_curve.setter
def snow_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_sparkles_threshold"></a>

#### use\_snow\_sparkles\_threshold

```python
@property
def use_snow_sparkles_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.use_snow_sparkles_threshold"></a>

#### use\_snow\_sparkles\_threshold

```python
@use_snow_sparkles_threshold.setter
def use_snow_sparkles_threshold(value: bool) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_sparkles_threshold"></a>

#### snow\_sparkles\_threshold

```python
@property
def snow_sparkles_threshold() -> float
```

(float):  [Read-Write] Snow Sparkles Threshold. Lower values exposes more sparkles.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_sparkles_threshold"></a>

#### snow\_sparkles\_threshold

```python
@snow_sparkles_threshold.setter
def snow_sparkles_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_sparkles_threshold_curve"></a>

#### snow\_sparkles\_threshold\_curve

```python
@property
def snow_sparkles_threshold_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWeatherMaterialFXSettings_51.snow_sparkles_threshold_curve"></a>

#### snow\_sparkles\_threshold\_curve

```python
@snow_sparkles_threshold_curve.setter
def snow_sparkles_threshold_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWindSettings_51"></a>