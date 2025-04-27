## RigVMFunction_MathMatrixToVectors Objects

```python
class RigVMFunction_MathMatrixToVectors(RigVMFunction_MathMatrixBase)
```

Converts the matrix to its vectors

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathMatrix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``origin`` (Vector):  [Read-Write]
- ``value`` (Matrix):  [Read-Write]
- ``x`` (Vector):  [Read-Write]
- ``y`` (Vector):  [Read-Write]
- ``z`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixToVectors.__init__"></a>

#### __init__

```python
def __init__(value: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                              [0.000000, 0.000000, 0.000000, 0.000000],
                              [0.000000, 0.000000, 0.000000, 0.000000],
                              [0.000000, 0.000000, 0.000000, 0.000000]],
             origin: Vector = [0.000000, 0.000000, 0.000000],
             x: Vector = [0.000000, 0.000000, 0.000000],
             y: Vector = [0.000000, 0.000000, 0.000000],
             z: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathMatrixToVectors.value"></a>

#### value

```python
@property
def value() -> Matrix
```

(Matrix):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixToVectors.value"></a>

#### value

```python
@value.setter
def value(value: Matrix) -> None
```

<a id="unreal.RigVMFunction_MathMatrixToVectors.origin"></a>

#### origin

```python
@property
def origin() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathMatrixToVectors.x"></a>

#### x

```python
@property
def x() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathMatrixToVectors.y"></a>

#### y

```python
@property
def y() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathMatrixToVectors.z"></a>

#### z

```python
@property
def z() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathMatrixToVectors"></a>