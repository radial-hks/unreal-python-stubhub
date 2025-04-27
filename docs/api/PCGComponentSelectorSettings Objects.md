## PCGComponentSelectorSettings Objects

```python
class PCGComponentSelectorSettings(StructBase)
```

PCGComponent Selector Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGActorSelector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_selection`` (PCGComponentSelection):  [Read-Write] How to select when filtering actors.
- ``component_selection_class`` (type(Class)):  [Read-Write] Actor class to match against when filtering actors.
- ``component_selection_tag`` (Name):  [Read-Write] Tag to match against when filtering actors.

<a id="unreal.PCGComponentSelectorSettings.__init__"></a>

#### __init__

```python
def __init__(component_selection: PCGComponentSelection = PCGComponentSelection
             .BY_TAG,
             component_selection_tag: Name = "None",
             component_selection_class: Class = None) -> None
```

<a id="unreal.PCGComponentSelectorSettings.component_selection"></a>

#### component_selection

```python
@property
def component_selection() -> PCGComponentSelection
```

(PCGComponentSelection):  [Read-Write] How to select when filtering actors.

<a id="unreal.PCGComponentSelectorSettings.component_selection"></a>

#### component_selection

```python
@component_selection.setter
def component_selection(value: PCGComponentSelection) -> None
```

<a id="unreal.PCGComponentSelectorSettings.component_selection_tag"></a>

#### component_selection_tag

```python
@property
def component_selection_tag() -> Name
```

(Name):  [Read-Write] Tag to match against when filtering actors.

<a id="unreal.PCGComponentSelectorSettings.component_selection_tag"></a>

#### component_selection_tag

```python
@component_selection_tag.setter
def component_selection_tag(value: Name) -> None
```

<a id="unreal.PCGComponentSelectorSettings.component_selection_class"></a>

#### component_selection_class

```python
@property
def component_selection_class() -> Class
```

(type(Class)):  [Read-Write] Actor class to match against when filtering actors.

<a id="unreal.PCGComponentSelectorSettings.component_selection_class"></a>

#### component_selection_class

```python
@component_selection_class.setter
def component_selection_class(value: Class) -> None
```

<a id="unreal.PCGSelfPruningParameters"></a>