## ComposurePostMoveSettings Objects

```python
class ComposurePostMoveSettings(StructBase)
```

Composure Post Move Settings

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposurePostMoves.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pivot`` (Vector2D):  [Read-Write] The normalized pivot point for applying rotation and scale to the image. The x and y values are normalized to the range 0-1 where 1 represents the full width and height of the image.
- ``rotation_angle`` (float):  [Read-Write] The anti clockwise rotation to apply to the image in degrees.
- ``scale`` (float):  [Read-Write] The scale to apply to the image.
- ``translation`` (Vector2D):  [Read-Write] The translation to apply to the image.  The x and y values are normalized to the range 0-1 where 1 represents the full width and height of the image.

<a id="unreal.ComposurePostMoveSettings.__init__"></a>

#### __init__

```python
def __init__(pivot: Vector2D = [0.000000, 0.000000],
             translation: Vector2D = [0.000000, 0.000000],
             rotation_angle: float = 0.000000,
             scale: float = 0.000000) -> None
```

<a id="unreal.ComposurePostMoveSettings.pivot"></a>

#### pivot

```python
@property
def pivot() -> Vector2D
```

(Vector2D):  [Read-Write] The normalized pivot point for applying rotation and scale to the image. The x and y values are normalized to the range 0-1 where 1 represents the full width and height of the image.

<a id="unreal.ComposurePostMoveSettings.pivot"></a>

#### pivot

```python
@pivot.setter
def pivot(value: Vector2D) -> None
```

<a id="unreal.ComposurePostMoveSettings.translation"></a>

#### translation

```python
@property
def translation() -> Vector2D
```

(Vector2D):  [Read-Write] The translation to apply to the image.  The x and y values are normalized to the range 0-1 where 1 represents the full width and height of the image.

<a id="unreal.ComposurePostMoveSettings.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector2D) -> None
```

<a id="unreal.ComposurePostMoveSettings.rotation_angle"></a>

#### rotation_angle

```python
@property
def rotation_angle() -> float
```

(float):  [Read-Write] The anti clockwise rotation to apply to the image in degrees.

<a id="unreal.ComposurePostMoveSettings.rotation_angle"></a>

#### rotation_angle

```python
@rotation_angle.setter
def rotation_angle(value: float) -> None
```

<a id="unreal.ComposurePostMoveSettings.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write] The scale to apply to the image.

<a id="unreal.ComposurePostMoveSettings.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.ComposureUVMapSettings"></a>