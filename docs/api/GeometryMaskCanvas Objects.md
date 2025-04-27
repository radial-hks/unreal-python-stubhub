## GeometryMaskCanvas Objects

```python
class GeometryMaskCanvas(Object)
```

A uniquely identified Canvas.

**C++ Source:**

- **Plugin**: GeometryMask
- **Module**: GeometryMask
- **File**: GeometryMaskCanvas.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_blur`` (bool):  [Read-Write] Optional Blur Toggle.
- ``apply_feather`` (bool):  [Read-Write] Optional Feather Toggle.
- ``blur_strength`` (double):  [Read-Write] Optional Blur Strength.
- ``canvas_name`` (Name):  [Read-Only] Uniquely identifies this canvas.
- ``inner_feather_radius`` (int32):  [Read-Write] Optional Inner Feather Radius.
- ``outer_feather_radius`` (int32):  [Read-Write] Optional Outer Feather Radius.

<a id="unreal.GeometryMaskCanvas.canvas_name"></a>

#### canvas_name

```python
@property
def canvas_name() -> Name
```

(Name):  [Read-Only] Uniquely identifies this canvas.

<a id="unreal.GeometryMaskCanvas.apply_blur"></a>

#### apply_blur

```python
@property
def apply_blur() -> bool
```

(bool):  [Read-Write] Optional Blur Toggle.

<a id="unreal.GeometryMaskCanvas.apply_blur"></a>

#### apply_blur

```python
@apply_blur.setter
def apply_blur(value: bool) -> None
```

<a id="unreal.GeometryMaskCanvas.blur_strength"></a>

#### blur_strength

```python
@property
def blur_strength() -> float
```

(double):  [Read-Write] Optional Blur Strength.

<a id="unreal.GeometryMaskCanvas.blur_strength"></a>

#### blur_strength

```python
@blur_strength.setter
def blur_strength(value: float) -> None
```

<a id="unreal.GeometryMaskCanvas.apply_feather"></a>

#### apply_feather

```python
@property
def apply_feather() -> bool
```

(bool):  [Read-Write] Optional Feather Toggle.

<a id="unreal.GeometryMaskCanvas.apply_feather"></a>

#### apply_feather

```python
@apply_feather.setter
def apply_feather(value: bool) -> None
```

<a id="unreal.GeometryMaskCanvas.outer_feather_radius"></a>

#### outer_feather_radius

```python
@property
def outer_feather_radius() -> int
```

(int32):  [Read-Write] Optional Outer Feather Radius.

<a id="unreal.GeometryMaskCanvas.outer_feather_radius"></a>

#### outer_feather_radius

```python
@outer_feather_radius.setter
def outer_feather_radius(value: int) -> None
```

<a id="unreal.GeometryMaskCanvas.inner_feather_radius"></a>

#### inner_feather_radius

```python
@property
def inner_feather_radius() -> int
```

(int32):  [Read-Write] Optional Inner Feather Radius.

<a id="unreal.GeometryMaskCanvas.inner_feather_radius"></a>

#### inner_feather_radius

```python
@inner_feather_radius.setter
def inner_feather_radius(value: int) -> None
```

<a id="unreal.GeometryMaskCanvas.get_texture"></a>

#### get_texture

```python
def get_texture() -> CanvasRenderTarget2D
```

x.get_texture() -> CanvasRenderTarget2D
Get the underlying render target.

Returns:
    CanvasRenderTarget2D:

<a id="unreal.GeometryMaskCanvas.get_color_channel"></a>

#### get_color_channel

```python
def get_color_channel() -> GeometryMaskColorChannel
```

x.get_color_channel() -> GeometryMaskColorChannel
Get the color channel to write to in the texture.

Returns:
    GeometryMaskColorChannel:

<a id="unreal.GeometryMaskCanvasActor"></a>