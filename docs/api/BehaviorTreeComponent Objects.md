## BehaviorTreeComponent Objects

```python
class BehaviorTreeComponent(BrainComponent)
```

Behavior Tree Component

**C++ Source:**

- **Module**: AIModule
- **File**: BehaviorTreeComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``default_behavior_tree_asset`` (BehaviorTree):  [Read-Write] data asset defining the tree
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.BehaviorTreeComponent.default_behavior_tree_asset"></a>

#### default_behavior_tree_asset

```python
@property
def default_behavior_tree_asset() -> BehaviorTree
```

(BehaviorTree):  [Read-Write] data asset defining the tree

<a id="unreal.BehaviorTreeComponent.default_behavior_tree_asset"></a>

#### default_behavior_tree_asset

```python
@default_behavior_tree_asset.setter
def default_behavior_tree_asset(value: BehaviorTree) -> None
```

<a id="unreal.BehaviorTreeComponent.set_dynamic_subtree"></a>

#### set_dynamic_subtree

```python
def set_dynamic_subtree(inject_tag: GameplayTag,
                        behavior_asset: BehaviorTree) -> None
```

x.set_dynamic_subtree(inject_tag, behavior_asset) -> None
assign subtree to RunBehaviorDynamic task specified by tag.

Args:
    inject_tag (GameplayTag): 
    behavior_asset (BehaviorTree):

<a id="unreal.BehaviorTreeComponent.get_tag_cooldown_end_time"></a>

#### get_tag_cooldown_end_time

```python
def get_tag_cooldown_end_time(cooldown_tag: GameplayTag) -> float
```

x.get_tag_cooldown_end_time(cooldown_tag) -> double


Args:
    cooldown_tag (GameplayTag): 

Returns:
    double: the cooldown tag end time, 0.0f if CooldownTag is not found

<a id="unreal.BehaviorTreeComponent.add_cooldown_tag_duration"></a>

#### add_cooldown_tag_duration

```python
def add_cooldown_tag_duration(cooldown_tag: GameplayTag,
                              cooldown_duration: float,
                              add_to_existing_duration: bool) -> None
```

x.add_cooldown_tag_duration(cooldown_tag, cooldown_duration, add_to_existing_duration) -> None
add to the cooldown tag's duration

Args:
    cooldown_tag (GameplayTag): 
    cooldown_duration (float): 
    add_to_existing_duration (bool):

<a id="unreal.BlackboardAssetProvider"></a>