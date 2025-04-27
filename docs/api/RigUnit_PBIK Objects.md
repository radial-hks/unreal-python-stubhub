## RigUnit_PBIK Objects

```python
class RigUnit_PBIK(RigUnit_HighlevelBaseMutable)
```

* Based on a Position Based solver at core, this node can solve multi chains within a root using multi effectors

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: PBIK
- **File**: RigUnit_PBIK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_settings`` (Array[PBIKBoneSetting]):  [Read-Write] Per-bone settings to control the resulting pose. Includes limits and preferred angles.
- ``debug`` (PBIKDebug):  [Read-Write] Debug drawing options.
- ``effectors`` (Array[PBIKEffector]):  [Read-Write] An array of effectors. These specify target transforms for different parts of the skeleton.
- ``excluded_bones`` (Array[Name]):  [Read-Write] These bones will be excluded from the solver. They will not bend and will not contribute to the constraint set.
  Use the ExcludedBones array instead of setting Rotation Stiffness to very high values or Rotation Limits with zero range.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``root`` (Name):  [Read-Write] This is usually the top-most skinned bone; often the "Pelvis" or "Hips", but can be set to any bone.
  Bones above the root will be ignored by the solver.
  Bones that are located *between* the Root and the effectors will be included in the solve.
- ``settings`` (PBIKSolverSettings):  [Read-Write] Global solver settings.

<a id="unreal.RigUnit_PBIK.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             root: Name = "None",
             effectors: Array[PBIKEffector] = [],
             bone_settings: Array[PBIKBoneSetting] = [],
             excluded_bones: Array[Name] = [],
             settings: PBIKSolverSettings = [
                 20, 0, 1.000000, False, PBIKRootBehavior.PRE_PULL,
                 [
                     0.000000, 1.000000, 1.000000, 1.000000, 1.000000,
                     1.000000, 1.000000, 1.000000
                 ], 1.000000, 30.000000, 1.300000
             ],
             debug: PBIKDebug = []) -> None
```

<a id="unreal.RigUnit_PBIK.root"></a>

#### root

```python
@property
def root() -> Name
```

(Name):  [Read-Write] This is usually the top-most skinned bone; often the "Pelvis" or "Hips", but can be set to any bone.
Bones above the root will be ignored by the solver.
Bones that are located *between* the Root and the effectors will be included in the solve.

<a id="unreal.RigUnit_PBIK.root"></a>

#### root

```python
@root.setter
def root(value: Name) -> None
```

<a id="unreal.RigUnit_PBIK.effectors"></a>

#### effectors

```python
@property
def effectors() -> Array[PBIKEffector]
```

(Array[PBIKEffector]):  [Read-Write] An array of effectors. These specify target transforms for different parts of the skeleton.

<a id="unreal.RigUnit_PBIK.effectors"></a>

#### effectors

```python
@effectors.setter
def effectors(value: Array[PBIKEffector]) -> None
```

<a id="unreal.RigUnit_PBIK.bone_settings"></a>

#### bone_settings

```python
@property
def bone_settings() -> Array[PBIKBoneSetting]
```

(Array[PBIKBoneSetting]):  [Read-Write] Per-bone settings to control the resulting pose. Includes limits and preferred angles.

<a id="unreal.RigUnit_PBIK.bone_settings"></a>

#### bone_settings

```python
@bone_settings.setter
def bone_settings(value: Array[PBIKBoneSetting]) -> None
```

<a id="unreal.RigUnit_PBIK.excluded_bones"></a>

#### excluded_bones

```python
@property
def excluded_bones() -> Array[Name]
```

(Array[Name]):  [Read-Write] These bones will be excluded from the solver. They will not bend and will not contribute to the constraint set.
Use the ExcludedBones array instead of setting Rotation Stiffness to very high values or Rotation Limits with zero range.

<a id="unreal.RigUnit_PBIK.excluded_bones"></a>

#### excluded_bones

```python
@excluded_bones.setter
def excluded_bones(value: Array[Name]) -> None
```

<a id="unreal.RigUnit_PBIK.settings"></a>

#### settings

```python
@property
def settings() -> PBIKSolverSettings
```

(PBIKSolverSettings):  [Read-Write] Global solver settings.

<a id="unreal.RigUnit_PBIK.settings"></a>

#### settings

```python
@settings.setter
def settings(value: PBIKSolverSettings) -> None
```

<a id="unreal.RigUnit_PBIK.debug"></a>

#### debug

```python
@property
def debug() -> PBIKDebug
```

(PBIKDebug):  [Read-Write] Debug drawing options.

<a id="unreal.RigUnit_PBIK.debug"></a>

#### debug

```python
@debug.setter
def debug(value: PBIKDebug) -> None
```

<a id="unreal.PyTestStruct"></a>