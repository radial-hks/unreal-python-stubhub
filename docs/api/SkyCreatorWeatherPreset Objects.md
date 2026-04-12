## SkyCreatorWeatherPreset Objects

```python
class SkyCreatorWeatherPreset(DataAsset)
```

Sky Creator Weather Preset

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherPreset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_cloud_settings`` (SkyCreatorBackgroundCloudSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``exponential_height_fog_settings`` (SkyCreatorExponentialHeightFogSettings):  [Read-Write]
- ``moon_light_settings`` (SkyCreatorMoonLightSettings):  [Read-Write]
- ``post_process_settings`` (SkyCreatorPostProcessSettings):  [Read-Write]
- ``sky_atmosphere_settings`` (SkyCreatorSkyAtmosphereSettings):  [Read-Write]
- ``sky_light_settings`` (SkyCreatorSkyLightSettings):  [Read-Write]
- ``star_map_settings`` (SkyCreatorStarMapSettings):  [Read-Write]
- ``sun_light_settings`` (SkyCreatorSunLightSettings):  [Read-Write]
- ``volumetric_cloud_settings`` (SkyCreatorVolumetricCloudSettings):  [Read-Write]
- ``weather_fx_settings`` (SkyCreatorWeatherFXSettings):  [Read-Write]
- ``weather_material_fx_settings`` (SkyCreatorWeatherMaterialFXSettings):  [Read-Write]
- ``wind_settings`` (SkyCreatorWindSettings):  [Read-Write]

<a id="unreal.SkyCreatorWeatherPreset.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.sky_atmosphere_settings"></a>

#### sky\_atmosphere\_settings

```python
@property
def sky_atmosphere_settings() -> SkyCreatorSkyAtmosphereSettings
```

(SkyCreatorSkyAtmosphereSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.volumetric_cloud_settings"></a>

#### volumetric\_cloud\_settings

```python
@property
def volumetric_cloud_settings() -> SkyCreatorVolumetricCloudSettings
```

(SkyCreatorVolumetricCloudSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.background_cloud_settings"></a>

#### background\_cloud\_settings

```python
@property
def background_cloud_settings() -> SkyCreatorBackgroundCloudSettings
```

(SkyCreatorBackgroundCloudSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.sky_light_settings"></a>

#### sky\_light\_settings

```python
@property
def sky_light_settings() -> SkyCreatorSkyLightSettings
```

(SkyCreatorSkyLightSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.sun_light_settings"></a>

#### sun\_light\_settings

```python
@property
def sun_light_settings() -> SkyCreatorSunLightSettings
```

(SkyCreatorSunLightSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.moon_light_settings"></a>

#### moon\_light\_settings

```python
@property
def moon_light_settings() -> SkyCreatorMoonLightSettings
```

(SkyCreatorMoonLightSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.exponential_height_fog_settings"></a>

#### exponential\_height\_fog\_settings

```python
@property
def exponential_height_fog_settings(
) -> SkyCreatorExponentialHeightFogSettings
```

(SkyCreatorExponentialHeightFogSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.star_map_settings"></a>

#### star\_map\_settings

```python
@property
def star_map_settings() -> SkyCreatorStarMapSettings
```

(SkyCreatorStarMapSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.weather_fx_settings"></a>

#### weather\_fx\_settings

```python
@property
def weather_fx_settings() -> SkyCreatorWeatherFXSettings
```

(SkyCreatorWeatherFXSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.weather_material_fx_settings"></a>

#### weather\_material\_fx\_settings

```python
@property
def weather_material_fx_settings() -> SkyCreatorWeatherMaterialFXSettings
```

(SkyCreatorWeatherMaterialFXSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.wind_settings"></a>

#### wind\_settings

```python
@property
def wind_settings() -> SkyCreatorWindSettings
```

(SkyCreatorWindSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.post_process_settings"></a>

#### post\_process\_settings

```python
@property
def post_process_settings() -> SkyCreatorPostProcessSettings
```

(SkyCreatorPostProcessSettings):  [Read-Only]

<a id="unreal.SkyCreatorWeatherPreset.get_weather_preset_settings"></a>

#### get\_weather\_preset\_settings

```python
def get_weather_preset_settings() -> SkyCreatorWeatherSettings
```

x.get_weather_preset_settings() -> SkyCreatorWeatherSettings
Get Weather Preset Settings

Returns:
    SkyCreatorWeatherSettings:

<a id="unreal.SkyCreatorWeatherPreset_51"></a>