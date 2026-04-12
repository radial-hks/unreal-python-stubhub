## Text3DEntityAtom Objects

```python
class Text3DEntityAtom(EntityAtomBase)
```

Text 3DEntity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: Text3DEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounce`` (float):  [Read-Write]
- ``boundary`` (Array[Vector2D]):  [Read-Write]
- ``color`` (str):  [Read-Write]
- ``draw_debug_boundary`` (bool):  [Read-Write]
- ``face_to_camera`` (bool):  [Read-Write]
- ``outline`` (float):  [Read-Write] 样式(plain; reflection; metal)
- ``portrait`` (bool):  [Read-Write]
- ``radius`` (float):  [Read-Write] 边界预设形状(circle; square)
- ``shape`` (str):  [Read-Write]
- ``space`` (float):  [Read-Write]
- ``text`` (str):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.Text3DEntityAtom.text"></a>

#### text

```python
@property
def text() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DEntityAtom.text"></a>

#### text

```python
@text.setter
def text(value: str) -> None
```

<a id="unreal.Text3DEntityAtom.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DEntityAtom.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.Text3DEntityAtom.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DEntityAtom.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.Text3DEntityAtom.outline"></a>

#### outline

```python
@property
def outline() -> float
```

(float):  [Read-Write] 样式(plain; reflection; metal)

<a id="unreal.Text3DEntityAtom.outline"></a>

#### outline

```python
@outline.setter
def outline(value: float) -> None
```

<a id="unreal.Text3DEntityAtom.portrait"></a>

#### portrait

```python
@property
def portrait() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Text3DEntityAtom.portrait"></a>

#### portrait

```python
@portrait.setter
def portrait(value: bool) -> None
```

<a id="unreal.Text3DEntityAtom.space"></a>

#### space

```python
@property
def space() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DEntityAtom.space"></a>

#### space

```python
@space.setter
def space(value: float) -> None
```

<a id="unreal.Text3DEntityAtom.bounce"></a>

#### bounce

```python
@property
def bounce() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DEntityAtom.bounce"></a>

#### bounce

```python
@bounce.setter
def bounce(value: float) -> None
```

<a id="unreal.Text3DEntityAtom.face_to_camera"></a>

#### face\_to\_camera

```python
@property
def face_to_camera() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Text3DEntityAtom.face_to_camera"></a>

#### face\_to\_camera

```python
@face_to_camera.setter
def face_to_camera(value: bool) -> None
```

<a id="unreal.Text3DEntityAtom.boundary"></a>

#### boundary

```python
@property
def boundary() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.Text3DEntityAtom.boundary"></a>

#### boundary

```python
@boundary.setter
def boundary(value: Array[Vector2D]) -> None
```

<a id="unreal.Text3DEntityAtom.shape"></a>

#### shape

```python
@property
def shape() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DEntityAtom.shape"></a>

#### shape

```python
@shape.setter
def shape(value: str) -> None
```

<a id="unreal.Text3DEntityAtom.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write] 边界预设形状(circle; square)

<a id="unreal.Text3DEntityAtom.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.Text3DEntityAtom.draw_debug_boundary"></a>

#### draw\_debug\_boundary

```python
@property
def draw_debug_boundary() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Text3DEntityAtom.draw_debug_boundary"></a>

#### draw\_debug\_boundary

```python
@draw_debug_boundary.setter
def draw_debug_boundary(value: bool) -> None
```

<a id="unreal.Text3DEntityAtom.set_type"></a>

#### set\_type

```python
def set_type(new_type: str) -> bool
```

x.set_type(new_type) -> bool
Set Type

Args:
    new_type (str): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_text"></a>

#### set\_text

```python
def set_text(new_text: str) -> bool
```

x.set_text(new_text) -> bool
UFUNCTION(BlueprintCallable, Category = "Text3DEntityAtom")
               bool SetPointEntityEid(const int64& NewPointEntityEid);

Args:
    new_text (str): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_space"></a>

#### set\_space

```python
def set_space(new_space: float) -> bool
```

x.set_space(new_space) -> bool
Set Space

Args:
    new_space (float): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_shape"></a>

#### set\_shape

```python
def set_shape(new_shape: str) -> bool
```

x.set_shape(new_shape) -> bool
Set Shape

Args:
    new_shape (str): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_radius"></a>

#### set\_radius

```python
def set_radius(new_radius: float) -> bool
```

x.set_radius(new_radius) -> bool
Set Radius

Args:
    new_radius (float): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_portrait"></a>

#### set\_portrait

```python
def set_portrait(new_portrait: bool) -> bool
```

x.set_portrait(new_portrait) -> bool
Set Portrait

Args:
    new_portrait (bool): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_outline"></a>

#### set\_outline

```python
def set_outline(new_outline: float) -> bool
```

x.set_outline(new_outline) -> bool
Set Outline

Args:
    new_outline (float): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_color"></a>

#### set\_color

```python
def set_color(new_color: str) -> bool
```

x.set_color(new_color) -> bool
Set Color

Args:
    new_color (str): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_boundary"></a>

#### set\_boundary

```python
def set_boundary(new_boundary: Array[Vector2D]) -> bool
```

x.set_boundary(new_boundary) -> bool
Set Boundary

Args:
    new_boundary (Array[Vector2D]): 

Returns:
    bool:

<a id="unreal.Text3DEntityAtom.set_bounce"></a>

#### set\_bounce

```python
def set_bounce(new_bounce: float) -> bool
```

x.set_bounce(new_bounce) -> bool
Set Bounce

Args:
    new_bounce (float): 

Returns:
    bool:

<a id="unreal.TransformAtom2D"></a>