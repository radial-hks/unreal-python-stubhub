## PCGSaveDynamicMeshToAssetSettings Objects

```python
class PCGSaveDynamicMeshToAssetSettings(PCGDynamicMeshBaseSettings)
```

Saves dynamic mesh data into a static mesh asset.

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGSaveDynamicMeshToAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``copy_mesh_to_asset_options`` (GeometryScriptCopyMeshToAssetOptions):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``export_materials_from_dynamic_mesh`` (bool):  [Read-Write] This option has higher priority than CopyMeshToAssetOptions.ReplaceMaterials.
  If true, we will replace the materials from the materials stored on the PCG Dynamic Mesh data.
  Otherwise, we will follow what is set in CopyMeshToAssetOptions.
- ``export_params`` (PCGAssetExporterParameters):  [Read-Write]
- ``expose_to_library`` (bool):  [Read-Write]
- ``mesh_write_lod`` (GeometryScriptMeshWriteLOD):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.export_params"></a>

#### export_params

```python
@property
def export_params() -> PCGAssetExporterParameters
```

(PCGAssetExporterParameters):  [Read-Write]

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.export_params"></a>

#### export_params

```python
@export_params.setter
def export_params(value: PCGAssetExporterParameters) -> None
```

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.export_materials_from_dynamic_mesh"></a>

#### export_materials_from_dynamic_mesh

```python
@property
def export_materials_from_dynamic_mesh() -> bool
```

(bool):  [Read-Write] This option has higher priority than CopyMeshToAssetOptions.ReplaceMaterials.
If true, we will replace the materials from the materials stored on the PCG Dynamic Mesh data.
Otherwise, we will follow what is set in CopyMeshToAssetOptions.

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.export_materials_from_dynamic_mesh"></a>

#### export_materials_from_dynamic_mesh

```python
@export_materials_from_dynamic_mesh.setter
def export_materials_from_dynamic_mesh(value: bool) -> None
```

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.copy_mesh_to_asset_options"></a>

#### copy_mesh_to_asset_options

```python
@property
def copy_mesh_to_asset_options() -> GeometryScriptCopyMeshToAssetOptions
```

(GeometryScriptCopyMeshToAssetOptions):  [Read-Write]

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.copy_mesh_to_asset_options"></a>

#### copy_mesh_to_asset_options

```python
@copy_mesh_to_asset_options.setter
def copy_mesh_to_asset_options(
        value: GeometryScriptCopyMeshToAssetOptions) -> None
```

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.mesh_write_lod"></a>

#### mesh_write_lod

```python
@property
def mesh_write_lod() -> GeometryScriptMeshWriteLOD
```

(GeometryScriptMeshWriteLOD):  [Read-Write]

<a id="unreal.PCGSaveDynamicMeshToAssetSettings.mesh_write_lod"></a>

#### mesh_write_lod

```python
@mesh_write_lod.setter
def mesh_write_lod(value: GeometryScriptMeshWriteLOD) -> None
```

<a id="unreal.PCGSpawnDynamicMeshSettings"></a>