## CharacterTrajectoryComponent Objects

```python
class CharacterTrajectoryComponent(ActorComponent)
```

Component for generating trajectories usable by Motion Matching. This component generates trajectories from ACharacter.
This is intended to provide an example and starting point for using Motion Matching with a common setup using the default UCharacterMovementComponent.
It is expected work flow to extend or replace this component for projects that use a custom movement component or custom movement modes.

**C++ Source:**

- **Plugin**: MotionTrajectory
- **Module**: MotionTrajectory
- **File**: CharacterTrajectoryComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``character_trajectory_data`` (CharacterTrajectoryData):  [Read-Write]
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``sampling_data`` (TrajectorySamplingData):  [Read-Write]
- ``trajectory`` (PoseSearchQueryTrajectory):  [Read-Write] Trajectory stored in world space so it can be directly passed to Motion Matching.

<a id="unreal.CharacterTrajectoryComponent.trajectory"></a>

#### trajectory

```python
@property
def trajectory() -> PoseSearchQueryTrajectory
```

(PoseSearchQueryTrajectory):  [Read-Only] Trajectory stored in world space so it can be directly passed to Motion Matching.

<a id="unreal.CharacterTrajectoryComponent.sampling_data"></a>

#### sampling_data

```python
@property
def sampling_data() -> TrajectorySamplingData
```

(TrajectorySamplingData):  [Read-Only]

<a id="unreal.CharacterTrajectoryComponent.character_trajectory_data"></a>

#### character_trajectory_data

```python
@property
def character_trajectory_data() -> CharacterTrajectoryData
```

(CharacterTrajectoryData):  [Read-Only]

<a id="unreal.ChaosClothComponent"></a>