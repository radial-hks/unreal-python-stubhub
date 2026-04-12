## AsyncAction\_PerformTargeting Objects

```python
class AsyncAction_PerformTargeting(BlueprintAsyncActionBase)
```

class: UAsyncAction_PerformTargeting

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: AsyncAction_PerformTargeting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``targeted`` (PerformTargetingReady):  [Read-Write]

<a id="unreal.AsyncAction_PerformTargeting.targeted"></a>

#### targeted

```python
@property
def targeted() -> PerformTargetingReady
```

(PerformTargetingReady):  [Read-Write]

<a id="unreal.AsyncAction_PerformTargeting.targeted"></a>

#### targeted

```python
@targeted.setter
def targeted(value: PerformTargetingReady) -> None
```

<a id="unreal.AsyncAction_PerformTargeting.get_targeting_handle"></a>

#### get\_targeting\_handle

```python
def get_targeting_handle() -> TargetingRequestHandle
```

x.get_targeting_handle() -> TargetingRequestHandle
Get Targeting Handle

Returns:
    TargetingRequestHandle:

<a id="unreal.TargetingTask"></a>