## DataRegistryAcquireStatus Objects

```python
class DataRegistryAcquireStatus(EnumBase)
```

State of a registry async request

**C++ Source:**

- **Plugin**: DataRegistry
- **Module**: DataRegistry
- **File**: DataRegistryTypes.h

<a id="unreal.DataRegistryAcquireStatus.NOT_STARTED"></a>

#### NOT\_STARTED

0: Not started yet

<a id="unreal.DataRegistryAcquireStatus.WAITING_FOR_INITIAL_ACQUIRE"></a>

#### WAITING\_FOR\_INITIAL\_ACQUIRE

1: Initial acquire still in progress

<a id="unreal.DataRegistryAcquireStatus.INITIAL_ACQUIRE_FINISHED"></a>

#### INITIAL\_ACQUIRE\_FINISHED

2: Temporary state, finished acquiring data but need to check resources

<a id="unreal.DataRegistryAcquireStatus.WAITING_FOR_RESOURCES"></a>

#### WAITING\_FOR\_RESOURCES

3: Data requested and returned, still loading dependent resources

<a id="unreal.DataRegistryAcquireStatus.ACQUIRE_FINISHED"></a>

#### ACQUIRE\_FINISHED

4: Fully loaded

<a id="unreal.DataRegistryAcquireStatus.ACQUIRE_ERROR"></a>

#### ACQUIRE\_ERROR

5: Failed to acquire, may have timed out or had network issues, can be retried later

<a id="unreal.DataRegistryAcquireStatus.DOES_NOT_EXIST"></a>

#### DOES\_NOT\_EXIST

6: Known to not exist, cannot be retried

<a id="unreal.CameraRigInitialOrientation"></a>