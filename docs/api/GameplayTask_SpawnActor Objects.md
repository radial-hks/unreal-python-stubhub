## GameplayTask_SpawnActor Objects

```python
class GameplayTask_SpawnActor(GameplayTask)
```

Convenience task for spawning actors (optionally limiting the spawning to the network authority). If not the net authority, we will not spawn
and Success will not be called. The nice thing this adds is the ability to modify expose on spawn properties while also implicitly checking
network role before spawning.

Though this task doesn't do much - games can implement similar tasks that carry out game specific rules. For example a 'SpawnProjectile'
task that limits the available classes to the games projectile class, and that does game specific stuff on spawn (for example, determining
firing position from a weapon attachment).

Long term we can also use this task as a sync point. If the executing client could wait execution until the server creates and replicates the
actor down to it. We could potentially also use this to do predictive actor spawning / reconciliation.

**C++ Source:**

- **Module**: GameplayTasks
- **File**: GameplayTask_SpawnActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``did_not_spawn`` (GameplayTaskSpawnActorDelegate):  [Read-Write] Called when we can't spawn: on clients or potentially on server if they fail to spawn (rare)
- ``success`` (GameplayTaskSpawnActorDelegate):  [Read-Write]

<a id="unreal.GameplayTask_SpawnActor.success"></a>

#### success

```python
@property
def success() -> GameplayTaskSpawnActorDelegate
```

(GameplayTaskSpawnActorDelegate):  [Read-Write]

<a id="unreal.GameplayTask_SpawnActor.success"></a>

#### success

```python
@success.setter
def success(value: GameplayTaskSpawnActorDelegate) -> None
```

<a id="unreal.GameplayTask_SpawnActor.did_not_spawn"></a>

#### did_not_spawn

```python
@property
def did_not_spawn() -> GameplayTaskSpawnActorDelegate
```

(GameplayTaskSpawnActorDelegate):  [Read-Write] Called when we can't spawn: on clients or potentially on server if they fail to spawn (rare)

<a id="unreal.GameplayTask_SpawnActor.did_not_spawn"></a>

#### did_not_spawn

```python
@did_not_spawn.setter
def did_not_spawn(value: GameplayTaskSpawnActorDelegate) -> None
```

<a id="unreal.GameplayTask_TimeLimitedExecution"></a>