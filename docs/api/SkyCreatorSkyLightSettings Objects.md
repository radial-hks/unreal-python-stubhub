## SkyCreatorSkyLightSettings Objects

```python
class SkyCreatorSkyLightSettings(StructBase)
```

Sky Creator Sky Light Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cloud_ambient_occlusion_strength`` (float):  [Read-Write] The strength of the ambient occlusion, higher value will block more light.
- ``intensity`` (float):  [Read-Write] Total energy that the light emits.
- ``light_color`` (LinearColor):  [Read-Write] Filter color of the light.
  Note that this can change the light's effective intensity.
- ``lower_hemisphere_color`` (LinearColor):  [Read-Write] Lower Hemisphere Color.
- ``night_intensity`` (float):  [Read-Write] Energy that the light emits in the nights.

<a id="unreal.SkyCreatorSkyLightSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(intensity: float = 0.000000,
             night_intensity: float = 0.000000,
             light_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             lower_hemisphere_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             cloud_ambient_occlusion_strength: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Write] Total energy that the light emits.

<a id="unreal.SkyCreatorSkyLightSettings.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings.night_intensity"></a>

#### night\_intensity

```python
@property
def night_intensity() -> float
```

(float):  [Read-Write] Energy that the light emits in the nights.

<a id="unreal.SkyCreatorSkyLightSettings.night_intensity"></a>

#### night\_intensity

```python
@night_intensity.setter
def night_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings.light_color"></a>

#### light\_color

```python
@property
def light_color() -> LinearColor
```

(LinearColor):  [Read-Write] Filter color of the light.
Note that this can change the light's effective intensity.

<a id="unreal.SkyCreatorSkyLightSettings.light_color"></a>

#### light\_color

```python
@light_color.setter
def light_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings.lower_hemisphere_color"></a>

#### lower\_hemisphere\_color

```python
@property
def lower_hemisphere_color() -> LinearColor
```

(LinearColor):  [Read-Write] Lower Hemisphere Color.

<a id="unreal.SkyCreatorSkyLightSettings.lower_hemisphere_color"></a>

#### lower\_hemisphere\_color

```python
@lower_hemisphere_color.setter
def lower_hemisphere_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyLightSettings.cloud_ambient_occlusion_strength"></a>

#### cloud\_ambient\_occlusion\_strength

```python
@property
def cloud_ambient_occlusion_strength() -> float
```

(float):  [Read-Write] The strength of the ambient occlusion, higher value will block more light.

<a id="unreal.SkyCreatorSkyLightSettings.cloud_ambient_occlusion_strength"></a>

#### cloud\_ambient\_occlusion\_strength

```python
@cloud_ambient_occlusion_strength.setter
def cloud_ambient_occlusion_strength(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings"></a>