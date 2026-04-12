## SkyCreatorWindSettings\_51 Objects

```python
class SkyCreatorWindSettings_51(StructBase)
```

风设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cloud_noise_detail_wind_speed_vertical`` (float):  [Read-Write] Vertical wind speed of Cloud Noise Detail in m/s.
- ``cloud_noise_detail_wind_speed_vertical_curve`` (CurveFloat):  [Read-Write]
- ``cloud_noise_shape_wind_direction`` (float):  [Read-Write] Wind direction angle of Cloud Noise in degrees.
- ``cloud_noise_shape_wind_direction_curve`` (CurveFloat):  [Read-Write]
- ``cloud_noise_shape_wind_speed_horizontal`` (float):  [Read-Write] Horizontal wind speed of Cloud Noise Shape in m/s.
- ``cloud_noise_shape_wind_speed_horizontal_curve`` (CurveFloat):  [Read-Write]
- ``cloud_wind_direction`` (float):  [Read-Write] Wind direction angle of Low Cloud layer in degrees.
- ``cloud_wind_direction_curve`` (CurveFloat):  [Read-Write]
- ``cloud_wind_speed`` (float):  [Read-Write] Wind speed of Low Cloud layer in m/s.
- ``cloud_wind_speed_curve`` (CurveFloat):  [Read-Write]
- ``precipitation_wind_direction`` (float):  [Read-Write] Wind direction angle of precipitation particles in degrees.
- ``precipitation_wind_direction_curve`` (CurveFloat):  [Read-Write]
- ``precipitation_wind_speed`` (float):  [Read-Write] Wind speed of precipitation particles.
- ``precipitation_wind_speed_curve`` (CurveFloat):  [Read-Write]
- ``use_cloud_noise_detail_wind_speed_vertical`` (bool):  [Read-Write]
- ``use_cloud_noise_shape_wind_direction`` (bool):  [Read-Write]
- ``use_cloud_noise_shape_wind_speed_horizontal`` (bool):  [Read-Write]
- ``use_cloud_wind_direction`` (bool):  [Read-Write]
- ``use_cloud_wind_speed`` (bool):  [Read-Write]
- ``use_precipitation_wind_direction`` (bool):  [Read-Write]
- ``use_precipitation_wind_speed`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_cloud_wind_direction: bool = False,
             cloud_wind_direction: float = 0.000000,
             cloud_wind_direction_curve: CurveFloat = None,
             use_cloud_wind_speed: bool = False,
             cloud_wind_speed: float = 0.000000,
             cloud_wind_speed_curve: CurveFloat = None,
             use_cloud_noise_shape_wind_direction: bool = False,
             cloud_noise_shape_wind_direction: float = 0.000000,
             cloud_noise_shape_wind_direction_curve: CurveFloat = None,
             use_cloud_noise_shape_wind_speed_horizontal: bool = False,
             cloud_noise_shape_wind_speed_horizontal: float = 0.000000,
             cloud_noise_shape_wind_speed_horizontal_curve: CurveFloat = None,
             use_cloud_noise_detail_wind_speed_vertical: bool = False,
             cloud_noise_detail_wind_speed_vertical: float = 0.000000,
             cloud_noise_detail_wind_speed_vertical_curve: CurveFloat = None,
             use_precipitation_wind_direction: bool = False,
             precipitation_wind_direction: float = 0.000000,
             precipitation_wind_direction_curve: CurveFloat = None,
             use_precipitation_wind_speed: bool = False,
             precipitation_wind_speed: float = 0.000000,
             precipitation_wind_speed_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_wind_direction"></a>

#### use\_cloud\_wind\_direction

```python
@property
def use_cloud_wind_direction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_wind_direction"></a>

#### use\_cloud\_wind\_direction

