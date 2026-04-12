## AbilityTask\_WaitTargetData Objects

```python
class AbilityTask_WaitTargetData(AbilityTask)
```

Wait for targeting actor (spawned from parameter) to provide data. Can be set not to end upon outputting data. Can be ended by task name.

WARNING: These actors are spawned once per ability activation and in their default form are not very efficient
For most games you will need to subclass and heavily modify this actor, or you will want to implement similar functions in a game-specific actor or blueprint to avoid actor spawn costs
This task is not well tested by internal games, but it is a useful class to look at to learn how target replication occurs

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_WaitTargetData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cancelled`` (WaitTargetDataDelegate):  [Read-Write]
- ``valid_data`` (WaitTargetDataDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitTargetData.valid_data"></a>

#### valid\_data

```python
@property
def valid_data() -> WaitTargetDataDelegate
```

(WaitTargetDataDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitTargetData.valid_data"></a>

#### valid\_data

```python
@valid_data.setter
def valid_data(value: WaitTargetDataDelegate) -> None
```

<a id="unreal.AbilityTask_WaitTargetData.cancelled"></a>

#### cancelled

```python
@property
def cancelled() -> WaitTargetDataDelegate
```

(WaitTargetDataDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitTargetData.cancelled"></a>

#### cancelled

```python
@cancelled.setter
def cancelled(value: WaitTargetDataDelegate) -> None
```

<a id="unreal.AbilityTask_WaitVelocityChange"></a>