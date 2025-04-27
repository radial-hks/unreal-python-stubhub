## SunPositionData Objects

```python
class SunPositionData(StructBase)
```

Sun Position Data

**C++ Source:**

- **Plugin**: SunPosition
- **Module**: SunPosition
- **File**: SunPosition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``azimuth`` (float):  [Read-Write] Sun azimuth
- ``corrected_elevation`` (float):  [Read-Write] Sun Elevation, corrected for atmospheric diffraction
- ``elevation`` (float):  [Read-Write] Sun Elevation
- ``solar_noon`` (Timespan):  [Read-Write] Solar noon
- ``sunrise_time`` (Timespan):  [Read-Write] Sunrise time
- ``sunset_time`` (Timespan):  [Read-Write] Sunset time

<a id="unreal.SunPositionData.__init__"></a>

#### __init__

```python
def __init__(elevation: float = 0.000000,
             corrected_elevation: float = 0.000000,
             azimuth: float = 0.000000,
             sunrise_time: Timespan = [0, 0, 0, 0, 0],
             sunset_time: Timespan = [0, 0, 0, 0, 0],
             solar_noon: Timespan = [0, 0, 0, 0, 0]) -> None
```

<a id="unreal.SunPositionData.elevation"></a>

#### elevation

```python
@property
def elevation() -> float
```

(float):  [Read-Write] Sun Elevation

<a id="unreal.SunPositionData.elevation"></a>

#### elevation

```python
@elevation.setter
def elevation(value: float) -> None
```

<a id="unreal.SunPositionData.corrected_elevation"></a>

#### corrected_elevation

```python
@property
def corrected_elevation() -> float
```

(float):  [Read-Write] Sun Elevation, corrected for atmospheric diffraction

<a id="unreal.SunPositionData.corrected_elevation"></a>

#### corrected_elevation

```python
@corrected_elevation.setter
def corrected_elevation(value: float) -> None
```

<a id="unreal.SunPositionData.azimuth"></a>

#### azimuth

```python
@property
def azimuth() -> float
```

(float):  [Read-Write] Sun azimuth

<a id="unreal.SunPositionData.azimuth"></a>

#### azimuth

```python
@azimuth.setter
def azimuth(value: float) -> None
```

<a id="unreal.SunPositionData.sunrise_time"></a>

#### sunrise_time

```python
@property
def sunrise_time() -> Timespan
```

(Timespan):  [Read-Write] Sunrise time

<a id="unreal.SunPositionData.sunrise_time"></a>

#### sunrise_time

```python
@sunrise_time.setter
def sunrise_time(value: Timespan) -> None
```

<a id="unreal.SunPositionData.sunset_time"></a>

#### sunset_time

```python
@property
def sunset_time() -> Timespan
```

(Timespan):  [Read-Write] Sunset time

<a id="unreal.SunPositionData.sunset_time"></a>

#### sunset_time

```python
@sunset_time.setter
def sunset_time(value: Timespan) -> None
```

<a id="unreal.SunPositionData.solar_noon"></a>

#### solar_noon

```python
@property
def solar_noon() -> Timespan
```

(Timespan):  [Read-Write] Solar noon

<a id="unreal.SunPositionData.solar_noon"></a>

#### solar_noon

```python
@solar_noon.setter
def solar_noon(value: Timespan) -> None
```

<a id="unreal.Object"></a>