## GeometryScriptSampleTextureOptions Objects

```python
class GeometryScriptSampleTextureOptions(StructBase)
```

Geometry Script Sample Texture Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: TextureMapFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sampling_method`` (GeometryScriptPixelSamplingMethod):  [Read-Write]
- ``uv_offset`` (Vector2D):  [Read-Write]
- ``uv_scale`` (Vector2D):  [Read-Write]
- ``wrap`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptSampleTextureOptions.__init__"></a>

#### __init__

```python
def __init__(
        sampling_method:
    GeometryScriptPixelSamplingMethod = GeometryScriptPixelSamplingMethod.
    BILINEAR,
        wrap: bool = False,
        uv_scale: Vector2D = [0.000000, 0.000000],
        uv_offset: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.GeometryScriptSampleTextureOptions.sampling_method"></a>

#### sampling_method

```python
@property
def sampling_method() -> GeometryScriptPixelSamplingMethod
```

(GeometryScriptPixelSamplingMethod):  [Read-Write]

<a id="unreal.GeometryScriptSampleTextureOptions.sampling_method"></a>

#### sampling_method

```python
@sampling_method.setter
def sampling_method(value: GeometryScriptPixelSamplingMethod) -> None
```

<a id="unreal.GeometryScriptSampleTextureOptions.wrap"></a>

#### wrap

```python
@property
def wrap() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSampleTextureOptions.wrap"></a>

#### wrap

```python
@wrap.setter
def wrap(value: bool) -> None
```

<a id="unreal.GeometryScriptSampleTextureOptions.uv_scale"></a>

#### uv_scale

```python
@property
def uv_scale() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.GeometryScriptSampleTextureOptions.uv_scale"></a>

#### uv_scale

```python
@uv_scale.setter
def uv_scale(value: Vector2D) -> None
```

<a id="unreal.GeometryScriptSampleTextureOptions.uv_offset"></a>

#### uv_offset

```python
@property
def uv_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.GeometryScriptSampleTextureOptions.uv_offset"></a>

#### uv_offset

```python
@uv_offset.setter
def uv_offset(value: Vector2D) -> None
```

<a id="unreal.ComputeDistanceFieldSettings"></a>