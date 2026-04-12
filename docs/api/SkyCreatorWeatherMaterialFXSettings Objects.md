## SkyCreatorWeatherMaterialFXSettings Objects

```python
class SkyCreatorWeatherMaterialFXSettings(StructBase)
```

Sky Creator Weather Material FXSettings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``puddles_amount`` (float):  [Read-Write] Puddles Coverage Amount.
- ``puddles_color`` (LinearColor):  [Read-Write] Puddles Coverage Color.
- ``rain_ripples_amount`` (float):  [Read-Write] Rain Ripples Amount.
- ``rain_ripples_damping`` (float):  [Read-Write] Damping of Rain Ripples. Higher values are fading Rain Ripples faster.
- ``rain_ripples_force_max_radius`` (float):  [Read-Write] Max Force Radius to write by the Rain Ripples Solver.
- ``rain_ripples_force_min_radius`` (float):  [Read-Write] Min Force Radius to write by the Rain Ripples Solver.
- ``rain_ripples_intensity`` (float):  [Read-Write] Rain Ripples normap map intensity.
- ``rain_ripples_rings_delay`` (float):  [Read-Write] Delay of Rain Ripples Rings propagation. Number represents Rain Ripples Solver frames to skip.
- ``rain_ripples_rings_number`` (float):  [Read-Write] Number of Rain Ripples Rings to propagate by a single raindrop.
- ``snow_amount`` (float):  [Read-Write] Snow Coverage Amount.
- ``snow_color`` (LinearColor):  [Read-Write] Snow Coverage Color.
- ``snow_intensity`` (float):  [Read-Write] Snow normap map intensity.
- ``snow_sparkles_threshold`` (float):  [Read-Write] Snow Sparkles Threshold. Lower values exposes more sparkles.
- ``wetness_amount`` (float):  [Read-Write] Wetness Amount.
- ``wetness_color`` (LinearColor):  [Read-Write] Wetness Color.
- ``wind_ripples_intensity`` (float):  [Read-Write] Wind Ripples normap map intensity.
- ``wind_ripples_speed`` (float):  [Read-Write] Speed of the Wind Ripples.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(wetness_amount: float = 0.000000,
             wetness_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             puddles_amount: float = 0.000000,
             puddles_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             rain_ripples_amount: float = 0.000000,
             rain_ripples_intensity: float = 0.000000,
             rain_ripples_force_min_radius: float = 0.000000,
             rain_ripples_force_max_radius: float = 0.000000,
             rain_ripples_rings_number: float = 0.000000,
             rain_ripples_rings_delay: float = 0.000000,
             rain_ripples_damping: float = 0.000000,
             wind_ripples_intensity: float = 0.000000,
             wind_ripples_speed: float = 0.000000,
             snow_amount: float = 0.000000,
             snow_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             snow_intensity: float = 0.000000,
             snow_sparkles_threshold: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wetness_amount"></a>

#### wetness\_amount

```python
@property
def wetness_amount() -> float
```

(float):  [Read-Write] Wetness Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wetness_amount"></a>

#### wetness\_amount

```python
@wetness_amount.setter
def wetness_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wetness_color"></a>

#### wetness\_color

```python
@property
def wetness_color() -> LinearColor
```

(LinearColor):  [Read-Write] Wetness Color.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wetness_color"></a>

#### wetness\_color

```python
@wetness_color.setter
def wetness_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.puddles_amount"></a>

#### puddles\_amount

```python
@property
def puddles_amount() -> float
```

(float):  [Read-Write] Puddles Coverage Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.puddles_amount"></a>

#### puddles\_amount

```python
@puddles_amount.setter
def puddles_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.puddles_color"></a>

#### puddles\_color

```python
@property
def puddles_color() -> LinearColor
```

(LinearColor):  [Read-Write] Puddles Coverage Color.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.puddles_color"></a>

#### puddles\_color

```python
@puddles_color.setter
def puddles_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_amount"></a>

#### rain\_ripples\_amount

```python
@property
def rain_ripples_amount() -> float
```

(float):  [Read-Write] Rain Ripples Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_amount"></a>

#### rain\_ripples\_amount

```python
@rain_ripples_amount.setter
def rain_ripples_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_intensity"></a>

#### rain\_ripples\_intensity

```python
@property
def rain_ripples_intensity() -> float
```

(float):  [Read-Write] Rain Ripples normap map intensity.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_intensity"></a>

#### rain\_ripples\_intensity

```python
@rain_ripples_intensity.setter
def rain_ripples_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_force_min_radius"></a>

#### rain\_ripples\_force\_min\_radius

```python
@property
def rain_ripples_force_min_radius() -> float
```

(float):  [Read-Write] Min Force Radius to write by the Rain Ripples Solver.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_force_min_radius"></a>

#### rain\_ripples\_force\_min\_radius

```python
@rain_ripples_force_min_radius.setter
def rain_ripples_force_min_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_force_max_radius"></a>

#### rain\_ripples\_force\_max\_radius

```python
@property
def rain_ripples_force_max_radius() -> float
```

(float):  [Read-Write] Max Force Radius to write by the Rain Ripples Solver.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_force_max_radius"></a>

#### rain\_ripples\_force\_max\_radius

```python
@rain_ripples_force_max_radius.setter
def rain_ripples_force_max_radius(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_rings_number"></a>

#### rain\_ripples\_rings\_number

```python
@property
def rain_ripples_rings_number() -> float
```

(float):  [Read-Write] Number of Rain Ripples Rings to propagate by a single raindrop.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_rings_number"></a>

#### rain\_ripples\_rings\_number

```python
@rain_ripples_rings_number.setter
def rain_ripples_rings_number(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_rings_delay"></a>

#### rain\_ripples\_rings\_delay

```python
@property
def rain_ripples_rings_delay() -> float
```

(float):  [Read-Write] Delay of Rain Ripples Rings propagation. Number represents Rain Ripples Solver frames to skip.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_rings_delay"></a>

#### rain\_ripples\_rings\_delay

```python
@rain_ripples_rings_delay.setter
def rain_ripples_rings_delay(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_damping"></a>

#### rain\_ripples\_damping

```python
@property
def rain_ripples_damping() -> float
```

(float):  [Read-Write] Damping of Rain Ripples. Higher values are fading Rain Ripples faster.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.rain_ripples_damping"></a>

#### rain\_ripples\_damping

```python
@rain_ripples_damping.setter
def rain_ripples_damping(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wind_ripples_intensity"></a>

#### wind\_ripples\_intensity

```python
@property
def wind_ripples_intensity() -> float
```

(float):  [Read-Write] Wind Ripples normap map intensity.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wind_ripples_intensity"></a>

#### wind\_ripples\_intensity

```python
@wind_ripples_intensity.setter
def wind_ripples_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wind_ripples_speed"></a>

#### wind\_ripples\_speed

```python
@property
def wind_ripples_speed() -> float
```

(float):  [Read-Write] Speed of the Wind Ripples.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.wind_ripples_speed"></a>

#### wind\_ripples\_speed

```python
@wind_ripples_speed.setter
def wind_ripples_speed(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_amount"></a>

#### snow\_amount

```python
@property
def snow_amount() -> float
```

(float):  [Read-Write] Snow Coverage Amount.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_amount"></a>

#### snow\_amount

```python
@snow_amount.setter
def snow_amount(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_color"></a>

#### snow\_color

```python
@property
def snow_color() -> LinearColor
```

(LinearColor):  [Read-Write] Snow Coverage Color.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_color"></a>

#### snow\_color

```python
@snow_color.setter
def snow_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_intensity"></a>

#### snow\_intensity

```python
@property
def snow_intensity() -> float
```

(float):  [Read-Write] Snow normap map intensity.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_intensity"></a>

#### snow\_intensity

```python
@snow_intensity.setter
def snow_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_sparkles_threshold"></a>

#### snow\_sparkles\_threshold

```python
@property
def snow_sparkles_threshold() -> float
```

(float):  [Read-Write] Snow Sparkles Threshold. Lower values exposes more sparkles.

<a id="unreal.SkyCreatorWeatherMaterialFXSettings.snow_sparkles_threshold"></a>

#### snow\_sparkles\_threshold

```python
@snow_sparkles_threshold.setter
def snow_sparkles_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings"></a>