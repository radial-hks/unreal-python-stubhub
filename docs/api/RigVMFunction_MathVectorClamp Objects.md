## RigVMFunction_MathVectorClamp Objects

```python
class RigVMFunction_MathVectorClamp(RigVMFunction_MathVectorBase)
```

Clamps the given value within the range provided by minimum and maximum for each component

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum`` (Vector):  [Read-Write]
- ``minimum`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClamp.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             minimum: Vector = [0.000000, 0.000000, 0.000000],
             maximum: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorClamp.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClamp.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorClamp.minimum"></a>

#### minimum

```python
@property
def minimum() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClamp.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorClamp.maximum"></a>

#### maximum

```python
@property
def maximum() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorClamp.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathVectorClamp.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorClamp"></a>