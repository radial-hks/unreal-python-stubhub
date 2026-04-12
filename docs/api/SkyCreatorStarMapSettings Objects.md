## SkyCreatorStarMapSettings Objects

```python
class SkyCreatorStarMapSettings(StructBase)
```

Sky Creator Star Map Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``night_horizon_color`` (LinearColor):  [Read-Write] Color tint of the horizon.
- ``night_zenith_color`` (LinearColor):  [Read-Write] Color tint of the zenith.
- ``star_map_atmosphere_threshold`` (float):  [Read-Write] Indicates how strong the star map can be faded into atmosphere.
  Lower values cause more stars appear at brighter points in atmosphere, e.g. at daytime.
- ``star_map_color_tint`` (LinearColor):  [Read-Write] Overall color tint of the Star Map.
- ``star_map_horizon_threshold`` (float):  [Read-Write] Indicates how strong the star map can be faded into horizon.
  Lower values cause more stars appear at horizon.
- ``star_map_intensity`` (float):  [Read-Write] Overall brightness of the Star Map.
- ``star_map_twinkle_intensity`` (float):  [Read-Write] Intensity of twinkling stars.
- ``star_map_twinkle_saturation`` (float):  [Read-Write] Saturation of twinkling stars.
- ``star_map_twinkle_speed`` (float):  [Read-Write] Twinkle speed of stars.

<a id="unreal.SkyCreatorStarMapSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    star_map_intensity: float = 0.000000,
    star_map_color_tint: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    star_map_twinkle_intensity: float = 0.000000,
    star_map_twinkle_saturation: float = 0.000000,
    star_map_twinkle_speed: float = 0.000000,
    star_map_horizon_threshold: float = 0.000000,
    star_map_atmosphere_threshold: float = 0.000000,
    night_horizon_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    night_zenith_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]
) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.star_map_intensity"></a>

#### star\_map\_intensity

```python
@property
def star_map_intensity() -> float
```

(float):  [Read-Write] Overall brightness of the Star Map.

<a id="unreal.SkyCreatorStarMapSettings.star_map_intensity"></a>

#### star\_map\_intensity

```python
@star_map_intensity.setter
def star_map_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.star_map_color_tint"></a>

#### star\_map\_color\_tint

```python
@property
def star_map_color_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Overall color tint of the Star Map.

<a id="unreal.SkyCreatorStarMapSettings.star_map_color_tint"></a>

#### star\_map\_color\_tint

```python
@star_map_color_tint.setter
def star_map_color_tint(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.star_map_twinkle_intensity"></a>

#### star\_map\_twinkle\_intensity

```python
@property
def star_map_twinkle_intensity() -> float
```

(float):  [Read-Write] Intensity of twinkling stars.

<a id="unreal.SkyCreatorStarMapSettings.star_map_twinkle_intensity"></a>

#### star\_map\_twinkle\_intensity

```python
@star_map_twinkle_intensity.setter
def star_map_twinkle_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.star_map_twinkle_saturation"></a>

#### star\_map\_twinkle\_saturation

```python
@property
def star_map_twinkle_saturation() -> float
```

(float):  [Read-Write] Saturation of twinkling stars.

<a id="unreal.SkyCreatorStarMapSettings.star_map_twinkle_saturation"></a>

#### star\_map\_twinkle\_saturation

```python
@star_map_twinkle_saturation.setter
def star_map_twinkle_saturation(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.star_map_twinkle_speed"></a>

#### star\_map\_twinkle\_speed

```python
@property
def star_map_twinkle_speed() -> float
```

(float):  [Read-Write] Twinkle speed of stars.

<a id="unreal.SkyCreatorStarMapSettings.star_map_twinkle_speed"></a>

#### star\_map\_twinkle\_speed

```python
@star_map_twinkle_speed.setter
def star_map_twinkle_speed(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.star_map_horizon_threshold"></a>

#### star\_map\_horizon\_threshold

```python
@property
def star_map_horizon_threshold() -> float
```

(float):  [Read-Write] Indicates how strong the star map can be faded into horizon.
Lower values cause more stars appear at horizon.

<a id="unreal.SkyCreatorStarMapSettings.star_map_horizon_threshold"></a>

#### star\_map\_horizon\_threshold

```python
@star_map_horizon_threshold.setter
def star_map_horizon_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.star_map_atmosphere_threshold"></a>

#### star\_map\_atmosphere\_threshold

```python
@property
def star_map_atmosphere_threshold() -> float
```

(float):  [Read-Write] Indicates how strong the star map can be faded into atmosphere.
Lower values cause more stars appear at brighter points in atmosphere, e.g. at daytime.

<a id="unreal.SkyCreatorStarMapSettings.star_map_atmosphere_threshold"></a>

#### star\_map\_atmosphere\_threshold

```python
@star_map_atmosphere_threshold.setter
def star_map_atmosphere_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.night_horizon_color"></a>

#### night\_horizon\_color

```python
@property
def night_horizon_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color tint of the horizon.

<a id="unreal.SkyCreatorStarMapSettings.night_horizon_color"></a>

#### night\_horizon\_color

```python
@night_horizon_color.setter
def night_horizon_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorStarMapSettings.night_zenith_color"></a>

#### night\_zenith\_color

```python
@property
def night_zenith_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color tint of the zenith.

<a id="unreal.SkyCreatorStarMapSettings.night_zenith_color"></a>

#### night\_zenith\_color

```python
@night_zenith_color.setter
def night_zenith_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorWeatherFXSettings"></a>