## AvaVisibilityModifier Objects

```python
class AvaVisibilityModifier(AvaArrangeBaseModifier)
```

Controls the visibility of a range of child actors by index.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaVisibilityModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``index`` (int32):  [Read-Write] Child index to set visibility, visible if bInvertVisibility is false else hidden
- ``invert_visibility`` (bool):  [Read-Write] If true, will hide the child index range instead of showing.
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``skip_when_hidden`` (bool):  [Read-Write] If true, when the top actor having this modifier is hidden, children actor visibility state will not be handled
- ``treat_as_range`` (bool):  [Read-Write] Treat index as a range from 0 to index

<a id="unreal.AvaVisibilityModifier.set_treat_as_range"></a>

#### set_treat_as_range

```python
def set_treat_as_range(treat_as_range: bool) -> None
```

x.set_treat_as_range(treat_as_range) -> None
Set Treat as Range

Args:
    treat_as_range (bool):

<a id="unreal.AvaVisibilityModifier.set_skip_when_hidden"></a>

#### set_skip_when_hidden

```python
def set_skip_when_hidden(skip: bool) -> None
```

x.set_skip_when_hidden(skip) -> None
Set Skip when Hidden

Args:
    skip (bool):

<a id="unreal.AvaVisibilityModifier.set_invert_visibility"></a>

#### set_invert_visibility

```python
def set_invert_visibility(invert_visibility: bool) -> None
```

x.set_invert_visibility(invert_visibility) -> None
Sets the child index range to hide instead of showing.

Args:
    invert_visibility (bool):

<a id="unreal.AvaVisibilityModifier.set_index"></a>

#### set_index

```python
def set_index(index: int) -> None
```

x.set_index(index) -> None
Set Index

Args:
    index (int32):

<a id="unreal.AvaVisibilityModifier.get_treat_as_range"></a>

#### get_treat_as_range

```python
def get_treat_as_range() -> bool
```

x.get_treat_as_range() -> bool
Get Treat as Range

Returns:
    bool:

<a id="unreal.AvaVisibilityModifier.get_skip_when_hidden"></a>

#### get_skip_when_hidden

```python
def get_skip_when_hidden() -> bool
```

x.get_skip_when_hidden() -> bool
Get Skip when Hidden

Returns:
    bool:

<a id="unreal.AvaVisibilityModifier.get_invert_visibility"></a>

#### get_invert_visibility

```python
def get_invert_visibility() -> bool
```

x.get_invert_visibility() -> bool
Returns true if hiding the child index range instead of showing.

Returns:
    bool:

<a id="unreal.AvaVisibilityModifier.get_index"></a>

#### get_index

```python
def get_index() -> int
```

x.get_index() -> int32
Get Index

Returns:
    int32:

<a id="unreal.AvaEaseCurve"></a>