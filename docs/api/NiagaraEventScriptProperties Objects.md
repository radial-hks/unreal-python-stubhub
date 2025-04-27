## NiagaraEventScriptProperties Objects

```python
class NiagaraEventScriptProperties(NiagaraEmitterScriptProperties)
```

Niagara Event Script Properties

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEmitter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execution_mode`` (ScriptExecutionMode):  [Read-Write] Controls which particles have the event script run on them.
- ``max_events_per_frame`` (uint32):  [Read-Write] Controls how many events are consumed by this event handler. If there are more events generated than this value, they will be ignored.
- ``min_spawn_number`` (uint32):  [Read-Write] The minimum spawn number when random spawn is used. Spawn Number is used as the maximum range.
- ``random_spawn_number`` (bool):  [Read-Write] Whether using a random spawn number.
- ``source_emitter_id`` (Guid):  [Read-Write] Id of the Emitter Handle that generated the event. If all zeroes, the event generator is assumed to be this emitter.
- ``source_event_name`` (Name):  [Read-Write] The name of the event generated. This will be "Collision" for collision events and the Event Name field on the DataSetWrite node in the module graph for others.
- ``spawn_number`` (uint32):  [Read-Write] Controls whether or not particles are spawned as a result of handling the event. Only valid for EScriptExecutionMode::SpawnedParticles. If Random Spawn Number is used, this will act as the maximum spawn range.
- ``update_attribute_initial_values`` (bool):  [Read-Write] Should Event Spawn Scripts modify the Initial values for particle attributes they modify.

<a id="unreal.NiagaraEventScriptProperties.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.DaySequenceCollectionEntry"></a>