## PoiEntityAtom Objects

```python
class PoiEntityAtom(EntityAtomBase)
```

Poi Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: PoiEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``general_label_style`` (PoiLabelContentStyle):  [Read-Write]
- ``label_bg_image_url`` (str):  [Read-Write] Image, HtmlToImage, RmlUI and Web
- ``label_bg_offset`` (Vector2D):  [Read-Write]
- ``label_bg_size`` (Vector2D):  [Read-Write]
- ``label_content`` (Array[str]):  [Read-Write]
- ``label_content_auto_wrap`` (bool):  [Read-Write]
- ``label_content_justification`` (str):  [Read-Write]
- ``label_content_offset`` (Vector2D):  [Read-Write]
- ``label_contents`` (Array[str]):  [Read-Write]
- ``label_top`` (bool):  [Read-Write]
- ``label_ui`` (str):  [Read-Write]
- ``label_visible`` (bool):  [Read-Write]
- ``marker_activate_url`` (str):  [Read-Write]
- ``marker_normal_url`` (str):  [Read-Write] Image and HtmlToImage
- ``marker_offset`` (Vector2D):  [Read-Write]
- ``marker_size`` (Vector2D):  [Read-Write]
- ``marker_ui`` (str):  [Read-Write]
- ``marker_visible`` (bool):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "PoiEntityAtom")
                 int CoordZRef = 0;
- ``scroll_policy`` (str):  [Read-Write]
- ``scroll_speed`` (float):  [Read-Write]
- ``specific_label_style`` (Map[str, PoiLabelContentStyle]):  [Read-Write]
- ``text_box_width`` (float):  [Read-Write]

<a id="unreal.PoiEntityAtom.marker_visible"></a>

#### marker\_visible

```python
@property
def marker_visible() -> bool
```

(bool):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "PoiEntityAtom")
               int CoordZRef = 0;

<a id="unreal.PoiEntityAtom.marker_visible"></a>

#### marker\_visible

```python
@marker_visible.setter
def marker_visible(value: bool) -> None
```

<a id="unreal.PoiEntityAtom.marker_ui"></a>

#### marker\_ui

```python
@property
def marker_ui() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiEntityAtom.marker_ui"></a>

#### marker\_ui

```python
@marker_ui.setter
def marker_ui(value: str) -> None
```

<a id="unreal.PoiEntityAtom.marker_normal_url"></a>

#### marker\_normal\_url

```python
@property
def marker_normal_url() -> str
```

(str):  [Read-Write] Image and HtmlToImage

<a id="unreal.PoiEntityAtom.marker_normal_url"></a>

#### marker\_normal\_url

```python
@marker_normal_url.setter
def marker_normal_url(value: str) -> None
```

<a id="unreal.PoiEntityAtom.marker_activate_url"></a>

#### marker\_activate\_url

```python
@property
def marker_activate_url() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiEntityAtom.marker_activate_url"></a>

#### marker\_activate\_url

```python
@marker_activate_url.setter
def marker_activate_url(value: str) -> None
```

<a id="unreal.PoiEntityAtom.marker_size"></a>

#### marker\_size

```python
@property
def marker_size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PoiEntityAtom.marker_size"></a>

#### marker\_size

```python
@marker_size.setter
def marker_size(value: Vector2D) -> None
```

<a id="unreal.PoiEntityAtom.marker_offset"></a>

#### marker\_offset

```python
@property
def marker_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PoiEntityAtom.marker_offset"></a>

#### marker\_offset

```python
@marker_offset.setter
def marker_offset(value: Vector2D) -> None
```

<a id="unreal.PoiEntityAtom.label_visible"></a>

#### label\_visible

```python
@property
def label_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_visible"></a>

#### label\_visible

```python
@label_visible.setter
def label_visible(value: bool) -> None
```

<a id="unreal.PoiEntityAtom.label_top"></a>

#### label\_top

```python
@property
def label_top() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_top"></a>

#### label\_top

```python
@label_top.setter
def label_top(value: bool) -> None
```

<a id="unreal.PoiEntityAtom.label_ui"></a>

#### label\_ui

```python
@property
def label_ui() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_ui"></a>

#### label\_ui

```python
@label_ui.setter
def label_ui(value: str) -> None
```

<a id="unreal.PoiEntityAtom.label_bg_image_url"></a>

#### label\_bg\_image\_url

```python
@property
def label_bg_image_url() -> str
```

(str):  [Read-Write] Image, HtmlToImage, RmlUI and Web

<a id="unreal.PoiEntityAtom.label_bg_image_url"></a>

#### label\_bg\_image\_url

```python
@label_bg_image_url.setter
def label_bg_image_url(value: str) -> None
```

<a id="unreal.PoiEntityAtom.label_bg_size"></a>

#### label\_bg\_size

```python
@property
def label_bg_size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_bg_size"></a>

