## Text3DStyle Objects

```python
class Text3DStyle(StructBase)
```

Text 3DStyle

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: Text3DAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (str):  [Read-Write]
- ``outline`` (float):  [Read-Write] 样式(plain; reflection; metal)
- ``portrait`` (bool):  [Read-Write]
- ``space`` (float):  [Read-Write]
- ``text`` (str):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.Text3DStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(text: str = "",
             color: str = "",
             type: str = "",
             outline: float = 0.000000,
             portrait: bool = False,
             space: float = 0.000000) -> None
```

<a id="unreal.Text3DStyle.text"></a>

#### text

```python
@property
def text() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DStyle.text"></a>

#### text

```python
@text.setter
def text(value: str) -> None
```

<a id="unreal.Text3DStyle.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DStyle.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.Text3DStyle.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DStyle.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.Text3DStyle.outline"></a>

#### outline

```python
@property
def outline() -> float
```

(float):  [Read-Write] 样式(plain; reflection; metal)

<a id="unreal.Text3DStyle.outline"></a>

#### outline

```python
@outline.setter
def outline(value: float) -> None
```

<a id="unreal.Text3DStyle.portrait"></a>

#### portrait

```python
@property
def portrait() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Text3DStyle.portrait"></a>

#### portrait

```python
@portrait.setter
def portrait(value: bool) -> None
```

<a id="unreal.Text3DStyle.space"></a>

#### space

```python
@property
def space() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DStyle.space"></a>

#### space

```python
@space.setter
def space(value: float) -> None
```

<a id="unreal.CreateText3DParams"></a>