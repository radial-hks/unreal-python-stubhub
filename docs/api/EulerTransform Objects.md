## EulerTransform Objects

```python
class EulerTransform(StructBase)
```

Euler Transform

**C++ Source:**

- **Module**: AnimationCore
- **File**: EulerTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write] The translation of this transform
- ``rotation`` (Rotator):  [Read-Write] The rotation of this transform
- ``scale`` (Vector):  [Read-Write] The scale of this transform

<a id="unreal.EulerTransform.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.EulerTransform.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] The translation of this transform

<a id="unreal.EulerTransform.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.EulerTransform.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] The rotation of this transform

<a id="unreal.EulerTransform.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.EulerTransform.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write] The scale of this transform

<a id="unreal.EulerTransform.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.TransformNoScale"></a>