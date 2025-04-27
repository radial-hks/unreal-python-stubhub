## IKGoalCreatorInterface Objects

```python
class IKGoalCreatorInterface(Interface)
```

IKGoal Creator Interface

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRigInterface.h

<a id="unreal.IKGoalCreatorInterface.add_ik_goals"></a>

#### add_ik_goals

```python
def add_ik_goals() -> Map[Name, IKRigGoal]
```

x.add_ik_goals() -> Map[Name, IKRigGoal]
Add your own goals to the OutGoals map (careful not to remove existing goals in the map!)

Returns:
    Map[Name, IKRigGoal]: 

    out_goals (Map[Name, IKRigGoal]):

<a id="unreal.PinBoneOp"></a>