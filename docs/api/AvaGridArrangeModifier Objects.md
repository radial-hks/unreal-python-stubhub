## AvaGridArrangeModifier Objects

```python
class AvaGridArrangeModifier(AvaArrangeBaseModifier)
```

Arranges child actors in a 2D grid format.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaGridArrangeModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``count`` (IntPoint):  [Read-Write] The width and height of the grid.
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``spread`` (Vector2D):  [Read-Write] The distance between each horizontal and vertical child.
- ``start_corner`` (AvaCorner2D):  [Read-Write] The 2D corner from which to start the arrangement.
- ``start_direction`` (AvaGridArrangeDirection):  [Read-Write] The direction from which to start the arrangement.

<a id="unreal.AvaGridArrangeModifier.spread"></a>

#### spread

```python
@property
def spread() -> Vector2D
```

(Vector2D):  [Read-Write] The distance between each horizontal and vertical child.

<a id="unreal.AvaGridArrangeModifier.spread"></a>

#### spread

```python
@spread.setter
def spread(value: Vector2D) -> None
```

<a id="unreal.AvaGridArrangeModifier.set_start_direction"></a>

#### set_start_direction

```python
def set_start_direction(direction: AvaGridArrangeDirection) -> None
```

x.set_start_direction(direction) -> None
Set Start Direction

Args:
    direction (AvaGridArrangeDirection):

<a id="unreal.AvaGridArrangeModifier.set_start_corner"></a>

#### set_start_corner

```python
def set_start_corner(corner: AvaCorner2D) -> None
```

x.set_start_corner(corner) -> None
Set Start Corner

Args:
    corner (AvaCorner2D):

<a id="unreal.AvaGridArrangeModifier.set_spread"></a>

#### set_spread

```python
def set_spread(spread: Vector2D) -> None
```

x.set_spread(spread) -> None
Sets the distance between each horizontal and vertical child.

Args:
    spread (Vector2D):

<a id="unreal.AvaGridArrangeModifier.set_count"></a>

#### set_count

```python
def set_count(count: IntPoint) -> None
```

x.set_count(count) -> None
Sets the width and height of the grid.

Args:
    count (IntPoint):

<a id="unreal.AvaGridArrangeModifier.get_start_direction"></a>

#### get_start_direction

```python
def get_start_direction() -> AvaGridArrangeDirection
```

x.get_start_direction() -> AvaGridArrangeDirection
Get Start Direction

Returns:
    AvaGridArrangeDirection:

<a id="unreal.AvaGridArrangeModifier.get_start_corner"></a>

#### get_start_corner

```python
def get_start_corner() -> AvaCorner2D
```

x.get_start_corner() -> AvaCorner2D
Get Start Corner

Returns:
    AvaCorner2D:

<a id="unreal.AvaGridArrangeModifier.get_spread"></a>

#### get_spread

```python
def get_spread() -> Vector2D
```

x.get_spread() -> Vector2D
Returns the distance between each horizontal and vertical child.

Returns:
    Vector2D:

<a id="unreal.AvaGridArrangeModifier.get_count"></a>

#### get_count

```python
def get_count() -> IntPoint
```

x.get_count() -> IntPoint
Returns the width and height of the grid.

Returns:
    IntPoint:

<a id="unreal.AvaHideEmptyModifier"></a>