## CameraRoamEntity Objects

```python
class CameraRoamEntity(WdpStandardEntity)
```

Camera Roam Entity

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpCameraPreset
- **File**: CameraRoamEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``current_frame_index`` (int32):  [Read-Only]
- ``current_frame_time`` (double):  [Read-Only]
- ``entity_atoms`` (Array[EntityAtomBase]):  [Read-Only]
- ``entity_id`` (int64):  [Read-Only]
- ``is_playing`` (bool):  [Read-Only]

<a id="unreal.CameraRoamEntity.current_frame_time"></a>

#### current\_frame\_time

```python
@property
def current_frame_time() -> float
```

(double):  [Read-Only]

<a id="unreal.CameraRoamEntity.current_frame_index"></a>

#### current\_frame\_index

```python
@property
def current_frame_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.CameraRoamEntity.is_playing"></a>

#### is\_playing

```python
@property
def is_playing() -> bool
```

(bool):  [Read-Only]

<a id="unreal.WdpCameraStartEntity"></a>