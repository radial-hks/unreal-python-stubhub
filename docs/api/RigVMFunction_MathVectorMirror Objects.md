## RigVMFunction_MathVectorMirror Objects

```python
class RigVMFunction_MathVectorMirror(RigVMFunction_MathVectorBase)
```

Mirror a vector about a normal vector.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``normal`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorMirror.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             normal: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorMirror.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorMirror.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorMirror.normal"></a>

#### normal

```python
@property
def normal() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorMirror.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorMirror.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorMirror"></a>