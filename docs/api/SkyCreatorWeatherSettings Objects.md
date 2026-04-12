## SkyCreatorWeatherSettings Objects

```python
class SkyCreatorWeatherSettings(StructBase)
```

Sky Creator Weather Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_cloud_settings`` (SkyCreatorBackgroundCloudSettings):  [Read-Write] Volumetric Cloud Settings.
- ``exponential_height_fog_settings`` (SkyCreatorExponentialHeightFogSettings):  [Read-Write] Exponential Height Fog Settings.
- ``moon_light_settings`` (SkyCreatorMoonLightSettings):  [Read-Write] Moon Light Settings.
- ``post_process_settings`` (SkyCreatorPostProcessSettings):  [Read-Write] Post Process Settings.
- ``sky_atmosphere_settings`` (SkyCreatorSkyAtmosphereSettings):  [Read-Write] Sky Atmosphere Settings.
- ``sky_light_settings`` (SkyCreatorSkyLightSettings):  [Read-Write] Sky Light Settings.
- ``star_map_settings`` (SkyCreatorStarMapSettings):  [Read-Write] Star Map Settings.
- ``sun_light_settings`` (SkyCreatorSunLightSettings):  [Read-Write] Sun Light Settings.
- ``volumetric_cloud_settings`` (SkyCreatorVolumetricCloudSettings):  [Read-Write] Volumetric Cloud Settings.
- ``weather_fx_settings`` (SkyCreatorWeatherFXSettings):  [Read-Write] Weather FX Settings.
- ``weather_material_fx_settings`` (SkyCreatorWeatherMaterialFXSettings):  [Read-Write] Weather Material FX Settings.
- ``wind_settings`` (SkyCreatorWindSettings):  [Read-Write] Wind Settings.

