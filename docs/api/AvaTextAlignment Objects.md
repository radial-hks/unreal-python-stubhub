## AvaTextAlignment Objects

```python
class AvaTextAlignment(StructBase)
```

Ava Text Alignment

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheText
- **File**: AvaTextDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``horizontal_alignment`` (Text3DHorizontalTextAlignment):  [Read-Write]
- ``vertical_alignment`` (Text3DVerticalTextAlignment):  [Read-Write]

<a id="unreal.AvaTextAlignment.__init__"></a>

#### __init__

```python
def __init__(
    horizontal_alignment:
    Text3DHorizontalTextAlignment = Text3DHorizontalTextAlignment.LEFT,
    vertical_alignment:
    Text3DVerticalTextAlignment = Text3DVerticalTextAlignment.FIRST_LINE
) -> None
```

<a id="unreal.AvaTextAlignment.horizontal_alignment"></a>

#### horizontal_alignment

```python
@property
def horizontal_alignment() -> Text3DHorizontalTextAlignment
```

(Text3DHorizontalTextAlignment):  [Read-Write]

<a id="unreal.AvaTextAlignment.horizontal_alignment"></a>

#### horizontal_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: Text3DHorizontalTextAlignment) -> None
```

<a id="unreal.AvaTextAlignment.vertical_alignment"></a>

#### vertical_alignment

```python
@property
def vertical_alignment() -> Text3DVerticalTextAlignment
```

(Text3DVerticalTextAlignment):  [Read-Write]

<a id="unreal.AvaTextAlignment.vertical_alignment"></a>

#### vertical_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: Text3DVerticalTextAlignment) -> None
```

<a id="unreal.AvaLinearGradientSettings"></a>