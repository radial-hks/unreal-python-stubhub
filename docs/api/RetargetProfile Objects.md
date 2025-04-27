## RetargetProfile Objects

```python
class RetargetProfile(StructBase)
```

Retarget Profile

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargetProfile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_chain_settings`` (bool):  [Read-Write] If true, the Chain Settings stored in this profile will be applied to the Retargeter (when plugged into the Retargeter).
- ``apply_global_settings`` (bool):  [Read-Write] If true, the global settings stored in this profile will be applied to the Retargeter (when plugged into the Retargeter).
- ``apply_root_settings`` (bool):  [Read-Write] If true, the root settings stored in this profile will be applied to the Retargeter (when plugged into the Retargeter).
- ``apply_source_retarget_pose`` (bool):  [Read-Write] If true, the Source Retarget Pose specified in this profile will be applied to the Retargeter (when plugged into the Retargeter).
- ``apply_target_retarget_pose`` (bool):  [Read-Write] If true, the TARGET Retarget Pose specified in this profile will be applied to the Retargeter (when plugged into the Retargeter).
- ``chain_settings`` (Map[Name, TargetChainSettings]):  [Read-Write] A (potentially sparse) set of setting overrides for the target chains (only applied when bApplyChainSettings is true).
- ``global_settings`` (RetargetGlobalSettings):  [Read-Write] Retarget settings to control global behavior, like Stride Warping (not applied unless bApplyGlobalSettings is true)
- ``root_settings`` (TargetRootSettings):  [Read-Write] Retarget settings to control behavior of the retarget root motion (not applied unless bApplyRootSettings is true)
- ``source_retarget_pose_name`` (Name):  [Read-Write] Override the SOURCE Retarget Pose to use when this profile is active.
  The pose must be present in the Retarget Asset and is not applied unless bApplySourceRetargetPose is true.
- ``target_retarget_pose_name`` (Name):  [Read-Write] Override the TARGET Retarget Pose to use when this profile is active.
  The pose must be present in the Retarget Asset and is not applied unless bApplyTargetRetargetPose is true.

<a id="unreal.RetargetProfile.__init__"></a>

#### __init__

```python
def __init__(
    apply_target_retarget_pose: bool = False,
    target_retarget_pose_name: Name = "None",
    apply_source_retarget_pose: bool = False,
    source_retarget_pose_name: Name = "None",
    apply_chain_settings: bool = False,
    chain_settings: Map[Name, TargetChainSettings] = {},
    apply_root_settings: bool = False,
    root_settings: TargetRootSettings = [
        1.000000, 1.000000, 0.000000, [1.000000, 1.000000, 1.000000],
        1.000000, 1.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], 1.000000, 0.000000
    ],
    apply_global_settings: bool = False,
    global_settings: RetargetGlobalSettings = [
        True, True, True, True, False, WarpingDirectionSource.GOALS,
        BasicAxis.Y, "None", 1.000000, 0.000000, 1.000000
    ]
) -> None
```

<a id="unreal.RetargetProfile.apply_target_retarget_pose"></a>

#### apply_target_retarget_pose

```python
@property
def apply_target_retarget_pose() -> bool
```

(bool):  [Read-Write] If true, the TARGET Retarget Pose specified in this profile will be applied to the Retargeter (when plugged into the Retargeter).

<a id="unreal.RetargetProfile.apply_target_retarget_pose"></a>

#### apply_target_retarget_pose

```python
@apply_target_retarget_pose.setter
def apply_target_retarget_pose(value: bool) -> None
```

<a id="unreal.RetargetProfile.target_retarget_pose_name"></a>

#### target_retarget_pose_name

```python
@property
def target_retarget_pose_name() -> Name
```

(Name):  [Read-Write] Override the TARGET Retarget Pose to use when this profile is active.
The pose must be present in the Retarget Asset and is not applied unless bApplyTargetRetargetPose is true.

<a id="unreal.RetargetProfile.target_retarget_pose_name"></a>

#### target_retarget_pose_name

```python
@target_retarget_pose_name.setter
def target_retarget_pose_name(value: Name) -> None
```

