## RigVMFunction_GetWorldTime Objects

```python
class RigVMFunction_GetWorldTime(RigVMFunction_AnimBase)
```

Returns the current time (year, month, day, hour, minute)

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_GetWorldTime.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``day`` (float):  [Read-Write]
- ``hours`` (float):  [Read-Write]
- ``minutes`` (float):  [Read-Write]
- ``month`` (float):  [Read-Write]
- ``overall_seconds`` (float):  [Read-Write]
- ``seconds`` (float):  [Read-Write]
- ``week_day`` (float):  [Read-Write]
- ``year`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_GetWorldTime.__init__"></a>

#### __init__

```python
def __init__(year: float = 0.000000,
             month: float = 0.000000,
             day: float = 0.000000,
             week_day: float = 0.000000,
             hours: float = 0.000000,
             minutes: float = 0.000000,
             seconds: float = 0.000000,
             overall_seconds: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_GetWorldTime.year"></a>

#### year

```python
@property
def year() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_GetWorldTime.month"></a>

#### month

```python
@property
def month() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_GetWorldTime.day"></a>

#### day

```python
@property
def day() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_GetWorldTime.week_day"></a>

#### week_day

```python
@property
def week_day() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_GetWorldTime.hours"></a>

#### hours

```python
@property
def hours() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_GetWorldTime.minutes"></a>

#### minutes

```python
@property
def minutes() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_GetWorldTime.seconds"></a>

#### seconds

```python
@property
def seconds() -> float
```

(float):  [Read-Only]

<a id="unreal.RigVMFunction_GetWorldTime.overall_seconds"></a>

#### overall_seconds

```python
@property
def overall_seconds() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_GetWorldTime"></a>