## CelestialPositionData Objects

```python
class CelestialPositionData(StructBase)
```

Celestial Position Data

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorFunctionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``azimuth`` (float):  [Read-Write] Celestial azimuth
- ``elevation`` (float):  [Read-Write] Celestial Elevation

<a id="unreal.CelestialPositionData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(elevation: float = 0.000000, azimuth: float = 0.000000) -> None
```

<a id="unreal.CelestialPositionData.elevation"></a>

#### elevation

```python
@property
def elevation() -> float
```

(float):  [Read-Write] Celestial Elevation

<a id="unreal.CelestialPositionData.elevation"></a>

#### elevation

```python
@elevation.setter
def elevation(value: float) -> None
```

<a id="unreal.CelestialPositionData.azimuth"></a>

#### azimuth

```python
@property
def azimuth() -> float
```

(float):  [Read-Write] Celestial azimuth

<a id="unreal.CelestialPositionData.azimuth"></a>

#### azimuth

```python
@azimuth.setter
def azimuth(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings"></a>