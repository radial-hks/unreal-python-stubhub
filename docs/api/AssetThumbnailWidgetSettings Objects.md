## AssetThumbnailWidgetSettings Objects

```python
class AssetThumbnailWidgetSettings(StructBase)
```

Copied mostly from FAssetThumbnailConfig

**C++ Source:**

- **Module**: UMGEditor
- **File**: AssetThumbnailWidget.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_asset_specific_thumbnail_overlay`` (bool):  [Read-Write]
- ``allow_hint_text`` (bool):  [Read-Write]
- ``allow_real_time_on_hovered`` (bool):  [Read-Write]
- ``asset_type_color_override`` (LinearColor):  [Read-Write]
- ``color_strip_orientation`` (ThumbnailColorStripOrientation_BlueprintType):  [Read-Write]
- ``force_generic_thumbnail`` (bool):  [Read-Write]
- ``generic_thumbnail_size`` (int32):  [Read-Write]
- ``highlighted_text_delegate`` (GetHighlightTextDelegate):  [Read-Write]
- ``hint_color_and_opacity`` (LinearColor):  [Read-Write]
- ``override_asset_type_color`` (bool):  [Read-Write] Whether to override the asset type's colour
- ``padding`` (Margin):  [Read-Write]
- ``thumbnail_label`` (ThumbnailLabelType_BlueprintType):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.__init__"></a>

#### __init__

```python
def __init__(
    force_generic_thumbnail: bool = False,
    allow_hint_text: bool = False,
    allow_real_time_on_hovered: bool = False,
    allow_asset_specific_thumbnail_overlay: bool = False,
    thumbnail_label:
    ThumbnailLabelType_BlueprintType = ThumbnailLabelType_BlueprintType.
    CLASS_NAME,
    highlighted_text_delegate:
    GetHighlightTextDelegate = GetHighlightTextDelegate(),
    hint_color_and_opacity: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    override_asset_type_color: bool = False,
    asset_type_color_override: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    padding: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    generic_thumbnail_size: int = 0,
    color_strip_orientation:
    ThumbnailColorStripOrientation_BlueprintType = ThumbnailColorStripOrientation_BlueprintType
    .HORIZONTAL_BOTTOM_EDGE
) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.force_generic_thumbnail"></a>

#### force_generic_thumbnail

```python
@property
def force_generic_thumbnail() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.force_generic_thumbnail"></a>

#### force_generic_thumbnail

```python
@force_generic_thumbnail.setter
def force_generic_thumbnail(value: bool) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.allow_hint_text"></a>

#### allow_hint_text

```python
@property
def allow_hint_text() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.allow_hint_text"></a>

#### allow_hint_text

```python
@allow_hint_text.setter
def allow_hint_text(value: bool) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.allow_real_time_on_hovered"></a>

#### allow_real_time_on_hovered

```python
@property
def allow_real_time_on_hovered() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.allow_real_time_on_hovered"></a>

#### allow_real_time_on_hovered

```python
@allow_real_time_on_hovered.setter
def allow_real_time_on_hovered(value: bool) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.allow_asset_specific_thumbnail_overlay"></a>

#### allow_asset_specific_thumbnail_overlay

```python
@property
def allow_asset_specific_thumbnail_overlay() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.allow_asset_specific_thumbnail_overlay"></a>

#### allow_asset_specific_thumbnail_overlay

```python
@allow_asset_specific_thumbnail_overlay.setter
def allow_asset_specific_thumbnail_overlay(value: bool) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.thumbnail_label"></a>

#### thumbnail_label

```python
@property
def thumbnail_label() -> ThumbnailLabelType_BlueprintType
```

(ThumbnailLabelType_BlueprintType):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.thumbnail_label"></a>

#### thumbnail_label

```python
@thumbnail_label.setter
def thumbnail_label(value: ThumbnailLabelType_BlueprintType) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.highlighted_text_delegate"></a>

#### highlighted_text_delegate

```python
@property
def highlighted_text_delegate() -> GetHighlightTextDelegate
```

(GetHighlightTextDelegate):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.highlighted_text_delegate"></a>

#### highlighted_text_delegate

```python
@highlighted_text_delegate.setter
def highlighted_text_delegate(value: GetHighlightTextDelegate) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.hint_color_and_opacity"></a>

#### hint_color_and_opacity

```python
@property
def hint_color_and_opacity() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.hint_color_and_opacity"></a>

#### hint_color_and_opacity

```python
@hint_color_and_opacity.setter
def hint_color_and_opacity(value: LinearColor) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.override_asset_type_color"></a>

#### override_asset_type_color

```python
@property
def override_asset_type_color() -> bool
```

(bool):  [Read-Write] Whether to override the asset type's colour

<a id="unreal.AssetThumbnailWidgetSettings.override_asset_type_color"></a>

#### override_asset_type_color

```python
@override_asset_type_color.setter
def override_asset_type_color(value: bool) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.asset_type_color_override"></a>

#### asset_type_color_override

```python
@property
def asset_type_color_override() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.asset_type_color_override"></a>

#### asset_type_color_override

```python
@asset_type_color_override.setter
def asset_type_color_override(value: LinearColor) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.padding"></a>

#### padding

```python
@property
def padding() -> Margin
```

(Margin):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.padding"></a>

#### padding

```python
@padding.setter
def padding(value: Margin) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.generic_thumbnail_size"></a>

#### generic_thumbnail_size

```python
@property
def generic_thumbnail_size() -> int
```

(int32):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.generic_thumbnail_size"></a>

#### generic_thumbnail_size

```python
@generic_thumbnail_size.setter
def generic_thumbnail_size(value: int) -> None
```

<a id="unreal.AssetThumbnailWidgetSettings.color_strip_orientation"></a>

#### color_strip_orientation

```python
@property
def color_strip_orientation() -> ThumbnailColorStripOrientation_BlueprintType
```

(ThumbnailColorStripOrientation_BlueprintType):  [Read-Write]

<a id="unreal.AssetThumbnailWidgetSettings.color_strip_orientation"></a>

#### color_strip_orientation

```python
@color_strip_orientation.setter
def color_strip_orientation(
        value: ThumbnailColorStripOrientation_BlueprintType) -> None
```

<a id="unreal.ContentBrowserDataFilter"></a>