#### label\_bg\_size

```python
@label_bg_size.setter
def label_bg_size(value: Vector2D) -> None
```

<a id="unreal.PoiEntityAtom.label_bg_offset"></a>

#### label\_bg\_offset

```python
@property
def label_bg_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_bg_offset"></a>

#### label\_bg\_offset

```python
@label_bg_offset.setter
def label_bg_offset(value: Vector2D) -> None
```

<a id="unreal.PoiEntityAtom.label_content"></a>

#### label\_content

```python
@property
def label_content() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_content"></a>

#### label\_content

```python
@label_content.setter
def label_content(value: Array[str]) -> None
```

<a id="unreal.PoiEntityAtom.label_content_justification"></a>

#### label\_content\_justification

```python
@property
def label_content_justification() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_content_justification"></a>

#### label\_content\_justification

```python
@label_content_justification.setter
def label_content_justification(value: str) -> None
```

<a id="unreal.PoiEntityAtom.label_content_auto_wrap"></a>

#### label\_content\_auto\_wrap

```python
@property
def label_content_auto_wrap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_content_auto_wrap"></a>

#### label\_content\_auto\_wrap

```python
@label_content_auto_wrap.setter
def label_content_auto_wrap(value: bool) -> None
```

<a id="unreal.PoiEntityAtom.scroll_policy"></a>

#### scroll\_policy

```python
@property
def scroll_policy() -> str
```

(str):  [Read-Write]

<a id="unreal.PoiEntityAtom.scroll_policy"></a>

#### scroll\_policy

```python
@scroll_policy.setter
def scroll_policy(value: str) -> None
```

<a id="unreal.PoiEntityAtom.scroll_speed"></a>

#### scroll\_speed

```python
@property
def scroll_speed() -> float
```

(float):  [Read-Write]

<a id="unreal.PoiEntityAtom.scroll_speed"></a>

#### scroll\_speed

```python
@scroll_speed.setter
def scroll_speed(value: float) -> None
```

<a id="unreal.PoiEntityAtom.label_content_offset"></a>

#### label\_content\_offset

```python
@property
def label_content_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_content_offset"></a>

#### label\_content\_offset

```python
@label_content_offset.setter
def label_content_offset(value: Vector2D) -> None
```

<a id="unreal.PoiEntityAtom.text_box_width"></a>

#### text\_box\_width

```python
@property
def text_box_width() -> float
```

(float):  [Read-Write]

<a id="unreal.PoiEntityAtom.text_box_width"></a>

#### text\_box\_width

```python
@text_box_width.setter
def text_box_width(value: float) -> None
```

<a id="unreal.PoiEntityAtom.label_contents"></a>

#### label\_contents

```python
@property
def label_contents() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.PoiEntityAtom.label_contents"></a>

#### label\_contents

```python
@label_contents.setter
def label_contents(value: Array[str]) -> None
```

<a id="unreal.PoiEntityAtom.general_label_style"></a>

#### general\_label\_style

```python
@property
def general_label_style() -> PoiLabelContentStyle
```

(PoiLabelContentStyle):  [Read-Write]

<a id="unreal.PoiEntityAtom.general_label_style"></a>

#### general\_label\_style

```python
@general_label_style.setter
def general_label_style(value: PoiLabelContentStyle) -> None
```

<a id="unreal.PoiEntityAtom.specific_label_style"></a>

#### specific\_label\_style

```python
@property
def specific_label_style() -> Map[str, PoiLabelContentStyle]
```

(Map[str, PoiLabelContentStyle]):  [Read-Write]

<a id="unreal.PoiEntityAtom.specific_label_style"></a>

#### specific\_label\_style

```python
@specific_label_style.setter
def specific_label_style(value: Map[str, PoiLabelContentStyle]) -> None
```

<a id="unreal.PoiEntityAtom.set_text_box_width"></a>

#### set\_text\_box\_width

```python
def set_text_box_width(box_width: float) -> bool
```

x.set_text_box_width(box_width) -> bool
Set Text Box Width

Args:
    box_width (float): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setspecific_label_style"></a>

#### setspecific\_label\_style

```python
def setspecific_label_style(
        newspecific_label_style: Map[str, PoiLabelContentStyle]) -> bool
```

x.setspecific_label_style(newspecific_label_style) -> bool
Setspecific Label Style

Args:
    newspecific_label_style (Map[str, PoiLabelContentStyle]): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.set_scroll_speed"></a>

#### set\_scroll\_speed

```python
def set_scroll_speed(speed: float) -> bool
```

x.set_scroll_speed(speed) -> bool
Set Scroll Speed

Args:
    speed (float): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.set_scroll_policy"></a>

#### set\_scroll\_policy

```python
def set_scroll_policy(policy: str) -> bool
```

x.set_scroll_policy(policy) -> bool
Set Scroll Policy

Args:
    policy (str): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setmarker_visible"></a>

