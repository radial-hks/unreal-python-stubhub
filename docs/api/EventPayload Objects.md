## EventPayload Objects

```python
class EventPayload(StructBase)
```

Event Payload

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneEventSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``event_name`` (Name):  [Read-Write] The name of the event to trigger
- ``parameters`` (MovieSceneEventParameters):  [Read-Write] The event parameters

<a id="unreal.EventPayload.__init__"></a>

#### __init__

```python
def __init__(event_name: Name = "None",
             parameters: MovieSceneEventParameters = []) -> None
```

<a id="unreal.EventPayload.event_name"></a>

#### event_name

```python
@property
def event_name() -> Name
```

(Name):  [Read-Write] The name of the event to trigger

<a id="unreal.EventPayload.event_name"></a>

#### event_name

```python
@event_name.setter
def event_name(value: Name) -> None
```

<a id="unreal.EventPayload.parameters"></a>

#### parameters

```python
@property
def parameters() -> MovieSceneEventParameters
```

(MovieSceneEventParameters):  [Read-Only] The event parameters

<a id="unreal.MovieSceneEventParameters"></a>