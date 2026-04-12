## CustomPoiLabelContentStyle Objects

```python
class CustomPoiLabelContentStyle(StructBase)
```

Custom Poi Label Content Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: CustomPoiEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation`` (str):  [Read-Write]
- ``auto_wrap`` (int32):  [Read-Write] left, center and right
- ``color`` (str):  [Read-Write]
- ``font_size`` (int32):  [Read-Write]
- ``height`` (int32):  [Read-Write]
- ``padding`` (str):  [Read-Write]
- ``scroll_speed`` (int32):  [Read-Write] leftToRight, rightToLeft, topToBottom and bottomToTop
- ``text_align`` (str):  [Read-Write]
- ``width`` (int32):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int = 0,
             height: int = 0,
             font_size: int = 0,
             padding: str = "",
             color: str = "",
             text_align: str = "",
             auto_wrap: int = 0,
             animation: str = "",
             scroll_speed: int = 0) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.width"></a>

#### width

```python
@property
def width() -> int
```

(int32):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.width"></a>

#### width

```python
@width.setter
def width(value: int) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.height"></a>

#### height

```python
@property
def height() -> int
```

(int32):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.height"></a>

#### height

```python
@height.setter
def height(value: int) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.font_size"></a>

#### font\_size

```python
@property
def font_size() -> int
```

(int32):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.font_size"></a>

#### font\_size

```python
@font_size.setter
def font_size(value: int) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.padding"></a>

#### padding

```python
@property
def padding() -> str
```

(str):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.padding"></a>

#### padding

```python
@padding.setter
def padding(value: str) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.text_align"></a>

#### text\_align

```python
@property
def text_align() -> str
```

(str):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.text_align"></a>

#### text\_align

```python
@text_align.setter
def text_align(value: str) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.auto_wrap"></a>

#### auto\_wrap

```python
@property
def auto_wrap() -> int
```

(int32):  [Read-Write] left, center and right

<a id="unreal.CustomPoiLabelContentStyle.auto_wrap"></a>

#### auto\_wrap

```python
@auto_wrap.setter
def auto_wrap(value: int) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.animation"></a>

#### animation

```python
@property
def animation() -> str
```

(str):  [Read-Write]

<a id="unreal.CustomPoiLabelContentStyle.animation"></a>

#### animation

```python
@animation.setter
def animation(value: str) -> None
```

<a id="unreal.CustomPoiLabelContentStyle.scroll_speed"></a>

#### scroll\_speed

```python
@property
def scroll_speed() -> int
```

(int32):  [Read-Write] leftToRight, rightToLeft, topToBottom and bottomToTop

<a id="unreal.CustomPoiLabelContentStyle.scroll_speed"></a>

#### scroll\_speed

```python
@scroll_speed.setter
def scroll_speed(value: int) -> None
```

<a id="unreal.HighlightAreaPosition"></a>