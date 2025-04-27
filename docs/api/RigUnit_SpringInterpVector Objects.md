## RigUnit_SpringInterpVector Objects

```python
class RigUnit_SpringInterpVector(RigVMFunction_SimBase)
```

Uses a simple spring model to interpolate a vector from Current to Target.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SpringInterp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``critical_damping`` (float):  [Read-Write]
- ``current`` (Vector):  [Read-Write]
- ``mass`` (float):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``stiffness`` (float):  [Read-Write]
- ``target`` (Vector):  [Read-Write]

<a id="unreal.RigUnit_SpringInterpVector.__init__"></a>

#### __init__

```python
def __init__(current: Vector = [0.000000, 0.000000, 0.000000],
             target: Vector = [0.000000, 0.000000, 0.000000],
             stiffness: float = 0.000000,
             critical_damping: float = 0.000000,
             mass: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_SpringInterpVector.current"></a>

#### current

```python
@property
def current() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_SpringInterpVector.current"></a>

#### current

```python
@current.setter
def current(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringInterpVector.target"></a>

#### target

```python
@property
def target() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_SpringInterpVector.target"></a>

#### target

```python
@target.setter
def target(value: Vector) -> None
```

<a id="unreal.RigUnit_SpringInterpVector.stiffness"></a>

#### stiffness

```python
@property
def stiffness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterpVector.stiffness"></a>

#### stiffness

```python
@stiffness.setter
def stiffness(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpVector.critical_damping"></a>

#### critical_damping

```python
@property
def critical_damping() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterpVector.critical_damping"></a>

#### critical_damping

```python
@critical_damping.setter
def critical_damping(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpVector.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterpVector.mass"></a>

#### mass

```python
@mass.setter
def mass(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterpVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_SpringInterpV2"></a>