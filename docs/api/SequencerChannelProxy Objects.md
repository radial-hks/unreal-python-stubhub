## SequencerChannelProxy Objects

```python
class SequencerChannelProxy(StructBase)
```

Sequencer Channel Proxy

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScriptingEditor
- **File**: SequencerCurveEditorObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_name`` (Name):  [Read-Write]
- ``section`` (MovieSceneSection):  [Read-Write]

<a id="unreal.SequencerChannelProxy.__init__"></a>

#### __init__

```python
def __init__(channel_name: Name = "None",
             section: MovieSceneSection = None) -> None
```

<a id="unreal.SequencerChannelProxy.channel_name"></a>

#### channel_name

```python
@property
def channel_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.SequencerChannelProxy.channel_name"></a>

#### channel_name

```python
@channel_name.setter
def channel_name(value: Name) -> None
```

<a id="unreal.SequencerChannelProxy.section"></a>

#### section

```python
@property
def section() -> MovieSceneSection
```

(MovieSceneSection):  [Read-Write]

<a id="unreal.SequencerChannelProxy.section"></a>

#### section

```python
@section.setter
def section(value: MovieSceneSection) -> None
```

<a id="unreal.SequencerBoundObjects"></a>