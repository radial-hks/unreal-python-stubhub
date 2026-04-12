## SimpleTargetingSelectionTask Objects

```python
class SimpleTargetingSelectionTask(TargetingTask)
```

class: USimpleTargetingSelectionTask This is a blueprintable TargetingTask class made for adding new Targets to the results list. Override the SelectTargets function and call AddTargetHitResult or AddTargetActor to select new targets.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: SimpleTargetingSelectionTask.h

<a id="unreal.SimpleTargetingSelectionTask.select_targets"></a>

#### select\_targets

```python
def select_targets(targeting_handle: TargetingRequestHandle,
                   source_context: TargetingSourceContext) -> None
```

x.select_targets(targeting_handle, source_context) -> None
Select Targets

Args:
    targeting_handle (TargetingRequestHandle): 
    source_context (TargetingSourceContext):

<a id="unreal.SimpleTargetingSelectionTask.add_target_actor"></a>

#### add\_target\_actor

```python
def add_target_actor(targeting_handle: TargetingRequestHandle,
                     actor: Actor) -> bool
```

x.add_target_actor(targeting_handle, actor) -> bool
Adds a single Actor to the Targeting Results for a given TargetingRequestHandle.
Returns false when the Actor was already in the list.

NOTE: If you have a HitResult associated with this selection, please use AddHitResult instead.

Args:
    targeting_handle (TargetingRequestHandle): 
    actor (Actor): 

Returns:
    bool:

<a id="unreal.SimpleTargetingSelectionTask.add_hit_result"></a>

#### add\_hit\_result

```python
def add_hit_result(targeting_handle: TargetingRequestHandle,
                   hit_result: HitResult) -> bool
```

x.add_hit_result(targeting_handle, hit_result) -> bool
Adds a HitResult to the Targeting Results for a given TargetingRequestHandle.
Returns False when the Actor that was hit was already in the list

Args:
    targeting_handle (TargetingRequestHandle): 
    hit_result (HitResult): 

Returns:
    bool:

<a id="unreal.TargetingSortTask_Base"></a>