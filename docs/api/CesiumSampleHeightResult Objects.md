## CesiumSampleHeightResult Objects

```python
class CesiumSampleHeightResult(StructBase)
```

The result of sampling the height on a tileset at the given cartographic
position.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumSampleHeightResult.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``longitude_latitude_height`` (Vector):  [Read-Write] The Longitude (X) and Latitude (Y) are the same values provided on input.
  The Height (Z) is the height sampled from the tileset if the SampleSuccess
  property is true, or the original height provided on input if SampleSuccess
  is false.
- ``sample_success`` (bool):  [Read-Write] True if the height as sampled from the tileset successfully. False if the
  tileset doesn't have any height at that position, or if something went
  wrong. If something went wrong, the Warnings pin of the sampling function
  will have more information about the problem.

<a id="unreal.CesiumSampleHeightResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(longitude_latitude_height: Vector = [
    0.000000, 0.000000, 0.000000
],
             sample_success: bool = False) -> None
```

<a id="unreal.CesiumSampleHeightResult.longitude_latitude_height"></a>

#### longitude\_latitude\_height

```python
@property
def longitude_latitude_height() -> Vector
```

(Vector):  [Read-Write] The Longitude (X) and Latitude (Y) are the same values provided on input.
The Height (Z) is the height sampled from the tileset if the SampleSuccess
property is true, or the original height provided on input if SampleSuccess
is false.

<a id="unreal.CesiumSampleHeightResult.longitude_latitude_height"></a>

#### longitude\_latitude\_height

```python
@longitude_latitude_height.setter
def longitude_latitude_height(value: Vector) -> None
```

<a id="unreal.CesiumSampleHeightResult.sample_success"></a>

#### sample\_success

```python
@property
def sample_success() -> bool
```

(bool):  [Read-Write] True if the height as sampled from the tileset successfully. False if the
tileset doesn't have any height at that position, or if something went
wrong. If something went wrong, the Warnings pin of the sampling function
will have more information about the problem.

<a id="unreal.CesiumSampleHeightResult.sample_success"></a>

#### sample\_success

```python
@sample_success.setter
def sample_success(value: bool) -> None
```

<a id="unreal.ActorDataLayer"></a>