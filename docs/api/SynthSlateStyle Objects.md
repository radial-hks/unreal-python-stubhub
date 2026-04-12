## SynthSlateStyle Objects

```python
class SynthSlateStyle(SlateWidgetStyle)
```

Represents the appearance of synth UI elements in slate.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SynthSlateStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_style`` (SynthSlateColorStyle):  [Read-Write] Image to use when the slider bar is in its disabled state
- ``size_type`` (SynthSlateSizeType):  [Read-Write] The size of the knobs to use.

<a id="unreal.SynthSlateStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        size_type: SynthSlateSizeType = SynthSlateSizeType.SMALL,
        color_style: SynthSlateColorStyle = SynthSlateColorStyle.LIGHT
) -> None
```

<a id="unreal.SynthSlateStyle.size_type"></a>

#### size\_type

```python
@property
def size_type() -> SynthSlateSizeType
```

(SynthSlateSizeType):  [Read-Write] The size of the knobs to use.

<a id="unreal.SynthSlateStyle.size_type"></a>

#### size\_type

```python
@size_type.setter
def size_type(value: SynthSlateSizeType) -> None
```

<a id="unreal.SynthSlateStyle.color_style"></a>

#### color\_style

```python
@property
def color_style() -> SynthSlateColorStyle
```

(SynthSlateColorStyle):  [Read-Write] Image to use when the slider bar is in its disabled state

<a id="unreal.SynthSlateStyle.color_style"></a>

#### color\_style

```python
@color_style.setter
def color_style(value: SynthSlateColorStyle) -> None
```

<a id="unreal.IntMargin"></a>