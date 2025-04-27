## RigVMFunction_MathMatrixFromVectors Objects

```python
class RigVMFunction_MathMatrixFromVectors(RigVMFunction_MathMatrixBase)
```

Makes a matrix from its vectors

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathMatrix.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``origin`` (Vector):  [Read-Write]
- ``result`` (Matrix):  [Read-Write]
- ``x`` (Vector):  [Read-Write]
- ``y`` (Vector):  [Read-Write]
- ``z`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromVectors.__init__"></a>

#### __init__

```python
def __init__(
    origin: Vector = [0.000000, 0.000000, 0.000000],
    x: Vector = [0.000000, 0.000000, 0.000000],
    y: Vector = [0.000000, 0.000000, 0.000000],
    z: Vector = [0.000000, 0.000000, 0.000000],
    result: Matrix = [[0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000],
                      [0.000000, 0.000000, 0.000000, 0.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromVectors.origin"></a>

#### origin

```python
@property
def origin() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromVectors.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromVectors.x"></a>

#### x

```python
@property
def x() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromVectors.x"></a>

#### x

```python
@x.setter
def x(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromVectors.y"></a>

#### y

```python
@property
def y() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromVectors.y"></a>

#### y

```python
@y.setter
def y(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromVectors.z"></a>

#### z

```python
@property
def z() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathMatrixFromVectors.z"></a>

#### z

```python
@z.setter
def z(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathMatrixFromVectors.result"></a>

#### result

```python
@property
def result() -> Matrix
```

(Matrix):  [Read-Only]

<a id="unreal.RigUnit_MathMatrixFromVectors"></a>