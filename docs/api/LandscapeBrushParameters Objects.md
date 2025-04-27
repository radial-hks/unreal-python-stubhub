## LandscapeBrushParameters Objects

```python
class LandscapeBrushParameters(StructBase)
```

Landscape Brush Parameters

**C++ Source:**

- **Module**: Landscape
- **File**: LandscapeBlueprintBrushBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``combined_result`` (TextureRenderTarget2D):  [Read-Write]
- ``layer_type`` (LandscapeToolTargetType):  [Read-Write]
- ``render_area_size`` (IntPoint):  [Read-Write]
- ``render_area_world_transform`` (Transform):  [Read-Write]
- ``weightmap_layer_name`` (Name):  [Read-Write]

<a id="unreal.LandscapeBrushParameters.__init__"></a>

#### __init__

```python
def __init__(render_area_world_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             render_area_size: IntPoint = [0, 0],
             combined_result: TextureRenderTarget2D = None,
             layer_type: LandscapeToolTargetType = LandscapeToolTargetType.
             HEIGHTMAP,
             weightmap_layer_name: Name = "None") -> None
```

<a id="unreal.LandscapeBrushParameters.render_area_world_transform"></a>

#### render_area_world_transform

```python
@property
def render_area_world_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.LandscapeBrushParameters.render_area_world_transform"></a>

#### render_area_world_transform

```python
@render_area_world_transform.setter
def render_area_world_transform(value: Transform) -> None
```

<a id="unreal.LandscapeBrushParameters.render_area_size"></a>

#### render_area_size

```python
@property
def render_area_size() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.LandscapeBrushParameters.render_area_size"></a>

#### render_area_size

```python
@render_area_size.setter
def render_area_size(value: IntPoint) -> None
```

<a id="unreal.LandscapeBrushParameters.combined_result"></a>

#### combined_result

```python
@property
def combined_result() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Write]

<a id="unreal.LandscapeBrushParameters.combined_result"></a>

#### combined_result

```python
@combined_result.setter
def combined_result(value: TextureRenderTarget2D) -> None
```

<a id="unreal.LandscapeBrushParameters.layer_type"></a>

#### layer_type

```python
@property
def layer_type() -> LandscapeToolTargetType
```

(LandscapeToolTargetType):  [Read-Write]

<a id="unreal.LandscapeBrushParameters.layer_type"></a>

#### layer_type

```python
@layer_type.setter
def layer_type(value: LandscapeToolTargetType) -> None
```

<a id="unreal.LandscapeBrushParameters.weightmap_layer_name"></a>

#### weightmap_layer_name

```python
@property
def weightmap_layer_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.LandscapeBrushParameters.weightmap_layer_name"></a>

#### weightmap_layer_name

```python
@weightmap_layer_name.setter
def weightmap_layer_name(value: Name) -> None
```

<a id="unreal.NamedFloat"></a>