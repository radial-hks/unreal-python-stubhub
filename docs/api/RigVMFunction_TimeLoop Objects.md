## RigVMFunction_TimeLoop Objects

```python
class RigVMFunction_TimeLoop(RigVMFunction_SimBase)
```

Simulates a time value - and outputs loop information

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Timeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute`` (float):  [Read-Write] the overall time in seconds
- ``duration`` (float):  [Read-Write] the duration of a single loop in seconds
- ``even`` (bool):  [Read-Write] true if the iteration of the loop is even
- ``flip_flop`` (float):  [Read-Write] the relative time in seconds (within the loop),
  going from 0 to duration and then back from duration to 0,
  or 0 to 1 and 1 to 0 if Normalize is turned on
- ``normalize`` (bool):  [Read-Write] if set to true the output relative and flipflop
  will be normalized over the duration.
- ``relative`` (float):  [Read-Write] the relative time in seconds (within the loop)
- ``speed`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_TimeLoop.__init__"></a>

#### __init__

```python
def __init__(speed: float = 0.000000,
             duration: float = 0.000000,
             normalize: bool = False,
             absolute: float = 0.000000,
             relative: float = 0.000000,
             flip_flop: float = 0.000000,
             even: bool = False) -> None
```

<a id="unreal.RigVMFunction_TimeLoop.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_TimeLoop.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.RigVMFunction_TimeLoop.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write] the duration of a single loop in seconds

<a id="unreal.RigVMFunction_TimeLoop.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.RigVMFunction_TimeLoop.normalize"></a>

#### normalize

```python
@property
def normalize() -> bool
```

(bool):  [Read-Write] if set to true the output relative and flipflop
will be normalized over the duration.

<a id="unreal.RigVMFunction_TimeLoop.normalize"></a>

#### normalize

```python
@normalize.setter
def normalize(value: bool) -> None
```

<a id="unreal.RigVMFunction_TimeLoop.absolute"></a>

#### absolute

```python
@property
def absolute() -> float
```

(float):  [Read-Only] the overall time in seconds

<a id="unreal.RigVMFunction_TimeLoop.relative"></a>

#### relative

```python
@property
def relative() -> float
```

(float):  [Read-Only] the relative time in seconds (within the loop)

<a id="unreal.RigVMFunction_TimeLoop.flip_flop"></a>

#### flip_flop

```python
@property
def flip_flop() -> float
```

(float):  [Read-Only] the relative time in seconds (within the loop),
going from 0 to duration and then back from duration to 0,
or 0 to 1 and 1 to 0 if Normalize is turned on

<a id="unreal.RigVMFunction_TimeLoop.even"></a>

#### even

```python
@property
def even() -> bool
```

(bool):  [Read-Only] true if the iteration of the loop is even

<a id="unreal.RigUnit_TimeLoop"></a>