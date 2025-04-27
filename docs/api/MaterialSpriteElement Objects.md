## MaterialSpriteElement Objects

```python
class MaterialSpriteElement(StructBase)
```

Material Sprite Element

**C++ Source:**

- **Module**: Engine
- **File**: MaterialBillboardComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_size_x`` (float):  [Read-Write] The base width of the sprite, multiplied with the DistanceToSizeCurve.
- ``base_size_y`` (float):  [Read-Write] The base height of the sprite, multiplied with the DistanceToSizeCurve.
- ``distance_to_opacity_curve`` (CurveFloat):  [Read-Write] A curve that maps distance on the X axis to the sprite opacity on the Y axis.
- ``distance_to_size_curve`` (CurveFloat):  [Read-Write] A curve that maps distance on the X axis to the sprite size on the Y axis.
- ``material`` (MaterialInterface):  [Read-Write] The material that the sprite is rendered with.
- ``size_is_in_screen_space`` (bool):  [Read-Write] Whether the size is defined in screen-space or world-space.

<a id="unreal.MaterialSpriteElement.__init__"></a>

#### __init__

```python
def __init__(material: MaterialInterface = None,
             distance_to_opacity_curve: CurveFloat = None,
             size_is_in_screen_space: bool = False,
             base_size_x: float = 0.000000,
             base_size_y: float = 0.000000,
             distance_to_size_curve: CurveFloat = None) -> None
```

<a id="unreal.MaterialSpriteElement.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] The material that the sprite is rendered with.

<a id="unreal.MaterialSpriteElement.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.MaterialSpriteElement.distance_to_opacity_curve"></a>

#### distance_to_opacity_curve

```python
@property
def distance_to_opacity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] A curve that maps distance on the X axis to the sprite opacity on the Y axis.

<a id="unreal.MaterialSpriteElement.distance_to_opacity_curve"></a>

#### distance_to_opacity_curve

```python
@distance_to_opacity_curve.setter
def distance_to_opacity_curve(value: CurveFloat) -> None
```

<a id="unreal.MaterialSpriteElement.size_is_in_screen_space"></a>

#### size_is_in_screen_space

```python
@property
def size_is_in_screen_space() -> bool
```

(bool):  [Read-Write] Whether the size is defined in screen-space or world-space.

<a id="unreal.MaterialSpriteElement.size_is_in_screen_space"></a>

#### size_is_in_screen_space

```python
@size_is_in_screen_space.setter
def size_is_in_screen_space(value: bool) -> None
```

<a id="unreal.MaterialSpriteElement.base_size_x"></a>

#### base_size_x

```python
@property
def base_size_x() -> float
```

(float):  [Read-Write] The base width of the sprite, multiplied with the DistanceToSizeCurve.

<a id="unreal.MaterialSpriteElement.base_size_x"></a>

#### base_size_x

```python
@base_size_x.setter
def base_size_x(value: float) -> None
```

<a id="unreal.MaterialSpriteElement.base_size_y"></a>

#### base_size_y

```python
@property
def base_size_y() -> float
```

(float):  [Read-Write] The base height of the sprite, multiplied with the DistanceToSizeCurve.

<a id="unreal.MaterialSpriteElement.base_size_y"></a>

#### base_size_y

```python
@base_size_y.setter
def base_size_y(value: float) -> None
```

<a id="unreal.MaterialSpriteElement.distance_to_size_curve"></a>

#### distance_to_size_curve

```python
@property
def distance_to_size_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] A curve that maps distance on the X axis to the sprite size on the Y axis.

<a id="unreal.MaterialSpriteElement.distance_to_size_curve"></a>

#### distance_to_size_curve

```python
@distance_to_size_curve.setter
def distance_to_size_curve(value: CurveFloat) -> None
```

<a id="unreal.EngineShowFlagsSetting"></a>