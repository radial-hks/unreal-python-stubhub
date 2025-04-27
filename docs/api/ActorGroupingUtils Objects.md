## ActorGroupingUtils Objects

```python
class ActorGroupingUtils(Object)
```

Helper class for grouping actors in the level editor

**C++ Source:**

- **Module**: UnrealEd
- **File**: ActorGroupingUtils.h

<a id="unreal.ActorGroupingUtils.unlock_selected_groups"></a>

#### unlock_selected_groups

```python
def unlock_selected_groups() -> None
```

x.unlock_selected_groups() -> None
Unlocks any groups in the current selection

<a id="unreal.ActorGroupingUtils.ungroup_selected"></a>

#### ungroup_selected

```python
def ungroup_selected() -> None
```

x.ungroup_selected() -> None
Disbands any groups in the current selection, does not attempt to maintain any hierarchy

<a id="unreal.ActorGroupingUtils.ungroup_actors"></a>

#### ungroup_actors

```python
def ungroup_actors(actors_to_ungroup: Array[Actor]) -> None
```

x.ungroup_actors(actors_to_ungroup) -> None
Disbands any groups that the provided actors belong to, does not attempt to maintain any hierarchy

Args:
    actors_to_ungroup (Array[Actor]):

<a id="unreal.ActorGroupingUtils.set_grouping_active"></a>

#### set_grouping_active

```python
@classmethod
def set_grouping_active(cls, grouping_active: bool) -> None
```

X.set_grouping_active(grouping_active) -> None
Set Grouping Active

Args:
    grouping_active (bool):

<a id="unreal.ActorGroupingUtils.remove_selected_from_group"></a>

#### remove_selected_from_group

```python
def remove_selected_from_group() -> None
```

x.remove_selected_from_group() -> None
Removes any groups or actors in the current selection from their immediate parent.
If all actors/subgroups are removed, the parent group will be destroyed.

<a id="unreal.ActorGroupingUtils.lock_selected_groups"></a>

#### lock_selected_groups

```python
def lock_selected_groups() -> None
```

x.lock_selected_groups() -> None
Locks any groups in the current selection

<a id="unreal.ActorGroupingUtils.is_grouping_active"></a>

#### is_grouping_active

```python
@classmethod
def is_grouping_active(cls) -> bool
```

X.is_grouping_active() -> bool
Is Grouping Active

Returns:
    bool:

<a id="unreal.ActorGroupingUtils.group_selected"></a>

#### group_selected

```python
def group_selected() -> GroupActor
```

x.group_selected() -> GroupActor
Creates a new group from the current selection removing the actors from any existing groups they are already in

Returns:
    GroupActor:

<a id="unreal.ActorGroupingUtils.group_actors"></a>

#### group_actors

```python
def group_actors(actors_to_group: Array[Actor]) -> GroupActor
```

x.group_actors(actors_to_group) -> GroupActor
Creates a new group from the provided list of actors removing the actors from any existing groups they are already in

Args:
    actors_to_group (Array[Actor]): 

Returns:
    GroupActor:

<a id="unreal.ActorGroupingUtils.get"></a>

#### get

```python
@classmethod
def get(cls) -> ActorGroupingUtils
```

X.get() -> ActorGroupingUtils
Convenience method for accessing grouping utils in a blueprint or script

Returns:
    ActorGroupingUtils:

<a id="unreal.ActorGroupingUtils.can_group_selected_actors"></a>

#### can_group_selected_actors

```python
def can_group_selected_actors() -> bool
```

x.can_group_selected_actors() -> bool
* Check if the currently selected actors can be grouped together

Returns:
    bool:

<a id="unreal.ActorGroupingUtils.can_group_actors"></a>

#### can_group_actors

```python
def can_group_actors(actors_to_group: Array[Actor]) -> bool
```

x.can_group_actors(actors_to_group) -> bool
Check if the provided list of actors can be grouped together

Args:
    actors_to_group (Array[Actor]): 

Returns:
    bool:

<a id="unreal.ActorGroupingUtils.add_selected_to_group"></a>

#### add_selected_to_group

```python
def add_selected_to_group() -> None
```

x.add_selected_to_group() -> None
Activates "Add to Group" mode which allows the user to select a group to append current selection

<a id="unreal.BlendSpaceFactory1D"></a>