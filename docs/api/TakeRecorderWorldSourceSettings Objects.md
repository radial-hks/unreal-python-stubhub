## TakeRecorderWorldSourceSettings Objects

```python
class TakeRecorderWorldSourceSettings(TakeRecorderSource)
```

A recording source that records world state

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorderSources
- **File**: TakeRecorderWorldSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``autotrack_actors`` (bool):  [Read-Write] Add a binding and track for all actors that aren't explicitly being recorded
- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``record_world_settings`` (bool):  [Read-Write] Record world settings
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderWorldSourceSettings.record_world_settings"></a>

#### record_world_settings

```python
@property
def record_world_settings() -> bool
```

(bool):  [Read-Write] Record world settings

<a id="unreal.TakeRecorderWorldSourceSettings.record_world_settings"></a>

#### record_world_settings

```python
@record_world_settings.setter
def record_world_settings(value: bool) -> None
```

<a id="unreal.TakeRecorderWorldSourceSettings.autotrack_actors"></a>

#### autotrack_actors

```python
@property
def autotrack_actors() -> bool
```

(bool):  [Read-Write] Add a binding and track for all actors that aren't explicitly being recorded

<a id="unreal.TakeRecorderWorldSourceSettings.autotrack_actors"></a>

#### autotrack_actors

```python
@autotrack_actors.setter
def autotrack_actors(value: bool) -> None
```

<a id="unreal.TakeRecorderWorldSource"></a>