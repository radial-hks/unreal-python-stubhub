## LiveLinkTransformControllerData Objects

```python
class LiveLinkTransformControllerData(StructBase)
```

Live Link Transform Controller Data

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLinkComponents
- **File**: LiveLinkTransformController.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sweep`` (bool):  [Read-Write] Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
  Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
- ``teleport`` (bool):  [Read-Write] Whether we teleport the physics state (if physics collision is enabled for this object).
  If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
  If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
  If CCD is on and not teleporting, this will affect objects along the entire sweep volume.
- ``use_location`` (bool):  [Read-Write] Whether we should set the owning actor's location with the value coming from live link.
- ``use_rotation`` (bool):  [Read-Write] Whether we should set the owning actor's rotation with the value coming from live link.
- ``use_scale`` (bool):  [Read-Write] Whether we should set the owning actor's scale with the value coming from live link.
- ``world_transform`` (bool):  [Read-Write] Set the transform of the component in world space of in its local reference frame.

<a id="unreal.LiveLinkTransformControllerData.__init__"></a>

#### __init__

```python
def __init__(world_transform: bool = False,
             use_location: bool = False,
             use_rotation: bool = False,
             use_scale: bool = False,
             sweep: bool = False,
             teleport: bool = False) -> None
```

<a id="unreal.LiveLinkTransformControllerData.world_transform"></a>

#### world_transform

```python
@property
def world_transform() -> bool
```

(bool):  [Read-Write] Set the transform of the component in world space of in its local reference frame.

<a id="unreal.LiveLinkTransformControllerData.world_transform"></a>

#### world_transform

```python
@world_transform.setter
def world_transform(value: bool) -> None
```

<a id="unreal.LiveLinkTransformControllerData.use_location"></a>

#### use_location

```python
@property
def use_location() -> bool
```

(bool):  [Read-Write] Whether we should set the owning actor's location with the value coming from live link.

<a id="unreal.LiveLinkTransformControllerData.use_location"></a>

#### use_location

```python
@use_location.setter
def use_location(value: bool) -> None
```

<a id="unreal.LiveLinkTransformControllerData.use_rotation"></a>

#### use_rotation

```python
@property
def use_rotation() -> bool
```

(bool):  [Read-Write] Whether we should set the owning actor's rotation with the value coming from live link.

<a id="unreal.LiveLinkTransformControllerData.use_rotation"></a>

#### use_rotation

```python
@use_rotation.setter
def use_rotation(value: bool) -> None
```

<a id="unreal.LiveLinkTransformControllerData.use_scale"></a>

#### use_scale

```python
@property
def use_scale() -> bool
```

(bool):  [Read-Write] Whether we should set the owning actor's scale with the value coming from live link.

<a id="unreal.LiveLinkTransformControllerData.use_scale"></a>

#### use_scale

```python
@use_scale.setter
def use_scale(value: bool) -> None
```

<a id="unreal.LiveLinkTransformControllerData.sweep"></a>

#### sweep

```python
@property
def sweep() -> bool
```

(bool):  [Read-Write] Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something.
Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.

<a id="unreal.LiveLinkTransformControllerData.sweep"></a>

#### sweep

```python
@sweep.setter
def sweep(value: bool) -> None
```

<a id="unreal.LiveLinkTransformControllerData.teleport"></a>

#### teleport

```python
@property
def teleport() -> bool
```

(bool):  [Read-Write] Whether we teleport the physics state (if physics collision is enabled for this object).
If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location).
If false, physics velocity is updated based on the change in position (affecting ragdoll parts).
If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

<a id="unreal.LiveLinkTransformControllerData.teleport"></a>

#### teleport

```python
@teleport.setter
def teleport(value: bool) -> None
```

<a id="unreal.CapturableProperty"></a>