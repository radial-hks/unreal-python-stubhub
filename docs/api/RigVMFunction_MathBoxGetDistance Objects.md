## RigVMFunction_MathBoxGetDistance Objects

```python
class RigVMFunction_MathBoxGetDistance(RigVMFunction_MathBoxBase)
```

Returns the distance to a given box

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathBox.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``distance`` (float):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``square`` (bool):  [Read-Write] if true the distance will be returned square
- ``valid`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetDistance.__init__"></a>

#### __init__

```python
def __init__(box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             position: Vector = [0.000000, 0.000000, 0.000000],
             square: bool = False,
             valid: bool = False,
             distance: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetDistance.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetDistance.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetDistance.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathBoxGetDistance.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetDistance.square"></a>

#### square

```python
@property
def square() -> bool
```

(bool):  [Read-Write] if true the distance will be returned square

<a id="unreal.RigVMFunction_MathBoxGetDistance.square"></a>

#### square

```python
@square.setter
def square(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathBoxGetDistance.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxGetDistance.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_MathBoxIsInside"></a>