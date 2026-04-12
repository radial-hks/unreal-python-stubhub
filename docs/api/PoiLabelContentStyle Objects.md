## PoiLabelContentStyle Objects

```python
class PoiLabelContentStyle(StructBase)
```

Poi Label Content Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: PoiEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``font_color`` (str):  [Read-Write] Regular, Light, Bold, Italic and Bold italic
- ``font_family`` (str):  [Read-Write]
- ``font_size`` (int32):  [Read-Write]
- ``font_type_face`` (str):  [Read-Write] Roboto
- ``text_animation`` (str):  [Read-Write]
- ``text_auto_wrap`` (bool):  [Read-Write] Top, Center and Bottom
- ``text_height`` (int32):  [Read-Write]
- ``text_horizontal_align`` (str):  [Read-Write]
- ``text_padding`` (Margin):  [Read-Write]
- ``text_scroll_speed`` (int32):  [Read-Write] ToLeft, ToRight, ToUp and ToBottom
- ``text_vertical_align`` (str):  [Read-Write] Left, Center and Right
- ``text_width`` (int32):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(font_family: str = "",
             font_type_face: str = "",
             font_color: str = "",
             font_size: int = 0,
             text_width: int = 0,
             text_height: int = 0,
             text_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
             text_horizontal_align: str = "",
             text_vertical_align: str = "",
             text_auto_wrap: bool = False,
             text_animation: str = "",
             text_scroll_speed: int = 0) -> None
```

<a id="unreal.PoiLabelContentStyle.font_family"></a>

#### font\_family

```python
@property
def font_family() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.font_family"></a>

#### font\_family

```python
@font_family.setter
def font_family(value: str) -> None
```

<a id="unreal.PoiLabelContentStyle.font_type_face"></a>

#### font\_type\_face

```python
@property
def font_type_face() -> str
```

(str):  [Read-Write] Roboto

<a id="unreal.PoiLabelContentStyle.font_type_face"></a>

#### font\_type\_face

```python
@font_type_face.setter
def font_type_face(value: str) -> None
```

<a id="unreal.PoiLabelContentStyle.font_color"></a>

#### font\_color

```python
@property
def font_color() -> str
```

(str):  [Read-Write] Regular, Light, Bold, Italic and Bold italic

<a id="unreal.PoiLabelContentStyle.font_color"></a>

#### font\_color

```python
@font_color.setter
def font_color(value: str) -> None
```

<a id="unreal.PoiLabelContentStyle.font_size"></a>

#### font\_size

```python
@property
def font_size() -> int
```

(int32):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.font_size"></a>

#### font\_size

```python
@font_size.setter
def font_size(value: int) -> None
```

<a id="unreal.PoiLabelContentStyle.text_width"></a>

#### text\_width

```python
@property
def text_width() -> int
```

(int32):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.text_width"></a>

#### text\_width

```python
@text_width.setter
def text_width(value: int) -> None
```

<a id="unreal.PoiLabelContentStyle.text_height"></a>

#### text\_height

```python
@property
def text_height() -> int
```

(int32):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.text_height"></a>

#### text\_height

```python
@text_height.setter
def text_height(value: int) -> None
```

<a id="unreal.PoiLabelContentStyle.text_padding"></a>

#### text\_padding

```python
@property
def text_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.text_padding"></a>

#### text\_padding

```python
@text_padding.setter
def text_padding(value: Margin) -> None
```

<a id="unreal.PoiLabelContentStyle.text_horizontal_align"></a>

#### text\_horizontal\_align

```python
@property
def text_horizontal_align() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.text_horizontal_align"></a>

#### text\_horizontal\_align

```python
@text_horizontal_align.setter
def text_horizontal_align(value: str) -> None
```

<a id="unreal.PoiLabelContentStyle.text_vertical_align"></a>

#### text\_vertical\_align

```python
@property
def text_vertical_align() -> str
```

(str):  [Read-Write] Left, Center and Right

<a id="unreal.PoiLabelContentStyle.text_vertical_align"></a>

#### text\_vertical\_align

```python
@text_vertical_align.setter
def text_vertical_align(value: str) -> None
```

<a id="unreal.PoiLabelContentStyle.text_auto_wrap"></a>

#### text\_auto\_wrap

```python
@property
def text_auto_wrap() -> bool
```

(bool):  [Read-Write] Top, Center and Bottom

<a id="unreal.PoiLabelContentStyle.text_auto_wrap"></a>

#### text\_auto\_wrap

```python
@text_auto_wrap.setter
def text_auto_wrap(value: bool) -> None
```

<a id="unreal.PoiLabelContentStyle.text_animation"></a>

#### text\_animation

```python
@property
def text_animation() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiLabelContentStyle.text_animation"></a>

#### text\_animation

```python
@text_animation.setter
def text_animation(value: str) -> None
```

<a id="unreal.PoiLabelContentStyle.text_scroll_speed"></a>

#### text\_scroll\_speed

```python
@property
def text_scroll_speed() -> int
```

(int32):  [Read-Write] ToLeft, ToRight, ToUp and ToBottom

<a id="unreal.PoiLabelContentStyle.text_scroll_speed"></a>

#### text\_scroll\_speed

```python
@text_scroll_speed.setter
def text_scroll_speed(value: int) -> None
```

<a id="unreal.PointCloudData"></a>