<a id="unreal.SkyCreatorWeatherSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    sky_atmosphere_settings: SkyCreatorSkyAtmosphereSettings = [
        0.033100, [0.175287, 0.409607, 1.000000, 1.000000], 8.000000, 0.003996,
        [1.000000, 1.000000, 1.000000, 1.000000], 0.000444,
        [1.000000, 1.000000, 1.000000, 1.000000], 0.800000, 1.200000, 0.001881,
        [0.345561, 1.000000, 0.045189, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000],
        [0.401978, 0.401978, 0.401978, 1.000000], 1.000000
    ],
    volumetric_cloud_settings: SkyCreatorVolumetricCloudSettings = [
        0.000000, 0.500000, 0.500000, 0.750000, 0.500000, 0.500000, 0.750000,
        0.500000, 0.500000, 0.000000, 0.000000, 0.500000, 0.001000, 0.050000,
        0.100000, [1.000000, 1.000000, 1.000000, 1.000000],
        [0.250000, 0.250000, 0.250000,
         1.000000], 0.250000, 100.000000, 0.000000, 0.250000,
        [0.010725, 0.015880, 0.025000,
         1.000000], 0.600000, -0.400000, 0.500000, 0.500000, 0.100000,
        0.500000, 0.500000, 0.625000, 0.250000, 0.125000, 0.250000
    ],
    background_cloud_settings: SkyCreatorBackgroundCloudSettings = [
        1.000000, [1.000000, 1.000000, 1.000000, 1.000000], 0.500000, 0.500000,
        0.500000, 0.800000
    ],
    sky_light_settings: SkyCreatorSkyLightSettings = [
        1.000000, 4.000000, [1.000000, 1.000000, 1.000000, 1.000000],
        [0.000600, 0.000700, 0.001000, 1.000000], 0.250000
    ],
    sun_light_settings: SkyCreatorSunLightSettings = [
        10.000000, [1.000000, 1.000000, 0.900000, 1.000000], 5500.000000,
        1.000000, [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000], 1.000000, 0.500000, 0.900000
    ],
    moon_light_settings: SkyCreatorMoonLightSettings = [
        0.040000, [0.480000, 0.740000, 1.000000, 1.000000], 8500.000000,
        1.000000, [1.000000, 0.880000, 0.400000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000], 1.000000, 0.500000, 0.900000
    ],
    exponential_height_fog_settings: SkyCreatorExponentialHeightFogSettings = [
        0.002000, 0.060000, [0.000000, 0.000000, 0.000000, 1.000000], 0.000000,
        0.000000, 0.600000, 8.000000, 2000.000000,
        [0.000000, 0.000000, 0.000000, 1.000000], 0.200000,
        [1.000000, 1.000000, 1.000000, 1.000000],
        [0.000000, 0.000000, 0.000000, 1.000000], 1.000000
    ],
    star_map_settings: SkyCreatorStarMapSettings = [
        0.250000, [1.000000, 1.000000, 1.000000, 1.000000], 1.000000, 0.250000,
        1.000000, 8.000000, 4.000000, [0.019600, 0.027609, 0.040000, 1.000000],
        [0.001384, 0.002343, 0.004000, 1.000000]
    ],
    weather_fx_settings: SkyCreatorWeatherFXSettings = [
        0.000000, [0.500000, 0.500000, 0.500000, 0.500000], -1000.000000,
        0.300000, 0.600000, 0.100000, 0.800000, 0.200000, 0.300000,
        [16.000000, 16.000000], [24.000000, 24.000000], 0.000000,
        [1.000000, 1.000000, 1.000000, 1.000000], -100.000000, 100.000000,
        1.000000, 2.000000, 1.000000, 2.000000, False, 1.000000, 10.000000,
        [1.000000, 1.000000, 1.000000, 1.000000],
        [1.000000, 1.000000, 1.000000, 1.000000], 0.250000, 50.000000,
        0.004000, 0.008000, 2.000000, 4.000000, 0.500000, 0.020000, 0.080000,
        0.002500, 10.000000, 0.000400, 0.000800, 0.000000,
        [0.200000, 0.200000, 0.200000, 1.000000], 10000.000000, 800.000000,
        [0.050000, 0.050000, 0.050000, 1.000000], 14000.000000, 1600.000000
    ],
    weather_material_fx_settings: SkyCreatorWeatherMaterialFXSettings = [
        0.000000, [0.500000, 0.500000, 0.500000, 1.000000], 0.000000,
        [0.300000, 0.300000, 0.300000, 1.000000], 0.000000, 0.100000, 0.500000,
        1.000000, 2.000000, 8.000000, 0.050000, 0.250000, 1.000000, 0.000000,
        [0.900000, 0.900000, 0.900000, 1.000000], 0.500000, 0.950000
    ],
    wind_settings: SkyCreatorWindSettings = [
        0.000000, 0.000000, 0.000000, 0.000000, 2.000000, 0.000000, 0.000000
    ],
    post_process_settings: SkyCreatorPostProcessSettings = [
        0.675000, -1.000000, 1.000000
    ]
) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.sky_atmosphere_settings"></a>

#### sky\_atmosphere\_settings

```python
@property
def sky_atmosphere_settings() -> SkyCreatorSkyAtmosphereSettings
```

(SkyCreatorSkyAtmosphereSettings):  [Read-Write] Sky Atmosphere Settings.

<a id="unreal.SkyCreatorWeatherSettings.sky_atmosphere_settings"></a>

#### sky\_atmosphere\_settings

