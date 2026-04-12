## RootPrePullSettings Objects

```python
class RootPrePullSettings(StructBase)
```

Root Pre Pull Settings

**C++ Source:**

- **Plugin**: FullBodyIK
- **Module**: PBIK
- **File**: PBIKSolver.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``position_alpha`` (float):  [Read-Write] Range 0-1, default is 1. Apply a large scale position offset to the entire body prior to constraint solving.
- ``position_alpha_x`` (float):  [Read-Write] Range 0-1, default is 1. Blend contribution to position offset in the X axis in component space.
- ``position_alpha_y`` (float):  [Read-Write] Range 0-1, default is 1. Blend contribution to position offset in the Y axis in component space.
- ``position_alpha_z`` (float):  [Read-Write] Range 0-1, default is 1. Blend contribution to position offset in the Z axis in component space.
- ``rotation_alpha`` (float):  [Read-Write] Range 0-1, default is 0. Apply a large scale rotation offset to the entire body prior to constraint solving.
- ``rotation_alpha_x`` (float):  [Read-Write] Range 0-1, default is 1. Blend contribution to rotation offset in the X axis in component space.
- ``rotation_alpha_y`` (float):  [Read-Write] Range 0-1, default is 1. Blend contribution to rotation offset in the Y axis in component space.
- ``rotation_alpha_z`` (float):  [Read-Write] Range 0-1, default is 1. Blend contribution to rotation offset in the Z axis in component space.

<a id="unreal.RootPrePullSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rotation_alpha: float = 0.000000,
             rotation_alpha_x: float = 0.000000,
             rotation_alpha_y: float = 0.000000,
             rotation_alpha_z: float = 0.000000,
             position_alpha: float = 0.000000,
             position_alpha_x: float = 0.000000,
             position_alpha_y: float = 0.000000,
             position_alpha_z: float = 0.000000) -> None
```

<a id="unreal.RootPrePullSettings.rotation_alpha"></a>

#### rotation\_alpha

```python
@property
def rotation_alpha() -> float
```

(float):  [Read-Write] Range 0-1, default is 0. Apply a large scale rotation offset to the entire body prior to constraint solving.

<a id="unreal.RootPrePullSettings.rotation_alpha"></a>

#### rotation\_alpha

```python
@rotation_alpha.setter
def rotation_alpha(value: float) -> None
```

<a id="unreal.RootPrePullSettings.rotation_alpha_x"></a>

#### rotation\_alpha\_x

```python
@property
def rotation_alpha_x() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend contribution to rotation offset in the X axis in component space.

<a id="unreal.RootPrePullSettings.rotation_alpha_x"></a>

#### rotation\_alpha\_x

```python
@rotation_alpha_x.setter
def rotation_alpha_x(value: float) -> None
```

<a id="unreal.RootPrePullSettings.rotation_alpha_y"></a>

#### rotation\_alpha\_y

```python
@property
def rotation_alpha_y() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend contribution to rotation offset in the Y axis in component space.

<a id="unreal.RootPrePullSettings.rotation_alpha_y"></a>

#### rotation\_alpha\_y

```python
@rotation_alpha_y.setter
def rotation_alpha_y(value: float) -> None
```

<a id="unreal.RootPrePullSettings.rotation_alpha_z"></a>

#### rotation\_alpha\_z

```python
@property
def rotation_alpha_z() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend contribution to rotation offset in the Z axis in component space.

<a id="unreal.RootPrePullSettings.rotation_alpha_z"></a>

#### rotation\_alpha\_z

```python
@rotation_alpha_z.setter
def rotation_alpha_z(value: float) -> None
```

<a id="unreal.RootPrePullSettings.position_alpha"></a>

#### position\_alpha

```python
@property
def position_alpha() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Apply a large scale position offset to the entire body prior to constraint solving.

<a id="unreal.RootPrePullSettings.position_alpha"></a>

#### position\_alpha

```python
@position_alpha.setter
def position_alpha(value: float) -> None
```

<a id="unreal.RootPrePullSettings.position_alpha_x"></a>

#### position\_alpha\_x

```python
@property
def position_alpha_x() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend contribution to position offset in the X axis in component space.

<a id="unreal.RootPrePullSettings.position_alpha_x"></a>

#### position\_alpha\_x

```python
@position_alpha_x.setter
def position_alpha_x(value: float) -> None
```

<a id="unreal.RootPrePullSettings.position_alpha_y"></a>

#### position\_alpha\_y

```python
@property
def position_alpha_y() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend contribution to position offset in the Y axis in component space.

<a id="unreal.RootPrePullSettings.position_alpha_y"></a>

#### position\_alpha\_y

```python
@position_alpha_y.setter
def position_alpha_y(value: float) -> None
```

<a id="unreal.RootPrePullSettings.position_alpha_z"></a>

#### position\_alpha\_z

```python
@property
def position_alpha_z() -> float
```

(float):  [Read-Write] Range 0-1, default is 1. Blend contribution to position offset in the Z axis in component space.

<a id="unreal.RootPrePullSettings.position_alpha_z"></a>

#### position\_alpha\_z

```python
@position_alpha_z.setter
def position_alpha_z(value: float) -> None
```

<a id="unreal.PBIKSolverSettings"></a>