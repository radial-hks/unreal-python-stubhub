## SkyCreatorSkyAtmosphereSettings Objects

```python
class SkyCreatorSkyAtmosphereSettings(StructBase)
```

Sky Creator Sky Atmosphere Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absorption`` (LinearColor):  [Read-Write] Absorption coefficients for another atmosphere layer.
  Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km.
  The default values represents ozone molecules absorption in the Earth atmosphere.
- ``absorption_scale`` (float):  [Read-Write] Absorption coefficients for another atmosphere layer.
  Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km.
  This approximates ozone molecules distribution in the Earth atmosphere.
- ``ground_albedo`` (LinearColor):  [Read-Write] The ground albedo that will tint the astmophere when the sun light will bounce on it.
  Only taken into account when MultiScattering > 0.0.
- ``height_fog_contribution`` (float):  [Read-Write] Scale the sky and atmosphere lights contribution to the height fog when
  SupportSkyAtmosphereAffectsHeightFog project setting is true.
- ``mie_absorption`` (LinearColor):  [Read-Write] The Mie absorption coefficients resulting from particles in the air at an altitude of 0 kilometer.
  As it becomes higher, light will be absorbed more.
- ``mie_absorption_scale`` (float):  [Read-Write] Mie absorption coefficient scale.
- ``mie_anisotropy`` (float):  [Read-Write] A value of 0 mean light is uniformly scattered.
  A value closer to 1 means lights will scatter more forward, resulting in halos around light sources.
- ``mie_exponential_distribution`` (float):  [Read-Write] The altitude in kilometer at which Mie effects are reduced to 40%.
- ``mie_scattering`` (LinearColor):  [Read-Write] The Mie scattering coefficients resulting from particles in the air at an altitude of 0 kilometer.
  As it becomes higher, light will be scattered more.
- ``mie_scattering_scale`` (float):  [Read-Write] Mie scattering coefficient scale.
- ``rayleigh_exponential_distribution`` (float):  [Read-Write] The altitude in kilometer at which Rayleigh scattering effect is reduced to 40%.
- ``rayleigh_scattering`` (LinearColor):  [Read-Write] The Rayleigh scattering coefficients resulting from molecules in the air at an altitude of 0 kilometer.
- ``rayleigh_scattering_scale`` (float):  [Read-Write] Rayleigh scattering coefficient scale.
- ``sky_luminance_factor`` (LinearColor):  [Read-Write] Scales the luminance of pixels representing the sky, i.e. not belonging to any surface.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rayleigh_scattering_scale: float = 0.000000,
             rayleigh_scattering: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             rayleigh_exponential_distribution: float = 0.000000,
             mie_scattering_scale: float = 0.000000,
             mie_scattering: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             mie_absorption_scale: float = 0.000000,
             mie_absorption: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             mie_anisotropy: float = 0.000000,
             mie_exponential_distribution: float = 0.000000,
             absorption_scale: float = 0.000000,
             absorption: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             sky_luminance_factor: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             ground_albedo: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             height_fog_contribution: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_scattering_scale"></a>

#### rayleigh\_scattering\_scale

```python
@property
def rayleigh_scattering_scale() -> float
```

(float):  [Read-Write] Rayleigh scattering coefficient scale.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_scattering_scale"></a>

#### rayleigh\_scattering\_scale

