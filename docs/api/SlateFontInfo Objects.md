## SlateFontInfo Objects

```python
class SlateFontInfo(StructBase)
```

A representation of a font in Slate.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateFontInfo.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``font_material`` (Object):  [Read-Write] The material to use when rendering
- ``font_object`` (Object):  [Read-Write] The font object (valid when used from UMG or a Slate widget style asset)
- ``force_monospaced`` (bool):  [Read-Write] Enable pseudo-monospaced font.
- ``letter_spacing`` (int32):  [Read-Write] The uniform spacing (or tracking) between all characters in the text.
- ``material_is_stencil`` (bool):  [Read-Write] When enabled, whole quads are filled by the material without automatically stenciling the text - this needs to be done within the material (using Font Signed Distance node).
- ``monospaced_width`` (float):  [Read-Write] The uniform width to apply to all characters when bForceMonospaced is enabled, proportional of the font Size.
- ``outline_settings`` (FontOutlineSettings):  [Read-Write] Settings for applying an outline to a font
- ``size`` (float):  [Read-Write] The font size is a measure in point values. The conversion of points to Slate Units is done at 96 DPI.
  So if you're using a tool like Photoshop to prototype layouts and UI mock ups, you can change the UMG Font settings
  to ensure that UMG font size is displayed in its 72 DPI equivalent, even if Slate will still use 96 DPI internally.
- ``skew_amount`` (float):  [Read-Write] A skew amount to apply to the text.
- ``typeface_font_name`` (Name):  [Read-Write] The name of the font to use from the default typeface (None will use the first entry)

<a id="unreal.SlateFontInfo.__init__"></a>

#### __init__

```python
def __init__(font_object: Object = None,
             font_material: Object = None,
             outline_settings: FontOutlineSettings = [
                 0, False, False, False, None,
                 [0.000000, 0.000000, 0.000000, 1.000000]
             ],
             typeface_font_name: Name = "None",
             size: float = 0.000000,
             letter_spacing: int = 0,
             skew_amount: float = 0.000000,
             force_monospaced: bool = False,
             material_is_stencil: bool = False,
             monospaced_width: float = 0.000000) -> None
```

<a id="unreal.SlateFontInfo.font_object"></a>

#### font_object

```python
@property
def font_object() -> Object
```

(Object):  [Read-Write] The font object (valid when used from UMG or a Slate widget style asset)

<a id="unreal.SlateFontInfo.font_object"></a>

#### font_object

```python
@font_object.setter
def font_object(value: Object) -> None
```

<a id="unreal.SlateFontInfo.font_material"></a>

#### font_material

```python
@property
def font_material() -> Object
```

(Object):  [Read-Write] The material to use when rendering

<a id="unreal.SlateFontInfo.font_material"></a>

#### font_material

```python
@font_material.setter
def font_material(value: Object) -> None
```

<a id="unreal.SlateFontInfo.outline_settings"></a>

#### outline_settings

```python
@property
def outline_settings() -> FontOutlineSettings
```

(FontOutlineSettings):  [Read-Write] Settings for applying an outline to a font

<a id="unreal.SlateFontInfo.outline_settings"></a>

#### outline_settings

```python
@outline_settings.setter
def outline_settings(value: FontOutlineSettings) -> None
```

<a id="unreal.SlateFontInfo.typeface_font_name"></a>

#### typeface_font_name

```python
@property
def typeface_font_name() -> Name
```

(Name):  [Read-Write] The name of the font to use from the default typeface (None will use the first entry)

<a id="unreal.SlateFontInfo.typeface_font_name"></a>

#### typeface_font_name

```python
@typeface_font_name.setter
def typeface_font_name(value: Name) -> None
```

<a id="unreal.SlateFontInfo.size"></a>

#### size

```python
@property
def size() -> float
```

(float):  [Read-Write] The font size is a measure in point values. The conversion of points to Slate Units is done at 96 DPI.
So if you're using a tool like Photoshop to prototype layouts and UI mock ups, you can change the UMG Font settings
to ensure that UMG font size is displayed in its 72 DPI equivalent, even if Slate will still use 96 DPI internally.

<a id="unreal.SlateFontInfo.size"></a>

#### size

```python
@size.setter
def size(value: float) -> None
```

<a id="unreal.SlateFontInfo.letter_spacing"></a>

#### letter_spacing

```python
@property
def letter_spacing() -> int
```

(int32):  [Read-Write] The uniform spacing (or tracking) between all characters in the text.

<a id="unreal.SlateFontInfo.letter_spacing"></a>

#### letter_spacing

```python
@letter_spacing.setter
def letter_spacing(value: int) -> None
```

<a id="unreal.SlateFontInfo.skew_amount"></a>

#### skew_amount

```python
@property
def skew_amount() -> float
```

(float):  [Read-Write] A skew amount to apply to the text.

<a id="unreal.SlateFontInfo.skew_amount"></a>

#### skew_amount

```python
@skew_amount.setter
def skew_amount(value: float) -> None
```

<a id="unreal.SlateFontInfo.force_monospaced"></a>

#### force_monospaced

```python
@property
def force_monospaced() -> bool
```

(bool):  [Read-Write] Enable pseudo-monospaced font.

<a id="unreal.SlateFontInfo.force_monospaced"></a>

#### force_monospaced

```python
@force_monospaced.setter
def force_monospaced(value: bool) -> None
```

<a id="unreal.SlateFontInfo.material_is_stencil"></a>

#### material_is_stencil

```python
@property
def material_is_stencil() -> bool
```

(bool):  [Read-Write] When enabled, whole quads are filled by the material without automatically stenciling the text - this needs to be done within the material (using Font Signed Distance node).

<a id="unreal.SlateFontInfo.material_is_stencil"></a>

#### material_is_stencil

```python
@material_is_stencil.setter
def material_is_stencil(value: bool) -> None
```

<a id="unreal.SlateFontInfo.monospaced_width"></a>

#### monospaced_width

```python
@property
def monospaced_width() -> float
```

(float):  [Read-Write] The uniform width to apply to all characters when bForceMonospaced is enabled, proportional of the font Size.

<a id="unreal.SlateFontInfo.monospaced_width"></a>

#### monospaced_width

```python
@monospaced_width.setter
def monospaced_width(value: float) -> None
```

<a id="unreal.FontOutlineSettings"></a>