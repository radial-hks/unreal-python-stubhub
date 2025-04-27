## ToolBarStyle Objects

```python
class ToolBarStyle(SlateWidgetStyle)
```

Represents the appearance of a toolbar

**C++ Source:**

- **Module**: SlateCore
- **File**: ToolBarStyle.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background_brush`` (SlateBrush):  [Read-Write] The brush used for the background of the toolbar
- ``background_padding`` (Margin):  [Read-Write]
- ``block_padding`` (Margin):  [Read-Write]
- ``button_content_fill_width`` (float):  [Read-Write]
- ``button_content_max_width`` (float):  [Read-Write]
- ``button_padding`` (Margin):  [Read-Write]
- ``button_style`` (ButtonStyle):  [Read-Write]
- ``check_box_padding`` (Margin):  [Read-Write]
- ``combo_button_padding`` (Margin):  [Read-Write]
- ``combo_button_style`` (ComboButtonStyle):  [Read-Write]
- ``editable_text_style`` (EditableTextBoxStyle):  [Read-Write]
- ``expand_brush`` (SlateBrush):  [Read-Write] The brush used for the expand arrow when the toolbar runs out of room and needs to display toolbar items in a menu
- ``icon_padding`` (Margin):  [Read-Write]
- ``icon_padding_with_collapsed_label`` (Margin):  [Read-Write]
- ``icon_padding_with_visible_label`` (Margin):  [Read-Write]
- ``icon_size`` (DeprecateSlateVector2D):  [Read-Write]
- ``indented_block_padding`` (Margin):  [Read-Write]
- ``label_padding`` (Margin):  [Read-Write]
- ``label_style`` (TextBlockStyle):  [Read-Write]
- ``num_columns`` (int32):  [Read-Write]
- ``separator_brush`` (SlateBrush):  [Read-Write]
- ``separator_padding`` (Margin):  [Read-Write]
- ``separator_thickness`` (float):  [Read-Write]
- ``settings_button_style`` (ButtonStyle):  [Read-Write]
- ``settings_combo_button`` (ComboButtonStyle):  [Read-Write]
- ``settings_toggle_button`` (CheckBoxStyle):  [Read-Write]
- ``show_labels`` (bool):  [Read-Write]
- ``toggle_button`` (CheckBoxStyle):  [Read-Write]
- ``uniform_block_height`` (float):  [Read-Write]
- ``uniform_block_width`` (float):  [Read-Write]
- ``vertical_alignment_override`` ('undefined'):  [Read-Write]

<a id="unreal.ToolBarStyle.__init__"></a>

#### __init__

