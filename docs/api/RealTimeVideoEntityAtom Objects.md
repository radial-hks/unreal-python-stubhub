## RealTimeVideoEntityAtom Objects

```python
class RealTimeVideoEntityAtom(EntityAtomBase)
```

Real Time Video Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: RealTimeVideoEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bg_overlap`` (str):  [Read-Write]
- ``bg_padding`` (Array[int32]):  [Read-Write]
- ``bg_url`` (str):  [Read-Write]
- ``bokeh`` (float):  [Read-Write]
- ``btn_activate_url`` (str):  [Read-Write]
- ``btn_normal_url`` (str):  [Read-Write]
- ``btn_offset`` (Vector2D):  [Read-Write]
- ``btn_size`` (Vector2D):  [Read-Write]
- ``corner_shift`` (Array[Vector2D]):  [Read-Write]
- ``label_content`` (Array[str]):  [Read-Write]
- ``label_content_auto_wrap`` (bool):  [Read-Write]
- ``label_content_justification`` (str):  [Read-Write]
- ``label_offset`` (Vector2D):  [Read-Write]
- ``label_size`` (Vector2D):  [Read-Write]
- ``offset`` (Vector2D):  [Read-Write]
- ``overlap_order`` (int32):  [Read-Write]
- ``resolution`` (Vector2D):  [Read-Write]
- ``state`` (str):  [Read-Write]
- ``url`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RealTimeVideoEntityAtom")
                 int CoordZRef = 0;

<a id="unreal.RealTimeVideoEntityAtom.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RealTimeVideoEntityAtom")
               int CoordZRef = 0;

<a id="unreal.RealTimeVideoEntityAtom.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.resolution"></a>

#### resolution

```python
@property
def resolution() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: Vector2D) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.state"></a>

#### state

```python
@property
def state() -> str
```

(str):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.state"></a>

#### state

```python
@state.setter
def state(value: str) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.overlap_order"></a>

#### overlap\_order

```python
@property
def overlap_order() -> int
```

(int32):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.overlap_order"></a>

#### overlap\_order

```python
@overlap_order.setter
def overlap_order(value: int) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.bokeh"></a>

#### bokeh

```python
@property
def bokeh() -> float
```

(float):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.bokeh"></a>

#### bokeh

```python
@bokeh.setter
def bokeh(value: float) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.corner_shift"></a>

#### corner\_shift

```python
@property
def corner_shift() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.corner_shift"></a>

#### corner\_shift

```python
@corner_shift.setter
def corner_shift(value: Array[Vector2D]) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.bg_url"></a>

#### bg\_url

```python
@property
def bg_url() -> str
```

(str):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.bg_url"></a>

#### bg\_url

```python
@bg_url.setter
def bg_url(value: str) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.bg_padding"></a>

#### bg\_padding

```python
@property
def bg_padding() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.bg_padding"></a>

#### bg\_padding

```python
@bg_padding.setter
def bg_padding(value: Array[int]) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.bg_overlap"></a>

#### bg\_overlap

```python
@property
def bg_overlap() -> str
```

(str):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.bg_overlap"></a>

#### bg\_overlap

```python
@bg_overlap.setter
def bg_overlap(value: str) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.label_content"></a>

#### label\_content

```python
@property
def label_content() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.label_content"></a>

#### label\_content

```python
@label_content.setter
def label_content(value: Array[str]) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.label_offset"></a>

#### label\_offset

```python
@property
def label_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.label_offset"></a>

#### label\_offset

```python
@label_offset.setter
def label_offset(value: Vector2D) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.label_size"></a>

#### label\_size

```python
@property
def label_size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.label_size"></a>

#### label\_size

```python
@label_size.setter
def label_size(value: Vector2D) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.label_content_justification"></a>

#### label\_content\_justification

```python
@property
def label_content_justification() -> str
```

(str):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.label_content_justification"></a>

#### label\_content\_justification

```python
@label_content_justification.setter
def label_content_justification(value: str) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.label_content_auto_wrap"></a>

#### label\_content\_auto\_wrap

```python
@property
def label_content_auto_wrap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.label_content_auto_wrap"></a>

#### label\_content\_auto\_wrap

```python
@label_content_auto_wrap.setter
def label_content_auto_wrap(value: bool) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.btn_normal_url"></a>

#### btn\_normal\_url

```python
@property
def btn_normal_url() -> str
```

(str):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.btn_normal_url"></a>

#### btn\_normal\_url

```python
@btn_normal_url.setter
def btn_normal_url(value: str) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.btn_activate_url"></a>

#### btn\_activate\_url

```python
@property
def btn_activate_url() -> str
```

(str):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.btn_activate_url"></a>

#### btn\_activate\_url

```python
@btn_activate_url.setter
def btn_activate_url(value: str) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.btn_offset"></a>

#### btn\_offset

```python
@property
def btn_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.btn_offset"></a>

#### btn\_offset

```python
@btn_offset.setter
def btn_offset(value: Vector2D) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.btn_size"></a>

#### btn\_size

