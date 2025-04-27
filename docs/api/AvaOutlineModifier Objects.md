## AvaOutlineModifier Objects

```python
class AvaOutlineModifier(AvaGeometryBaseModifier)
```

This modifier adds an outline around a 2D shape with a specific distance

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaOutlineModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance`` (float):  [Read-Write] Set the distance for the outline
- ``mode`` (AvaOutlineMode):  [Read-Write] Set the mode like inset or outset
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``remove_inside`` (bool):  [Read-Write] Remove the inside part and create a hole in the shape

<a id="unreal.AvaOutlineModifier.set_remove_inside"></a>

#### set_remove_inside

```python
def set_remove_inside(remove_inside: bool) -> None
```

x.set_remove_inside(remove_inside) -> None
Set Remove Inside

Args:
    remove_inside (bool):

<a id="unreal.AvaOutlineModifier.set_mode"></a>

#### set_mode

```python
def set_mode(mode: AvaOutlineMode) -> None
```

x.set_mode(mode) -> None
Set Mode

Args:
    mode (AvaOutlineMode):

<a id="unreal.AvaOutlineModifier.set_distance"></a>

#### set_distance

```python
def set_distance(distance: float) -> None
```

x.set_distance(distance) -> None
Set Distance

Args:
    distance (float):

<a id="unreal.AvaOutlineModifier.get_remove_inside"></a>

#### get_remove_inside

```python
def get_remove_inside() -> bool
```

x.get_remove_inside() -> bool
Get Remove Inside

Returns:
    bool:

<a id="unreal.AvaOutlineModifier.get_mode"></a>

#### get_mode

```python
def get_mode() -> AvaOutlineMode
```

x.get_mode() -> AvaOutlineMode
Get Mode

Returns:
    AvaOutlineMode:

<a id="unreal.AvaOutlineModifier.get_distance"></a>

#### get_distance

```python
def get_distance() -> float
```

x.get_distance() -> float
Get Distance

Returns:
    float:

<a id="unreal.AvaPatternModifier"></a>