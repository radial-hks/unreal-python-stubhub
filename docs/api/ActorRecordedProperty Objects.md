## ActorRecordedProperty Objects

```python
class ActorRecordedProperty(StructBase)
```

Actor Recorded Property

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeRecorderSourceProperty.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``property_name`` (Name):  [Read-Write]
- ``recorder_name`` (Text):  [Read-Only]

<a id="unreal.ActorRecordedProperty.__init__"></a>

#### __init__

```python
def __init__(property_name: Name = "None", enabled: bool = False) -> None
```

<a id="unreal.ActorRecordedProperty.property_name"></a>

#### property_name

```python
@property
def property_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ActorRecordedProperty.property_name"></a>

#### property_name

```python
@property_name.setter
def property_name(value: Name) -> None
```

<a id="unreal.ActorRecordedProperty.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ActorRecordedProperty.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.AudioInputDeviceInfoProperty"></a>