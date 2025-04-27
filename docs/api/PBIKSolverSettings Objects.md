## PBIKSolverSettings Objects

```python
class PBIKSolverSettings(StructBase)
```

PBIKSolver Settings

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: PBIK
- **File**: PBIKSolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_stretch`` (bool):  [Read-Write] If true, joints will translate to reach the effectors; causing bones to lengthen if necessary. Good for cartoon effects. Default is false.
- ``global_pull_chain_alpha`` (float):  [Read-Write] A global multiplier for all Pull Chain Alpha values on all effectors. Range is 0.0 to 1.0. Default is 1.0.
- ``iterations`` (int32):  [Read-Write] High iteration counts can help solve complex joint configurations with competing constraints, but will increase runtime cost. Default is 20.
- ``mass_multiplier`` (float):  [Read-Write] A global mass multiplier; higher values will make the joints more stiff, but require more iterations. Typical range is 0.0 to 10.0.
- ``max_angle`` (float):  [Read-Write] Maximum angle that a joint can be rotated per constraint iteration. Lower this value if the solve is diverging. Range is 0.0 to 180.0. Default is 30.
- ``over_relaxation`` (float):  [Read-Write] Pushes constraints beyond their normal amount to speed up convergence. Increasing this may speed up convergence, but at the cost of stability. Range is 1.0 - 2.0. Default is 1.3.
- ``pre_pull_root_settings`` (RootPrePullSettings):  [Read-Write] Settings only applicable when Root Behavior is set to "PrePull". Use these values to adjust the gross movement and orientation of the entire skeleton.
- ``root_behavior`` (PBIKRootBehavior):  [Read-Write] (Default is PrePull) Set the behavior of the solver root.
  Pre Pull: translates and rotates the root (and all children) by the average motion of the stretched effectors to help achieve faster convergence when reaching far.
  Pin to Input: locks the translation and rotation of the root bone to the input pose. Overrides any bone settings applied to the root. Good for partial-body solves.
  Free: treats the root bone like any other and allows it to move freely or according to any bone settings applied to it.
- ``sub_iterations`` (int32):  [Read-Write] Iterations used for sub-chains defined by the Chain Depth of the effectors. These are solved BEFORE the main iteration pass. Default is 0.

<a id="unreal.PBIKSolverSettings.__init__"></a>

#### __init__

```python
def __init__(iterations: int = 0,
             sub_iterations: int = 0,
             mass_multiplier: float = 0.000000,
             allow_stretch: bool = False,
             root_behavior: PBIKRootBehavior = PBIKRootBehavior.PRE_PULL,
             pre_pull_root_settings: RootPrePullSettings = [
                 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000,
                 1.000000, 1.000000
             ],
             global_pull_chain_alpha: float = 0.000000,
             max_angle: float = 0.000000,
             over_relaxation: float = 0.000000) -> None
```

<a id="unreal.PBIKSolverSettings.iterations"></a>

#### iterations

```python
@property
def iterations() -> int
```

(int32):  [Read-Write] High iteration counts can help solve complex joint configurations with competing constraints, but will increase runtime cost. Default is 20.

<a id="unreal.PBIKSolverSettings.iterations"></a>

#### iterations

```python
@iterations.setter
def iterations(value: int) -> None
```

<a id="unreal.PBIKSolverSettings.sub_iterations"></a>

#### sub_iterations

```python
@property
def sub_iterations() -> int
```

(int32):  [Read-Write] Iterations used for sub-chains defined by the Chain Depth of the effectors. These are solved BEFORE the main iteration pass. Default is 0.

<a id="unreal.PBIKSolverSettings.sub_iterations"></a>

#### sub_iterations

```python
@sub_iterations.setter
def sub_iterations(value: int) -> None
```

<a id="unreal.PBIKSolverSettings.mass_multiplier"></a>

#### mass_multiplier

```python
@property
def mass_multiplier() -> float
```

(float):  [Read-Write] A global mass multiplier; higher values will make the joints more stiff, but require more iterations. Typical range is 0.0 to 10.0.

<a id="unreal.PBIKSolverSettings.mass_multiplier"></a>

#### mass_multiplier

```python
@mass_multiplier.setter
def mass_multiplier(value: float) -> None
```

<a id="unreal.PBIKSolverSettings.allow_stretch"></a>

#### allow_stretch

```python
@property
def allow_stretch() -> bool
```

(bool):  [Read-Write] If true, joints will translate to reach the effectors; causing bones to lengthen if necessary. Good for cartoon effects. Default is false.

<a id="unreal.PBIKSolverSettings.allow_stretch"></a>

#### allow_stretch

```python
@allow_stretch.setter
def allow_stretch(value: bool) -> None
```

<a id="unreal.PBIKSolverSettings.root_behavior"></a>

#### root_behavior

```python
@property
def root_behavior() -> PBIKRootBehavior
```

(PBIKRootBehavior):  [Read-Write] (Default is PrePull) Set the behavior of the solver root.
Pre Pull: translates and rotates the root (and all children) by the average motion of the stretched effectors to help achieve faster convergence when reaching far.
Pin to Input: locks the translation and rotation of the root bone to the input pose. Overrides any bone settings applied to the root. Good for partial-body solves.
Free: treats the root bone like any other and allows it to move freely or according to any bone settings applied to it.

<a id="unreal.PBIKSolverSettings.root_behavior"></a>

#### root_behavior

```python
@root_behavior.setter
def root_behavior(value: PBIKRootBehavior) -> None
```

<a id="unreal.PBIKSolverSettings.pre_pull_root_settings"></a>

#### pre_pull_root_settings

```python
@property
def pre_pull_root_settings() -> RootPrePullSettings
```

(RootPrePullSettings):  [Read-Write] Settings only applicable when Root Behavior is set to "PrePull". Use these values to adjust the gross movement and orientation of the entire skeleton.

<a id="unreal.PBIKSolverSettings.pre_pull_root_settings"></a>

#### pre_pull_root_settings

```python
@pre_pull_root_settings.setter
def pre_pull_root_settings(value: RootPrePullSettings) -> None
```

<a id="unreal.PBIKSolverSettings.global_pull_chain_alpha"></a>

#### global_pull_chain_alpha

```python
@property
def global_pull_chain_alpha() -> float
```

(float):  [Read-Write] A global multiplier for all Pull Chain Alpha values on all effectors. Range is 0.0 to 1.0. Default is 1.0.

<a id="unreal.PBIKSolverSettings.global_pull_chain_alpha"></a>

#### global_pull_chain_alpha

```python
@global_pull_chain_alpha.setter
def global_pull_chain_alpha(value: float) -> None
```

<a id="unreal.PBIKSolverSettings.max_angle"></a>

#### max_angle

```python
@property
def max_angle() -> float
```

(float):  [Read-Write] Maximum angle that a joint can be rotated per constraint iteration. Lower this value if the solve is diverging. Range is 0.0 to 180.0. Default is 30.

<a id="unreal.PBIKSolverSettings.max_angle"></a>

#### max_angle

```python
@max_angle.setter
def max_angle(value: float) -> None
```

<a id="unreal.PBIKSolverSettings.over_relaxation"></a>

#### over_relaxation

```python
@property
def over_relaxation() -> float
```

(float):  [Read-Write] Pushes constraints beyond their normal amount to speed up convergence. Increasing this may speed up convergence, but at the cost of stability. Range is 1.0 - 2.0. Default is 1.3.

<a id="unreal.PBIKSolverSettings.over_relaxation"></a>

#### over_relaxation

```python
@over_relaxation.setter
def over_relaxation(value: float) -> None
```

<a id="unreal.PBIKDebug"></a>