## SkyCreatorSunLightSettings Objects

```python
class SkyCreatorSunLightSettings(StructBase)
```

Sky Creator Sun Light Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``atmosphere_disk_color_scale`` (LinearColor):  [Read-Write] A color multiplied with the sun disk luminance.
- ``cloud_scattered_luminance_scale`` (LinearColor):  [Read-Write] Scales the lights contribution when scattered in cloud participating media.
- ``cloud_shadow_on_atmosphere_strength`` (float):  [Read-Write] The strength of the shadow on atmosphere. Disabled when 0.
- ``cloud_shadow_on_surface_strength`` (float):  [Read-Write] The strength of the shadow on opaque and transparent meshes. Disabled when 0.
- ``cloud_shadow_strength`` (float):  [Read-Write] The overall strength of the cloud shadow, higher value will block more light.
- ``intensity`` (float):  [Read-Write] Maximum illumination from the light in lux.
- ``light_color`` (LinearColor):  [Read-Write] Filter color of the light.
  Note that this can change the light's effective intensity.
- ``temperature`` (float):  [Read-Write] Color temperature in Kelvin of the blackbody illuminant.
  White (D65) is 6500K.
- ``volumetric_scattering_intensity`` (float):  [Read-Write] Intensity of the volumetric scattering from sun.
  This scales Intensity and Light Color.

<a id="unreal.SkyCreatorSunLightSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(intensity: float = 0.000000,
             light_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             temperature: float = 0.000000,
             volumetric_scattering_intensity: float = 0.000000,
             atmosphere_disk_color_scale: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             cloud_scattered_luminance_scale: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             cloud_shadow_strength: float = 0.000000,
             cloud_shadow_on_atmosphere_strength: float = 0.000000,
             cloud_shadow_on_surface_strength: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Write] Maximum illumination from the light in lux.

<a id="unreal.SkyCreatorSunLightSettings.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.light_color"></a>

#### light\_color

```python
@property
def light_color() -> LinearColor
```

(LinearColor):  [Read-Write] Filter color of the light.
Note that this can change the light's effective intensity.

<a id="unreal.SkyCreatorSunLightSettings.light_color"></a>

#### light\_color

```python
@light_color.setter
def light_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.temperature"></a>

#### temperature

```python
@property
def temperature() -> float
```

(float):  [Read-Write] Color temperature in Kelvin of the blackbody illuminant.
White (D65) is 6500K.

<a id="unreal.SkyCreatorSunLightSettings.temperature"></a>

#### temperature

```python
@temperature.setter
def temperature(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.volumetric_scattering_intensity"></a>

#### volumetric\_scattering\_intensity

```python
@property
def volumetric_scattering_intensity() -> float
```

(float):  [Read-Write] Intensity of the volumetric scattering from sun.
This scales Intensity and Light Color.

<a id="unreal.SkyCreatorSunLightSettings.volumetric_scattering_intensity"></a>

#### volumetric\_scattering\_intensity

```python
@volumetric_scattering_intensity.setter
def volumetric_scattering_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.atmosphere_disk_color_scale"></a>

#### atmosphere\_disk\_color\_scale

```python
@property
def atmosphere_disk_color_scale() -> LinearColor
```

(LinearColor):  [Read-Write] A color multiplied with the sun disk luminance.

<a id="unreal.SkyCreatorSunLightSettings.atmosphere_disk_color_scale"></a>

#### atmosphere\_disk\_color\_scale

```python
@atmosphere_disk_color_scale.setter
def atmosphere_disk_color_scale(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.cloud_scattered_luminance_scale"></a>

#### cloud\_scattered\_luminance\_scale

```python
@property
def cloud_scattered_luminance_scale() -> LinearColor
```

(LinearColor):  [Read-Write] Scales the lights contribution when scattered in cloud participating media.

<a id="unreal.SkyCreatorSunLightSettings.cloud_scattered_luminance_scale"></a>

#### cloud\_scattered\_luminance\_scale

```python
@cloud_scattered_luminance_scale.setter
def cloud_scattered_luminance_scale(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.cloud_shadow_strength"></a>

#### cloud\_shadow\_strength

```python
@property
def cloud_shadow_strength() -> float
```

(float):  [Read-Write] The overall strength of the cloud shadow, higher value will block more light.

<a id="unreal.SkyCreatorSunLightSettings.cloud_shadow_strength"></a>

#### cloud\_shadow\_strength

```python
@cloud_shadow_strength.setter
def cloud_shadow_strength(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.cloud_shadow_on_atmosphere_strength"></a>

#### cloud\_shadow\_on\_atmosphere\_strength

```python
@property
def cloud_shadow_on_atmosphere_strength() -> float
```

(float):  [Read-Write] The strength of the shadow on atmosphere. Disabled when 0.

<a id="unreal.SkyCreatorSunLightSettings.cloud_shadow_on_atmosphere_strength"></a>

#### cloud\_shadow\_on\_atmosphere\_strength

```python
@cloud_shadow_on_atmosphere_strength.setter
def cloud_shadow_on_atmosphere_strength(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings.cloud_shadow_on_surface_strength"></a>

#### cloud\_shadow\_on\_surface\_strength

```python
@property
def cloud_shadow_on_surface_strength() -> float
```

(float):  [Read-Write] The strength of the shadow on opaque and transparent meshes. Disabled when 0.

<a id="unreal.SkyCreatorSunLightSettings.cloud_shadow_on_surface_strength"></a>

#### cloud\_shadow\_on\_surface\_strength

```python
@cloud_shadow_on_surface_strength.setter
def cloud_shadow_on_surface_strength(value: float) -> None
```

<a id="unreal.SkyCreatorMoonLightSettings"></a>