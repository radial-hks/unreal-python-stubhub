## NiagaraDataInterfaceRenderTargetCube Objects

```python
class NiagaraDataInterfaceRenderTargetCube(NiagaraDataInterfaceRWBase)
```

Niagara Data Interface Render Target Cube

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceRenderTargetCube.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inherit_user_parameter_settings`` (bool):  [Read-Write] When enabled texture parameters (size / etc) are taken from the user provided render target.
  If no valid user parameter is set the system will be invalid.
  Note: The resource will be recreated if UAV access is not available, which will reset the contents.
- ``override_format`` (bool):  [Read-Write]
- ``override_render_target_filter`` (TextureFilter):  [Read-Write] When enabled overrides the filter of the render target, otherwise uses the project default setting.
- ``override_render_target_format`` (TextureRenderTargetFormat):  [Read-Write] When enabled overrides the format of the render target, otherwise uses the project default setting.
- ``preview_render_target`` (bool):  [Read-Write]
- ``render_target_user_parameter`` (NiagaraUserParameterBinding):  [Read-Write] When valid the user parameter is used as the render target rather than creating one internal, note that the input render target will be adjusted by the Niagara simulation
- ``size`` (int32):  [Read-Write]

<a id="unreal.NiagaraDataInterfaceRenderTargetVolume"></a>