```python
def __init__(
    background_brush: SlateBrush = [
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
        SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
         SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]
    ],
    expand_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                 SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                SlateBrushDrawType.IMAGE,
                                SlateBrushTileType.NO_TILE,
                                SlateBrushMirrorType.NO_MIRROR,
                                [0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000, 0.000000], None,
                                [[0.000000, 0.000000, 0.000000, 0.000000],
                                 [[0.000000, 0.000000, 0.000000, 0.000000],
                                  SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                 0.000000,
                                 SlateBrushRoundingType.HALF_HEIGHT_RADIUS,
                                 False]],
    separator_brush: SlateBrush = [[[1.000000, 1.000000, 1.000000, 1.000000],
                                    SlateColorStylingMode.USE_COLOR_SPECIFIED],
                                   SlateBrushDrawType.IMAGE,
                                   SlateBrushTileType.NO_TILE,
                                   SlateBrushMirrorType.NO_MIRROR,
                                   [0.000000, 0.000000],
                                   [0.000000, 0.000000, 0.000000,
                                    0.000000], None,
                                   [[0.000000, 0.000000, 0.000000, 0.000000],
                                    [[0.000000, 0.000000, 0.000000, 0.000000],
                                     SlateColorStylingMode.USE_COLOR_SPECIFIED
                                     ], 0.000000,
                                    SlateBrushRoundingType.HALF_HEIGHT_RADIUS,
                                    False]],
    label_style: TextBlockStyle = [
        [
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "None", 24.000000, 0, 0.000000, False, False, 1.000000
        ],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], [0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        TextTransformPolicy.NONE, TextOverflowPolicy.CLIP
    ],
    editable_text_style: EditableTextBoxStyle = [
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [4.000000, 2.000000, 4.000000, 2.000000],
        [[
            None, None,
            [
                0, False, False, False, None,
                [0.000000, 0.000000, 0.000000, 1.000000]
            ], "Regular", 9.000000, 0, 0.000000, False, False, 1.000000
        ],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND], [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 1.000000],
         [[0.000000, 0.000000, 0.000000, 0.000000], 0],
         [[[0.000000, 0.000000, 0.000000, 0.000000],
           0], SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         TextTransformPolicy.NONE, TextOverflowPolicy.CLIP],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [[[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]], 16.000000]
    ],
    toggle_button: CheckBoxStyle = [
        SlateCheckBoxType.CHECK_BOX,
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [2.000000, 0.000000, 0.000000, 0.000000],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], [None], [None], [None]
    ],
    combo_button_style: ComboButtonStyle = [
        [[[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE,
          SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
          [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [0.000000, 0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [5.000000, 5.000000, 5.000000, 5.000000],
        [2.000000, 2.000000, 2.000000,
         2.000000], VerticalAlignment.V_ALIGN_CENTER
    ],
    settings_button_style: ButtonStyle = [
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]
    ],
    settings_combo_button: ComboButtonStyle = [
        [[[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE,
          SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
          [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.IMAGE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[[1.000000, 1.000000, 1.000000, 1.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED],
          SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
          SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
          [0.000000, 0.000000, 0.000000, 0.000000], None,
          [[0.000000, 0.000000, 0.000000, 0.000000],
           [[0.000000, 0.000000, 0.000000, 0.000000],
            SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
           SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [[1.000000, 0.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_FOREGROUND],
         [0.000000, 0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 1.000000],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [5.000000, 5.000000, 5.000000, 5.000000],
        [2.000000, 2.000000, 2.000000,
         2.000000], VerticalAlignment.V_ALIGN_CENTER
    ],
    settings_toggle_button: CheckBoxStyle = [
        SlateCheckBoxType.CHECK_BOX,
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [2.000000, 0.000000, 0.000000, 0.000000],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 1.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], [None], [None], [None]
    ],
    button_style: ButtonStyle = [
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED], SlateBrushDrawType.IMAGE,
         SlateBrushTileType.NO_TILE, SlateBrushMirrorType.NO_MIRROR,
         [0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[[1.000000, 1.000000, 1.000000, 1.000000],
          SlateColorStylingMode.USE_COLOR_SPECIFIED],
         SlateBrushDrawType.NO_DRAW_TYPE, SlateBrushTileType.NO_TILE,
         SlateBrushMirrorType.NO_MIRROR, [0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000], None,
         [[0.000000, 0.000000, 0.000000, 0.000000],
          [[0.000000, 0.000000, 0.000000, 0.000000],
           SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
          SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False]],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [[1.000000, 0.000000, 1.000000, 1.000000],
         SlateColorStylingMode.USE_COLOR_FOREGROUND],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 0.000000], [None], [None]
    ],
    label_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    uniform_block_width: float = 0.000000,
    uniform_block_height: float = 0.000000,
    num_columns: int = 0,
    icon_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    separator_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    separator_thickness: float = 0.000000,
    combo_button_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    button_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    check_box_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    block_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    indented_block_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    background_padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    icon_size: DeprecateSlateVector2D = [0.000000, 0.000000],
    show_labels: bool = False,
    button_content_max_width: float = 0.000000,
    button_content_fill_width: float = 0.000000,
    icon_padding_with_visible_label: Margin = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    icon_padding_with_collapsed_label: Margin = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    vertical_alignment_override: type = ()
) -> None
```

<a id="unreal.ToolBarStyle.background_brush"></a>

#### background_brush

```python
@property
def background_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] The brush used for the background of the toolbar

<a id="unreal.ToolBarStyle.background_brush"></a>

#### background_brush

```python
@background_brush.setter
def background_brush(value: SlateBrush) -> None
```

<a id="unreal.ToolBarStyle.expand_brush"></a>

#### expand_brush

```python
@property
def expand_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write] The brush used for the expand arrow when the toolbar runs out of room and needs to display toolbar items in a menu

<a id="unreal.ToolBarStyle.expand_brush"></a>

#### expand_brush

