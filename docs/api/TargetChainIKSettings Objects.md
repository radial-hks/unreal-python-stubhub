## TargetChainIKSettings Objects

```python
class TargetChainIKSettings(StructBase)
```

Target Chain IKSettings

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRetargetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affected_by_ik_warping`` (bool):  [Read-Write] Is this IK goal affected by the stride warping (in Global Settings). Typically this is true for all feet, but not for hands.
- ``blend_to_source`` (float):  [Read-Write] Range 0 to 1. Default 0. Blends IK goal position from retargeted location (0) to source bone location (1).
  At 0 the goal is placed at the retargeted location.
  At 1 the goal is placed at the location of the source chain's end bone.
- ``blend_to_source_weights`` (Vector):  [Read-Write] Range 0 to 1. Default 1. Weight each axis separately when using Blend To Source.
  At 0 the goal is placed at the retargeted location.
  At 1 the goal is placed at the location of the source chain's end bone.
- ``enable_ik`` (bool):  [Read-Write] Whether to modify the location of the IK goal on this chain. Default is true.
  NOTE: This only has an effect if the chain has an IK Goal assigned to it in the Target IK Rig asset.
  NOTE: If off, and this chain has an IK Goal, the IK will still be evaluated, but the Goal is set to the input bone location (from the FK pass).
- ``extension`` (float):  [Read-Write] Range 0 to 5. Default 1. Brings IK goal closer (0) or further (1+) from origin of chain.
  At 0 the effector is placed at the origin of the chain (ie Shoulder, Hip etc).
  At 1 the effector is left at the end of the chain (ie Wrist, Foot etc)
  Values in-between 0-1 will slide the effector along the vector from the start to the end of the chain.
  Values greater than 1 will stretch the chain beyond the retargeted length.
- ``scale_vertical`` (float):  [Read-Write] Range +-Infinity. Default 1. Scales the vertical component of the IK goal's position.
- ``static_local_offset`` (Vector):  [Read-Write] Default 0, 0, 0. Apply a static local-space offset to IK goal position.
- ``static_offset`` (Vector):  [Read-Write] Default 0, 0, 0. Apply a static global-space offset to IK goal position.
- ``static_rotation_offset`` (Rotator):  [Read-Write] Default 0, 0, 0. Apply a static local-space offset to IK goal rotation.

<a id="unreal.TargetChainIKSettings.__init__"></a>

#### __init__

```python
def __init__(enable_ik: bool = False,
             blend_to_source: float = 0.000000,
             blend_to_source_weights: Vector = [0.000000, 0.000000, 0.000000],
             static_offset: Vector = [0.000000, 0.000000, 0.000000],
             static_local_offset: Vector = [0.000000, 0.000000, 0.000000],
             static_rotation_offset: Rotator = [0.000000, 0.000000, 0.000000],
             scale_vertical: float = 0.000000,
             extension: float = 0.000000,
             affected_by_ik_warping: bool = False) -> None
```

<a id="unreal.TargetChainIKSettings.enable_ik"></a>

#### enable_ik

```python
@property
def enable_ik() -> bool
```

(bool):  [Read-Write] Whether to modify the location of the IK goal on this chain. Default is true.
NOTE: This only has an effect if the chain has an IK Goal assigned to it in the Target IK Rig asset.
NOTE: If off, and this chain has an IK Goal, the IK will still be evaluated, but the Goal is set to the input bone location (from the FK pass).

<a id="unreal.TargetChainIKSettings.enable_ik"></a>

#### enable_ik

```python
@enable_ik.setter
def enable_ik(value: bool) -> None
```

<a id="unreal.TargetChainIKSettings.blend_to_source"></a>

#### blend_to_source

```python
@property
def blend_to_source() -> float
```

(float):  [Read-Write] Range 0 to 1. Default 0. Blends IK goal position from retargeted location (0) to source bone location (1).
At 0 the goal is placed at the retargeted location.
At 1 the goal is placed at the location of the source chain's end bone.

