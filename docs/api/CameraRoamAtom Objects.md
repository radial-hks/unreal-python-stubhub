## CameraRoamAtom Objects

```python
class CameraRoamAtom(EntityAtomBase)
```

Camera Roam Atom

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpCameraPreset
- **File**: CameraRoamAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_rotation`` (bool):  [Read-Only]
- ``frames`` (Array[WdpCameraRoamFrame]):  [Read-Only]
- ``reset_after_finished`` (bool):  [Read-Only]

<a id="unreal.CameraRoamAtom.frames"></a>

#### frames

```python
@property
def frames() -> Array[WdpCameraRoamFrame]
```

(Array[WdpCameraRoamFrame]):  [Read-Only]

<a id="unreal.CameraRoamAtom.auto_rotation"></a>

#### auto\_rotation

```python
@property
def auto_rotation() -> bool
```

(bool):  [Read-Only]

<a id="unreal.CameraRoamAtom.reset_after_finished"></a>

#### reset\_after\_finished

```python
@property
def reset_after_finished() -> bool
```

(bool):  [Read-Only]

<a id="unreal.CameraStartAtom"></a>