## ModelerRenderInfo Objects

```python
class ModelerRenderInfo(StructBase)
```

Modeler Render Info

**C++ Source:**

- **Plugin**: AesRuntime
- **Module**: UrbanScene
- **File**: UrbanModelerRender.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``build_resource`` (UrbanSceneBuildResource):  [Read-Write]
- ``eid_data`` (str):  [Read-Write]
- ``instanced_static_mesh_components`` (Array[InstancedStaticMeshComponent]):  [Read-Write]
- ``resource_data_nodes`` (Array[UrbanSceneNode_ResourceData]):  [Read-Write]
- ``static_mesh_components`` (Array[StaticMeshComponent]):  [Read-Write]
- ``static_mesh_nodes`` (Array[UrbanSceneNode_StaticMesh]):  [Read-Write]

<a id="unreal.ModelerRenderInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(build_resource: UrbanSceneBuildResource = None,
             static_mesh_components: Array[StaticMeshComponent] = [],
             instanced_static_mesh_components: Array[
                 InstancedStaticMeshComponent] = [],
             static_mesh_nodes: Array[UrbanSceneNode_StaticMesh] = [],
             resource_data_nodes: Array[UrbanSceneNode_ResourceData] = [],
             eid_data: str = "") -> None
```

<a id="unreal.ModelerRenderInfo.build_resource"></a>

#### build\_resource

```python
@property
def build_resource() -> UrbanSceneBuildResource
```

(UrbanSceneBuildResource):  [Read-Write]

<a id="unreal.ModelerRenderInfo.build_resource"></a>

#### build\_resource

```python
@build_resource.setter
def build_resource(value: UrbanSceneBuildResource) -> None
```

<a id="unreal.ModelerRenderInfo.static_mesh_components"></a>

#### static\_mesh\_components

```python
@property
def static_mesh_components() -> Array[StaticMeshComponent]
```

(Array[StaticMeshComponent]):  [Read-Write]

<a id="unreal.ModelerRenderInfo.static_mesh_components"></a>

#### static\_mesh\_components

```python
@static_mesh_components.setter
def static_mesh_components(value: Array[StaticMeshComponent]) -> None
```

<a id="unreal.ModelerRenderInfo.instanced_static_mesh_components"></a>

#### instanced\_static\_mesh\_components

```python
@property
def instanced_static_mesh_components() -> Array[InstancedStaticMeshComponent]
```

(Array[InstancedStaticMeshComponent]):  [Read-Write]

<a id="unreal.ModelerRenderInfo.instanced_static_mesh_components"></a>

#### instanced\_static\_mesh\_components

```python
@instanced_static_mesh_components.setter
def instanced_static_mesh_components(
        value: Array[InstancedStaticMeshComponent]) -> None
```

<a id="unreal.ModelerRenderInfo.static_mesh_nodes"></a>

#### static\_mesh\_nodes

```python
@property
def static_mesh_nodes() -> Array[UrbanSceneNode_StaticMesh]
```

(Array[UrbanSceneNode_StaticMesh]):  [Read-Write]

<a id="unreal.ModelerRenderInfo.static_mesh_nodes"></a>

#### static\_mesh\_nodes

```python
@static_mesh_nodes.setter
def static_mesh_nodes(value: Array[UrbanSceneNode_StaticMesh]) -> None
```

<a id="unreal.ModelerRenderInfo.resource_data_nodes"></a>

#### resource\_data\_nodes

```python
@property
def resource_data_nodes() -> Array[UrbanSceneNode_ResourceData]
```

(Array[UrbanSceneNode_ResourceData]):  [Read-Write]

<a id="unreal.ModelerRenderInfo.resource_data_nodes"></a>

#### resource\_data\_nodes

```python
@resource_data_nodes.setter
def resource_data_nodes(value: Array[UrbanSceneNode_ResourceData]) -> None
```

<a id="unreal.ModelerRenderInfo.eid_data"></a>

#### eid\_data

```python
@property
def eid_data() -> str
```

(str):  [Read-Write]

<a id="unreal.ModelerRenderInfo.eid_data"></a>

#### eid\_data

```python
@eid_data.setter
def eid_data(value: str) -> None
```

<a id="unreal.Eid"></a>