```python
@sky_atmosphere_settings.setter
def sky_atmosphere_settings(value: SkyCreatorSkyAtmosphereSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.volumetric_cloud_settings"></a>

#### volumetric\_cloud\_settings

```python
@property
def volumetric_cloud_settings() -> SkyCreatorVolumetricCloudSettings
```

(SkyCreatorVolumetricCloudSettings):  [Read-Write] Volumetric Cloud Settings.

<a id="unreal.SkyCreatorWeatherSettings.volumetric_cloud_settings"></a>

#### volumetric\_cloud\_settings

```python
@volumetric_cloud_settings.setter
def volumetric_cloud_settings(
        value: SkyCreatorVolumetricCloudSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.background_cloud_settings"></a>

#### background\_cloud\_settings

```python
@property
def background_cloud_settings() -> SkyCreatorBackgroundCloudSettings
```

(SkyCreatorBackgroundCloudSettings):  [Read-Write] Volumetric Cloud Settings.

<a id="unreal.SkyCreatorWeatherSettings.background_cloud_settings"></a>

#### background\_cloud\_settings

```python
@background_cloud_settings.setter
def background_cloud_settings(
        value: SkyCreatorBackgroundCloudSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.sky_light_settings"></a>

#### sky\_light\_settings

```python
@property
def sky_light_settings() -> SkyCreatorSkyLightSettings
```

(SkyCreatorSkyLightSettings):  [Read-Write] Sky Light Settings.

<a id="unreal.SkyCreatorWeatherSettings.sky_light_settings"></a>

#### sky\_light\_settings

```python
@sky_light_settings.setter
def sky_light_settings(value: SkyCreatorSkyLightSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.sun_light_settings"></a>

#### sun\_light\_settings

```python
@property
def sun_light_settings() -> SkyCreatorSunLightSettings
```

(SkyCreatorSunLightSettings):  [Read-Write] Sun Light Settings.

<a id="unreal.SkyCreatorWeatherSettings.sun_light_settings"></a>

#### sun\_light\_settings

```python
@sun_light_settings.setter
def sun_light_settings(value: SkyCreatorSunLightSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.moon_light_settings"></a>

#### moon\_light\_settings

```python
@property
def moon_light_settings() -> SkyCreatorMoonLightSettings
```

(SkyCreatorMoonLightSettings):  [Read-Write] Moon Light Settings.

<a id="unreal.SkyCreatorWeatherSettings.moon_light_settings"></a>

#### moon\_light\_settings

```python
@moon_light_settings.setter
def moon_light_settings(value: SkyCreatorMoonLightSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.exponential_height_fog_settings"></a>

#### exponential\_height\_fog\_settings

```python
@property
def exponential_height_fog_settings(
) -> SkyCreatorExponentialHeightFogSettings
```

(SkyCreatorExponentialHeightFogSettings):  [Read-Write] Exponential Height Fog Settings.

<a id="unreal.SkyCreatorWeatherSettings.exponential_height_fog_settings"></a>

#### exponential\_height\_fog\_settings

```python
@exponential_height_fog_settings.setter
def exponential_height_fog_settings(
        value: SkyCreatorExponentialHeightFogSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.star_map_settings"></a>

#### star\_map\_settings

```python
@property
def star_map_settings() -> SkyCreatorStarMapSettings
```

(SkyCreatorStarMapSettings):  [Read-Write] Star Map Settings.

<a id="unreal.SkyCreatorWeatherSettings.star_map_settings"></a>

#### star\_map\_settings

```python
@star_map_settings.setter
def star_map_settings(value: SkyCreatorStarMapSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.weather_fx_settings"></a>

#### weather\_fx\_settings

```python
@property
def weather_fx_settings() -> SkyCreatorWeatherFXSettings
```

(SkyCreatorWeatherFXSettings):  [Read-Write] Weather FX Settings.

<a id="unreal.SkyCreatorWeatherSettings.weather_fx_settings"></a>

#### weather\_fx\_settings

```python
@weather_fx_settings.setter
def weather_fx_settings(value: SkyCreatorWeatherFXSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.weather_material_fx_settings"></a>

#### weather\_material\_fx\_settings

```python
@property
def weather_material_fx_settings() -> SkyCreatorWeatherMaterialFXSettings
```

(SkyCreatorWeatherMaterialFXSettings):  [Read-Write] Weather Material FX Settings.

<a id="unreal.SkyCreatorWeatherSettings.weather_material_fx_settings"></a>

#### weather\_material\_fx\_settings

```python
@weather_material_fx_settings.setter
def weather_material_fx_settings(
        value: SkyCreatorWeatherMaterialFXSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.wind_settings"></a>

#### wind\_settings

```python
@property
def wind_settings() -> SkyCreatorWindSettings
```

(SkyCreatorWindSettings):  [Read-Write] Wind Settings.

<a id="unreal.SkyCreatorWeatherSettings.wind_settings"></a>

#### wind\_settings

```python
@wind_settings.setter
def wind_settings(value: SkyCreatorWindSettings) -> None
```

<a id="unreal.SkyCreatorWeatherSettings.post_process_settings"></a>

#### post\_process\_settings

```python
@property
def post_process_settings() -> SkyCreatorPostProcessSettings
```

(SkyCreatorPostProcessSettings):  [Read-Write] Post Process Settings.

<a id="unreal.SkyCreatorWeatherSettings.post_process_settings"></a>

#### post\_process\_settings

```python
@post_process_settings.setter
def post_process_settings(value: SkyCreatorPostProcessSettings) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51"></a>