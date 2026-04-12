## IKRig\_BodyMover Objects

```python
class IKRig_BodyMover(IKRigSolver)
```

IKRig Body Mover

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRig_BodyMover.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``position_alpha`` (float):  [Read-Write] Blend the translational effect of this solver on/off. Range is 0-1. Default is 1.0.
- ``position_negative_x`` (float):  [Read-Write] Multiply the NEGATIVE X translation. Range is 0-1. Default is 1.0.
- ``position_negative_y`` (float):  [Read-Write] Multiply the NEGATIVE Y translation. Range is 0-1. Default is 1.0.
- ``position_negative_z`` (float):  [Read-Write] Multiply the NEGATIVE Z translation. Range is 0-1. Default is 1.0.
- ``position_positive_x`` (float):  [Read-Write] Multiply the POSITIVE X translation. Range is 0-1. Default is 1.0.
- ``position_positive_y`` (float):  [Read-Write] Multiply the POSITIVE Y translation. Range is 0-1. Default is 1.0.
- ``position_positive_z`` (float):  [Read-Write] Multiply the POSITIVE Z translation. Range is 0-1. Default is 1.0.
- ``root_bone`` (Name):  [Read-Only] The target bone to move with the effectors.
- ``rotate_x_alpha`` (float):  [Read-Write] Blend the X-axis rotational effect on/off. Range is 0-1. Default is 1.0.
- ``rotate_y_alpha`` (float):  [Read-Write] Blend the Y-axis rotational effect on/off. Range is 0-1. Default is 1.0.
- ``rotate_z_alpha`` (float):  [Read-Write] Blend the Z-axis rotational effect on/off. Range is 0-1. Default is 1.0.
- ``rotation_alpha`` (float):  [Read-Write] Blend the total rotational effect on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_alpha"></a>

#### position\_alpha

```python
@property
def position_alpha() -> float
```

(float):  [Read-Write] Blend the translational effect of this solver on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_alpha"></a>

#### position\_alpha

```python
@position_alpha.setter
def position_alpha(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.position_positive_x"></a>

#### position\_positive\_x

```python
@property
def position_positive_x() -> float
```

(float):  [Read-Write] Multiply the POSITIVE X translation. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_positive_x"></a>

#### position\_positive\_x

```python
@position_positive_x.setter
def position_positive_x(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.position_negative_x"></a>

#### position\_negative\_x

```python
@property
def position_negative_x() -> float
```

(float):  [Read-Write] Multiply the NEGATIVE X translation. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_negative_x"></a>

#### position\_negative\_x

```python
@position_negative_x.setter
def position_negative_x(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.position_positive_y"></a>

#### position\_positive\_y

```python
@property
def position_positive_y() -> float
```

(float):  [Read-Write] Multiply the POSITIVE Y translation. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_positive_y"></a>

#### position\_positive\_y

```python
@position_positive_y.setter
def position_positive_y(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.position_negative_y"></a>

#### position\_negative\_y

```python
@property
def position_negative_y() -> float
```

(float):  [Read-Write] Multiply the NEGATIVE Y translation. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_negative_y"></a>

#### position\_negative\_y

```python
@position_negative_y.setter
def position_negative_y(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.position_positive_z"></a>

#### position\_positive\_z

```python
@property
def position_positive_z() -> float
```

(float):  [Read-Write] Multiply the POSITIVE Z translation. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_positive_z"></a>

#### position\_positive\_z

```python
@position_positive_z.setter
def position_positive_z(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.position_negative_z"></a>

#### position\_negative\_z

```python
@property
def position_negative_z() -> float
```

(float):  [Read-Write] Multiply the NEGATIVE Z translation. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.position_negative_z"></a>

#### position\_negative\_z

```python
@position_negative_z.setter
def position_negative_z(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.rotation_alpha"></a>

#### rotation\_alpha

```python
@property
def rotation_alpha() -> float
```

(float):  [Read-Write] Blend the total rotational effect on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.rotation_alpha"></a>

#### rotation\_alpha

```python
@rotation_alpha.setter
def rotation_alpha(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.rotate_x_alpha"></a>

#### rotate\_x\_alpha

```python
@property
def rotate_x_alpha() -> float
```

(float):  [Read-Write] Blend the X-axis rotational effect on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.rotate_x_alpha"></a>

#### rotate\_x\_alpha

```python
@rotate_x_alpha.setter
def rotate_x_alpha(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.rotate_y_alpha"></a>

#### rotate\_y\_alpha

```python
@property
def rotate_y_alpha() -> float
```

(float):  [Read-Write] Blend the Y-axis rotational effect on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.rotate_y_alpha"></a>

#### rotate\_y\_alpha

```python
@rotate_y_alpha.setter
def rotate_y_alpha(value: float) -> None
```

<a id="unreal.IKRig_BodyMover.rotate_z_alpha"></a>

#### rotate\_z\_alpha

```python
@property
def rotate_z_alpha() -> float
```

(float):  [Read-Write] Blend the Z-axis rotational effect on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_BodyMover.rotate_z_alpha"></a>

#### rotate\_z\_alpha

```python
@rotate_z_alpha.setter
def rotate_z_alpha(value: float) -> None
```

<a id="unreal.IKRig_LimbEffector"></a>