## TargetingSubsystem Objects

```python
class TargetingSubsystem(GameInstanceSubsystem)
```

class: UTargetingSubsystem The Targeting Subsystem is the entry point for users to initiate targeting requests. The entry point to the system is the target request handle. The handle is used to interface with the targeting data stores. Data stores are templated classes around generic data structs that the system and tasks use to accomplish a targeting request. The targeting system has 3 mandatory data stores and 1 required for async targeting request. These data stores are required to be set up before the system can properly run a targeting request. The mandatory 3 data stores are FTargetingRequestData, FTargetingTaskSet, and FTargetingSourceContext. FTargetingAsyncTaskData is implicitly setup when an async targeting request is initiated. Users can do all the pieces manually in C++ by setting up the required data stores themselves, or, to have it a bit more automated, the user can use the APIs that utilize UTargetingPreset data asset. For immediate targeting requests users will call the Execute methods. These functions perform all the tasks till completion. The system will not go latent. For async targeting requests users will call the Start Async methods. The system will queue up a targeting request and as each task is processed the system can run through all the tasks to completion or stop processing until the next frame while it waits for a task to complete. Note about Targeting Handles, when a targeting handle is created it will not implicitly release the handle. It is up to the creator to either grab a Async Task Data or Immediate Task Data and set a flag indicating the system should do it for them after the callback fires, or it is up to the user to release the handle when they are done with it.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingSubsystem.h

<a id="unreal.TargetingSubsystem.start_async_targeting_request"></a>

#### start\_async\_targeting\_request

```python
def start_async_targeting_request(
    targeting_preset: TargetingPreset, source_context: TargetingSourceContext,
    completion_dynamic_delegate: TargetingRequestDynamicDelegate
) -> TargetingRequestHandle
```

x.start_async_targeting_request(targeting_preset, source_context, completion_dynamic_delegate) -> TargetingRequestHandle
Method to queue an async targeting request based on a gameplay targeting preset.

Args:
    targeting_preset (TargetingPreset): 
    source_context (TargetingSourceContext): 
    completion_dynamic_delegate (TargetingRequestDynamicDelegate): 

Returns:
    TargetingRequestHandle:

<a id="unreal.TargetingSubsystem.remove_async_targeting_request_with_handle"></a>

#### remove\_async\_targeting\_request\_with\_handle

```python
def remove_async_targeting_request_with_handle(
        targeting_handle: TargetingRequestHandle) -> TargetingRequestHandle
```

x.remove_async_targeting_request_with_handle(targeting_handle) -> TargetingRequestHandle
Method to remove an async targeting request with a given targeting handle

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    TargetingRequestHandle: 

    targeting_handle (TargetingRequestHandle):

<a id="unreal.TargetingSubsystem.override_collision_query_task_data"></a>

#### override\_collision\_query\_task\_data

```python
@classmethod
def override_collision_query_task_data(
        cls, targeting_handle: TargetingRequestHandle,
        collision_query_data_override: CollisionQueryTaskData) -> None
```

X.override_collision_query_task_data(targeting_handle, collision_query_data_override) -> None
Function that lets you set a data store from a certain Targeting Handle to add some Collision Query Param Overrides

Args:
    targeting_handle (TargetingRequestHandle): 
    collision_query_data_override (CollisionQueryTaskData):

<a id="unreal.TargetingSubsystem.get_targeting_source_context"></a>

#### get\_targeting\_source\_context

```python
def get_targeting_source_context(
        targeting_handle: TargetingRequestHandle) -> TargetingSourceContext
```

x.get_targeting_source_context(targeting_handle) -> TargetingSourceContext
Returns the targeting source context for the targeting request handle

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    TargetingSourceContext:

<a id="unreal.TargetingSubsystem.get_targeting_results_actors"></a>

#### get\_targeting\_results\_actors

```python
def get_targeting_results_actors(
        targeting_handle: TargetingRequestHandle) -> Array[Actor]
```

x.get_targeting_results_actors(targeting_handle) -> Array[Actor]
Method to get the actor targets from a given targeting request handle

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Array[Actor]: 

    targets (Array[Actor]):

<a id="unreal.TargetingSubsystem.get_targeting_results"></a>

#### get\_targeting\_results

```python
def get_targeting_results(
        targeting_handle: TargetingRequestHandle) -> Array[HitResult]
```

x.get_targeting_results(targeting_handle) -> Array[HitResult]
Helper method to get the set of hit results for a given targeting handle

Args:
    targeting_handle (TargetingRequestHandle): 

Returns:
    Array[HitResult]: 

    out_targets (Array[HitResult]):

<a id="unreal.TargetingSubsystem.execute_targeting_request"></a>

#### execute\_targeting\_request

```python
def execute_targeting_request(
        targeting_preset: TargetingPreset,
        source_context: TargetingSourceContext,
        completion_dynamic_delegate: TargetingRequestDynamicDelegate) -> None
```

x.execute_targeting_request(targeting_preset, source_context, completion_dynamic_delegate) -> None
Method to execute an immediate targeting request based on a gameplay targeting preset.

Args:
    targeting_preset (TargetingPreset): 
    source_context (TargetingSourceContext): 
    completion_dynamic_delegate (TargetingRequestDynamicDelegate):

<a id="unreal.TargetingFilterTask_SortByDistance"></a>