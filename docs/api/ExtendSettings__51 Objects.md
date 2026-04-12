## ExtendSettings\_51 Objects

```python
class ExtendSettings_51(StructBase)
```

额外参数设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cloud_map_offset`` (Vector2D):  [Read-Write]
- ``cloud_map_offset_curve`` (CurveVector):  [Read-Write]
- ``moon_azimuth`` (float):  [Read-Write]
- ``moon_elevation`` (float):  [Read-Write]
- ``moonrise_time`` (float):  [Read-Write]
- ``moonset_time`` (float):  [Read-Write]
- ``sun_azimuth`` (float):  [Read-Write]
- ``sun_elevation`` (float):  [Read-Write]
- ``sunrise_time`` (float):  [Read-Write]
- ``sunset_time`` (float):  [Read-Write]
- ``use_cloud_map_offset`` (bool):  [Read-Write] 云偏移

<a id="unreal.ExtendSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_cloud_map_offset: bool = False,
             cloud_map_offset: Vector2D = [0.000000, 0.000000],
             cloud_map_offset_curve: CurveVector = None,
             sunrise_time: float = 0.000000,
             sunset_time: float = 0.000000,
             sun_elevation: float = 0.000000,
             sun_azimuth: float = 0.000000,
             moonrise_time: float = 0.000000,
             moonset_time: float = 0.000000,
             moon_elevation: float = 0.000000,
             moon_azimuth: float = 0.000000) -> None
```

<a id="unreal.ExtendSettings_51.use_cloud_map_offset"></a>

#### use\_cloud\_map\_offset

```python
@property
def use_cloud_map_offset() -> bool
```

(bool):  [Read-Write] 云偏移

<a id="unreal.ExtendSettings_51.use_cloud_map_offset"></a>

#### use\_cloud\_map\_offset

```python
@use_cloud_map_offset.setter
def use_cloud_map_offset(value: bool) -> None
```

<a id="unreal.ExtendSettings_51.cloud_map_offset"></a>

#### cloud\_map\_offset

```python
@property
def cloud_map_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.ExtendSettings_51.cloud_map_offset"></a>

#### cloud\_map\_offset

```python
@cloud_map_offset.setter
def cloud_map_offset(value: Vector2D) -> None
```

<a id="unreal.ExtendSettings_51.cloud_map_offset_curve"></a>

#### cloud\_map\_offset\_curve

```python
@property
def cloud_map_offset_curve() -> CurveVector
```

(CurveVector):  [Read-Write]

<a id="unreal.ExtendSettings_51.cloud_map_offset_curve"></a>

#### cloud\_map\_offset\_curve

```python
@cloud_map_offset_curve.setter
def cloud_map_offset_curve(value: CurveVector) -> None
```

<a id="unreal.ExtendSettings_51.sunrise_time"></a>

#### sunrise\_time

```python
@property
def sunrise_time() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.sunrise_time"></a>

#### sunrise\_time

```python
@sunrise_time.setter
def sunrise_time(value: float) -> None
```

<a id="unreal.ExtendSettings_51.sunset_time"></a>

#### sunset\_time

```python
@property
def sunset_time() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.sunset_time"></a>

#### sunset\_time

```python
@sunset_time.setter
def sunset_time(value: float) -> None
```

<a id="unreal.ExtendSettings_51.sun_elevation"></a>

#### sun\_elevation

```python
@property
def sun_elevation() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.sun_elevation"></a>

#### sun\_elevation

```python
@sun_elevation.setter
def sun_elevation(value: float) -> None
```

<a id="unreal.ExtendSettings_51.sun_azimuth"></a>

#### sun\_azimuth

```python
@property
def sun_azimuth() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.sun_azimuth"></a>

#### sun\_azimuth

```python
@sun_azimuth.setter
def sun_azimuth(value: float) -> None
```

<a id="unreal.ExtendSettings_51.moonrise_time"></a>

#### moonrise\_time

```python
@property
def moonrise_time() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.moonrise_time"></a>

#### moonrise\_time

```python
@moonrise_time.setter
def moonrise_time(value: float) -> None
```

<a id="unreal.ExtendSettings_51.moonset_time"></a>

#### moonset\_time

```python
@property
def moonset_time() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.moonset_time"></a>

#### moonset\_time

```python
@moonset_time.setter
def moonset_time(value: float) -> None
```

<a id="unreal.ExtendSettings_51.moon_elevation"></a>

#### moon\_elevation

```python
@property
def moon_elevation() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.moon_elevation"></a>

#### moon\_elevation

```python
@moon_elevation.setter
def moon_elevation(value: float) -> None
```

<a id="unreal.ExtendSettings_51.moon_azimuth"></a>

#### moon\_azimuth

```python
@property
def moon_azimuth() -> float
```

(float):  [Read-Write]

<a id="unreal.ExtendSettings_51.moon_azimuth"></a>

#### moon\_azimuth

```python
@moon_azimuth.setter
def moon_azimuth(value: float) -> None
```

<a id="unreal.TimeInterval"></a>