## AvaJustifyModifier Objects

```python
class AvaJustifyModifier(AvaArrangeBaseModifier)
```

Justify Modifier

Aligns child actors, based on their bounding box, according to the specified justification

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaJustifyModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``depth_alignment`` (AvaJustifyDepth):  [Read-Write]
- ``depth_anchor`` (float):  [Read-Write]
- ``horizontal_alignment`` (AvaJustifyHorizontal):  [Read-Write]
- ``horizontal_anchor`` (float):  [Read-Write]
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``vertical_alignment`` (AvaJustifyVertical):  [Read-Write]
- ``vertical_anchor`` (float):  [Read-Write]

<a id="unreal.AvaJustifyModifier.horizontal_anchor"></a>

#### horizontal_anchor

```python
@property
def horizontal_anchor() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaJustifyModifier.horizontal_anchor"></a>

#### horizontal_anchor

```python
@horizontal_anchor.setter
def horizontal_anchor(value: float) -> None
```

<a id="unreal.AvaJustifyModifier.vertical_anchor"></a>

#### vertical_anchor

```python
@property
def vertical_anchor() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaJustifyModifier.vertical_anchor"></a>

#### vertical_anchor

```python
@vertical_anchor.setter
def vertical_anchor(value: float) -> None
```

<a id="unreal.AvaJustifyModifier.depth_anchor"></a>

#### depth_anchor

```python
@property
def depth_anchor() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaJustifyModifier.depth_anchor"></a>

#### depth_anchor

```python
@depth_anchor.setter
def depth_anchor(value: float) -> None
```

<a id="unreal.AvaJustifyModifier.set_vertical_anchor"></a>

#### set_vertical_anchor

```python
def set_vertical_anchor(vertical_anchor: float) -> None
```

x.set_vertical_anchor(vertical_anchor) -> None
Set Vertical Anchor

Args:
    vertical_anchor (float):

<a id="unreal.AvaJustifyModifier.set_vertical_alignment"></a>

#### set_vertical_alignment

```python
def set_vertical_alignment(vertical_alignment: AvaJustifyVertical) -> None
```

x.set_vertical_alignment(vertical_alignment) -> None
Set Vertical Alignment

Args:
    vertical_alignment (AvaJustifyVertical):

<a id="unreal.AvaJustifyModifier.set_horizontal_anchor"></a>

#### set_horizontal_anchor

```python
def set_horizontal_anchor(horizontal_anchor: float) -> None
```

x.set_horizontal_anchor(horizontal_anchor) -> None
Set Horizontal Anchor

Args:
    horizontal_anchor (float):

<a id="unreal.AvaJustifyModifier.set_horizontal_alignment"></a>

#### set_horizontal_alignment

```python
def set_horizontal_alignment(
        horizontal_alignment: AvaJustifyHorizontal) -> None
```

x.set_horizontal_alignment(horizontal_alignment) -> None
Set Horizontal Alignment

Args:
    horizontal_alignment (AvaJustifyHorizontal):

<a id="unreal.AvaJustifyModifier.set_depth_anchor"></a>

#### set_depth_anchor

```python
def set_depth_anchor(depth_anchor: float) -> None
```

x.set_depth_anchor(depth_anchor) -> None
Set Depth Anchor

Args:
    depth_anchor (float):

<a id="unreal.AvaJustifyModifier.set_depth_alignment"></a>

#### set_depth_alignment

```python
def set_depth_alignment(depth_alignment: AvaJustifyDepth) -> None
```

x.set_depth_alignment(depth_alignment) -> None
Set Depth Alignment

Args:
    depth_alignment (AvaJustifyDepth):

<a id="unreal.AvaJustifyModifier.get_vertical_anchor"></a>

#### get_vertical_anchor

```python
def get_vertical_anchor() -> float
```

x.get_vertical_anchor() -> float
Get Vertical Anchor

Returns:
    float:

<a id="unreal.AvaJustifyModifier.get_vertical_alignment"></a>

#### get_vertical_alignment

```python
def get_vertical_alignment() -> AvaJustifyVertical
```

x.get_vertical_alignment() -> AvaJustifyVertical
Get Vertical Alignment

Returns:
    AvaJustifyVertical:

<a id="unreal.AvaJustifyModifier.get_horizontal_anchor"></a>

#### get_horizontal_anchor

```python
def get_horizontal_anchor() -> float
```

x.get_horizontal_anchor() -> float
Get Horizontal Anchor

Returns:
    float:

<a id="unreal.AvaJustifyModifier.get_horizontal_alignment"></a>

#### get_horizontal_alignment

```python
def get_horizontal_alignment() -> AvaJustifyHorizontal
```

x.get_horizontal_alignment() -> AvaJustifyHorizontal
Get Horizontal Alignment

Returns:
    AvaJustifyHorizontal:

<a id="unreal.AvaJustifyModifier.get_depth_anchor"></a>

#### get_depth_anchor

```python
def get_depth_anchor() -> float
```

x.get_depth_anchor() -> float
Get Depth Anchor

Returns:
    float:

<a id="unreal.AvaJustifyModifier.get_depth_alignment"></a>

#### get_depth_alignment

```python
def get_depth_alignment() -> AvaJustifyDepth
```

x.get_depth_alignment() -> AvaJustifyDepth
Get Depth Alignment

Returns:
    AvaJustifyDepth:

<a id="unreal.AvaLookAtModifier"></a>