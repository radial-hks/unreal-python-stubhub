## IKRigComponent Objects

```python
class IKRigComponent(ActorComponent)
```

IKRig Component

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRigComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.IKRigComponent.set_ik_rig_goal_transform"></a>

#### set_ik_rig_goal_transform

```python
def set_ik_rig_goal_transform(goal_name: Name, transform: Transform,
                              position_alpha: float,
                              rotation_alpha: float) -> None
```

x.set_ik_rig_goal_transform(goal_name, transform, position_alpha, rotation_alpha) -> None
Set an IK Rig Goal transform (assumed in Component Space of Skeletal Mesh) with separate alpha values.

Args:
    goal_name (Name): 
    transform (Transform): 
    position_alpha (float): 
    rotation_alpha (float):

<a id="unreal.IKRigComponent.set_ik_rig_goal_position_and_rotation"></a>

#### set_ik_rig_goal_position_and_rotation

```python
def set_ik_rig_goal_position_and_rotation(goal_name: Name, position: Vector,
                                          rotation: Quat,
                                          position_alpha: float,
                                          rotation_alpha: float) -> None
```

x.set_ik_rig_goal_position_and_rotation(goal_name, position, rotation, position_alpha, rotation_alpha) -> None
Set an IK Rig Goal position and rotation (assumed in Component Space of Skeletal Mesh) with separate alpha values.

Args:
    goal_name (Name): 
    position (Vector): 
    rotation (Quat): 
    position_alpha (float): 
    rotation_alpha (float):

<a id="unreal.IKRigComponent.set_ik_rig_goal"></a>

#### set_ik_rig_goal

```python
def set_ik_rig_goal(goal: IKRigGoal) -> None
```

x.set_ik_rig_goal(goal) -> None
Apply a IKRigGoal and store it on this rig. Goal transform assumed in Component Space of Skeletal Mesh.

Args:
    goal (IKRigGoal):

<a id="unreal.IKRigComponent.clear_all_goals"></a>

#### clear_all_goals

```python
def clear_all_goals() -> None
```

x.clear_all_goals() -> None
Remove all stored goals in this component.

<a id="unreal.IKRigComponent.add_ik_goals"></a>

#### add_ik_goals

```python
def add_ik_goals() -> Map[Name, IKRigGoal]
```

x.add_ik_goals() -> Map[Name, IKRigGoal]
Add your own goals to the OutGoals map (careful not to remove existing goals in the map!)

Returns:
    Map[Name, IKRigGoal]: 

    out_goals (Map[Name, IKRigGoal]):

<a id="unreal.RetargetChainSettings"></a>