```python
@property
def btn_size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RealTimeVideoEntityAtom.btn_size"></a>

#### btn\_size

```python
@btn_size.setter
def btn_size(value: Vector2D) -> None
```

<a id="unreal.RealTimeVideoEntityAtom.set_url"></a>

#### set\_url

```python
def set_url(newurl: str) -> bool
```

x.set_url(newurl) -> bool
UFUNCTION(BlueprintCallable, Category = "RealTimeVideoEntityAtom")
               bool Set_CoordZRef(const int& NewCoordZRef);

Args:
    newurl (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_state"></a>

#### set\_state

```python
def set_state(newstate: str) -> bool
```

x.set_state(newstate) -> bool
Set State

Args:
    newstate (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_resolution"></a>

#### set\_resolution

```python
def set_resolution(new_resolution: Vector2D) -> bool
```

x.set_resolution(new_resolution) -> bool
Set Resolution

Args:
    new_resolution (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_overlap_order"></a>

#### set\_overlap\_order

```python
def set_overlap_order(newoverlap_order: int) -> bool
```

x.set_overlap_order(newoverlap_order) -> bool
Set Overlap Order

Args:
    newoverlap_order (int32): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_offset"></a>

#### set\_offset

```python
def set_offset(newoffset: Vector2D) -> bool
```

x.set_offset(newoffset) -> bool
Set Offset

Args:
    newoffset (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_label_size"></a>

#### set\_label\_size

```python
def set_label_size(new_label_size: Vector2D) -> bool
```

x.set_label_size(new_label_size) -> bool
Set Label Size

Args:
    new_label_size (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_label_offset"></a>

#### set\_label\_offset

```python
def set_label_offset(new_label_offset: Vector2D) -> bool
```

x.set_label_offset(new_label_offset) -> bool
Set Label Offset

Args:
    new_label_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_label_content_justification"></a>

#### set\_label\_content\_justification

```python
def set_label_content_justification(
        new_label_content_justification: str) -> bool
```

x.set_label_content_justification(new_label_content_justification) -> bool
Set Label Content Justification

Args:
    new_label_content_justification (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_label_content_auto_wrap"></a>

#### set\_label\_content\_auto\_wrap

```python
def set_label_content_auto_wrap(new_auto_wrap: bool) -> bool
```

x.set_label_content_auto_wrap(new_auto_wrap) -> bool
Set Label Content Auto Wrap

Args:
    new_auto_wrap (bool): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_label_content"></a>

#### set\_label\_content

```python
def set_label_content(new_label_content: Array[str]) -> bool
```

x.set_label_content(new_label_content) -> bool
Set Label Content

Args:
    new_label_content (Array[str]): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_conrner_shift"></a>

#### set\_conrner\_shift

```python
def set_conrner_shift(new_conrner_shift: Array[Vector2D]) -> bool
```

x.set_conrner_shift(new_conrner_shift) -> bool
Set Conrner Shift

Args:
    new_conrner_shift (Array[Vector2D]): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_btn_size"></a>

#### set\_btn\_size

```python
def set_btn_size(new_btn_size: Vector2D) -> bool
```

x.set_btn_size(new_btn_size) -> bool
Set Btn Size

Args:
    new_btn_size (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_btn_offset"></a>

#### set\_btn\_offset

```python
def set_btn_offset(new_btn_offset: Vector2D) -> bool
```

x.set_btn_offset(new_btn_offset) -> bool
Set Btn Offset

Args:
    new_btn_offset (Vector2D): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_btn_normal_url"></a>

#### set\_btn\_normal\_url

```python
def set_btn_normal_url(new_btn_normal_url: str) -> bool
```

x.set_btn_normal_url(new_btn_normal_url) -> bool
Set Btn Normal Url

Args:
    new_btn_normal_url (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_btn_activate_url"></a>

#### set\_btn\_activate\_url

```python
def set_btn_activate_url(new_btn_activate_url: str) -> bool
```

x.set_btn_activate_url(new_btn_activate_url) -> bool
Set Btn Activate Url

Args:
    new_btn_activate_url (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_bokeh"></a>

#### set\_bokeh

```python
def set_bokeh(new_bokeh: float) -> bool
```

x.set_bokeh(new_bokeh) -> bool
Set Bokeh

Args:
    new_bokeh (float): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_bg_url"></a>

#### set\_bg\_url

```python
def set_bg_url(new_bg_url: str) -> bool
```

x.set_bg_url(new_bg_url) -> bool
Set Bg Url

Args:
    new_bg_url (str): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_bg_padding"></a>

#### set\_bg\_padding

```python
def set_bg_padding(new_bg_padding: Array[int]) -> bool
```

x.set_bg_padding(new_bg_padding) -> bool
Set Bg Padding

Args:
    new_bg_padding (Array[int32]): 

Returns:
    bool:

<a id="unreal.RealTimeVideoEntityAtom.set_bg_overlap"></a>

#### set\_bg\_overlap

```python
def set_bg_overlap(new_bg_overlap: str) -> bool
```

x.set_bg_overlap(new_bg_overlap) -> bool
Set Bg Overlap

Args:
    new_bg_overlap (str): 

Returns:
    bool:

<a id="unreal.RoadHeatMapEntityAtom"></a>