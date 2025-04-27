## IKRetargeter Objects

```python
class IKRetargeter(Object)
```

IKRetargeter

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargeter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chain_draw_size`` (float):  [Read-Write] The visual size of the IK goals in the viewport.
- ``chain_draw_thickness`` (float):  [Read-Write] The thickness of lines on the IK goals in the viewport.
- ``debug_draw`` (bool):  [Read-Write] Toggle debug drawing for retargeting in the viewport.
- ``draw_chain_lines`` (bool):  [Read-Write] Draw lines on each bone chain.
- ``draw_final_goals`` (bool):  [Read-Write] Draw final IK goal locations.
- ``draw_root_circle`` (bool):  [Read-Write] Draw circle on the floor below the retarget root.
- ``draw_single_bone_chains`` (bool):  [Read-Write] Draw spheres on single bone chains.
- ``draw_source_locations`` (bool):  [Read-Write] Draw goal locations from source skeleton.
- ``draw_warping_frame`` (bool):  [Read-Write] Draw coordinate frame used to define stride warping directions.
- ``ignore_root_lock_in_preview`` (bool):  [Read-Write] When true, animation sequences with "Force Root Lock" turned On will act as though it is Off.
  This affects only the preview in the retarget editor. Use ExportRootLockMode to control exported animation behavior.
  This setting has no effect on runtime retargeting where root motion is copied from the source component.
- ``source_ik_rig_asset`` (IKRigDefinition):  [Read-Write] The rig to copy animation FROM.
- ``source_mesh_offset`` (Vector):  [Read-Write] The offset applied to the source mesh in the editor viewport.
- ``source_preview_mesh`` (SkeletalMesh):  [Read-Write] Optional. Override the Skeletal Mesh to copy animation from. Uses the preview mesh from the Source IK Rig asset by default.
- ``target_ik_rig_asset`` (IKRigDefinition):  [Read-Write] The rig to copy animation TO.
- ``target_mesh_offset`` (Vector):  [Read-Write] The offset applied to the target mesh in the editor viewport.
- ``target_mesh_scale`` (float):  [Read-Write] Scale the target mesh in the viewport for easier visualization next to the source.
- ``target_preview_mesh`` (SkeletalMesh):  [Read-Write] Optional. Override the Skeletal Mesh to preview the retarget on. Uses the preview mesh from the Target IK Rig asset by default.

<a id="unreal.IKRetargeter.set_root_settings_in_retarget_profile"></a>

#### set_root_settings_in_retarget_profile

```python
@classmethod
def set_root_settings_in_retarget_profile(
        cls, retarget_profile: RetargetProfile,
        root_settings: TargetRootSettings) -> RetargetProfile
```

X.set_root_settings_in_retarget_profile(retarget_profile, root_settings) -> RetargetProfile
Set the root settings in a retarget profile (will set bApplyRootSettings to true).

Args:
    retarget_profile (RetargetProfile): 
    root_settings (TargetRootSettings): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.set_global_settings_in_retarget_profile"></a>

#### set_global_settings_in_retarget_profile

```python
@classmethod
def set_global_settings_in_retarget_profile(
        cls, retarget_profile: RetargetProfile,
        global_settings: RetargetGlobalSettings) -> RetargetProfile
```

X.set_global_settings_in_retarget_profile(retarget_profile, global_settings) -> RetargetProfile
Set the global settings in a retarget profile (will set bApplyGlobalSettings to true).

Args:
    retarget_profile (RetargetProfile): 
    global_settings (RetargetGlobalSettings): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.set_chain_speed_plant_settings_in_retarget_profile"></a>

#### set_chain_speed_plant_settings_in_retarget_profile

```python
@classmethod
def set_chain_speed_plant_settings_in_retarget_profile(
        cls, retarget_profile: RetargetProfile,
        speed_plant_settings: TargetChainSpeedPlantSettings,
        target_chain_name: Name) -> RetargetProfile
```

X.set_chain_speed_plant_settings_in_retarget_profile(retarget_profile, speed_plant_settings, target_chain_name) -> RetargetProfile
Set the chain Speed Plant settings in a retarget profile (will set bApplyChainSettings to true).

Args:
    retarget_profile (RetargetProfile): 
    speed_plant_settings (TargetChainSpeedPlantSettings): 
    target_chain_name (Name): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.set_chain_settings_in_retarget_profile"></a>

#### set_chain_settings_in_retarget_profile

```python
@classmethod
def set_chain_settings_in_retarget_profile(
        cls, retarget_profile: RetargetProfile,
        chain_settings: TargetChainSettings,
        target_chain_name: Name) -> RetargetProfile
```

X.set_chain_settings_in_retarget_profile(retarget_profile, chain_settings, target_chain_name) -> RetargetProfile
Set the chain settings in a retarget profile (will set bApplyChainSettings to true).

Args:
    retarget_profile (RetargetProfile): 
    chain_settings (TargetChainSettings): 
    target_chain_name (Name): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.set_chain_ik_settings_in_retarget_profile"></a>

#### set_chain_ik_settings_in_retarget_profile

```python
@classmethod
def set_chain_ik_settings_in_retarget_profile(
        cls, retarget_profile: RetargetProfile,
        ik_settings: TargetChainIKSettings,
        target_chain_name: Name) -> RetargetProfile
```

X.set_chain_ik_settings_in_retarget_profile(retarget_profile, ik_settings, target_chain_name) -> RetargetProfile
Set the chain IK settings in a retarget profile (will set bApplyChainSettings to true).

Args:
    retarget_profile (RetargetProfile): 
    ik_settings (TargetChainIKSettings): 
    target_chain_name (Name): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.set_chain_fk_settings_in_retarget_profile"></a>

#### set_chain_fk_settings_in_retarget_profile

