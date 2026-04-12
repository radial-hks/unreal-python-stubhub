## CustomPoiEntityAtom Objects

```python
class CustomPoiEntityAtom(EntityAtomBase)
```

Custom Poi Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: CustomPoiEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``general_label_style`` (CustomPoiLabelContentStyle):  [Read-Write]
- ``label_content`` (Array[str]):  [Read-Write]
- ``label_style`` (CustomPoiLabelStyle):  [Read-Write]
- ``marker_activate_url`` (str):  [Read-Write]
- ``marker_normal_url`` (str):  [Read-Write]
- ``marker_offset`` (Vector2D):  [Read-Write]
- ``marker_size`` (Vector2D):  [Read-Write]
- ``marker_visible`` (bool):  [Read-Write]
- ``specific_label_style`` (Map[str, CustomPoiLabelContentStyle]):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.marker_normal_url"></a>

#### marker\_normal\_url

```python
@property
def marker_normal_url() -> str
```

(str):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.marker_normal_url"></a>

#### marker\_normal\_url

```python
@marker_normal_url.setter
def marker_normal_url(value: str) -> None
```

<a id="unreal.CustomPoiEntityAtom.marker_activate_url"></a>

#### marker\_activate\_url

```python
@property
def marker_activate_url() -> str
```

(str):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.marker_activate_url"></a>

#### marker\_activate\_url

```python
@marker_activate_url.setter
def marker_activate_url(value: str) -> None
```

<a id="unreal.CustomPoiEntityAtom.marker_visible"></a>

#### marker\_visible

```python
@property
def marker_visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.marker_visible"></a>

#### marker\_visible

```python
@marker_visible.setter
def marker_visible(value: bool) -> None
```

<a id="unreal.CustomPoiEntityAtom.marker_size"></a>

#### marker\_size

```python
@property
def marker_size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.marker_size"></a>

#### marker\_size

```python
@marker_size.setter
def marker_size(value: Vector2D) -> None
```

<a id="unreal.CustomPoiEntityAtom.marker_offset"></a>

#### marker\_offset

```python
@property
def marker_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.marker_offset"></a>

#### marker\_offset

```python
@marker_offset.setter
def marker_offset(value: Vector2D) -> None
```

<a id="unreal.CustomPoiEntityAtom.label_style"></a>

#### label\_style

```python
@property
def label_style() -> CustomPoiLabelStyle
```

(CustomPoiLabelStyle):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.label_style"></a>

#### label\_style

```python
@label_style.setter
def label_style(value: CustomPoiLabelStyle) -> None
```

<a id="unreal.CustomPoiEntityAtom.label_content"></a>

#### label\_content

```python
@property
def label_content() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.label_content"></a>

#### label\_content

```python
@label_content.setter
def label_content(value: Array[str]) -> None
```

<a id="unreal.CustomPoiEntityAtom.general_label_style"></a>

#### general\_label\_style

```python
@property
def general_label_style() -> CustomPoiLabelContentStyle
```

(CustomPoiLabelContentStyle):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.general_label_style"></a>

#### general\_label\_style

```python
@general_label_style.setter
def general_label_style(value: CustomPoiLabelContentStyle) -> None
```

<a id="unreal.CustomPoiEntityAtom.specific_label_style"></a>

#### specific\_label\_style

```python
@property
def specific_label_style() -> Map[str, CustomPoiLabelContentStyle]
```

(Map[str, CustomPoiLabelContentStyle]):  [Read-Write]

<a id="unreal.CustomPoiEntityAtom.specific_label_style"></a>

#### specific\_label\_style

```python
@specific_label_style.setter
def specific_label_style(value: Map[str, CustomPoiLabelContentStyle]) -> None
```

<a id="unreal.CustomPoiEntityAtom.setspecific_label_style"></a>

#### setspecific\_label\_style

```python
def setspecific_label_style(
        newspecific_label_style: Map[str, CustomPoiLabelContentStyle]) -> bool
```

x.setspecific_label_style(newspecific_label_style) -> bool
Setspecific Label Style

Args:
    newspecific_label_style (Map[str, CustomPoiLabelContentStyle]): 

Returns:
    bool:

<a id="unreal.CustomPoiEntityAtom.setmarker_visible"></a>

#### setmarker\_visible

```python
def setmarker_visible(visible: bool) -> bool
```

x.setmarker_visible(visible) -> bool
Setmarker Visible

Args:
    visible (bool): 

Returns:
    bool:

<a id="unreal.CustomPoiEntityAtom.setmarker_size"></a>

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

<a id="unreal.CustomPoiEntityAtom.setmarker_offset"></a>

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

<a id="unreal.CustomPoiEntityAtom.setmarker_normal_url"></a>

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

<a id="unreal.CustomPoiEntityAtom.setmarker_activate_url"></a>

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

<a id="unreal.CustomPoiEntityAtom.setlabel_style"></a>

#### setlabel\_style

```python
def setlabel_style(newlabel_style: CustomPoiLabelStyle) -> bool
```

x.setlabel_style(newlabel_style) -> bool
Setlabel Style

Args:
    newlabel_style (CustomPoiLabelStyle): 

Returns:
    bool:

<a id="unreal.CustomPoiEntityAtom.setlabel_content"></a>

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

<a id="unreal.CustomPoiEntityAtom.setgeneral_label_style"></a>

#### setgeneral\_label\_style

```python
def setgeneral_label_style(
        newgeneral_label_style: CustomPoiLabelContentStyle) -> bool
```

x.setgeneral_label_style(newgeneral_label_style) -> bool
Setgeneral Label Style

Args:
    newgeneral_label_style (CustomPoiLabelContentStyle): 

Returns:
    bool:

<a id="unreal.CustomPoiEntityPickAtom"></a>