```python
@expand_brush.setter
def expand_brush(value: SlateBrush) -> None
```

<a id="unreal.ToolBarStyle.separator_brush"></a>

#### separator_brush

```python
@property
def separator_brush() -> SlateBrush
```

(SlateBrush):  [Read-Write]

<a id="unreal.ToolBarStyle.separator_brush"></a>

#### separator_brush

```python
@separator_brush.setter
def separator_brush(value: SlateBrush) -> None
```

<a id="unreal.ToolBarStyle.label_style"></a>

#### label_style

```python
@property
def label_style() -> TextBlockStyle
```

(TextBlockStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.label_style"></a>

#### label_style

```python
@label_style.setter
def label_style(value: TextBlockStyle) -> None
```

<a id="unreal.ToolBarStyle.editable_text_style"></a>

#### editable_text_style

```python
@property
def editable_text_style() -> EditableTextBoxStyle
```

(EditableTextBoxStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.editable_text_style"></a>

#### editable_text_style

```python
@editable_text_style.setter
def editable_text_style(value: EditableTextBoxStyle) -> None
```

<a id="unreal.ToolBarStyle.toggle_button"></a>

#### toggle_button

```python
@property
def toggle_button() -> CheckBoxStyle
```

(CheckBoxStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.toggle_button"></a>

#### toggle_button

```python
@toggle_button.setter
def toggle_button(value: CheckBoxStyle) -> None
```

<a id="unreal.ToolBarStyle.combo_button_style"></a>

#### combo_button_style

```python
@property
def combo_button_style() -> ComboButtonStyle
```

(ComboButtonStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.combo_button_style"></a>

#### combo_button_style

```python
@combo_button_style.setter
def combo_button_style(value: ComboButtonStyle) -> None
```

<a id="unreal.ToolBarStyle.settings_button_style"></a>

#### settings_button_style

```python
@property
def settings_button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.settings_button_style"></a>

#### settings_button_style

```python
@settings_button_style.setter
def settings_button_style(value: ButtonStyle) -> None
```

<a id="unreal.ToolBarStyle.settings_combo_button"></a>

#### settings_combo_button

```python
@property
def settings_combo_button() -> ComboButtonStyle
```

(ComboButtonStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.settings_combo_button"></a>

#### settings_combo_button

```python
@settings_combo_button.setter
def settings_combo_button(value: ComboButtonStyle) -> None
```

<a id="unreal.ToolBarStyle.settings_toggle_button"></a>

#### settings_toggle_button

```python
@property
def settings_toggle_button() -> CheckBoxStyle
```

(CheckBoxStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.settings_toggle_button"></a>

#### settings_toggle_button

```python
@settings_toggle_button.setter
def settings_toggle_button(value: CheckBoxStyle) -> None
```

<a id="unreal.ToolBarStyle.button_style"></a>

#### button_style

```python
@property
def button_style() -> ButtonStyle
```

(ButtonStyle):  [Read-Write]

<a id="unreal.ToolBarStyle.button_style"></a>

#### button_style

```python
@button_style.setter
def button_style(value: ButtonStyle) -> None
```

<a id="unreal.ToolBarStyle.label_padding"></a>

#### label_padding

```python
@property
def label_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.label_padding"></a>

#### label_padding

```python
@label_padding.setter
def label_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.uniform_block_width"></a>

#### uniform_block_width

```python
@property
def uniform_block_width() -> float
```

(float):  [Read-Write]

<a id="unreal.ToolBarStyle.uniform_block_width"></a>

#### uniform_block_width

```python
@uniform_block_width.setter
def uniform_block_width(value: float) -> None
```

<a id="unreal.ToolBarStyle.uniform_block_height"></a>

#### uniform_block_height

```python
@property
def uniform_block_height() -> float
```

(float):  [Read-Write]

<a id="unreal.ToolBarStyle.uniform_block_height"></a>

#### uniform_block_height

```python
@uniform_block_height.setter
def uniform_block_height(value: float) -> None
```

<a id="unreal.ToolBarStyle.num_columns"></a>

#### num_columns

```python
@property
def num_columns() -> int
```

(int32):  [Read-Write]

<a id="unreal.ToolBarStyle.num_columns"></a>

#### num_columns

```python
@num_columns.setter
def num_columns(value: int) -> None
```

<a id="unreal.ToolBarStyle.icon_padding"></a>

#### icon_padding

```python
@property
def icon_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.icon_padding"></a>

#### icon_padding

```python
@icon_padding.setter
def icon_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.separator_padding"></a>

#### separator_padding

```python
@property
def separator_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.separator_padding"></a>

#### separator_padding

```python
@separator_padding.setter
def separator_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.separator_thickness"></a>

#### separator_thickness

```python
@property
def separator_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.ToolBarStyle.separator_thickness"></a>

#### separator_thickness

```python
@separator_thickness.setter
def separator_thickness(value: float) -> None
```

<a id="unreal.ToolBarStyle.combo_button_padding"></a>

#### combo_button_padding

```python
@property
def combo_button_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.combo_button_padding"></a>

#### combo_button_padding

```python
@combo_button_padding.setter
def combo_button_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.button_padding"></a>

#### button_padding

```python
@property
def button_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.button_padding"></a>

#### button_padding

```python
@button_padding.setter
def button_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.check_box_padding"></a>

#### check_box_padding

```python
@property
def check_box_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.check_box_padding"></a>

#### check_box_padding

```python
@check_box_padding.setter
def check_box_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.block_padding"></a>

#### block_padding

```python
@property
def block_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.block_padding"></a>

#### block_padding

```python
@block_padding.setter
def block_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.indented_block_padding"></a>

#### indented_block_padding

```python
@property
def indented_block_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.indented_block_padding"></a>

#### indented_block_padding

```python
@indented_block_padding.setter
def indented_block_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.background_padding"></a>

#### background_padding

```python
@property
def background_padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.background_padding"></a>

#### background_padding

```python
@background_padding.setter
def background_padding(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.icon_size"></a>

#### icon_size

```python
@property
def icon_size() -> DeprecateSlateVector2D
```

(DeprecateSlateVector2D):  [Read-Write]

<a id="unreal.ToolBarStyle.icon_size"></a>

#### icon_size

```python
@icon_size.setter
def icon_size(value: DeprecateSlateVector2D) -> None
```

<a id="unreal.ToolBarStyle.show_labels"></a>

#### show_labels

```python
@property
def show_labels() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ToolBarStyle.show_labels"></a>

#### show_labels

```python
@show_labels.setter
def show_labels(value: bool) -> None
```

<a id="unreal.ToolBarStyle.button_content_max_width"></a>

#### button_content_max_width

```python
@property
def button_content_max_width() -> float
```

(float):  [Read-Write]

<a id="unreal.ToolBarStyle.button_content_max_width"></a>

#### button_content_max_width

```python
@button_content_max_width.setter
def button_content_max_width(value: float) -> None
```

<a id="unreal.ToolBarStyle.button_content_fill_width"></a>

#### button_content_fill_width

```python
@property
def button_content_fill_width() -> float
```

(float):  [Read-Write]

<a id="unreal.ToolBarStyle.button_content_fill_width"></a>

#### button_content_fill_width

```python
@button_content_fill_width.setter
def button_content_fill_width(value: float) -> None
```

<a id="unreal.ToolBarStyle.icon_padding_with_visible_label"></a>

#### icon_padding_with_visible_label

```python
@property
def icon_padding_with_visible_label() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.icon_padding_with_visible_label"></a>

#### icon_padding_with_visible_label

```python
@icon_padding_with_visible_label.setter
def icon_padding_with_visible_label(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.icon_padding_with_collapsed_label"></a>

#### icon_padding_with_collapsed_label

```python
@property
def icon_padding_with_collapsed_label() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.ToolBarStyle.icon_padding_with_collapsed_label"></a>

#### icon_padding_with_collapsed_label

```python
@icon_padding_with_collapsed_label.setter
def icon_padding_with_collapsed_label(value: Margin) -> None
```

<a id="unreal.ToolBarStyle.vertical_alignment_override"></a>

#### vertical_alignment_override

```python
@property
def vertical_alignment_override() -> type
```

('undefined'):  [Read-Write]

<a id="unreal.ToolBarStyle.vertical_alignment_override"></a>

#### vertical_alignment_override

```python
@vertical_alignment_override.setter
def vertical_alignment_override(value: type) -> None
```

<a id="unreal.Anchors"></a>