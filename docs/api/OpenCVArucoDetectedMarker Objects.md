## OpenCVArucoDetectedMarker Objects

```python
class OpenCVArucoDetectedMarker(StructBase)
```

Open CVAruco Detected Marker

**C++ Source:**

- **Plugin**: OpenCV
- **Module**: OpenCVHelper
- **File**: OpenCVBlueprintFunctionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``corners`` (Array[Vector2D]):  [Read-Write]
- ``id`` (int32):  [Read-Write]
- ``pose`` (Transform):  [Read-Write]

<a id="unreal.OpenCVArucoDetectedMarker.__init__"></a>

#### __init__

```python
def __init__(
    id: int = 0,
    corners: Array[Vector2D] = [],
    pose: Transform = [[0.000000, 0.000000, 0.000000],
                       [-0.000000, 0.000000, 0.000000],
                       [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.OpenCVArucoDetectedMarker.id"></a>

#### id

```python
@property
def id() -> int
```

(int32):  [Read-Write]

<a id="unreal.OpenCVArucoDetectedMarker.id"></a>

#### id

```python
@id.setter
def id(value: int) -> None
```

<a id="unreal.OpenCVArucoDetectedMarker.corners"></a>

#### corners

```python
@property
def corners() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.OpenCVArucoDetectedMarker.corners"></a>

#### corners

```python
@corners.setter
def corners(value: Array[Vector2D]) -> None
```

<a id="unreal.OpenCVArucoDetectedMarker.pose"></a>

#### pose

```python
@property
def pose() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.OpenCVArucoDetectedMarker.pose"></a>

#### pose

```python
@pose.setter
def pose(value: Transform) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase"></a>