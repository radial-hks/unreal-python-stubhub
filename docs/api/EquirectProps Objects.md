## EquirectProps Objects

```python
class EquirectProps(StructBase)
```

Properties for equirect layers

**C++ Source:**

- **Module**: Engine
- **File**: StereoLayerComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``left_bias`` (Vector2D):  [Read-Write] Left eye's texture coordinate bias after mapping to 2D.
- ``left_scale`` (Vector2D):  [Read-Write] Left eye's texture coordinate scale after mapping to 2D.
- ``left_uv_rect`` (Box2D):  [Read-Write] Left source texture UVRect, specifying portion of input texture corresponding to left eye.
- ``radius`` (float):  [Read-Write] Sphere radius. As of UE 5.3, equirect layers are supported only by the Oculus OpenXR runtime and only with a radius of 0 (infinite sphere).
- ``right_bias`` (Vector2D):  [Read-Write] Right eye's texture coordinate bias after mapping to 2D.
- ``right_scale`` (Vector2D):  [Read-Write] Right eye's texture coordinate scale after mapping to 2D.
- ``right_uv_rect`` (Box2D):  [Read-Write] Right source texture UVRect, specifying portion of input texture corresponding to right eye.

<a id="unreal.EquirectProps.__init__"></a>

#### __init__

```python
def __init__(left_uv_rect: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000],
                                    False],
             right_uv_rect: Box2D = [[0.000000, 0.000000],
                                     [0.000000, 0.000000], False],
             left_scale: Vector2D = [0.000000, 0.000000],
             right_scale: Vector2D = [0.000000, 0.000000],
             left_bias: Vector2D = [0.000000, 0.000000],
             right_bias: Vector2D = [0.000000, 0.000000],
             radius: float = 0.000000) -> None
```

<a id="unreal.EquirectProps.left_uv_rect"></a>

#### left_uv_rect

```python
@property
def left_uv_rect() -> Box2D
```

(Box2D):  [Read-Only] Left source texture UVRect, specifying portion of input texture corresponding to left eye.

<a id="unreal.EquirectProps.right_uv_rect"></a>

#### right_uv_rect

```python
@property
def right_uv_rect() -> Box2D
```

(Box2D):  [Read-Only] Right source texture UVRect, specifying portion of input texture corresponding to right eye.

<a id="unreal.EquirectProps.left_scale"></a>

#### left_scale

```python
@property
def left_scale() -> Vector2D
```

(Vector2D):  [Read-Only] Left eye's texture coordinate scale after mapping to 2D.

<a id="unreal.EquirectProps.right_scale"></a>

#### right_scale

```python
@property
def right_scale() -> Vector2D
```

(Vector2D):  [Read-Only] Right eye's texture coordinate scale after mapping to 2D.

<a id="unreal.EquirectProps.left_bias"></a>

#### left_bias

```python
@property
def left_bias() -> Vector2D
```

(Vector2D):  [Read-Only] Left eye's texture coordinate bias after mapping to 2D.

<a id="unreal.EquirectProps.right_bias"></a>

#### right_bias

```python
@property
def right_bias() -> Vector2D
```

(Vector2D):  [Read-Only] Right eye's texture coordinate bias after mapping to 2D.

<a id="unreal.EquirectProps.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Only] Sphere radius. As of UE 5.3, equirect layers are supported only by the Oculus OpenXR runtime and only with a radius of 0 (infinite sphere).

<a id="unreal.LightmassWorldInfoSettings"></a>