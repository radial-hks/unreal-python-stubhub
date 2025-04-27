## GeographicCoordinates Objects

```python
class GeographicCoordinates(StructBase)
```

Geographic Coordinates

**C++ Source:**

- **Plugin**: GeoReferencing
- **Module**: GeoReferencing
- **File**: GeographicCoordinates.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``altitude`` (double):  [Read-Write]
- ``latitude`` (double):  [Read-Write]
- ``longitude`` (double):  [Read-Write] FVector where X = Latitude, Y = Longitude, Z = Altitude

<a id="unreal.GeographicCoordinates.__init__"></a>

#### __init__

```python
def __init__(longitude: float = 0.000000,
             latitude: float = 0.000000,
             altitude: float = 0.000000) -> None
```

<a id="unreal.GeographicCoordinates.longitude"></a>

#### longitude

```python
@property
def longitude() -> float
```

(double):  [Read-Write] FVector where X = Latitude, Y = Longitude, Z = Altitude

<a id="unreal.GeographicCoordinates.longitude"></a>

#### longitude

```python
@longitude.setter
def longitude(value: float) -> None
```

<a id="unreal.GeographicCoordinates.latitude"></a>

#### latitude

```python
@property
def latitude() -> float
```

(double):  [Read-Write]

<a id="unreal.GeographicCoordinates.latitude"></a>

#### latitude

```python
@latitude.setter
def latitude(value: float) -> None
```

<a id="unreal.GeographicCoordinates.altitude"></a>

#### altitude

```python
@property
def altitude() -> float
```

(double):  [Read-Write]

<a id="unreal.GeographicCoordinates.altitude"></a>

#### altitude

```python
@altitude.setter
def altitude(value: float) -> None
```

<a id="unreal.MVVMBlueprintFunctionReference"></a>