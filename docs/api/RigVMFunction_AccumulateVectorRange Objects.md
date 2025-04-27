## RigVMFunction_AccumulateVectorRange Objects

```python
class RigVMFunction_AccumulateVectorRange(RigVMFunction_AccumulateBase)
```

Accumulates the min and max values over time

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Accumulate.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum`` (Vector):  [Read-Write]
- ``minimum`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorRange.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             minimum: Vector = [0.000000, 0.000000, 0.000000],
             maximum: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorRange.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_AccumulateVectorRange.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_AccumulateVectorRange.minimum"></a>

#### minimum

```python
@property
def minimum() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_AccumulateVectorRange.maximum"></a>

#### maximum

```python
@property
def maximum() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_AccumulateVectorRange"></a>