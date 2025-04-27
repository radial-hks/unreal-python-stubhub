## TargetChainSpeedPlantSettings Objects

```python
class TargetChainSpeedPlantSettings(StructBase)
```

Target Chain Speed Plant Settings

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_speed_planting`` (bool):  [Read-Write] The name of the curve on the source animation that contains the speed of the end effector bone.
- ``speed_curve_name`` (Name):  [Read-Write] The name of the curve on the source animation that contains the speed of the end effector bone.
- ``speed_threshold`` (float):  [Read-Write] Range 0 to 100. Default 15. The maximum speed a source bone can be moving while being considered 'planted'.
  The target IK goal will not be allowed to move whenever the source bone speed drops below this threshold speed.
- ``unplant_critical_damping`` (float):  [Read-Write] How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)
- ``unplant_stiffness`` (float):  [Read-Write] How stiff the spring model is that smoothly pulls the IK position after unplanting (more stiffness means more oscillation around the target value)

<a id="unreal.TargetChainSpeedPlantSettings.__init__"></a>

#### __init__

```python
def __init__(enable_speed_planting: bool = False,
             speed_curve_name: Name = "None",
             speed_threshold: float = 0.000000,
             unplant_stiffness: float = 0.000000,
             unplant_critical_damping: float = 0.000000) -> None
```

<a id="unreal.TargetChainSpeedPlantSettings.enable_speed_planting"></a>

#### enable_speed_planting

```python
@property
def enable_speed_planting() -> bool
```

(bool):  [Read-Write] The name of the curve on the source animation that contains the speed of the end effector bone.

<a id="unreal.TargetChainSpeedPlantSettings.enable_speed_planting"></a>

#### enable_speed_planting

```python
@enable_speed_planting.setter
def enable_speed_planting(value: bool) -> None
```

<a id="unreal.TargetChainSpeedPlantSettings.speed_curve_name"></a>

#### speed_curve_name

```python
@property
def speed_curve_name() -> Name
```

(Name):  [Read-Write] The name of the curve on the source animation that contains the speed of the end effector bone.

<a id="unreal.TargetChainSpeedPlantSettings.speed_curve_name"></a>

#### speed_curve_name

```python
@speed_curve_name.setter
def speed_curve_name(value: Name) -> None
```

<a id="unreal.TargetChainSpeedPlantSettings.speed_threshold"></a>

#### speed_threshold

```python
@property
def speed_threshold() -> float
```

(float):  [Read-Write] Range 0 to 100. Default 15. The maximum speed a source bone can be moving while being considered 'planted'.
The target IK goal will not be allowed to move whenever the source bone speed drops below this threshold speed.

<a id="unreal.TargetChainSpeedPlantSettings.speed_threshold"></a>

#### speed_threshold

```python
@speed_threshold.setter
def speed_threshold(value: float) -> None
```

<a id="unreal.TargetChainSpeedPlantSettings.unplant_stiffness"></a>

#### unplant_stiffness

```python
@property
def unplant_stiffness() -> float
```

(float):  [Read-Write] How stiff the spring model is that smoothly pulls the IK position after unplanting (more stiffness means more oscillation around the target value)

<a id="unreal.TargetChainSpeedPlantSettings.unplant_stiffness"></a>

#### unplant_stiffness

```python
@unplant_stiffness.setter
def unplant_stiffness(value: float) -> None
```

<a id="unreal.TargetChainSpeedPlantSettings.unplant_critical_damping"></a>

#### unplant_critical_damping

```python
@property
def unplant_critical_damping() -> float
```

(float):  [Read-Write] How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)

<a id="unreal.TargetChainSpeedPlantSettings.unplant_critical_damping"></a>

#### unplant_critical_damping

```python
@unplant_critical_damping.setter
def unplant_critical_damping(value: float) -> None
```

<a id="unreal.TargetChainIKSettings"></a>