```python
@rayleigh_scattering_scale.setter
def rayleigh_scattering_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_scattering"></a>

#### rayleigh\_scattering

```python
@property
def rayleigh_scattering() -> LinearColor
```

(LinearColor):  [Read-Write] The Rayleigh scattering coefficients resulting from molecules in the air at an altitude of 0 kilometer.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_scattering"></a>

#### rayleigh\_scattering

```python
@rayleigh_scattering.setter
def rayleigh_scattering(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_exponential_distribution"></a>

#### rayleigh\_exponential\_distribution

```python
@property
def rayleigh_exponential_distribution() -> float
```

(float):  [Read-Write] The altitude in kilometer at which Rayleigh scattering effect is reduced to 40%.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.rayleigh_exponential_distribution"></a>

#### rayleigh\_exponential\_distribution

```python
@rayleigh_exponential_distribution.setter
def rayleigh_exponential_distribution(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_scattering_scale"></a>

#### mie\_scattering\_scale

```python
@property
def mie_scattering_scale() -> float
```

(float):  [Read-Write] Mie scattering coefficient scale.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_scattering_scale"></a>

#### mie\_scattering\_scale

```python
@mie_scattering_scale.setter
def mie_scattering_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_scattering"></a>

#### mie\_scattering

```python
@property
def mie_scattering() -> LinearColor
```

(LinearColor):  [Read-Write] The Mie scattering coefficients resulting from particles in the air at an altitude of 0 kilometer.
As it becomes higher, light will be scattered more.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_scattering"></a>

#### mie\_scattering

```python
@mie_scattering.setter
def mie_scattering(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_absorption_scale"></a>

#### mie\_absorption\_scale

```python
@property
def mie_absorption_scale() -> float
```

(float):  [Read-Write] Mie absorption coefficient scale.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_absorption_scale"></a>

#### mie\_absorption\_scale

```python
@mie_absorption_scale.setter
def mie_absorption_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_absorption"></a>

#### mie\_absorption

```python
@property
def mie_absorption() -> LinearColor
```

(LinearColor):  [Read-Write] The Mie absorption coefficients resulting from particles in the air at an altitude of 0 kilometer.
As it becomes higher, light will be absorbed more.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_absorption"></a>

#### mie\_absorption

```python
@mie_absorption.setter
def mie_absorption(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_anisotropy"></a>

#### mie\_anisotropy

```python
@property
def mie_anisotropy() -> float
```

(float):  [Read-Write] A value of 0 mean light is uniformly scattered.
A value closer to 1 means lights will scatter more forward, resulting in halos around light sources.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_anisotropy"></a>

#### mie\_anisotropy

```python
@mie_anisotropy.setter
def mie_anisotropy(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_exponential_distribution"></a>

#### mie\_exponential\_distribution

```python
@property
def mie_exponential_distribution() -> float
```

(float):  [Read-Write] The altitude in kilometer at which Mie effects are reduced to 40%.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.mie_exponential_distribution"></a>

#### mie\_exponential\_distribution

```python
@mie_exponential_distribution.setter
def mie_exponential_distribution(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.absorption_scale"></a>

#### absorption\_scale

```python
@property
def absorption_scale() -> float
```

(float):  [Read-Write] Absorption coefficients for another atmosphere layer.
Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km.
This approximates ozone molecules distribution in the Earth atmosphere.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.absorption_scale"></a>

#### absorption\_scale

```python
@absorption_scale.setter
def absorption_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.absorption"></a>

#### absorption

```python
@property
def absorption() -> LinearColor
```

(LinearColor):  [Read-Write] Absorption coefficients for another atmosphere layer.
Density increase from 0 to 1 between 10 to 25km and decreases from 1 to 0 between 25 to 40km.
The default values represents ozone molecules absorption in the Earth atmosphere.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.absorption"></a>

#### absorption

```python
@absorption.setter
def absorption(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.sky_luminance_factor"></a>

#### sky\_luminance\_factor

```python
@property
def sky_luminance_factor() -> LinearColor
```

(LinearColor):  [Read-Write] Scales the luminance of pixels representing the sky, i.e. not belonging to any surface.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.sky_luminance_factor"></a>

#### sky\_luminance\_factor

```python
@sky_luminance_factor.setter
def sky_luminance_factor(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.ground_albedo"></a>

#### ground\_albedo

```python
@property
def ground_albedo() -> LinearColor
```

(LinearColor):  [Read-Write] The ground albedo that will tint the astmophere when the sun light will bounce on it.
Only taken into account when MultiScattering > 0.0.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.ground_albedo"></a>

#### ground\_albedo

```python
@ground_albedo.setter
def ground_albedo(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings.height_fog_contribution"></a>

#### height\_fog\_contribution

```python
@property
def height_fog_contribution() -> float
```

(float):  [Read-Write] Scale the sky and atmosphere lights contribution to the height fog when
SupportSkyAtmosphereAffectsHeightFog project setting is true.

<a id="unreal.SkyCreatorSkyAtmosphereSettings.height_fog_contribution"></a>

#### height\_fog\_contribution

```python
@height_fog_contribution.setter
def height_fog_contribution(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings"></a>