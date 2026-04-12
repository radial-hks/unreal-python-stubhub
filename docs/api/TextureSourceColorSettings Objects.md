## TextureSourceColorSettings Objects

```python
class TextureSourceColorSettings(StructBase)
```

Texture Source Color Settings

**C++ Source:**

- **Module**: Engine
- **File**: Texture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blue_chromaticity_coordinate`` (Vector2D):  [Read-Write] Blue chromaticity coordinate of the source color space.
- ``chromatic_adaptation_method`` (TextureChromaticAdaptationMethod):  [Read-Write] Chromatic adaption method applied if the source white point differs from the working color space white point.
- ``color_space`` (TextureColorSpace):  [Read-Write] Source color space of the texture.
- ``encoding_override`` (TextureSourceEncoding):  [Read-Write] Source encoding of the texture, exposing more options than just sRGB.
- ``green_chromaticity_coordinate`` (Vector2D):  [Read-Write] Green chromaticity coordinate of the source color space.
- ``red_chromaticity_coordinate`` (Vector2D):  [Read-Write] Red chromaticity coordinate of the source color space.
- ``white_chromaticity_coordinate`` (Vector2D):  [Read-Write] White chromaticity coordinate of the source color space.

<a id="unreal.TextureSourceColorSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    encoding_override: TextureSourceEncoding = TextureSourceEncoding.TSE_NONE,
    color_space: TextureColorSpace = TextureColorSpace.TCS_NONE,
    red_chromaticity_coordinate: Vector2D = [0.000000, 0.000000],
    green_chromaticity_coordinate: Vector2D = [0.000000, 0.000000],
    blue_chromaticity_coordinate: Vector2D = [0.000000, 0.000000],
    white_chromaticity_coordinate: Vector2D = [0.000000, 0.000000],
    chromatic_adaptation_method:
    TextureChromaticAdaptationMethod = TextureChromaticAdaptationMethod.
    TCAM_NONE
) -> None
```

<a id="unreal.TextureSourceColorSettings.encoding_override"></a>

#### encoding\_override

```python
@property
def encoding_override() -> TextureSourceEncoding
```

(TextureSourceEncoding):  [Read-Write] Source encoding of the texture, exposing more options than just sRGB.

<a id="unreal.TextureSourceColorSettings.encoding_override"></a>

#### encoding\_override

```python
@encoding_override.setter
def encoding_override(value: TextureSourceEncoding) -> None
```

<a id="unreal.TextureSourceColorSettings.color_space"></a>

#### color\_space

```python
@property
def color_space() -> TextureColorSpace
```

(TextureColorSpace):  [Read-Write] Source color space of the texture.

<a id="unreal.TextureSourceColorSettings.color_space"></a>

#### color\_space

```python
@color_space.setter
def color_space(value: TextureColorSpace) -> None
```

<a id="unreal.TextureSourceColorSettings.red_chromaticity_coordinate"></a>

#### red\_chromaticity\_coordinate

```python
@property
def red_chromaticity_coordinate() -> Vector2D
```

(Vector2D):  [Read-Write] Red chromaticity coordinate of the source color space.

<a id="unreal.TextureSourceColorSettings.red_chromaticity_coordinate"></a>

#### red\_chromaticity\_coordinate

```python
@red_chromaticity_coordinate.setter
def red_chromaticity_coordinate(value: Vector2D) -> None
```

<a id="unreal.TextureSourceColorSettings.green_chromaticity_coordinate"></a>

#### green\_chromaticity\_coordinate

```python
@property
def green_chromaticity_coordinate() -> Vector2D
```

(Vector2D):  [Read-Write] Green chromaticity coordinate of the source color space.

<a id="unreal.TextureSourceColorSettings.green_chromaticity_coordinate"></a>

#### green\_chromaticity\_coordinate

```python
@green_chromaticity_coordinate.setter
def green_chromaticity_coordinate(value: Vector2D) -> None
```

<a id="unreal.TextureSourceColorSettings.blue_chromaticity_coordinate"></a>

#### blue\_chromaticity\_coordinate

```python
@property
def blue_chromaticity_coordinate() -> Vector2D
```

(Vector2D):  [Read-Write] Blue chromaticity coordinate of the source color space.

<a id="unreal.TextureSourceColorSettings.blue_chromaticity_coordinate"></a>

#### blue\_chromaticity\_coordinate

```python
@blue_chromaticity_coordinate.setter
def blue_chromaticity_coordinate(value: Vector2D) -> None
```

<a id="unreal.TextureSourceColorSettings.white_chromaticity_coordinate"></a>

#### white\_chromaticity\_coordinate

```python
@property
def white_chromaticity_coordinate() -> Vector2D
```

(Vector2D):  [Read-Write] White chromaticity coordinate of the source color space.

<a id="unreal.TextureSourceColorSettings.white_chromaticity_coordinate"></a>

#### white\_chromaticity\_coordinate

```python
@white_chromaticity_coordinate.setter
def white_chromaticity_coordinate(value: Vector2D) -> None
```

<a id="unreal.TextureSourceColorSettings.chromatic_adaptation_method"></a>

#### chromatic\_adaptation\_method

```python
@property
def chromatic_adaptation_method() -> TextureChromaticAdaptationMethod
```

(TextureChromaticAdaptationMethod):  [Read-Write] Chromatic adaption method applied if the source white point differs from the working color space white point.

<a id="unreal.TextureSourceColorSettings.chromatic_adaptation_method"></a>

#### chromatic\_adaptation\_method

```python
@chromatic_adaptation_method.setter
def chromatic_adaptation_method(
        value: TextureChromaticAdaptationMethod) -> None
```

<a id="unreal.CanvasIcon"></a>