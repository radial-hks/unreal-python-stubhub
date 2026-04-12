## SkyCreatorExponentialHeightFogSettings Objects

```python
class SkyCreatorExponentialHeightFogSettings(StructBase)
```

Sky Creator Exponential Height Fog Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``directional_inscattering_color`` (LinearColor):  [Read-Write] Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light.
  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
- ``directional_inscattering_exponent`` (float):  [Read-Write] Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.
  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
- ``directional_inscattering_start_distance`` (float):  [Read-Write] Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light.
  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.
- ``fog_density`` (float):  [Read-Write] Global density factor of fog.
- ``fog_height_falloff`` (float):  [Read-Write] Height density factor, controls how the density increases as height decreases.
  Smaller values make the visible transition larger.
- ``fog_inscattering_color`` (LinearColor):  [Read-Write] Fog Inscattering Color.
- ``fog_start_distance`` (float):  [Read-Write] Distance from the camera that the fog will start.
- ``second_fog_density`` (float):  [Read-Write] Global density factor of secondary fog.
- ``second_fog_height_falloff`` (float):  [Read-Write] Height density factor, controls how the density increases as height decreases.
  Smaller values make the visible transition larger.
- ``volumetric_fog_albedo`` (LinearColor):  [Read-Write] The height fog particle reflectiveness used by volumetric fog.
  Water particles in air have an albedo near white, while dust has slightly darker value.
- ``volumetric_fog_emissive`` (LinearColor):  [Read-Write] Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.
  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,
  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all.
- ``volumetric_fog_extinction_scale`` (float):  [Read-Write] Scales the height fog particle extinction amount used by volumetric fog.
  Values larger than 1 cause fog particles everywhere absorb more light.
- ``volumetric_fog_scattering_distribution`` (float):  [Read-Write] Controls the scattering phase function - how much incoming light scatters in various directions.
  A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.
  In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fog_density: float = 0.000000,
             fog_height_falloff: float = 0.000000,
             fog_inscattering_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             fog_start_distance: float = 0.000000,
             second_fog_density: float = 0.000000,
             second_fog_height_falloff: float = 0.000000,
             directional_inscattering_exponent: float = 0.000000,
             directional_inscattering_start_distance: float = 0.000000,
             directional_inscattering_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             volumetric_fog_scattering_distribution: float = 0.000000,
             volumetric_fog_albedo: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             volumetric_fog_emissive: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             volumetric_fog_extinction_scale: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_density"></a>

#### fog\_density

```python
@property
def fog_density() -> float
```

(float):  [Read-Write] Global density factor of fog.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_density"></a>

#### fog\_density

```python
@fog_density.setter
def fog_density(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_height_falloff"></a>

#### fog\_height\_falloff

```python
@property
def fog_height_falloff() -> float
```

(float):  [Read-Write] Height density factor, controls how the density increases as height decreases.
Smaller values make the visible transition larger.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_height_falloff"></a>

#### fog\_height\_falloff

```python
@fog_height_falloff.setter
def fog_height_falloff(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_inscattering_color"></a>

#### fog\_inscattering\_color

```python
@property
def fog_inscattering_color() -> LinearColor
```

(LinearColor):  [Read-Write] Fog Inscattering Color.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_inscattering_color"></a>

#### fog\_inscattering\_color

```python
@fog_inscattering_color.setter
def fog_inscattering_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_start_distance"></a>

#### fog\_start\_distance

```python
@property
def fog_start_distance() -> float
```

(float):  [Read-Write] Distance from the camera that the fog will start.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.fog_start_distance"></a>

#### fog\_start\_distance

```python
@fog_start_distance.setter
def fog_start_distance(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.second_fog_density"></a>

#### second\_fog\_density

```python
@property
def second_fog_density() -> float
```

(float):  [Read-Write] Global density factor of secondary fog.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.second_fog_density"></a>

#### second\_fog\_density

```python
@second_fog_density.setter
def second_fog_density(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.second_fog_height_falloff"></a>

#### second\_fog\_height\_falloff

```python
@property
def second_fog_height_falloff() -> float
```

(float):  [Read-Write] Height density factor, controls how the density increases as height decreases.
Smaller values make the visible transition larger.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.second_fog_height_falloff"></a>

#### second\_fog\_height\_falloff

```python
@second_fog_height_falloff.setter
def second_fog_height_falloff(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_exponent"></a>

#### directional\_inscattering\_exponent

```python
@property
def directional_inscattering_exponent() -> float
```

(float):  [Read-Write] Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.
Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_exponent"></a>

#### directional\_inscattering\_exponent

```python
@directional_inscattering_exponent.setter
def directional_inscattering_exponent(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_start_distance"></a>

#### directional\_inscattering\_start\_distance

```python
@property
def directional_inscattering_start_distance() -> float
```

(float):  [Read-Write] Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light.
Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_start_distance"></a>

#### directional\_inscattering\_start\_distance

```python
@directional_inscattering_start_distance.setter
def directional_inscattering_start_distance(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_color"></a>

#### directional\_inscattering\_color

```python
@property
def directional_inscattering_color() -> LinearColor
```

(LinearColor):  [Read-Write] Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light.
Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.directional_inscattering_color"></a>

#### directional\_inscattering\_color

```python
@directional_inscattering_color.setter
def directional_inscattering_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_scattering_distribution"></a>

#### volumetric\_fog\_scattering\_distribution

```python
@property
def volumetric_fog_scattering_distribution() -> float
```

(float):  [Read-Write] Controls the scattering phase function - how much incoming light scatters in various directions.
A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.
In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_scattering_distribution"></a>

#### volumetric\_fog\_scattering\_distribution

```python
@volumetric_fog_scattering_distribution.setter
def volumetric_fog_scattering_distribution(value: float) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_albedo"></a>

#### volumetric\_fog\_albedo

```python
@property
def volumetric_fog_albedo() -> LinearColor
```

(LinearColor):  [Read-Write] The height fog particle reflectiveness used by volumetric fog.
Water particles in air have an albedo near white, while dust has slightly darker value.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_albedo"></a>

#### volumetric\_fog\_albedo

```python
@volumetric_fog_albedo.setter
def volumetric_fog_albedo(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_emissive"></a>

#### volumetric\_fog\_emissive

```python
@property
def volumetric_fog_emissive() -> LinearColor
```

(LinearColor):  [Read-Write] Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.
In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,
So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_emissive"></a>

#### volumetric\_fog\_emissive

```python
@volumetric_fog_emissive.setter
def volumetric_fog_emissive(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_extinction_scale"></a>

#### volumetric\_fog\_extinction\_scale

```python
@property
def volumetric_fog_extinction_scale() -> float
```

(float):  [Read-Write] Scales the height fog particle extinction amount used by volumetric fog.
Values larger than 1 cause fog particles everywhere absorb more light.

<a id="unreal.SkyCreatorExponentialHeightFogSettings.volumetric_fog_extinction_scale"></a>

#### volumetric\_fog\_extinction\_scale

```python
@volumetric_fog_extinction_scale.setter
def volumetric_fog_extinction_scale(value: float) -> None
```

<a id="unreal.SkyCreatorStarMapSettings"></a>