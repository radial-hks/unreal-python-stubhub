## FontOutlineSettings Objects

```python
class FontOutlineSettings(StructBase)
```

Settings for applying an outline to a font

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateFontInfo.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_outline_to_drop_shadows`` (bool):  [Read-Write] When enabled the outline will be applied to any drop shadow that uses this font
- ``mitered_corners`` (bool):  [Read-Write] When enabled, outlines have sharp mitered corners, otherwise they are rounded.
- ``outline_color`` (LinearColor):  [Read-Write] The color of the outline for any character in this font
- ``outline_material`` (Object):  [Read-Write] Optional material to apply to the outline
- ``outline_size`` (int32):  [Read-Write] Size of the outline in slate units (at 1.0 font scale this unit is a pixel)
- ``separate_fill_alpha`` (bool):  [Read-Write] When enabled the outline will be completely translucent where the filled area will be.  This allows for a separate fill alpha value
  The trade off when enabling this is slightly worse quality for completely opaque fills where the inner outline border meets the fill area

<a id="unreal.FontOutlineSettings.__init__"></a>

#### __init__

```python
def __init__(
    outline_size: int = 0,
    mitered_corners: bool = False,
    separate_fill_alpha: bool = False,
    apply_outline_to_drop_shadows: bool = False,
    outline_material: Object = None,
    outline_color: LinearColor = [0.000000, 0.000000, 0.000000,
                                  0.000000]) -> None
```

<a id="unreal.FontOutlineSettings.outline_size"></a>

#### outline_size

```python
@property
def outline_size() -> int
```

(int32):  [Read-Write] Size of the outline in slate units (at 1.0 font scale this unit is a pixel)

<a id="unreal.FontOutlineSettings.outline_size"></a>

#### outline_size

```python
@outline_size.setter
def outline_size(value: int) -> None
```

<a id="unreal.FontOutlineSettings.mitered_corners"></a>

#### mitered_corners

```python
@property
def mitered_corners() -> bool
```

(bool):  [Read-Write] When enabled, outlines have sharp mitered corners, otherwise they are rounded.

<a id="unreal.FontOutlineSettings.mitered_corners"></a>

#### mitered_corners

```python
@mitered_corners.setter
def mitered_corners(value: bool) -> None
```

<a id="unreal.FontOutlineSettings.separate_fill_alpha"></a>

#### separate_fill_alpha

```python
@property
def separate_fill_alpha() -> bool
```

(bool):  [Read-Write] When enabled the outline will be completely translucent where the filled area will be.  This allows for a separate fill alpha value
The trade off when enabling this is slightly worse quality for completely opaque fills where the inner outline border meets the fill area

<a id="unreal.FontOutlineSettings.separate_fill_alpha"></a>

#### separate_fill_alpha

```python
@separate_fill_alpha.setter
def separate_fill_alpha(value: bool) -> None
```

<a id="unreal.FontOutlineSettings.apply_outline_to_drop_shadows"></a>

#### apply_outline_to_drop_shadows

```python
@property
def apply_outline_to_drop_shadows() -> bool
```

(bool):  [Read-Write] When enabled the outline will be applied to any drop shadow that uses this font

<a id="unreal.FontOutlineSettings.apply_outline_to_drop_shadows"></a>

#### apply_outline_to_drop_shadows

```python
@apply_outline_to_drop_shadows.setter
def apply_outline_to_drop_shadows(value: bool) -> None
```

<a id="unreal.FontOutlineSettings.outline_material"></a>

#### outline_material

```python
@property
def outline_material() -> Object
```

(Object):  [Read-Write] Optional material to apply to the outline

<a id="unreal.FontOutlineSettings.outline_material"></a>

#### outline_material

```python
@outline_material.setter
def outline_material(value: Object) -> None
```

<a id="unreal.FontOutlineSettings.outline_color"></a>

#### outline_color

```python
@property
def outline_color() -> LinearColor
```

(LinearColor):  [Read-Write] The color of the outline for any character in this font

<a id="unreal.FontOutlineSettings.outline_color"></a>

#### outline_color

```python
@outline_color.setter
def outline_color(value: LinearColor) -> None
```

<a id="unreal.ShapedTextOptions"></a>