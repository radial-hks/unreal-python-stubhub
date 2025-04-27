## WidgetTransform Objects

```python
class WidgetTransform(StructBase)
```

Describes the standard transformation of a widget

**C++ Source:**

- **Module**: UMG
- **File**: WidgetTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write] The angle in degrees to rotate
- ``scale`` (Vector2D):  [Read-Write] The scale to apply to the widget
- ``shear`` (Vector2D):  [Read-Write] The amount to shear the widget in slate units
- ``translation`` (Vector2D):  [Read-Write] The amount to translate the widget in slate units

<a id="unreal.WidgetTransform.__init__"></a>

#### __init__

```python
def __init__(translation: Vector2D = [0.000000, 0.000000],
             scale: Vector2D = [0.000000, 0.000000],
             shear: Vector2D = [0.000000, 0.000000],
             angle: float = 0.000000) -> None
```

<a id="unreal.WidgetTransform.translation"></a>

#### translation

```python
@property
def translation() -> Vector2D
```

(Vector2D):  [Read-Write] The amount to translate the widget in slate units

<a id="unreal.WidgetTransform.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector2D) -> None
```

<a id="unreal.WidgetTransform.scale"></a>

#### scale

```python
@property
def scale() -> Vector2D
```

(Vector2D):  [Read-Write] The scale to apply to the widget

<a id="unreal.WidgetTransform.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector2D) -> None
```

<a id="unreal.WidgetTransform.shear"></a>

#### shear

```python
@property
def shear() -> Vector2D
```

(Vector2D):  [Read-Write] The amount to shear the widget in slate units

<a id="unreal.WidgetTransform.shear"></a>

#### shear

```python
@shear.setter
def shear(value: Vector2D) -> None
```

<a id="unreal.WidgetTransform.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Write] The angle in degrees to rotate

<a id="unreal.WidgetTransform.angle"></a>

#### angle

```python
@angle.setter
def angle(value: float) -> None
```

<a id="unreal.SlateWidgetStyle"></a>