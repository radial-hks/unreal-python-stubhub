## DisplayClusterPositionalParams Objects

```python
class DisplayClusterPositionalParams(StructBase)
```

Positional location and rotation parameters for use with nDisplay stage actors.
Note that the origin point is purposely not included as these parameters are meant to be shared between actors
with different origins.

**C++ Source:**

- **Plugin**: nDisplayModularFeatures
- **Module**: DisplayClusterLightCardExtender
- **File**: DisplayClusterPositionalParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_from_center`` (double):  [Read-Write]
- ``latitude`` (double):  [Read-Write]
- ``longitude`` (double):  [Read-Write]
- ``pitch`` (double):  [Read-Write]
- ``radial_offset`` (double):  [Read-Write]
- ``scale`` (Vector2D):  [Read-Write]
- ``spin`` (double):  [Read-Write]
- ``yaw`` (double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.__init__"></a>

#### __init__

```python
def __init__(distance_from_center: float = 0.000000,
             longitude: float = 0.000000,
             latitude: float = 0.000000,
             spin: float = 0.000000,
             pitch: float = 0.000000,
             yaw: float = 0.000000,
             radial_offset: float = 0.000000,
             scale: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.DisplayClusterPositionalParams.distance_from_center"></a>

#### distance_from_center

```python
@property
def distance_from_center() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.distance_from_center"></a>

#### distance_from_center

```python
@distance_from_center.setter
def distance_from_center(value: float) -> None
```

<a id="unreal.DisplayClusterPositionalParams.longitude"></a>

#### longitude

```python
@property
def longitude() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.longitude"></a>

#### longitude

```python
@longitude.setter
def longitude(value: float) -> None
```

<a id="unreal.DisplayClusterPositionalParams.latitude"></a>

#### latitude

```python
@property
def latitude() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.latitude"></a>

#### latitude

```python
@latitude.setter
def latitude(value: float) -> None
```

<a id="unreal.DisplayClusterPositionalParams.spin"></a>

#### spin

```python
@property
def spin() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.spin"></a>

#### spin

```python
@spin.setter
def spin(value: float) -> None
```

<a id="unreal.DisplayClusterPositionalParams.pitch"></a>

#### pitch

```python
@property
def pitch() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.pitch"></a>

#### pitch

```python
@pitch.setter
def pitch(value: float) -> None
```

<a id="unreal.DisplayClusterPositionalParams.yaw"></a>

#### yaw

```python
@property
def yaw() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.yaw"></a>

#### yaw

```python
@yaw.setter
def yaw(value: float) -> None
```

<a id="unreal.DisplayClusterPositionalParams.radial_offset"></a>

#### radial_offset

```python
@property
def radial_offset() -> float
```

(double):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.radial_offset"></a>

#### radial_offset

```python
@radial_offset.setter
def radial_offset(value: float) -> None
```

<a id="unreal.DisplayClusterPositionalParams.scale"></a>

#### scale

```python
@property
def scale() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.DisplayClusterPositionalParams.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector2D) -> None
```

<a id="unreal.GeometryMaskReadParameters"></a>