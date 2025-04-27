## SequencerOutlinerScriptingObject Objects

```python
class SequencerOutlinerScriptingObject(Object)
```

Sequencer Outliner Scripting Object

**C++ Source:**

- **Module**: SequencerCore
- **File**: OutlinerScriptingObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_selection_changed`` (SequencerOutlinerSelectionChanged):  [Read-Write]

<a id="unreal.SequencerOutlinerScriptingObject.on_selection_changed"></a>

#### on_selection_changed

```python
@property
def on_selection_changed() -> SequencerOutlinerSelectionChanged
```

(SequencerOutlinerSelectionChanged):  [Read-Write]

<a id="unreal.SequencerOutlinerScriptingObject.on_selection_changed"></a>

#### on_selection_changed

```python
@on_selection_changed.setter
def on_selection_changed(value: SequencerOutlinerSelectionChanged) -> None
```

<a id="unreal.SequencerOutlinerScriptingObject.set_selection"></a>

#### set_selection

```python
def set_selection(selection: Array[SequencerViewModelScriptingStruct]) -> None
```

x.set_selection(selection) -> None
Set Selection

Args:
    selection (Array[SequencerViewModelScriptingStruct]):

<a id="unreal.SequencerOutlinerScriptingObject.get_selection"></a>

#### get_selection

```python
def get_selection() -> Array[SequencerViewModelScriptingStruct]
```

x.get_selection() -> Array[SequencerViewModelScriptingStruct]
Get Selection

Returns:
    Array[SequencerViewModelScriptingStruct]:

<a id="unreal.SequencerOutlinerScriptingObject.get_root_node"></a>

#### get_root_node

```python
def get_root_node() -> SequencerViewModelScriptingStruct
```

x.get_root_node() -> SequencerViewModelScriptingStruct
Get Root Node

Returns:
    SequencerViewModelScriptingStruct:

<a id="unreal.SequencerOutlinerScriptingObject.get_children"></a>

#### get_children

```python
def get_children(
        node: SequencerViewModelScriptingStruct,
        type_name: Name = "None") -> Array[SequencerViewModelScriptingStruct]
```

x.get_children(node, type_name="None") -> Array[SequencerViewModelScriptingStruct]
Get Children

Args:
    node (SequencerViewModelScriptingStruct): 
    type_name (Name): 

Returns:
    Array[SequencerViewModelScriptingStruct]:

<a id="unreal.SequencerScriptingLayer"></a>