#### setmarker\_visible

```python
def setmarker_visible(visible: bool) -> bool
```

x.setmarker_visible(visible) -> bool
UFUNCTION(BlueprintCallable, Category = "PoiEntityAtom")
               bool Set_CoordZRef(const int& NewCoordZRef);

Args:
    visible (bool): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setmarker_ui"></a>

#### setmarker\_ui

```python
def setmarker_ui(newmarker_ui: str) -> bool
```

x.setmarker_ui(newmarker_ui) -> bool
Setmarker Ui

Args:
    newmarker_ui (str): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setmarker_size"></a>

#### setmarker\_size

```python
def setmarker_size(newmarker_size: Vector2D) -> bool
```

x.setmarker_size(newmarker_size) -> bool
Setmarker Size

Args:
    newmarker_size (Vector2D): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setmarker_offset"></a>

#### setmarker\_offset

```python
def setmarker_offset(newmarker_offset: Vector2D) -> bool
```

x.setmarker_offset(newmarker_offset) -> bool
Setmarker Offset

Args:
    newmarker_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setmarker_normal_url"></a>

#### setmarker\_normal\_url

```python
def setmarker_normal_url(newmarker_normal_url: str) -> bool
```

x.setmarker_normal_url(newmarker_normal_url) -> bool
Setmarker Normal Url

Args:
    newmarker_normal_url (str): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setmarker_activate_url"></a>

#### setmarker\_activate\_url

```python
def setmarker_activate_url(newmarker_activate_url: str) -> bool
```

x.setmarker_activate_url(newmarker_activate_url) -> bool
Setmarker Activate Url

Args:
    newmarker_activate_url (str): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_visible"></a>

#### setlabel\_visible

```python
def setlabel_visible(visible: bool) -> bool
```

x.setlabel_visible(visible) -> bool
Setlabel Visible

Args:
    visible (bool): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_top"></a>

#### setlabel\_top

```python
def setlabel_top(top: bool) -> bool
```

x.setlabel_top(top) -> bool
Setlabel Top

Args:
    top (bool): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_ui"></a>

#### setlabel\_ui

```python
def setlabel_ui(newlabel_ui: str) -> bool
```

x.setlabel_ui(newlabel_ui) -> bool
Setlabel Ui

Args:
    newlabel_ui (str): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_contents"></a>

#### setlabel\_contents

```python
def setlabel_contents(newlabel_contents: Array[str]) -> bool
```

x.setlabel_contents(newlabel_contents) -> bool
Setlabel Contents

Args:
    newlabel_contents (Array[str]): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_content_justification"></a>

#### setlabel\_content\_justification

```python
def setlabel_content_justification(
        newlabel_content_justification: str) -> bool
```

x.setlabel_content_justification(newlabel_content_justification) -> bool
Setlabel Content Justification

Args:
    newlabel_content_justification (str): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_content_autowrap"></a>

#### setlabel\_content\_autowrap

```python
def setlabel_content_autowrap(auto_wrap: bool) -> bool
```

x.setlabel_content_autowrap(auto_wrap) -> bool
Setlabel Content Autowrap

Args:
    auto_wrap (bool): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_content"></a>

#### setlabel\_content

```python
def setlabel_content(newlabel_content: Array[str]) -> bool
```

x.setlabel_content(newlabel_content) -> bool
Setlabel Content

Args:
    newlabel_content (Array[str]): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_bg_size"></a>

#### setlabel\_bg\_size

```python
def setlabel_bg_size(newlabel_bg_size: Vector2D) -> bool
```

x.setlabel_bg_size(newlabel_bg_size) -> bool
Setlabel Bg Size

Args:
    newlabel_bg_size (Vector2D): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_bg_offset"></a>

#### setlabel\_bg\_offset

```python
def setlabel_bg_offset(newlabel_bg_offset: Vector2D) -> bool
```

x.setlabel_bg_offset(newlabel_bg_offset) -> bool
Setlabel Bg Offset

Args:
    newlabel_bg_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setlabel_bg_image_url"></a>

#### setlabel\_bg\_image\_url

```python
def setlabel_bg_image_url(newlabel_bg_image_url: str) -> bool
```

x.setlabel_bg_image_url(newlabel_bg_image_url) -> bool
Setlabel Bg Image Url

Args:
    newlabel_bg_image_url (str): 

Returns:
    bool:

<a id="unreal.PoiEntityAtom.setgeneral_label_style"></a>

#### setgeneral\_label\_style

```python
def setgeneral_label_style(
        newgeneral_label_style: PoiLabelContentStyle) -> bool
```

x.setgeneral_label_style(newgeneral_label_style) -> bool
Setgeneral Label Style

Args:
    newgeneral_label_style (PoiLabelContentStyle): 

Returns:
    bool:

<a id="unreal.CustomPoiEntityAtom"></a>