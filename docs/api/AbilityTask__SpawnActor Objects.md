## AbilityTask\_SpawnActor Objects

```python
class AbilityTask_SpawnActor(AbilityTask)
```

Convenience task for spawning actors on the network authority. If not the net authority, we will not spawn and Success will not be called.
The nice thing this adds is the ability to modify expose on spawn properties while also implicitly checking network role before spawning.

Though this task doesn't do much - games can implement similiar tasks that carry out game specific rules. For example a 'SpawnProjectile'
task that limits the available classes to the games projectile class, and that does game specific stuff on spawn (for example, determining
firing position from a weapon attachment - logic that we don't necessarily want in ability blueprints).

Long term we can also use this task as a sync point. If the executing client could wait execution until the server creates and replicates the
actor down to it. We could potentially also use this to do predictive actor spawning / reconciliation.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_SpawnActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``did_not_spawn`` (SpawnActorDelegate):  [Read-Write] Called when we can't spawn: on clients or potentially on server if they fail to spawn (rare)
- ``success`` (SpawnActorDelegate):  [Read-Write]

<a id="unreal.AbilityTask_SpawnActor.success"></a>

#### success

```python
@property
def success() -> SpawnActorDelegate
```

(SpawnActorDelegate):  [Read-Write]

<a id="unreal.AbilityTask_SpawnActor.success"></a>

#### success

```python
@success.setter
def success(value: SpawnActorDelegate) -> None
```

<a id="unreal.AbilityTask_SpawnActor.did_not_spawn"></a>

#### did\_not\_spawn

```python
@property
def did_not_spawn() -> SpawnActorDelegate
```

(SpawnActorDelegate):  [Read-Write] Called when we can't spawn: on clients or potentially on server if they fail to spawn (rare)

<a id="unreal.AbilityTask_SpawnActor.did_not_spawn"></a>

#### did\_not\_spawn

```python
@did_not_spawn.setter
def did_not_spawn(value: SpawnActorDelegate) -> None
```

<a id="unreal.AbilityTask_StartAbilityState"></a>