## SequencerModuleOutlinerScriptingObject Objects

```python
class SequencerModuleOutlinerScriptingObject(SequencerOutlinerScriptingObject)
```

Sequencer Module Outliner Scripting Object

**C++ Source:**

- **Module**: Sequencer
- **File**: SequencerModuleOutlinerScriptingObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_selection_changed`` (SequencerOutlinerSelectionChanged):  [Read-Write]

<a id="unreal.SequencerModuleOutlinerScriptingObject.get_previous_key"></a>

#### get_previous_key

```python
def get_previous_key(
    nodes: Array[SequencerViewModelScriptingStruct],
    frame_number: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> FrameNumber
```

x.get_previous_key(nodes, frame_number, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> FrameNumber
Get Previous Key

Args:
    nodes (Array[SequencerViewModelScriptingStruct]): 
    frame_number (FrameNumber): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    FrameNumber:

<a id="unreal.SequencerModuleOutlinerScriptingObject.get_next_key"></a>

#### get_next_key

```python
def get_next_key(
    nodes: Array[SequencerViewModelScriptingStruct],
    frame_number: FrameNumber,
    time_unit: MovieSceneTimeUnit = MovieSceneTimeUnit.DISPLAY_RATE
) -> FrameNumber
```

x.get_next_key(nodes, frame_number, time_unit=MovieSceneTimeUnit.DISPLAY_RATE) -> FrameNumber
Get Next Key

Args:
    nodes (Array[SequencerViewModelScriptingStruct]): 
    frame_number (FrameNumber): 
    time_unit (MovieSceneTimeUnit): 

Returns:
    FrameNumber:

<a id="unreal.SequencerModuleScriptingLayer"></a>