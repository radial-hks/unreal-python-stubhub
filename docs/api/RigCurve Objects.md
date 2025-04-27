## RigCurve Objects

```python
class RigCurve(RigElement)
```

Rig Curve

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigCurveContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``index`` (int32):  [Read-Only]
- ``name`` (Name):  [Read-Write]
- ``value`` (float):  [Read-Only]

<a id="unreal.RigCurve.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             index: int = 0,
             value: float = 0.000000) -> None
```

<a id="unreal.RigCurve.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Only]

<a id="unreal.RigSpace"></a>