<a id="unreal.RetargetProfile.apply_source_retarget_pose"></a>

#### apply_source_retarget_pose

```python
@property
def apply_source_retarget_pose() -> bool
```

(bool):  [Read-Write] If true, the Source Retarget Pose specified in this profile will be applied to the Retargeter (when plugged into the Retargeter).

<a id="unreal.RetargetProfile.apply_source_retarget_pose"></a>

#### apply_source_retarget_pose

```python
@apply_source_retarget_pose.setter
def apply_source_retarget_pose(value: bool) -> None
```

<a id="unreal.RetargetProfile.source_retarget_pose_name"></a>

#### source_retarget_pose_name

```python
@property
def source_retarget_pose_name() -> Name
```

(Name):  [Read-Write] Override the SOURCE Retarget Pose to use when this profile is active.
The pose must be present in the Retarget Asset and is not applied unless bApplySourceRetargetPose is true.

<a id="unreal.RetargetProfile.source_retarget_pose_name"></a>

#### source_retarget_pose_name

```python
@source_retarget_pose_name.setter
def source_retarget_pose_name(value: Name) -> None
```

<a id="unreal.RetargetProfile.apply_chain_settings"></a>

#### apply_chain_settings

```python
@property
def apply_chain_settings() -> bool
```

(bool):  [Read-Write] If true, the Chain Settings stored in this profile will be applied to the Retargeter (when plugged into the Retargeter).

<a id="unreal.RetargetProfile.apply_chain_settings"></a>

#### apply_chain_settings

```python
@apply_chain_settings.setter
def apply_chain_settings(value: bool) -> None
```

<a id="unreal.RetargetProfile.chain_settings"></a>

#### chain_settings

```python
@property
def chain_settings() -> Map[Name, TargetChainSettings]
```

(Map[Name, TargetChainSettings]):  [Read-Write] A (potentially sparse) set of setting overrides for the target chains (only applied when bApplyChainSettings is true).

<a id="unreal.RetargetProfile.chain_settings"></a>

#### chain_settings

```python
@chain_settings.setter
def chain_settings(value: Map[Name, TargetChainSettings]) -> None
```

<a id="unreal.RetargetProfile.apply_root_settings"></a>

#### apply_root_settings

```python
@property
def apply_root_settings() -> bool
```

(bool):  [Read-Write] If true, the root settings stored in this profile will be applied to the Retargeter (when plugged into the Retargeter).

<a id="unreal.RetargetProfile.apply_root_settings"></a>

#### apply_root_settings

```python
@apply_root_settings.setter
def apply_root_settings(value: bool) -> None
```

<a id="unreal.RetargetProfile.root_settings"></a>

#### root_settings

```python
@property
def root_settings() -> TargetRootSettings
```

(TargetRootSettings):  [Read-Write] Retarget settings to control behavior of the retarget root motion (not applied unless bApplyRootSettings is true)

<a id="unreal.RetargetProfile.root_settings"></a>

#### root_settings

```python
@root_settings.setter
def root_settings(value: TargetRootSettings) -> None
```

<a id="unreal.RetargetProfile.apply_global_settings"></a>

#### apply_global_settings

```python
@property
def apply_global_settings() -> bool
```

(bool):  [Read-Write] If true, the global settings stored in this profile will be applied to the Retargeter (when plugged into the Retargeter).

<a id="unreal.RetargetProfile.apply_global_settings"></a>

#### apply_global_settings

```python
@apply_global_settings.setter
def apply_global_settings(value: bool) -> None
```

<a id="unreal.RetargetProfile.global_settings"></a>

#### global_settings

```python
@property
def global_settings() -> RetargetGlobalSettings
```

(RetargetGlobalSettings):  [Read-Write] Retarget settings to control global behavior, like Stride Warping (not applied unless bApplyGlobalSettings is true)

<a id="unreal.RetargetProfile.global_settings"></a>

#### global_settings

```python
@global_settings.setter
def global_settings(value: RetargetGlobalSettings) -> None
```

<a id="unreal.RetargetGlobalSettings"></a>