## ActorRecorderPropertyMap Objects

```python
class ActorRecorderPropertyMap(Object)
```

This represents a list of all possible properties and components on an actor
which can be recorded by the Actor Recorder and whether or not the user wishes
to record them. If you wish to expose a property to be recorded it needs to be marked
as "Interp" (C++) or "Expose to Cinematics" in Blueprints.

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeRecorderSourceProperty.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``children`` (Array[ActorRecorderPropertyMap]):  [Read-Write]
- ``properties`` (Array[ActorRecordedProperty]):  [Read-Write] Represents properties exposed to Cinematics that can possibly be recorded.
- ``recorded_object`` (Object):  [Read-Only]

<a id="unreal.ActorRecorderPropertyMap.properties"></a>

#### properties

```python
@property
def properties() -> Array[ActorRecordedProperty]
```

(Array[ActorRecordedProperty]):  [Read-Write] Represents properties exposed to Cinematics that can possibly be recorded.

<a id="unreal.ActorRecorderPropertyMap.properties"></a>

#### properties

```python
@properties.setter
def properties(value: Array[ActorRecordedProperty]) -> None
```

<a id="unreal.ActorRecorderPropertyMap.children"></a>

#### children

```python
@property
def children() -> Array[ActorRecorderPropertyMap]
```

(Array[ActorRecorderPropertyMap]):  [Read-Write]

<a id="unreal.ActorRecorderPropertyMap.children"></a>

#### children

```python
@children.setter
def children(value: Array[ActorRecorderPropertyMap]) -> None
```

<a id="unreal.TakeRecorderAudioInputSettings"></a>