```python
@use_cloud_wind_direction.setter
def use_cloud_wind_direction(value: bool) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_direction"></a>

#### cloud\_wind\_direction

```python
@property
def cloud_wind_direction() -> float
```

(float):  [Read-Write] Wind direction angle of Low Cloud layer in degrees.

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_direction"></a>

#### cloud\_wind\_direction

```python
@cloud_wind_direction.setter
def cloud_wind_direction(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_direction_curve"></a>

#### cloud\_wind\_direction\_curve

```python
@property
def cloud_wind_direction_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_direction_curve"></a>

#### cloud\_wind\_direction\_curve

```python
@cloud_wind_direction_curve.setter
def cloud_wind_direction_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_wind_speed"></a>

#### use\_cloud\_wind\_speed

```python
@property
def use_cloud_wind_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_wind_speed"></a>

#### use\_cloud\_wind\_speed

```python
@use_cloud_wind_speed.setter
def use_cloud_wind_speed(value: bool) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_speed"></a>

#### cloud\_wind\_speed

```python
@property
def cloud_wind_speed() -> float
```

(float):  [Read-Write] Wind speed of Low Cloud layer in m/s.

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_speed"></a>

#### cloud\_wind\_speed

```python
@cloud_wind_speed.setter
def cloud_wind_speed(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_speed_curve"></a>

#### cloud\_wind\_speed\_curve

```python
@property
def cloud_wind_speed_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.cloud_wind_speed_curve"></a>

#### cloud\_wind\_speed\_curve

```python
@cloud_wind_speed_curve.setter
def cloud_wind_speed_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_noise_shape_wind_direction"></a>

#### use\_cloud\_noise\_shape\_wind\_direction

```python
@property
def use_cloud_noise_shape_wind_direction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_noise_shape_wind_direction"></a>

#### use\_cloud\_noise\_shape\_wind\_direction

```python
@use_cloud_noise_shape_wind_direction.setter
def use_cloud_noise_shape_wind_direction(value: bool) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_direction"></a>

#### cloud\_noise\_shape\_wind\_direction

```python
@property
def cloud_noise_shape_wind_direction() -> float
```

(float):  [Read-Write] Wind direction angle of Cloud Noise in degrees.

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_direction"></a>

#### cloud\_noise\_shape\_wind\_direction

```python
@cloud_noise_shape_wind_direction.setter
def cloud_noise_shape_wind_direction(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_direction_curve"></a>

#### cloud\_noise\_shape\_wind\_direction\_curve

```python
@property
def cloud_noise_shape_wind_direction_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_direction_curve"></a>

#### cloud\_noise\_shape\_wind\_direction\_curve

```python
@cloud_noise_shape_wind_direction_curve.setter
def cloud_noise_shape_wind_direction_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_noise_shape_wind_speed_horizontal"></a>

#### use\_cloud\_noise\_shape\_wind\_speed\_horizontal

```python
@property
def use_cloud_noise_shape_wind_speed_horizontal() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_noise_shape_wind_speed_horizontal"></a>

#### use\_cloud\_noise\_shape\_wind\_speed\_horizontal

```python
@use_cloud_noise_shape_wind_speed_horizontal.setter
def use_cloud_noise_shape_wind_speed_horizontal(value: bool) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_speed_horizontal"></a>

#### cloud\_noise\_shape\_wind\_speed\_horizontal

```python
@property
def cloud_noise_shape_wind_speed_horizontal() -> float
```

(float):  [Read-Write] Horizontal wind speed of Cloud Noise Shape in m/s.

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_speed_horizontal"></a>

#### cloud\_noise\_shape\_wind\_speed\_horizontal

```python
@cloud_noise_shape_wind_speed_horizontal.setter
def cloud_noise_shape_wind_speed_horizontal(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_speed_horizontal_curve"></a>

#### cloud\_noise\_shape\_wind\_speed\_horizontal\_curve

```python
@property
def cloud_noise_shape_wind_speed_horizontal_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_shape_wind_speed_horizontal_curve"></a>

#### cloud\_noise\_shape\_wind\_speed\_horizontal\_curve

```python
@cloud_noise_shape_wind_speed_horizontal_curve.setter
def cloud_noise_shape_wind_speed_horizontal_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_noise_detail_wind_speed_vertical"></a>

#### use\_cloud\_noise\_detail\_wind\_speed\_vertical

```python
@property
def use_cloud_noise_detail_wind_speed_vertical() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.use_cloud_noise_detail_wind_speed_vertical"></a>

#### use\_cloud\_noise\_detail\_wind\_speed\_vertical

```python
@use_cloud_noise_detail_wind_speed_vertical.setter
def use_cloud_noise_detail_wind_speed_vertical(value: bool) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_detail_wind_speed_vertical"></a>

#### cloud\_noise\_detail\_wind\_speed\_vertical

```python
@property
def cloud_noise_detail_wind_speed_vertical() -> float
```

(float):  [Read-Write] Vertical wind speed of Cloud Noise Detail in m/s.

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_detail_wind_speed_vertical"></a>

#### cloud\_noise\_detail\_wind\_speed\_vertical

```python
@cloud_noise_detail_wind_speed_vertical.setter
def cloud_noise_detail_wind_speed_vertical(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_detail_wind_speed_vertical_curve"></a>

#### cloud\_noise\_detail\_wind\_speed\_vertical\_curve

```python
@property
def cloud_noise_detail_wind_speed_vertical_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.cloud_noise_detail_wind_speed_vertical_curve"></a>

#### cloud\_noise\_detail\_wind\_speed\_vertical\_curve

```python
@cloud_noise_detail_wind_speed_vertical_curve.setter
def cloud_noise_detail_wind_speed_vertical_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.use_precipitation_wind_direction"></a>

#### use\_precipitation\_wind\_direction

```python
@property
def use_precipitation_wind_direction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.use_precipitation_wind_direction"></a>

#### use\_precipitation\_wind\_direction

```python
@use_precipitation_wind_direction.setter
def use_precipitation_wind_direction(value: bool) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_direction"></a>

#### precipitation\_wind\_direction

```python
@property
def precipitation_wind_direction() -> float
```

(float):  [Read-Write] Wind direction angle of precipitation particles in degrees.

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_direction"></a>

#### precipitation\_wind\_direction

```python
@precipitation_wind_direction.setter
def precipitation_wind_direction(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_direction_curve"></a>

#### precipitation\_wind\_direction\_curve

```python
@property
def precipitation_wind_direction_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_direction_curve"></a>

#### precipitation\_wind\_direction\_curve

```python
@precipitation_wind_direction_curve.setter
def precipitation_wind_direction_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.use_precipitation_wind_speed"></a>

#### use\_precipitation\_wind\_speed

```python
@property
def use_precipitation_wind_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.use_precipitation_wind_speed"></a>

#### use\_precipitation\_wind\_speed

```python
@use_precipitation_wind_speed.setter
def use_precipitation_wind_speed(value: bool) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_speed"></a>

#### precipitation\_wind\_speed

```python
@property
def precipitation_wind_speed() -> float
```

(float):  [Read-Write] Wind speed of precipitation particles.

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_speed"></a>

#### precipitation\_wind\_speed

```python
@precipitation_wind_speed.setter
def precipitation_wind_speed(value: float) -> None
```

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_speed_curve"></a>

#### precipitation\_wind\_speed\_curve

```python
@property
def precipitation_wind_speed_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorWindSettings_51.precipitation_wind_speed_curve"></a>

#### precipitation\_wind\_speed\_curve

```python
@precipitation_wind_speed_curve.setter
def precipitation_wind_speed_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51"></a>