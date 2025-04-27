## SplinePoint Objects

```python
class SplinePoint(StructBase)
```

Spline Point

**C++ Source:**

- **Module**: Engine
- **File**: SplineComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``arrive_tangent`` (Vector):  [Read-Write]
- ``input_key`` (float):  [Read-Write]
- ``leave_tangent`` (Vector):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``type`` (SplinePointType):  [Read-Write]

<a id="unreal.SplinePoint.__init__"></a>

#### __init__

```python
def __init__(input_key: float = 0.000000,
             position: Vector = [0.000000, 0.000000, 0.000000],
             arrive_tangent: Vector = [0.000000, 0.000000, 0.000000],
             leave_tangent: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000],
             type: SplinePointType = SplinePointType.LINEAR) -> None
```

<a id="unreal.SplinePoint.input_key"></a>

#### input_key

```python
@property
def input_key() -> float
```

(float):  [Read-Write]

<a id="unreal.SplinePoint.input_key"></a>

#### input_key

```python
@input_key.setter
def input_key(value: float) -> None
```

<a id="unreal.SplinePoint.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SplinePoint.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.SplinePoint.arrive_tangent"></a>

#### arrive_tangent

```python
@property
def arrive_tangent() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SplinePoint.arrive_tangent"></a>

#### arrive_tangent

```python
@arrive_tangent.setter
def arrive_tangent(value: Vector) -> None
```

<a id="unreal.SplinePoint.leave_tangent"></a>

#### leave_tangent

```python
@property
def leave_tangent() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SplinePoint.leave_tangent"></a>

#### leave_tangent

```python
@leave_tangent.setter
def leave_tangent(value: Vector) -> None
```

<a id="unreal.SplinePoint.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.SplinePoint.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.SplinePoint.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SplinePoint.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.SplinePoint.type"></a>

#### type

```python
@property
def type() -> SplinePointType
```

(SplinePointType):  [Read-Write]

<a id="unreal.SplinePoint.type"></a>

#### type

```python
@type.setter
def type(value: SplinePointType) -> None
```

<a id="unreal.CullDistanceSizePair"></a>