<a id="unreal.TargetChainIKSettings.blend_to_source"></a>

#### blend_to_source

```python
@blend_to_source.setter
def blend_to_source(value: float) -> None
```

<a id="unreal.TargetChainIKSettings.blend_to_source_weights"></a>

#### blend_to_source_weights

```python
@property
def blend_to_source_weights() -> Vector
```

(Vector):  [Read-Write] Range 0 to 1. Default 1. Weight each axis separately when using Blend To Source.
At 0 the goal is placed at the retargeted location.
At 1 the goal is placed at the location of the source chain's end bone.

<a id="unreal.TargetChainIKSettings.blend_to_source_weights"></a>

#### blend_to_source_weights

```python
@blend_to_source_weights.setter
def blend_to_source_weights(value: Vector) -> None
```

<a id="unreal.TargetChainIKSettings.static_offset"></a>

#### static_offset

```python
@property
def static_offset() -> Vector
```

(Vector):  [Read-Write] Default 0, 0, 0. Apply a static global-space offset to IK goal position.

<a id="unreal.TargetChainIKSettings.static_offset"></a>

#### static_offset

```python
@static_offset.setter
def static_offset(value: Vector) -> None
```

<a id="unreal.TargetChainIKSettings.static_local_offset"></a>

#### static_local_offset

```python
@property
def static_local_offset() -> Vector
```

(Vector):  [Read-Write] Default 0, 0, 0. Apply a static local-space offset to IK goal position.

<a id="unreal.TargetChainIKSettings.static_local_offset"></a>

#### static_local_offset

```python
@static_local_offset.setter
def static_local_offset(value: Vector) -> None
```

<a id="unreal.TargetChainIKSettings.static_rotation_offset"></a>

#### static_rotation_offset

```python
@property
def static_rotation_offset() -> Rotator
```

(Rotator):  [Read-Write] Default 0, 0, 0. Apply a static local-space offset to IK goal rotation.

<a id="unreal.TargetChainIKSettings.static_rotation_offset"></a>

#### static_rotation_offset

```python
@static_rotation_offset.setter
def static_rotation_offset(value: Rotator) -> None
```

<a id="unreal.TargetChainIKSettings.scale_vertical"></a>

#### scale_vertical

```python
@property
def scale_vertical() -> float
```

(float):  [Read-Write] Range +-Infinity. Default 1. Scales the vertical component of the IK goal's position.

<a id="unreal.TargetChainIKSettings.scale_vertical"></a>

#### scale_vertical

```python
@scale_vertical.setter
def scale_vertical(value: float) -> None
```

<a id="unreal.TargetChainIKSettings.extension"></a>

#### extension

```python
@property
def extension() -> float
```

(float):  [Read-Write] Range 0 to 5. Default 1. Brings IK goal closer (0) or further (1+) from origin of chain.
At 0 the effector is placed at the origin of the chain (ie Shoulder, Hip etc).
At 1 the effector is left at the end of the chain (ie Wrist, Foot etc)
Values in-between 0-1 will slide the effector along the vector from the start to the end of the chain.
Values greater than 1 will stretch the chain beyond the retargeted length.

<a id="unreal.TargetChainIKSettings.extension"></a>

#### extension

```python
@extension.setter
def extension(value: float) -> None
```

<a id="unreal.TargetChainIKSettings.affected_by_ik_warping"></a>

#### affected_by_ik_warping

```python
@property
def affected_by_ik_warping() -> bool
```

(bool):  [Read-Write] Is this IK goal affected by the stride warping (in Global Settings). Typically this is true for all feet, but not for hands.

<a id="unreal.TargetChainIKSettings.affected_by_ik_warping"></a>

#### affected_by_ik_warping

```python
@affected_by_ik_warping.setter
def affected_by_ik_warping(value: bool) -> None
```

<a id="unreal.TargetChainFKSettings"></a>