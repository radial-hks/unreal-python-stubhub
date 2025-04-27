## RigVMFunction_FramesToSeconds Objects

```python
class RigVMFunction_FramesToSeconds(RigVMFunction_AnimBase)
```

Converts frames to seconds based on the current frame rate

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_TimeConversion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frames`` (float):  [Read-Write]
- ``seconds`` (float):  [Read-Write]

<a id="unreal.RigVMFunction_FramesToSeconds.__init__"></a>

#### __init__

```python
def __init__(frames: float = 0.000000, seconds: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_FramesToSeconds.frames"></a>

#### frames

```python
@property
def frames() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_FramesToSeconds.frames"></a>

#### frames

```python
@frames.setter
def frames(value: float) -> None
```

<a id="unreal.RigVMFunction_FramesToSeconds.seconds"></a>

#### seconds

```python
@property
def seconds() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_FramesToSeconds"></a>