```python
@classmethod
def set_chain_fk_settings_in_retarget_profile(
        cls, retarget_profile: RetargetProfile,
        fk_settings: TargetChainFKSettings,
        target_chain_name: Name) -> RetargetProfile
```

X.set_chain_fk_settings_in_retarget_profile(retarget_profile, fk_settings, target_chain_name) -> RetargetProfile
Set the chain FK settings in a retarget profile (will set bApplyChainSettings to true).

Args:
    retarget_profile (RetargetProfile): 
    fk_settings (TargetChainFKSettings): 
    target_chain_name (Name): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.has_target_ik_rig"></a>

#### has_target_ik_rig

```python
def has_target_ik_rig() -> bool
```

x.has_target_ik_rig() -> bool
Returns true if the target IK Rig has been assigned

Returns:
    bool:

<a id="unreal.IKRetargeter.has_source_ik_rig"></a>

#### has_source_ik_rig

```python
def has_source_ik_rig() -> bool
```

x.has_source_ik_rig() -> bool
Returns true if the source IK Rig has been assigned

Returns:
    bool:

<a id="unreal.IKRetargeter.get_root_settings_from_retarget_profile"></a>

#### get_root_settings_from_retarget_profile

```python
@classmethod
def get_root_settings_from_retarget_profile(
    cls, retarget_profile: RetargetProfile
) -> Tuple[TargetRootSettings, RetargetProfile]
```

X.get_root_settings_from_retarget_profile(retarget_profile) -> (TargetRootSettings, retarget_profile=RetargetProfile)
Returns the root settings in the supplied Retarget Profile.

Args:
    retarget_profile (RetargetProfile): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.get_root_settings_from_retarget_asset"></a>

#### get_root_settings_from_retarget_asset

```python
@classmethod
def get_root_settings_from_retarget_asset(
        cls, retarget_asset: IKRetargeter,
        optional_profile_name: Name) -> TargetRootSettings
```

X.get_root_settings_from_retarget_asset(retarget_asset, optional_profile_name) -> TargetRootSettings
Returns the root settings in an IK Retargeter Asset using the given profile name (optional)

Args:
    retarget_asset (IKRetargeter): 
    optional_profile_name (Name): 

Returns:
    TargetRootSettings: 

    out_settings (TargetRootSettings):

<a id="unreal.IKRetargeter.get_global_settings_from_retarget_profile"></a>

#### get_global_settings_from_retarget_profile

```python
@classmethod
def get_global_settings_from_retarget_profile(
    cls, retarget_profile: RetargetProfile
) -> Tuple[RetargetGlobalSettings, RetargetProfile]
```

X.get_global_settings_from_retarget_profile(retarget_profile) -> (RetargetGlobalSettings, retarget_profile=RetargetProfile)
Returns the global settings in the supplied Retarget Profile.

Args:
    retarget_profile (RetargetProfile): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.get_global_settings_from_retarget_asset"></a>

#### get_global_settings_from_retarget_asset

```python
@classmethod
def get_global_settings_from_retarget_asset(
        cls, retarget_asset: IKRetargeter,
        optional_profile_name: Name) -> RetargetGlobalSettings
```

X.get_global_settings_from_retarget_asset(retarget_asset, optional_profile_name) -> RetargetGlobalSettings
Returns the global settings in an IK Retargeter Asset using the given profile name (optional)

Args:
    retarget_asset (IKRetargeter): 
    optional_profile_name (Name): 

Returns:
    RetargetGlobalSettings: 

    out_settings (RetargetGlobalSettings):

<a id="unreal.IKRetargeter.get_chain_using_goal_from_retarget_asset"></a>

#### get_chain_using_goal_from_retarget_asset

```python
@classmethod
def get_chain_using_goal_from_retarget_asset(
        cls, retarget_asset: IKRetargeter,
        ik_goal_name: Name) -> TargetChainSettings
```

X.get_chain_using_goal_from_retarget_asset(retarget_asset, ik_goal_name) -> TargetChainSettings
Returns the chain settings associated with a given Goal in an IK Retargeter Asset using the given profile name (optional)

Args:
    retarget_asset (IKRetargeter): 
    ik_goal_name (Name): 

Returns:
    TargetChainSettings:

<a id="unreal.IKRetargeter.get_chain_settings_from_retarget_profile"></a>

#### get_chain_settings_from_retarget_profile

```python
@classmethod
def get_chain_settings_from_retarget_profile(
        cls, retarget_profile: RetargetProfile, target_chain_name: Name
) -> Tuple[TargetChainSettings, RetargetProfile]
```

X.get_chain_settings_from_retarget_profile(retarget_profile, target_chain_name) -> (TargetChainSettings, retarget_profile=RetargetProfile)
Returns the chain settings associated with a given target chain in the supplied Retarget Profile.

Args:
    retarget_profile (RetargetProfile): 
    target_chain_name (Name): 

Returns:
    RetargetProfile: 

    retarget_profile (RetargetProfile):

<a id="unreal.IKRetargeter.get_chain_settings_from_retarget_asset"></a>

#### get_chain_settings_from_retarget_asset

```python
@classmethod
def get_chain_settings_from_retarget_asset(
        cls, retarget_asset: IKRetargeter, target_chain_name: Name,
        optional_profile_name: Name) -> TargetChainSettings
```

X.get_chain_settings_from_retarget_asset(retarget_asset, target_chain_name, optional_profile_name) -> TargetChainSettings
Returns the chain settings associated with a given target chain in an IK Retargeter Asset using the given profile name (optional)

Args:
    retarget_asset (IKRetargeter): 
    target_chain_name (Name): 
    optional_profile_name (Name): 

Returns:
    TargetChainSettings:

<a id="unreal.IKRigEffectorGoal"></a>