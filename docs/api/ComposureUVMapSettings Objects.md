## ComposureUVMapSettings Objects

```python
class ComposureUVMapSettings(StructBase)
```

Composure UVMap Settings

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposureUVMap.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``displacement_decode_parameters`` (Vector2D):  [Read-Write] Decoding parameters for DisplacementTexture. DeltaUV = ((RedChannel, GreenChannel) - Y) * X.
- ``displacement_texture`` (Texture):  [Read-Write] Displacement texture to use.
- ``post_uv_displacement_matrix`` (Matrix):  [Read-Write] UV Matrix to apply after displacing UV using DisplacementTexture.
- ``pre_uv_displacement_matrix`` (Matrix):  [Read-Write] UV Matrix to apply before sampling DisplacementTexture.
- ``use_displacement_blue_and_alpha_channels`` (bool):  [Read-Write] Whether to use blue and alpha channel instead of red and green channel in computation of DeltaUV.

<a id="unreal.ComposureUVMapSettings.__init__"></a>

#### __init__

```python
def __init__(pre_uv_displacement_matrix: Matrix = [
    [0.000000, 0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 0.000000]
],
             post_uv_displacement_matrix: Matrix = [
                 [0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000, 0.000000, 0.000000]
             ],
             displacement_decode_parameters: Vector2D = [0.000000, 0.000000],
             displacement_texture: Texture = None,
             use_displacement_blue_and_alpha_channels: bool = False) -> None
```

<a id="unreal.ComposureUVMapSettings.pre_uv_displacement_matrix"></a>

#### pre_uv_displacement_matrix

```python
@property
def pre_uv_displacement_matrix() -> Matrix
```

(Matrix):  [Read-Write] UV Matrix to apply before sampling DisplacementTexture.

<a id="unreal.ComposureUVMapSettings.pre_uv_displacement_matrix"></a>

#### pre_uv_displacement_matrix

```python
@pre_uv_displacement_matrix.setter
def pre_uv_displacement_matrix(value: Matrix) -> None
```

<a id="unreal.ComposureUVMapSettings.post_uv_displacement_matrix"></a>

#### post_uv_displacement_matrix

```python
@property
def post_uv_displacement_matrix() -> Matrix
```

(Matrix):  [Read-Write] UV Matrix to apply after displacing UV using DisplacementTexture.

<a id="unreal.ComposureUVMapSettings.post_uv_displacement_matrix"></a>

#### post_uv_displacement_matrix

```python
@post_uv_displacement_matrix.setter
def post_uv_displacement_matrix(value: Matrix) -> None
```

<a id="unreal.ComposureUVMapSettings.displacement_decode_parameters"></a>

#### displacement_decode_parameters

```python
@property
def displacement_decode_parameters() -> Vector2D
```

(Vector2D):  [Read-Write] Decoding parameters for DisplacementTexture. DeltaUV = ((RedChannel, GreenChannel) - Y) * X.

<a id="unreal.ComposureUVMapSettings.displacement_decode_parameters"></a>

#### displacement_decode_parameters

```python
@displacement_decode_parameters.setter
def displacement_decode_parameters(value: Vector2D) -> None
```

<a id="unreal.ComposureUVMapSettings.displacement_texture"></a>

#### displacement_texture

```python
@property
def displacement_texture() -> Texture
```

(Texture):  [Read-Write] Displacement texture to use.

<a id="unreal.ComposureUVMapSettings.displacement_texture"></a>

#### displacement_texture

```python
@displacement_texture.setter
def displacement_texture(value: Texture) -> None
```

<a id="unreal.ComposureUVMapSettings.use_displacement_blue_and_alpha_channels"></a>

#### use_displacement_blue_and_alpha_channels

```python
@property
def use_displacement_blue_and_alpha_channels() -> bool
```

(bool):  [Read-Write] Whether to use blue and alpha channel instead of red and green channel in computation of DeltaUV.

<a id="unreal.ComposureUVMapSettings.use_displacement_blue_and_alpha_channels"></a>

#### use_displacement_blue_and_alpha_channels

```python
@use_displacement_blue_and_alpha_channels.setter
def use_displacement_blue_and_alpha_channels(value: bool) -> None
```

<a id="unreal.ObjectMixerWidgetUserConfig"></a>