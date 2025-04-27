## TakeRecorderChaosCacheSource Objects

```python
class TakeRecorderChaosCacheSource(TakeRecorderSource)
```

A recording source selector for the chaos integration into take recorder

**C++ Source:**

- **Plugin**: ChaosCaching
- **Module**: ChaosCachingEditor
- **File**: TakeRecorderChaosCacheSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chaos_cache_manager`` (ChaosCacheManager):  [Read-Write] Chaos Cache manager to be used as take recorder source
- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderChaosCacheSource.chaos_cache_manager"></a>

#### chaos_cache_manager

```python
@property
def chaos_cache_manager() -> ChaosCacheManager
```

(ChaosCacheManager):  [Read-Write] Chaos Cache manager to be used as take recorder source

<a id="unreal.TakeRecorderChaosCacheSource.chaos_cache_manager"></a>

#### chaos_cache_manager

```python
@chaos_cache_manager.setter
def chaos_cache_manager(value: ChaosCacheManager) -> None
```

<a id="unreal.RigVM"></a>