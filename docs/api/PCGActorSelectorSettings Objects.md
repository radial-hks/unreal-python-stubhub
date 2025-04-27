## PCGActorSelectorSettings Objects

```python
class PCGActorSelectorSettings(StructBase)
```

Helper struct for organizing queries against the world to gather actors.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGActorSelector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_filter`` (PCGActorFilter):  [Read-Write] Which actors to consider.
- ``actor_reference_selector`` (PCGAttributePropertyInputSelector):  [Read-Write] Controls what attribute to read from when the actor selector uses the "FromInput" actor filter.
- ``actor_selection`` (PCGActorSelection):  [Read-Write] How to select when filtering actors.
- ``actor_selection_class`` (type(Class)):  [Read-Write] Actor class to match against when filtering actors.
- ``actor_selection_tag`` (Name):  [Read-Write] Tag to match against when filtering actors.
- ``disable_filter`` (bool):  [Read-Write] Enables/disables fine-grained actor filtering options.
- ``ignore_self_and_children`` (bool):  [Read-Write] If true, ignores results found from within this actor's hierarchy.
- ``include_children`` (bool):  [Read-Write] Whether to consider child actors.
- ``must_overlap_self`` (bool):  [Read-Write] Filters out actors that do not overlap the source component bounds.
- ``select_multiple`` (bool):  [Read-Write] If true processes all matching actors, otherwise returns data from first match.

<a id="unreal.PCGActorSelectorSettings.__init__"></a>

#### __init__

```python
def __init__(actor_filter: PCGActorFilter = PCGActorFilter.SELF,
             must_overlap_self: bool = False,
             include_children: bool = False,
             disable_filter: bool = False,
             actor_selection: PCGActorSelection = PCGActorSelection.BY_TAG,
             actor_selection_tag: Name = "None",
             actor_selection_class: Class = None,
             actor_reference_selector: PCGAttributePropertyInputSelector = [],
             select_multiple: bool = False,
             ignore_self_and_children: bool = False) -> None
```

<a id="unreal.PCGActorSelectorSettings.actor_filter"></a>

#### actor_filter

```python
@property
def actor_filter() -> PCGActorFilter
```

(PCGActorFilter):  [Read-Write] Which actors to consider.

<a id="unreal.PCGActorSelectorSettings.actor_filter"></a>

#### actor_filter

```python
@actor_filter.setter
def actor_filter(value: PCGActorFilter) -> None
```

<a id="unreal.PCGActorSelectorSettings.must_overlap_self"></a>

#### must_overlap_self

```python
@property
def must_overlap_self() -> bool
```

(bool):  [Read-Write] Filters out actors that do not overlap the source component bounds.

<a id="unreal.PCGActorSelectorSettings.must_overlap_self"></a>

#### must_overlap_self

```python
@must_overlap_self.setter
def must_overlap_self(value: bool) -> None
```

<a id="unreal.PCGActorSelectorSettings.include_children"></a>

#### include_children

```python
@property
def include_children() -> bool
```

(bool):  [Read-Write] Whether to consider child actors.

<a id="unreal.PCGActorSelectorSettings.include_children"></a>

#### include_children

```python
@include_children.setter
def include_children(value: bool) -> None
```

<a id="unreal.PCGActorSelectorSettings.disable_filter"></a>

#### disable_filter

```python
@property
def disable_filter() -> bool
```

(bool):  [Read-Write] Enables/disables fine-grained actor filtering options.

<a id="unreal.PCGActorSelectorSettings.disable_filter"></a>

#### disable_filter

```python
@disable_filter.setter
def disable_filter(value: bool) -> None
```

<a id="unreal.PCGActorSelectorSettings.actor_selection"></a>

#### actor_selection

```python
@property
def actor_selection() -> PCGActorSelection
```

(PCGActorSelection):  [Read-Write] How to select when filtering actors.

<a id="unreal.PCGActorSelectorSettings.actor_selection"></a>

#### actor_selection

```python
@actor_selection.setter
def actor_selection(value: PCGActorSelection) -> None
```

<a id="unreal.PCGActorSelectorSettings.actor_selection_tag"></a>

#### actor_selection_tag

```python
@property
def actor_selection_tag() -> Name
```

(Name):  [Read-Write] Tag to match against when filtering actors.

<a id="unreal.PCGActorSelectorSettings.actor_selection_tag"></a>

#### actor_selection_tag

```python
@actor_selection_tag.setter
def actor_selection_tag(value: Name) -> None
```

<a id="unreal.PCGActorSelectorSettings.actor_selection_class"></a>

#### actor_selection_class

```python
@property
def actor_selection_class() -> Class
```

(type(Class)):  [Read-Write] Actor class to match against when filtering actors.

<a id="unreal.PCGActorSelectorSettings.actor_selection_class"></a>

#### actor_selection_class

```python
@actor_selection_class.setter
def actor_selection_class(value: Class) -> None
```

<a id="unreal.PCGActorSelectorSettings.actor_reference_selector"></a>

#### actor_reference_selector

```python
@property
def actor_reference_selector() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Controls what attribute to read from when the actor selector uses the "FromInput" actor filter.

<a id="unreal.PCGActorSelectorSettings.actor_reference_selector"></a>

#### actor_reference_selector

```python
@actor_reference_selector.setter
def actor_reference_selector(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGActorSelectorSettings.select_multiple"></a>

#### select_multiple

```python
@property
def select_multiple() -> bool
```

(bool):  [Read-Write] If true processes all matching actors, otherwise returns data from first match.

<a id="unreal.PCGActorSelectorSettings.select_multiple"></a>

#### select_multiple

```python
@select_multiple.setter
def select_multiple(value: bool) -> None
```

<a id="unreal.PCGActorSelectorSettings.ignore_self_and_children"></a>

#### ignore_self_and_children

```python
@property
def ignore_self_and_children() -> bool
```

(bool):  [Read-Write] If true, ignores results found from within this actor's hierarchy.

<a id="unreal.PCGActorSelectorSettings.ignore_self_and_children"></a>

#### ignore_self_and_children

```python
@ignore_self_and_children.setter
def ignore_self_and_children(value: bool) -> None
```

<a id="unreal.PCGComponentSelectorSettings"></a>