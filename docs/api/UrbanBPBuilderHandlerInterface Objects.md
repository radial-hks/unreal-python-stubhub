## UrbanBPBuilderHandlerInterface Objects

```python
class UrbanBPBuilderHandlerInterface(Interface)
```

Urban BPBuilder Handler Interface

**C++ Source:**

- **Plugin**: AesBuilder
- **Module**: UrbanEntityBuilder
- **File**: UrbanBPBuilderHandlerInterface.h

<a id="unreal.UrbanBPBuilderHandlerInterface.receive_static_mesh_nodes"></a>

#### receive\_static\_mesh\_nodes

```python
def receive_static_mesh_nodes(
        static_mesh_nodes: Array[UrbanSceneNode_StaticMesh]) -> None
```

x.receive_static_mesh_nodes(static_mesh_nodes) -> None
Override for set extern data

Args:
    static_mesh_nodes (Array[UrbanSceneNode_StaticMesh]):

<a id="unreal.UrbanBPBuilderHandlerInterface.receive_resource_data_nodes"></a>

#### receive\_resource\_data\_nodes

```python
def receive_resource_data_nodes(
        resource_data_nodes: Array[UrbanSceneNode_ResourceData]) -> None
```

x.receive_resource_data_nodes(resource_data_nodes) -> None
Receive Resource Data Nodes

Args:
    resource_data_nodes (Array[UrbanSceneNode_ResourceData]):

<a id="unreal.UrbanBPBuilderHandlerInterface.receive_property_string"></a>

#### receive\_property\_string

```python
def receive_property_string(new: bool, modeler_path: str,
                            property_string: Array[str]) -> None
```

x.receive_property_string(new, modeler_path, property_string) -> None
Receive Property String

Args:
    new (bool): 
    modeler_path (str): 
    property_string (Array[str]):

<a id="unreal.UrbanBPBuilderHandlerInterface.receive_eid_data"></a>

#### receive\_eid\_data

```python
def receive_eid_data(eid_data: str) -> None
```

x.receive_eid_data(eid_data) -> None
Receive Eid Data

Args:
    eid_data (str):

<a id="unreal.UrbanBPBuilderHandlerInterface.on_finished"></a>

#### on\_finished

```python
def on_finished(identity_name: str, build_result: bool,
                build_resource: UrbanSceneBuildResource) -> None
```

x.on_finished(identity_name, build_result, build_resource) -> None
On Finished

Args:
    identity_name (str): 
    build_result (bool): 
    build_resource (UrbanSceneBuildResource):

<a id="unreal.UrbanBpBuildPyCallable"></a>