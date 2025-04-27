## NiagaraDataInterfaceSceneCapture2D Objects

```python
class NiagaraDataInterfaceSceneCapture2D(NiagaraDataInterface)
```

Data Interface which can control or read from a scene capture component.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceSceneCapture2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_move_offset_location`` (Vector):  [Read-Write] Location offset when applying auto movement.
- ``auto_move_offset_location_mode`` (NDISceneCapture2DOffsetMode):  [Read-Write] Should we apply the auto move offset in local or world space?
- ``auto_move_offset_rotation`` (Rotator):  [Read-Write] Rotation offset when applying auto movement.
- ``auto_move_offset_rotation_mode`` (NDISceneCapture2DOffsetMode):  [Read-Write] How we should apply the rotation
- ``auto_move_with_component`` (bool):  [Read-Write] When enabled the scene capture component will be automatically moved to the location of the NiagaraComponent with an optional offset.
- ``managed_capture_every_frame`` (bool):  [Read-Write]
- ``managed_capture_on_movement`` (bool):  [Read-Write]
- ``managed_capture_source`` (SceneCaptureSource):  [Read-Write]
- ``managed_fov_angle`` (float):  [Read-Write]
- ``managed_ortho_width`` (float):  [Read-Write]
- ``managed_projection_type`` (CameraProjectionMode):  [Read-Write]
- ``managed_show_only_actors`` (Array[Actor]):  [Read-Write]
- ``managed_texture_format`` (TextureRenderTargetFormat):  [Read-Write]
- ``managed_texture_size`` (IntPoint):  [Read-Write]
- ``scene_capture_user_parameter`` (NiagaraUserParameterBinding):  [Read-Write] When valid should point to either a Scene Capture 2D Component or a Scene Capture 2D Actor.
- ``source_mode`` (NDISceneCapture2DSourceMode):  [Read-Write] How should we find the scene capture component to use?

<a id="unreal.NiagaraDataInterfaceSceneCapture2D.set_scene_capture2d_managed_show_only_actors"></a>

#### set_scene_capture2d_managed_show_only_actors

```python
@classmethod
def set_scene_capture2d_managed_show_only_actors(
        cls, niagara_system: NiagaraComponent, parameter_name: Name,
        show_only_actors: Array[Actor]) -> None
```

X.set_scene_capture2d_managed_show_only_actors(niagara_system, parameter_name, show_only_actors) -> None
Allows you to set the show only actors when Niagara manages the component.  If Niagara does not manage the component use the regular BP methods.

Args:
    niagara_system (NiagaraComponent): 
    parameter_name (Name): 
    show_only_actors (Array[Actor]):

<a id="unreal.NiagaraDataInterfaceStaticMesh"></a>