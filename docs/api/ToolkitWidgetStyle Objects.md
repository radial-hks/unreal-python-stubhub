## ToolkitWidgetStyle Objects

```python
class ToolkitWidgetStyle(SlateWidgetStyle)
```

FToolkitWidgetStyle is the FSlateWidgetStyle that defines the styling of a ToolkitWidget

**C++ Source:**

- **Module**: WidgetRegistration
- **File**: FToolkitWidgetStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_tool_title_border_padding`` (Margin):  [Read-Write]
- ``title_background_brush`` (SlateBrush):  [Read-Write]
- ``title_font`` (SlateFontInfo):  [Read-Write]
- ``title_foreground_color`` (SlateColor):  [Read-Write]
- ``title_padding`` (Margin):  [Read-Write]
- ``tool_context_text_block_padding`` (Margin):  [Read-Write]
- ``tool_details_background_brush`` (SlateBrush):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.__init__"></a>

#### __init__

```python
def __init__(
    title_background_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    tool_details_background_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    title_foreground_color: SlateColor = [[
        1.000000, 0.000000, 1.000000, 1.000000
    ], SlateColorStylingMode.USE_COLOR_SPECIFIED],
    title_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    active_tool_title_border_padding: Margin = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    tool_context_text_block_padding: Margin = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    title_font: SlateFontInfo = [
        None, None,
        [
            0, False, False, False, None,
            [0.000000, 0.000000, 0.000000, 1.000000]
        ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
    ]
) -> None
```

<a id="unreal.ToolkitWidgetStyle.title_background_brush"></a>

#### title_background_brush

```python
@property
def title_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.title_background_brush"></a>

#### title_background_brush

```python
@title_background_brush.setter
def title_background_brush(value: SlateBrush) -> None
```

<a id="unreal.ToolkitWidgetStyle.tool_details_background_brush"></a>

#### tool_details_background_brush

```python
@property
def tool_details_background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.tool_details_background_brush"></a>

#### tool_details_background_brush

```python
@tool_details_background_brush.setter
def tool_details_background_brush(value: SlateBrush) -> None
```

<a id="unreal.ToolkitWidgetStyle.title_foreground_color"></a>

#### title_foreground_color

```python
@property
def title_foreground_color() -> SlateColor
```

(SlateColor):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.title_foreground_color"></a>

#### title_foreground_color

```python
@title_foreground_color.setter
def title_foreground_color(value: SlateColor) -> None
```

<a id="unreal.ToolkitWidgetStyle.title_padding"></a>

#### title_padding

```python
@property
def title_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.title_padding"></a>

#### title_padding

```python
@title_padding.setter
def title_padding(value: Margin) -> None
```

<a id="unreal.ToolkitWidgetStyle.active_tool_title_border_padding"></a>

#### active_tool_title_border_padding

```python
@property
def active_tool_title_border_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.active_tool_title_border_padding"></a>

#### active_tool_title_border_padding

```python
@active_tool_title_border_padding.setter
def active_tool_title_border_padding(value: Margin) -> None
```

<a id="unreal.ToolkitWidgetStyle.tool_context_text_block_padding"></a>

#### tool_context_text_block_padding

```python
@property
def tool_context_text_block_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.tool_context_text_block_padding"></a>

#### tool_context_text_block_padding

```python
@tool_context_text_block_padding.setter
def tool_context_text_block_padding(value: Margin) -> None
```

<a id="unreal.ToolkitWidgetStyle.title_font"></a>

#### title_font

```python
@property
def title_font() -> SlateFontInfo
```

(SlateFontInfo):  [Read-Write]

<a id="unreal.ToolkitWidgetStyle.title_font"></a>

#### title_font

```python
@title_font.setter
def title_font(value: SlateFontInfo) -> None
```

<a id="unreal.InterchangeFilePickerParameters"></a>