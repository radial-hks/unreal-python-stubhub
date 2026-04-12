## ViewshedStyle Objects

```python
class ViewshedStyle(StructBase)
```

Viewshed Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ViewShedAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``field_of_view`` (float):  [Read-Write]
- ``hidden_color`` (str):  [Read-Write]
- ``outline`` (bool):  [Read-Write]
- ``radius`` (float):  [Read-Write]
- ``visible_color`` (str):  [Read-Write]

<a id="unreal.ViewshedStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(visible_color: str = "",
             hidden_color: str = "",
             outline: bool = False,
             field_of_view: float = 0.000000,
             radius: float = 0.000000) -> None
```

<a id="unreal.ViewshedStyle.visible_color"></a>

#### visible\_color

```python
@property
def visible_color() -> str
```

(str):  [Read-Write]

<a id="unreal.ViewshedStyle.visible_color"></a>

#### visible\_color

```python
@visible_color.setter
def visible_color(value: str) -> None
```

<a id="unreal.ViewshedStyle.hidden_color"></a>

#### hidden\_color

```python
@property
def hidden_color() -> str
```

(str):  [Read-Write]

<a id="unreal.ViewshedStyle.hidden_color"></a>

#### hidden\_color

```python
@hidden_color.setter
def hidden_color(value: str) -> None
```

<a id="unreal.ViewshedStyle.outline"></a>

#### outline

```python
@property
def outline() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ViewshedStyle.outline"></a>

#### outline

```python
@outline.setter
def outline(value: bool) -> None
```

<a id="unreal.ViewshedStyle.field_of_view"></a>

#### field\_of\_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write]

<a id="unreal.ViewshedStyle.field_of_view"></a>

#### field\_of\_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.ViewshedStyle.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write]

<a id="unreal.ViewshedStyle.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.CreateViewshedParams"></a>