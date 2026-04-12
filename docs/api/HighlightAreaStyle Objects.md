## HighlightAreaStyle Objects

```python
class HighlightAreaStyle(StructBase)
```

Highlight Area Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HighlightAreaAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exterior_brightness`` (float):  [Read-Write]
- ``exterior_color`` (str):  [Read-Write]
- ``exterior_contrast`` (float):  [Read-Write]
- ``exterior_outline_color`` (str):  [Read-Write]
- ``exterior_saturation`` (float):  [Read-Write]
- ``interior_color`` (str):  [Read-Write]

<a id="unreal.HighlightAreaStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(interior_color: str = "",
             exterior_color: str = "",
             exterior_outline_color: str = "",
             exterior_saturation: float = 0.000000,
             exterior_brightness: float = 0.000000,
             exterior_contrast: float = 0.000000) -> None
```

<a id="unreal.HighlightAreaStyle.interior_color"></a>

#### interior\_color

```python
@property
def interior_color() -> str
```

(str):  [Read-Write]

<a id="unreal.HighlightAreaStyle.interior_color"></a>

#### interior\_color

```python
@interior_color.setter
def interior_color(value: str) -> None
```

<a id="unreal.HighlightAreaStyle.exterior_color"></a>

#### exterior\_color

```python
@property
def exterior_color() -> str
```

(str):  [Read-Write]

<a id="unreal.HighlightAreaStyle.exterior_color"></a>

#### exterior\_color

```python
@exterior_color.setter
def exterior_color(value: str) -> None
```

<a id="unreal.HighlightAreaStyle.exterior_outline_color"></a>

#### exterior\_outline\_color

```python
@property
def exterior_outline_color() -> str
```

(str):  [Read-Write]

<a id="unreal.HighlightAreaStyle.exterior_outline_color"></a>

#### exterior\_outline\_color

```python
@exterior_outline_color.setter
def exterior_outline_color(value: str) -> None
```

<a id="unreal.HighlightAreaStyle.exterior_saturation"></a>

#### exterior\_saturation

```python
@property
def exterior_saturation() -> float
```

(float):  [Read-Write]

<a id="unreal.HighlightAreaStyle.exterior_saturation"></a>

#### exterior\_saturation

```python
@exterior_saturation.setter
def exterior_saturation(value: float) -> None
```

<a id="unreal.HighlightAreaStyle.exterior_brightness"></a>

#### exterior\_brightness

```python
@property
def exterior_brightness() -> float
```

(float):  [Read-Write]

<a id="unreal.HighlightAreaStyle.exterior_brightness"></a>

#### exterior\_brightness

```python
@exterior_brightness.setter
def exterior_brightness(value: float) -> None
```

<a id="unreal.HighlightAreaStyle.exterior_contrast"></a>

#### exterior\_contrast

```python
@property
def exterior_contrast() -> float
```

(float):  [Read-Write]

<a id="unreal.HighlightAreaStyle.exterior_contrast"></a>

#### exterior\_contrast

```python
@exterior_contrast.setter
def exterior_contrast(value: float) -> None
```

<a id="unreal.CreateHighlightAreaParams"></a>