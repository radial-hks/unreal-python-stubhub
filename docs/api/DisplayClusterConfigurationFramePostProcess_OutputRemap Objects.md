## DisplayClusterConfigurationFramePostProcess_OutputRemap Objects

```python
class DisplayClusterConfigurationFramePostProcess_OutputRemap(StructBase)
```

Screen space remapping of the final backbuffer output. Applied at the whole window

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_OutputRemap.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_source`` (DisplayClusterConfigurationFramePostProcess_OutputRemapSource):  [Read-Write] Selects either the Static Mesh or External File setting as the source for output remapping
- ``enable`` (bool):  [Read-Write] Enables or disables output remapping
- ``external_file`` (str):  [Read-Write] The external .obj file to use for output remapping when the Data Source is set to File
- ``mesh_component_name`` (str):  [Read-Write] The MeshComponent reference (ProceduralMeshComponent or StaticMeshComponent) to use for output remapping when the Data Source is set to Mesh Component
- ``static_mesh`` (StaticMesh):  [Read-Write] The Static Mesh reference to use for output remapping when the Data Source is set to Static Mesh

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.__init__"></a>

#### __init__

```python
def __init__(
        enable: bool = False,
        data_source:
    DisplayClusterConfigurationFramePostProcess_OutputRemapSource = DisplayClusterConfigurationFramePostProcess_OutputRemapSource
    .STATIC_MESH,
        static_mesh: StaticMesh = None,
        mesh_component_name: str = "",
        external_file: str = "") -> None
```

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.enable"></a>

#### enable

```python
@property
def enable() -> bool
```

(bool):  [Read-Write] Enables or disables output remapping

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.enable"></a>

#### enable

```python
@enable.setter
def enable(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.data_source"></a>

#### data_source

```python
@property
def data_source(
) -> DisplayClusterConfigurationFramePostProcess_OutputRemapSource
```

(DisplayClusterConfigurationFramePostProcess_OutputRemapSource):  [Read-Write] Selects either the Static Mesh or External File setting as the source for output remapping

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.data_source"></a>

#### data_source

```python
@data_source.setter
def data_source(
    value: DisplayClusterConfigurationFramePostProcess_OutputRemapSource
) -> None
```

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Only] The Static Mesh reference to use for output remapping when the Data Source is set to Static Mesh

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.mesh_component_name"></a>

#### mesh_component_name

```python
@property
def mesh_component_name() -> str
```

(str):  [Read-Only] The MeshComponent reference (ProceduralMeshComponent or StaticMeshComponent) to use for output remapping when the Data Source is set to Mesh Component

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.external_file"></a>

#### external_file

```python
@property
def external_file() -> str
```

(str):  [Read-Write] The external .obj file to use for output remapping when the Data Source is set to File

<a id="unreal.DisplayClusterConfigurationFramePostProcess_OutputRemap.external_file"></a>

#### external_file

```python
@external_file.setter
def external_file(value: str) -> None
```

<a id="unreal.DisplayClusterConfigurationTile_Settings"></a>