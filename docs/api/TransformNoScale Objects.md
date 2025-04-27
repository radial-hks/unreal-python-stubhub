## TransformNoScale Objects

```python
class TransformNoScale(StructBase)
```

Transform No Scale

**C++ Source:**

- **Module**: AnimationCore
- **File**: TransformNoScale.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write] The translation of this transform
- ``rotation`` (Quat):  [Read-Write] The rotation of this transform

<a id="unreal.TransformNoScale.__init__"></a>

#### __init__

```python
def __init__(
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.TransformNoScale.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] The translation of this transform

<a id="unreal.TransformNoScale.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.TransformNoScale.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

(Quat):  [Read-Write] The rotation of this transform

<a id="unreal.TransformNoScale.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Quat) -> None
```

<a id="unreal.JsonStringifyOptions"></a>