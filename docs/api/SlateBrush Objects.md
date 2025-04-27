## SlateBrush Objects

```python
class SlateBrush(StructBase)
```

A brush which contains information about how to draw a Slate element
//, meta = (HasNativeMake = ""))

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateBrush.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``draw_as`` (SlateBrushDrawType):  [Read-Write] How to draw the image
- ``image_size`` (DeprecateSlateVector2D):  [Read-Write] Size of the resource in Slate Units
- ``image_type`` (SlateBrushImageType):  [Read-Write] The type of image
- ``margin`` (Margin):  [Read-Write] The margin to use in Box and Border modes
- ``mirroring`` (SlateBrushMirrorType):  [Read-Write] How to mirror the image in Image mode.  This is normally only used for dynamic image brushes where the source texture
            comes from a hardware device such as a web camera.
- ``outline_settings`` (SlateBrushOutlineSettings):  [Read-Write] How to draw the outline.  Currently only used for RoundedBox type brushes.
- ``resource_name`` (Name):  [Read-Write] The name of the rendering resource to use
- ``resource_object`` (Object):  [Read-Write] The image to render for this brush, can be a UTexture or UMaterialInterface or an object implementing
  the AtlasedTextureInterface.
- ``tiling`` (SlateBrushTileType):  [Read-Write] How to tile the image in Image mode
- ``tint_color`` (SlateColor):  [Read-Write] Tinting applied to the image.

<a id="unreal.SlateBrush.__init__"></a>

#### __init__

```python
def __init__(
    tint_color: SlateColor = [[1.000000, 0.000000, 1.000000, 1.000000],
                              SlateColorStylingMode.USE_COLOR_SPECIFIED],
    draw_as: SlateBrushDrawType = SlateBrushDrawType.NO_DRAW_TYPE,
    tiling: SlateBrushTileType = SlateBrushTileType.NO_TILE,
    mirroring: SlateBrushMirrorType = SlateBrushMirrorType.NO_MIRROR,
    image_size: DeprecateSlateVector2D = [0.000000, 0.000000],
    margin: Margin = [0.000000, 0.000000, 0.000000, 0.000000],
    resource_object: Object = None,
    outline_settings: SlateBrushOutlineSettings = [
        [0.000000, 0.000000, 0.000000, 0.000000],
        [[0.000000, 0.000000, 0.000000, 0.000000],
         SlateColorStylingMode.USE_COLOR_SPECIFIED], 0.000000,
        SlateBrushRoundingType.HALF_HEIGHT_RADIUS, False
    ]
) -> None
```

<a id="unreal.SlateBrush.tint_color"></a>

#### tint_color

```python
@property
def tint_color() -> SlateColor
```

(SlateColor):  [Read-Write] Tinting applied to the image.

<a id="unreal.SlateBrush.tint_color"></a>

#### tint_color

```python
@tint_color.setter
def tint_color(value: SlateColor) -> None
```

<a id="unreal.SlateBrush.draw_as"></a>

#### draw_as

```python
@property
def draw_as() -> SlateBrushDrawType
```

(SlateBrushDrawType):  [Read-Write] How to draw the image

<a id="unreal.SlateBrush.draw_as"></a>

#### draw_as

```python
@draw_as.setter
def draw_as(value: SlateBrushDrawType) -> None
```

<a id="unreal.SlateBrush.tiling"></a>

#### tiling

```python
@property
def tiling() -> SlateBrushTileType
```

(SlateBrushTileType):  [Read-Write] How to tile the image in Image mode

<a id="unreal.SlateBrush.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: SlateBrushTileType) -> None
```

<a id="unreal.SlateBrush.mirroring"></a>

#### mirroring

```python
@property
def mirroring() -> SlateBrushMirrorType
```

(SlateBrushMirrorType):  [Read-Write] How to mirror the image in Image mode.  This is normally only used for dynamic image brushes where the source texture
          comes from a hardware device such as a web camera.

<a id="unreal.SlateBrush.mirroring"></a>

#### mirroring

```python
@mirroring.setter
def mirroring(value: SlateBrushMirrorType) -> None
```

<a id="unreal.SlateBrush.image_size"></a>

#### image_size

```python
@property
def image_size() -> DeprecateSlateVector2D
```

(DeprecateSlateVector2D):  [Read-Write] Size of the resource in Slate Units

<a id="unreal.SlateBrush.image_size"></a>

#### image_size

```python
@image_size.setter
def image_size(value: DeprecateSlateVector2D) -> None
```

<a id="unreal.SlateBrush.margin"></a>

#### margin

```python
@property
def margin() -> Margin
```

(Margin):  [Read-Write] The margin to use in Box and Border modes

<a id="unreal.SlateBrush.margin"></a>

#### margin

```python
@margin.setter
def margin(value: Margin) -> None
```

<a id="unreal.SlateBrush.resource_object"></a>

#### resource_object

```python
@property
def resource_object() -> Object
```

(Object):  [Read-Write] The image to render for this brush, can be a UTexture or UMaterialInterface or an object implementing
the AtlasedTextureInterface.

<a id="unreal.SlateBrush.resource_object"></a>

#### resource_object

```python
@resource_object.setter
def resource_object(value: Object) -> None
```

<a id="unreal.SlateBrush.texture_object"></a>

#### texture_object

```python
@property
def texture_object() -> Object
```

deprecated: 'texture_object' was renamed to 'resource_object'.

<a id="unreal.SlateBrush.texture_object"></a>

#### texture_object

```python
@texture_object.setter
def texture_object(value: Object) -> None
```

<a id="unreal.SlateBrush.outline_settings"></a>

#### outline_settings

```python
@property
def outline_settings() -> SlateBrushOutlineSettings
```

(SlateBrushOutlineSettings):  [Read-Write] How to draw the outline.  Currently only used for RoundedBox type brushes.

<a id="unreal.SlateBrush.outline_settings"></a>

#### outline_settings

```python
@outline_settings.setter
def outline_settings(value: SlateBrushOutlineSettings) -> None
```

<a id="unreal.SlateBrushOutlineSettings"></a>