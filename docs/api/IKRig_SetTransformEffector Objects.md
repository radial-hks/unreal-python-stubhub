## IKRig_SetTransformEffector Objects

```python
class IKRig_SetTransformEffector(Object)
```

IKRig Set Transform Effector

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRig_SetTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Blend the effector on/off. Range is 0-1. Default is 1.0.
- ``enable_position`` (bool):  [Read-Write] If true, Goal will drive the translation of the target bone. Default is true.
- ``enable_rotation`` (bool):  [Read-Write] If true, Goal will drive the rotation of the target bone. Default is true.

<a id="unreal.IKRig_SetTransformEffector.enable_position"></a>

#### enable_position

```python
@property
def enable_position() -> bool
```

(bool):  [Read-Write] If true, Goal will drive the translation of the target bone. Default is true.

<a id="unreal.IKRig_SetTransformEffector.enable_position"></a>

#### enable_position

```python
@enable_position.setter
def enable_position(value: bool) -> None
```

<a id="unreal.IKRig_SetTransformEffector.enable_rotation"></a>

#### enable_rotation

```python
@property
def enable_rotation() -> bool
```

(bool):  [Read-Write] If true, Goal will drive the rotation of the target bone. Default is true.

<a id="unreal.IKRig_SetTransformEffector.enable_rotation"></a>

#### enable_rotation

```python
@enable_rotation.setter
def enable_rotation(value: bool) -> None
```

<a id="unreal.IKRig_SetTransformEffector.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write] Blend the effector on/off. Range is 0-1. Default is 1.0.

<a id="unreal.IKRig_SetTransformEffector.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.IKRig_SetTransform"></a>