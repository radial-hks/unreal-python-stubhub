## AnimGroupRole Objects

```python
class AnimGroupRole(EnumBase)
```

EAnim Group Role

**C++ Source:**

- **Module**: Engine
- **File**: AnimationAsset.h

<a id="unreal.AnimGroupRole.CAN_BE_LEADER"></a>

#### CAN_BE_LEADER

0: This node can be the leader, as long as it has a higher blend weight than the previous best leader.

<a id="unreal.AnimGroupRole.ALWAYS_FOLLOWER"></a>

#### ALWAYS_FOLLOWER

1: This node will always be a follower (unless there are only followers, in which case the first one ticked wins).

<a id="unreal.AnimGroupRole.ALWAYS_LEADER"></a>

#### ALWAYS_LEADER

2: This node will always be a leader (if more than one node is AlwaysLeader, the last one ticked wins).

<a id="unreal.AnimGroupRole.TRANSITION_LEADER"></a>

#### TRANSITION_LEADER

3: This node will be excluded from the sync group while blending in. Once blended in it will be the sync group leader until blended out

<a id="unreal.AnimGroupRole.TRANSITION_FOLLOWER"></a>

#### TRANSITION_FOLLOWER

4: This node will be excluded from the sync group while blending in. Once blended in it will be a follower until blended out

<a id="unreal.AnimGroupRole.EXCLUSIVE_ALWAYS_LEADER"></a>

#### EXCLUSIVE_ALWAYS_LEADER

5: This node will always be a leader. If it fails to be ticked as a leader it will be run as ungrouped asset player (EAnimSyncMethod::DoNotSync) .

<a id="unreal.AnimAlphaInputType"></a>