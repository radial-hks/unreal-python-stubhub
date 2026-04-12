## AbilityTask\_NetworkSyncPoint Objects

```python
class AbilityTask_NetworkSyncPoint(AbilityTask)
```

Task for providing a generic sync point for client server (one can wait for a signal from the other)

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_NetworkSyncPoint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_sync`` (NetworkSyncDelegate):  [Read-Write]

<a id="unreal.AbilityTask_NetworkSyncPoint.on_sync"></a>

#### on\_sync

```python
@property
def on_sync() -> NetworkSyncDelegate
```

(NetworkSyncDelegate):  [Read-Write]

<a id="unreal.AbilityTask_NetworkSyncPoint.on_sync"></a>

#### on\_sync

```python
@on_sync.setter
def on_sync(value: NetworkSyncDelegate) -> None
```

<a id="unreal.AbilityTask_PlayMontageAndWait"></a>