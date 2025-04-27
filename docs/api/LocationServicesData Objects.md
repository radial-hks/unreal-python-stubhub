## LocationServicesData Objects

```python
class LocationServicesData(StructBase)
```

Struct to hold relevant location data retrieved from the mobile implementation's Location Service

**C++ Source:**

- **Plugin**: LocationServicesBPLibrary
- **Module**: LocationServicesBPLibrary
- **File**: LocationServicesBPLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``altitude`` (float):  [Read-Write] In meters, if provided with the result
- ``horizontal_accuracy`` (float):  [Read-Write] Estimated horizontal (Android: overall) accuracy of the result, in meters
- ``latitude`` (float):  [Read-Write]
- ``longitude`` (float):  [Read-Write]
- ``timestamp`` (float):  [Read-Write] Timestamp from when this location data was taken (UTC time in milliseconds since 1 January 1970)
- ``vertical_accuracy`` (float):  [Read-Write] Estimated accuracy of the result, in meters (iOS only)

<a id="unreal.LocationServicesData.__init__"></a>

#### __init__

```python
def __init__(timestamp: float = 0.000000,
             longitude: float = 0.000000,
             latitude: float = 0.000000,
             horizontal_accuracy: float = 0.000000,
             vertical_accuracy: float = 0.000000,
             altitude: float = 0.000000) -> None
```

<a id="unreal.LocationServicesData.timestamp"></a>

#### timestamp

```python
@property
def timestamp() -> float
```

(float):  [Read-Write] Timestamp from when this location data was taken (UTC time in milliseconds since 1 January 1970)

<a id="unreal.LocationServicesData.timestamp"></a>

#### timestamp

```python
@timestamp.setter
def timestamp(value: float) -> None
```

<a id="unreal.LocationServicesData.longitude"></a>

#### longitude

```python
@property
def longitude() -> float
```

(float):  [Read-Write]

<a id="unreal.LocationServicesData.longitude"></a>

#### longitude

```python
@longitude.setter
def longitude(value: float) -> None
```

<a id="unreal.LocationServicesData.latitude"></a>

#### latitude

```python
@property
def latitude() -> float
```

(float):  [Read-Write]

<a id="unreal.LocationServicesData.latitude"></a>

#### latitude

```python
@latitude.setter
def latitude(value: float) -> None
```

<a id="unreal.LocationServicesData.horizontal_accuracy"></a>

#### horizontal_accuracy

```python
@property
def horizontal_accuracy() -> float
```

(float):  [Read-Write] Estimated horizontal (Android: overall) accuracy of the result, in meters

<a id="unreal.LocationServicesData.horizontal_accuracy"></a>

#### horizontal_accuracy

```python
@horizontal_accuracy.setter
def horizontal_accuracy(value: float) -> None
```

<a id="unreal.LocationServicesData.vertical_accuracy"></a>

#### vertical_accuracy

```python
@property
def vertical_accuracy() -> float
```

(float):  [Read-Write] Estimated accuracy of the result, in meters (iOS only)

<a id="unreal.LocationServicesData.vertical_accuracy"></a>

#### vertical_accuracy

```python
@vertical_accuracy.setter
def vertical_accuracy(value: float) -> None
```

<a id="unreal.LocationServicesData.altitude"></a>

#### altitude

```python
@property
def altitude() -> float
```

(float):  [Read-Write] In meters, if provided with the result

<a id="unreal.LocationServicesData.altitude"></a>

#### altitude

```python
@altitude.setter
def altitude(value: float) -> None
```

<a id="unreal.MetasoundFrontendVersionNumber"></a>