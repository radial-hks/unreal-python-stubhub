## AbilityTask\_WaitInputRelease Objects

```python
class AbilityTask_WaitInputRelease(AbilityTask)
```

Waits until the input is released from activating an ability. Clients will replicate a 'release input' event to the server, but not the exact time it was held locally.
We expect server to execute this task in parallel and keep its own time.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_WaitInputRelease.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_release`` (InputReleaseDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitInputRelease.on_release"></a>

#### on\_release

```python
@property
def on_release() -> InputReleaseDelegate
```

(InputReleaseDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitInputRelease.on_release"></a>

#### on\_release

```python
@on_release.setter
def on_release(value: InputReleaseDelegate) -> None
```

<a id="unreal.AbilityTask_WaitMovementModeChange"></a>