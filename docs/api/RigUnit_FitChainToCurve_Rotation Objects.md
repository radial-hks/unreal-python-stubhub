## RigUnit_FitChainToCurve_Rotation Objects

```python
class RigUnit_FitChainToCurve_Rotation(StructBase)
```

Rig Unit Fit Chain to Curve Rotation

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_FitChainToCurve.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ratio`` (float):  [Read-Only] The ratio of where this rotation sits along the chain
- ``rotation`` (Quat):  [Read-Write] The rotation to be applied

<a id="unreal.RigUnit_FitChainToCurve_Rotation.__init__"></a>

#### __init__

```python
def __init__(rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             ratio: float = 0.000000) -> None
```

<a id="unreal.RigUnit_FitChainToCurve_Rotation.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

(Quat):  [Read-Write] The rotation to be applied

<a id="unreal.RigUnit_FitChainToCurve_Rotation.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Quat) -> None
```

<a id="unreal.RigUnit_FitChainToCurve_Rotation.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Only] The ratio of where this rotation sits along the chain

<a id="unreal.RigUnit_FitChainToCurve_DebugSettings"></a>