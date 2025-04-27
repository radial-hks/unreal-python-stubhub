## AvaColorChangeData Objects

```python
class AvaColorChangeData(StructBase)
```

Ava Color Change Data

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: Avalanche
- **File**: AvaDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_style`` (AvaColorStyle):  [Read-Write]
- ``is_unlit`` (bool):  [Read-Write]
- ``primary_color`` (LinearColor):  [Read-Write]
- ``secondary_color`` (LinearColor):  [Read-Write]

<a id="unreal.AvaColorChangeData.__init__"></a>

#### __init__

```python
def __init__(color_style: AvaColorStyle = AvaColorStyle.NONE,
             primary_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             secondary_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             is_unlit: bool = False) -> None
```

<a id="unreal.AvaColorChangeData.color_style"></a>

#### color_style

```python
@property
def color_style() -> AvaColorStyle
```

(AvaColorStyle):  [Read-Write]

<a id="unreal.AvaColorChangeData.color_style"></a>

#### color_style

```python
@color_style.setter
def color_style(value: AvaColorStyle) -> None
```

<a id="unreal.AvaColorChangeData.primary_color"></a>

#### primary_color

```python
@property
def primary_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaColorChangeData.primary_color"></a>

#### primary_color

```python
@primary_color.setter
def primary_color(value: LinearColor) -> None
```

<a id="unreal.AvaColorChangeData.secondary_color"></a>

#### secondary_color

```python
@property
def secondary_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AvaColorChangeData.secondary_color"></a>

#### secondary_color

```python
@secondary_color.setter
def secondary_color(value: LinearColor) -> None
```

<a id="unreal.AvaColorChangeData.is_unlit"></a>

#### is_unlit

```python
@property
def is_unlit() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AvaColorChangeData.is_unlit"></a>

#### is_unlit

```python
@is_unlit.setter
def is_unlit(value: bool) -> None
```

<a id="unreal.AvaAnchorAlignment"></a>