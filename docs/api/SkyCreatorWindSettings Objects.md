## SkyCreatorWindSettings Objects

```python
class SkyCreatorWindSettings(StructBase)
```

Sky Creator Wind Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cloud_noise_detail_wind_speed_vertical`` (float):  [Read-Write] Vertical wind speed of Cloud Noise Detail in m/s.
- ``cloud_noise_shape_wind_direction`` (float):  [Read-Write] Wind direction angle of Cloud Noise in degrees.
- ``cloud_noise_shape_wind_speed_horizontal`` (float):  [Read-Write] Horizontal wind speed of Cloud Noise Shape in m/s.
- ``cloud_wind_direction`` (float):  [Read-Write] Wind direction angle of Low Cloud layer in degrees.
- ``cloud_wind_speed`` (float):  [Read-Write] Wind speed of Low Cloud layer in m/s.
- ``precipitation_wind_direction`` (float):  [Read-Write] Wind direction angle of precipitation particles in degrees.
- ``precipitation_wind_speed`` (float):  [Read-Write] Wind speed of precipitation particles.

<a id="unreal.SkyCreatorWindSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cloud_wind_direction: float = 0.000000,
             cloud_wind_speed: float = 0.000000,
             cloud_noise_shape_wind_direction: float = 0.000000,
             cloud_noise_shape_wind_speed_horizontal: float = 0.000000,
             cloud_noise_detail_wind_speed_vertical: float = 0.000000,
             precipitation_wind_direction: float = 0.000000,
             precipitation_wind_speed: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorWindSettings.cloud_wind_direction"></a>

#### cloud\_wind\_direction

```python
@property
def cloud_wind_direction() -> float
```

(float):  [Read-Write] Wind direction angle of Low Cloud layer in degrees.

<a id="unreal.SkyCreatorWindSettings.cloud_wind_direction"></a>

#### cloud\_wind\_direction

```python
@cloud_wind_direction.setter
def cloud_wind_direction(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings.cloud_wind_speed"></a>

#### cloud\_wind\_speed

```python
@property
def cloud_wind_speed() -> float
```

(float):  [Read-Write] Wind speed of Low Cloud layer in m/s.

<a id="unreal.SkyCreatorWindSettings.cloud_wind_speed"></a>

#### cloud\_wind\_speed

```python
@cloud_wind_speed.setter
def cloud_wind_speed(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings.cloud_noise_shape_wind_direction"></a>

#### cloud\_noise\_shape\_wind\_direction

```python
@property
def cloud_noise_shape_wind_direction() -> float
```

(float):  [Read-Write] Wind direction angle of Cloud Noise in degrees.

<a id="unreal.SkyCreatorWindSettings.cloud_noise_shape_wind_direction"></a>

#### cloud\_noise\_shape\_wind\_direction

```python
@cloud_noise_shape_wind_direction.setter
def cloud_noise_shape_wind_direction(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings.cloud_noise_shape_wind_speed_horizontal"></a>

#### cloud\_noise\_shape\_wind\_speed\_horizontal

```python
@property
def cloud_noise_shape_wind_speed_horizontal() -> float
```

(float):  [Read-Write] Horizontal wind speed of Cloud Noise Shape in m/s.

<a id="unreal.SkyCreatorWindSettings.cloud_noise_shape_wind_speed_horizontal"></a>

#### cloud\_noise\_shape\_wind\_speed\_horizontal

```python
@cloud_noise_shape_wind_speed_horizontal.setter
def cloud_noise_shape_wind_speed_horizontal(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings.cloud_noise_detail_wind_speed_vertical"></a>

#### cloud\_noise\_detail\_wind\_speed\_vertical

```python
@property
def cloud_noise_detail_wind_speed_vertical() -> float
```

(float):  [Read-Write] Vertical wind speed of Cloud Noise Detail in m/s.

<a id="unreal.SkyCreatorWindSettings.cloud_noise_detail_wind_speed_vertical"></a>

#### cloud\_noise\_detail\_wind\_speed\_vertical

```python
@cloud_noise_detail_wind_speed_vertical.setter
def cloud_noise_detail_wind_speed_vertical(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings.precipitation_wind_direction"></a>

#### precipitation\_wind\_direction

```python
@property
def precipitation_wind_direction() -> float
```

(float):  [Read-Write] Wind direction angle of precipitation particles in degrees.

<a id="unreal.SkyCreatorWindSettings.precipitation_wind_direction"></a>

#### precipitation\_wind\_direction

```python
@precipitation_wind_direction.setter
def precipitation_wind_direction(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings.precipitation_wind_speed"></a>

#### precipitation\_wind\_speed

```python
@property
def precipitation_wind_speed() -> float
```

(float):  [Read-Write] Wind speed of precipitation particles.

<a id="unreal.SkyCreatorWindSettings.precipitation_wind_speed"></a>

#### precipitation\_wind\_speed

```python
@precipitation_wind_speed.setter
def precipitation_wind_speed(value: float) -> None
```

<a id="unreal.SkyCreatorPostProcessSettings"></a>