## NodalPointOffset Objects

```python
class NodalPointOffset(StructBase)
```

Lens nodal point offset

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location_offset`` (Vector):  [Read-Write]
- ``rotation_offset`` (Quat):  [Read-Write]

<a id="unreal.NodalPointOffset.__init__"></a>

#### __init__

```python
def __init__(
        location_offset: Vector = [0.000000, 0.000000, 0.000000],
        rotation_offset: Quat = [0.000000, 0.000000, 0.000000,
                                 1.000000]) -> None
```

<a id="unreal.NodalPointOffset.location_offset"></a>

#### location_offset

```python
@property
def location_offset() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.NodalPointOffset.location_offset"></a>

#### location_offset

```python
@location_offset.setter
def location_offset(value: Vector) -> None
```

<a id="unreal.NodalPointOffset.rotation_offset"></a>

#### rotation_offset

```python
@property
def rotation_offset() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.NodalPointOffset.rotation_offset"></a>

#### rotation_offset

```python
@rotation_offset.setter
def rotation_offset(value: Quat) -> None
```

<a id="unreal.ImageCenterInfo"></a>