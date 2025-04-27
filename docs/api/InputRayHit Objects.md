## InputRayHit Objects

```python
class InputRayHit(StructBase)
```

* FInputRayHit is returned by various hit-test interface functions.
* Generally this is intended to be returned as the result of a hit-test with a FInputDeviceRay

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InputState.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``has_hit_normal`` (bool):  [Read-Write] True if HitNormal was set
- ``hit`` (bool):  [Read-Write] true if ray hit something, false otherwise
- ``hit_depth`` (double):  [Read-Write] distance along ray at which intersection occurred
- ``hit_identifier`` (int32):  [Read-Write] Client-defined integer identifier for hit object/element/target/etc
- ``hit_normal`` (Vector):  [Read-Write] Normal at hit point, if available
- ``hit_object`` (Object):  [Read-Write] Client-defined pointer for UObject-derived hit owners.
  HitOwner and HitObject should be set to the same pointer if the HitOwner derives from UObject.

<a id="unreal.InputRayHit.__init__"></a>

#### __init__

```python
def __init__(hit: bool = False,
             hit_depth: float = 0.000000,
             hit_normal: Vector = [0.000000, 0.000000, 0.000000],
             has_hit_normal: bool = False,
             hit_identifier: int = 0,
             hit_object: Object = None) -> None
```

<a id="unreal.InputRayHit.hit"></a>

#### hit

```python
@property
def hit() -> bool
```

(bool):  [Read-Write] true if ray hit something, false otherwise

<a id="unreal.InputRayHit.hit"></a>

#### hit

```python
@hit.setter
def hit(value: bool) -> None
```

<a id="unreal.InputRayHit.hit_depth"></a>

#### hit_depth

```python
@property
def hit_depth() -> float
```

(double):  [Read-Write] distance along ray at which intersection occurred

<a id="unreal.InputRayHit.hit_depth"></a>

#### hit_depth

```python
@hit_depth.setter
def hit_depth(value: float) -> None
```

<a id="unreal.InputRayHit.hit_normal"></a>

#### hit_normal

```python
@property
def hit_normal() -> Vector
```

(Vector):  [Read-Write] Normal at hit point, if available

<a id="unreal.InputRayHit.hit_normal"></a>

#### hit_normal

```python
@hit_normal.setter
def hit_normal(value: Vector) -> None
```

<a id="unreal.InputRayHit.has_hit_normal"></a>

#### has_hit_normal

```python
@property
def has_hit_normal() -> bool
```

(bool):  [Read-Write] True if HitNormal was set

<a id="unreal.InputRayHit.has_hit_normal"></a>

#### has_hit_normal

```python
@has_hit_normal.setter
def has_hit_normal(value: bool) -> None
```

<a id="unreal.InputRayHit.hit_identifier"></a>

#### hit_identifier

```python
@property
def hit_identifier() -> int
```

(int32):  [Read-Write] Client-defined integer identifier for hit object/element/target/etc

<a id="unreal.InputRayHit.hit_identifier"></a>

#### hit_identifier

```python
@hit_identifier.setter
def hit_identifier(value: int) -> None
```

<a id="unreal.InputRayHit.hit_object"></a>

#### hit_object

```python
@property
def hit_object() -> Object
```

(Object):  [Read-Write] Client-defined pointer for UObject-derived hit owners.
HitOwner and HitObject should be set to the same pointer if the HitOwner derives from UObject.

<a id="unreal.InputRayHit.hit_object"></a>

#### hit_object

```python
@hit_object.setter
def hit_object(value: Object) -> None
```

<a id="unreal.DeviceButtonState"></a>