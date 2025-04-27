## CameraShakeBase Objects

```python
class CameraShakeBase(Object)
```

Base class for a camera shake. A camera shake contains a root shake "pattern" which is
the object that contains the actual logic driving how the camera is shaken. Keeping the two
separate makes it possible to completely change how a shake works without having to create
a completely different asset.

**C++ Source:**

- **Module**: Engine
- **File**: CameraShakeBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``root_shake_pattern`` (CameraShakePattern):  [Read-Write] The root pattern for this camera shake
- ``shake_scale`` (float):  [Read-Write] The overall scale to apply to the shake. Only valid when the shake is active.
- ``single_instance`` (bool):  [Read-Write] If true to only allow a single instance of this shake class to play at any given time.
  Subsequent attempts to play this shake will simply restart the timer.

<a id="unreal.CameraShakeBase.shake_scale"></a>

#### shake_scale

```python
@property
def shake_scale() -> float
```

(float):  [Read-Write] The overall scale to apply to the shake. Only valid when the shake is active.

<a id="unreal.CameraShakeBase.shake_scale"></a>

#### shake_scale

```python
@shake_scale.setter
def shake_scale(value: float) -> None
```

<a id="unreal.CameraShakeBase.set_root_shake_pattern"></a>

#### set_root_shake_pattern

```python
def set_root_shake_pattern(pattern: CameraShakePattern) -> None
```

x.set_root_shake_pattern(pattern) -> None
Sets the root pattern of this camera shake

Args:
    pattern (CameraShakePattern):

<a id="unreal.CameraShakeBase.get_root_shake_pattern"></a>

#### get_root_shake_pattern

```python
def get_root_shake_pattern() -> CameraShakePattern
```

x.get_root_shake_pattern() -> CameraShakePattern
Gets the root pattern of this camera shake

Returns:
    CameraShakePattern:

<a id="unreal.CameraShakeSourceActor"></a>