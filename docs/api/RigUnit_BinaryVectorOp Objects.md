## RigUnit_BinaryVectorOp Objects

```python
class RigUnit_BinaryVectorOp(RigUnit)
```

Two args and a result of Vector type

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Vector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``argument0`` (Vector):  [Read-Write]
- ``argument1`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_BinaryVectorOp.__init__"></a>

#### __init__

```python
def __init__(argument0: Vector = [0.000000, 0.000000, 0.000000],
             argument1: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_BinaryVectorOp.argument0"></a>

#### argument0

```python
@property
def argument0() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_BinaryVectorOp.argument0"></a>

#### argument0

```python
@argument0.setter
def argument0(value: Vector) -> None
```

<a id="unreal.RigUnit_BinaryVectorOp.argument1"></a>

#### argument1

```python
@property
def argument1() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_BinaryVectorOp.argument1"></a>

#### argument1

```python
@argument1.setter
def argument1(value: Vector) -> None
```

<a id="unreal.RigUnit_BinaryVectorOp.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_Multiply_VectorVector"></a>