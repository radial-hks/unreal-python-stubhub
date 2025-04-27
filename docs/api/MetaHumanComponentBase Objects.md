## MetaHumanComponentBase Objects

```python
class MetaHumanComponentBase(ActorComponent)
```

Meta Human Component Base

**C++ Source:**

- **Plugin**: MetaHumanSDK
- **Module**: MetaHumanSDKRuntime
- **File**: MetaHumanComponentBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``body_component_name`` (str):  [Read-Write]
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_body_correctives`` (bool):  [Read-Write] * Enable evaluation of the body procedural control rig, the head movement IK control rig and the arm and finger pose drivers.
  * When enabled, evaluation for LODs can still be controlled via the Body LOD threshold.
  * When disabled, the body procedural control rig, the head movement IK control rig and the arm and finger pose drivers will not be evaluated which will result in higher performance but decreases mesh deformation quality.
- ``enable_neck_correctives`` (bool):  [Read-Write] * Enable evaluation of neck correctives.
  * When enabled, evaluation for LODs can still be controlled via the LOD threshold.
  * When disabled, neck correctives will not be evaluated which will result in higher performance but decreases mesh deformation quality.
- ``enable_neck_proc_control_rig`` (bool):  [Read-Write] * Enable evaluation of the neck procedural control rig.
  * When enabled, evaluation for LODs can still be controlled via the LOD threshold.
  * When disabled, the neck procedural control rig will not be evaluated which will result in higher performance but decreases mesh deformation quality.
- ``face_component_name`` (str):  [Read-Write]
- ``feet`` (MetaHumanCustomizableBodyPart):  [Read-Write]
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``legs`` (MetaHumanCustomizableBodyPart):  [Read-Write]
- ``neck_correctives_lod_threshold`` (int32):  [Read-Write] * Max LOD level where neck correctives (pose drivers) are evaluated.
  * For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating neck correctives.
  * Setting it to -1 will always evaluate it and disable LODing.
- ``neck_proc_control_rig_lod_threshold`` (int32):  [Read-Write] * Max LOD level where the neck procedural control rig is evaluated.
  * For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating the neck procedural control rig.
  * Setting it to -1 will always evaluate it and disable LODing.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``rig_logic_lod_threshold`` (int32):  [Read-Write] * Max LOD level where Rig Logic is evaluated.
  * For example if you have the threshold set to 2, it will evaluate until including LOD 2 (based on 0 index). In case the LOD level gets set to 3, it will stop evaluating Rig Logic.
  * Setting it to -1 will always evaluate it and disable LODing.
- ``torso`` (MetaHumanCustomizableBodyPart):  [Read-Write] Body Parts

<a id="unreal.MetaHumanComponentUE"></a>