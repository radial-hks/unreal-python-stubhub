## AvaPatternModifierGridLayoutOptions Objects

```python
class AvaPatternModifierGridLayoutOptions(StructBase)
```

Ava Pattern Modifier Grid Layout Options

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaPatternModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulate_transform`` (bool):  [Read-Write]
- ``axis_inverted`` (Vector2b):  [Read-Write]
- ``centered`` (bool):  [Read-Write] Center the layout based on the plane
- ``plane`` (AvaPatternModifierPlane):  [Read-Write]
- ``repeat_count`` (IntPoint):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``spacing`` (Vector2D):  [Read-Write] Row, Column

<a id="unreal.AvaPatternModifierGridLayoutOptions.__init__"></a>

#### __init__

```python
def __init__(plane: AvaPatternModifierPlane = AvaPatternModifierPlane.XY,
             axis_inverted: Vector2b = [False, False],
             repeat_count: IntPoint = [0, 0],
             spacing: Vector2D = [0.000000, 0.000000],
             centered: bool = False,
             accumulate_transform: bool = False,
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.plane"></a>

#### plane

```python
@property
def plane() -> AvaPatternModifierPlane
```

(AvaPatternModifierPlane):  [Read-Write]

<a id="unreal.AvaPatternModifierGridLayoutOptions.plane"></a>

#### plane

```python
@plane.setter
def plane(value: AvaPatternModifierPlane) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.axis_inverted"></a>

#### axis_inverted

```python
@property
def axis_inverted() -> Vector2b
```

(Vector2b):  [Read-Write]

<a id="unreal.AvaPatternModifierGridLayoutOptions.axis_inverted"></a>

#### axis_inverted

```python
@axis_inverted.setter
def axis_inverted(value: Vector2b) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.repeat_count"></a>

#### repeat_count

```python
@property
def repeat_count() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.AvaPatternModifierGridLayoutOptions.repeat_count"></a>

#### repeat_count

```python
@repeat_count.setter
def repeat_count(value: IntPoint) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.spacing"></a>

#### spacing

```python
@property
def spacing() -> Vector2D
```

(Vector2D):  [Read-Write] Row, Column

<a id="unreal.AvaPatternModifierGridLayoutOptions.spacing"></a>

#### spacing

```python
@spacing.setter
def spacing(value: Vector2D) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.centered"></a>

#### centered

```python
@property
def centered() -> bool
```

(bool):  [Read-Write] Center the layout based on the plane

<a id="unreal.AvaPatternModifierGridLayoutOptions.centered"></a>

#### centered

```python
@centered.setter
def centered(value: bool) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.accumulate_transform"></a>

#### accumulate_transform

```python
@property
def accumulate_transform() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaPatternModifierGridLayoutOptions.accumulate_transform"></a>

#### accumulate_transform

```python
@accumulate_transform.setter
def accumulate_transform(value: bool) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.AvaPatternModifierGridLayoutOptions.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.AvaPatternModifierGridLayoutOptions.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AvaPatternModifierGridLayoutOptions.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.AvaCloneModifierGridLayoutOptions"></a>