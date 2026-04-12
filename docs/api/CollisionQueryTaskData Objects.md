## CollisionQueryTaskData Objects

```python
class CollisionQueryTaskData(StructBase)
```

Data Store struct used to extend collision-based targeting tasks providing extra data from outside

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: CollisionQueryTaskData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ignored_actors`` (Array[Actor]):  [Read-Write] Any extra actors we want to ignore. Note: Given that this is a globally-managed struct, we're manually adding refs to it in UTargetingSubsystem::AddReferencedObjects

<a id="unreal.CollisionQueryTaskData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(ignored_actors: Array[Actor] = []) -> None
```

<a id="unreal.CollisionQueryTaskData.ignored_actors"></a>

#### ignored\_actors

```python
@property
def ignored_actors() -> Array[Actor]
```

(Array[Actor]):  [Read-Write] Any extra actors we want to ignore. Note: Given that this is a globally-managed struct, we're manually adding refs to it in UTargetingSubsystem::AddReferencedObjects

<a id="unreal.CollisionQueryTaskData.ignored_actors"></a>

#### ignored\_actors

```python
@ignored_actors.setter
def ignored_actors(value: Array[Actor]) -> None
```

<a id="unreal.TargetingTaskSet"></a>