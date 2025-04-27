## AITestSpawnInfo Objects

```python
class AITestSpawnInfo(AITestSpawnInfoBase)
```

FAITestSpawnInfo

Generic AI Test Spawn Info used in FAITestSpawnSet within a generic AFunctionalAITest test.

**C++ Source:**

- **Module**: FunctionalTesting
- **File**: FunctionalAITest.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``behavior_tree`` (BehaviorTree):  [Read-Write] if set will be applied to spawned AI
- ``controller_class`` (type(Class)):  [Read-Write] class to override default pawn's controller class. If None the default will be used
- ``number_to_spawn`` (int32):  [Read-Write]
- ``pawn_class`` (type(Class)):  [Read-Write] Determines AI to be spawned
- ``pre_spawn_delay`` (float):  [Read-Write] delay before attempting first spawn
- ``spawn_delay`` (float):  [Read-Write] delay between consecutive spawn attempts
- ``spawn_location`` (Actor):  [Read-Write] Where should AI be spawned
- ``team_id`` (GenericTeamId):  [Read-Write]

<a id="unreal.AITestSpawnInfo.__init__"></a>

#### __init__

```python
def __init__(spawn_location: Actor = None,
             number_to_spawn: int = 0,
             spawn_delay: float = 0.000000,
             pre_spawn_delay: float = 0.000000,
             pawn_class: Class = None,
             controller_class: Class = None,
             team_id: GenericTeamId = [255],
             behavior_tree: BehaviorTree = None) -> None
```

<a id="unreal.AITestSpawnInfo.pawn_class"></a>

#### pawn_class

```python
@property
def pawn_class() -> Class
```

(type(Class)):  [Read-Write] Determines AI to be spawned

<a id="unreal.AITestSpawnInfo.pawn_class"></a>

#### pawn_class

```python
@pawn_class.setter
def pawn_class(value: Class) -> None
```

<a id="unreal.AITestSpawnInfo.controller_class"></a>

#### controller_class

```python
@property
def controller_class() -> Class
```

(type(Class)):  [Read-Write] class to override default pawn's controller class. If None the default will be used

<a id="unreal.AITestSpawnInfo.controller_class"></a>

#### controller_class

```python
@controller_class.setter
def controller_class(value: Class) -> None
```

<a id="unreal.AITestSpawnInfo.team_id"></a>

#### team_id

```python
@property
def team_id() -> GenericTeamId
```

(GenericTeamId):  [Read-Write]

<a id="unreal.AITestSpawnInfo.team_id"></a>

#### team_id

```python
@team_id.setter
def team_id(value: GenericTeamId) -> None
```

<a id="unreal.AITestSpawnInfo.behavior_tree"></a>

#### behavior_tree

```python
@property
def behavior_tree() -> BehaviorTree
```

(BehaviorTree):  [Read-Write] if set will be applied to spawned AI

<a id="unreal.AITestSpawnInfo.behavior_tree"></a>

#### behavior_tree

```python
@behavior_tree.setter
def behavior_tree(value: BehaviorTree) -> None
```

<a id="unreal.PendingDelayedSpawn"></a>