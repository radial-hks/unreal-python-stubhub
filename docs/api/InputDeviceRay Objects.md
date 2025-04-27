## InputDeviceRay Objects

```python
class InputDeviceRay(StructBase)
```

FInputDeviceRay represents a 3D ray created based on an input device.
If the device is a 2D input device like a mouse, then the ray may
have an associated 2D screen position.

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InputState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``has2d`` (bool):  [Read-Write] If true, WorldRay has 2D device position coordinates
- ``screen_position`` (Vector2D):  [Read-Write] 2D device position coordinates associated with the ray
- ``world_ray`` (Ray):  [Read-Write] 3D ray in 3D scene, in world coordinates

<a id="unreal.InputDeviceRay.__init__"></a>

#### __init__

```python
def __init__(world_ray: Ray = [[0.000000, 0.000000, 0.000000],
                               [0.000000, 0.000000, 0.000000]],
             has2d: bool = False,
             screen_position: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.InputDeviceRay.world_ray"></a>

#### world_ray

```python
@property
def world_ray() -> Ray
```

(Ray):  [Read-Write] 3D ray in 3D scene, in world coordinates

<a id="unreal.InputDeviceRay.world_ray"></a>

#### world_ray

```python
@world_ray.setter
def world_ray(value: Ray) -> None
```

<a id="unreal.InputDeviceRay.has2d"></a>

#### has2d

```python
@property
def has2d() -> bool
```

(bool):  [Read-Write] If true, WorldRay has 2D device position coordinates

<a id="unreal.InputDeviceRay.has2d"></a>

#### has2d

```python
@has2d.setter
def has2d(value: bool) -> None
```

<a id="unreal.InputDeviceRay.screen_position"></a>

#### screen_position

```python
@property
def screen_position() -> Vector2D
```

(Vector2D):  [Read-Write] 2D device position coordinates associated with the ray

<a id="unreal.InputDeviceRay.screen_position"></a>

#### screen_position

```python
@screen_position.setter
def screen_position(value: Vector2D) -> None
```

<a id="unreal.PropertyEntry"></a>