## DisplayClusterMediaOutputSynchronizationPolicyThresholdBase Objects

```python
class DisplayClusterMediaOutputSynchronizationPolicyThresholdBase(
        DisplayClusterMediaOutputSynchronizationPolicyEthernetBarrierBase)
```

* Base class for threshold based media synchronization policies.
*
* Basically it uses the same approach that we use in 'Ethernet' sync policy where v-blanks are used as the timepoints.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterMedia
- **File**: DisplayClusterMediaOutputSynchronizationPolicyThresholdBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``barrier_timeout_ms`` (int32):  [Read-Write] Barrier timeout (ms)
- ``margin_ms`` (int32):  [Read-Write] Synchronization margin (ms)

<a id="unreal.DisplayClusterMediaOutputSynchronizationPolicyThresholdBase.margin_ms"></a>

#### margin_ms

```python
@property
def margin_ms() -> int
```

(int32):  [Read-Write] Synchronization margin (ms)

<a id="unreal.DisplayClusterMediaOutputSynchronizationPolicyThresholdBase.margin_ms"></a>

#### margin_ms

```python
@margin_ms.setter
def margin_ms(value: int) -> None
```

<a id="unreal.DisplayClusterMediaOutputSynchronizationPolicyVblank"></a>