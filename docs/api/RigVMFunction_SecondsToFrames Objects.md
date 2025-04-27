## RigVMFunction_SecondsToFrames Objects

```python
class RigVMFunction_SecondsToFrames(RigVMFunction_AnimBase)
```

Converts seconds to frames based on the current frame rate

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_TimeConversion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frames`` (float):  [Read-Write]
- ``seconds`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_SecondsToFrames.__init__"></a>

#### __init__

```python
def __init__(seconds: float = 0.000000, frames: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_SecondsToFrames.seconds"></a>

#### seconds

```python
@property
def seconds() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_SecondsToFrames.seconds"></a>

#### seconds

```python
@seconds.setter
def seconds(value: float) -> None
```

<a id="unreal.RigVMFunction_SecondsToFrames.frames"></a>

#### frames

```python
@property
def frames() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_SecondsToFrames"></a>