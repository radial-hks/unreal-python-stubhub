## RigUnit_SpringInterp Objects

```python
class RigUnit_SpringInterp(RigVMFunction_SimBase)
```

Uses a simple spring model to interpolate a float from Current to Target.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SpringInterp.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``critical_damping`` (float):  [Read-Write]
- ``current`` (float):  [Read-Write]
- ``mass`` (float):  [Read-Write]
- ``result`` (float):  [Read-Write]
- ``stiffness`` (float):  [Read-Write]
- ``target`` (float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterp.__init__"></a>

#### __init__

```python
def __init__(current: float = 0.000000,
             target: float = 0.000000,
             stiffness: float = 0.000000,
             critical_damping: float = 0.000000,
             mass: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigUnit_SpringInterp.current"></a>

#### current

```python
@property
def current() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterp.current"></a>

#### current

```python
@current.setter
def current(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterp.target"></a>

#### target

```python
@property
def target() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterp.target"></a>

#### target

```python
@target.setter
def target(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterp.stiffness"></a>

#### stiffness

```python
@property
def stiffness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterp.stiffness"></a>

#### stiffness

```python
@stiffness.setter
def stiffness(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterp.critical_damping"></a>

#### critical_damping

```python
@property
def critical_damping() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterp.critical_damping"></a>

#### critical_damping

```python
@critical_damping.setter
def critical_damping(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterp.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_SpringInterp.mass"></a>

#### mass

```python
@mass.setter
def mass(value: float) -> None
```

<a id="unreal.RigUnit_SpringInterp.result"></a>

#### result

```python
@property
def result() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_SpringInterpVector"></a>