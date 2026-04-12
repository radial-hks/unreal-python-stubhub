## ProjectToolLibrary Objects

```python
class ProjectToolLibrary(BlueprintFunctionLibrary)
```

Project Tool Library

**C++ Source:**

- **Plugin**: WdpProjectTools
- **Module**: WdpProjectTools
- **File**: ProjectToolLibrary.h

<a id="unreal.ProjectToolLibrary.update_id_info"></a>

#### update\_id\_info

```python
@classmethod
def update_id_info(cls, actor_name: Name, eid_str: str, ism_name: Name,
                   instance_index_str: str, node_id_str: str) -> None
```

X.update_id_info(actor_name, eid_str, ism_name, instance_index_str, node_id_str) -> None
Update Id Info

Args:
    actor_name (Name): 
    eid_str (str): 
    ism_name (Name): 
    instance_index_str (str): 
    node_id_str (str):

<a id="unreal.ProjectToolLibrary.set_layer_name_for_selected_actors"></a>

#### set\_layer\_name\_for\_selected\_actors

```python
@classmethod
def set_layer_name_for_selected_actors(cls, layer_name: str) -> None
```

X.set_layer_name_for_selected_actors(layer_name) -> None
Set Layer Name for Selected Actors

Args:
    layer_name (str):

<a id="unreal.ProjectToolLibrary.remove_node_id_for_selected_ism_actors"></a>

#### remove\_node\_id\_for\_selected\_ism\_actors

```python
@classmethod
def remove_node_id_for_selected_ism_actors(cls) -> None
```

X.remove_node_id_for_selected_ism_actors() -> None
UFUNCTION(BlueprintCallable, Category = "WdpProjectTools|ProjectIdsExportLibrary")
static void AllocNodeIdForAllISMActors();

<a id="unreal.ProjectToolLibrary.remove_node_id_for_all_ism_actors"></a>

#### remove\_node\_id\_for\_all\_ism\_actors

```python
@classmethod
def remove_node_id_for_all_ism_actors(cls) -> None
```

X.remove_node_id_for_all_ism_actors() -> None
Remove Node Id for All ISMActors

<a id="unreal.ProjectToolLibrary.remove_layer_name_for_selected_actors"></a>

#### remove\_layer\_name\_for\_selected\_actors

```python
@classmethod
def remove_layer_name_for_selected_actors(cls) -> None
```

X.remove_layer_name_for_selected_actors() -> None
Remove Layer Name for Selected Actors

<a id="unreal.ProjectToolLibrary.remove_layer_name_for_all_actors"></a>

#### remove\_layer\_name\_for\_all\_actors

```python
@classmethod
def remove_layer_name_for_all_actors(cls) -> None
```

X.remove_layer_name_for_all_actors() -> None
Remove Layer Name for All Actors

<a id="unreal.ProjectToolLibrary.remove_id_for_selected_actors"></a>

#### remove\_id\_for\_selected\_actors

```python
@classmethod
def remove_id_for_selected_actors(cls) -> None
```

X.remove_id_for_selected_actors() -> None
UFUNCTION(BlueprintCallable, Category = "WdpProjectTools|ProjectIdsExportLibrary")
static void AllocIdForAllActors();

<a id="unreal.ProjectToolLibrary.remove_id_for_all_actors"></a>

#### remove\_id\_for\_all\_actors

```python
@classmethod
def remove_id_for_all_actors(cls) -> None
```

X.remove_id_for_all_actors() -> None
Remove Id for All Actors

<a id="unreal.ProjectToolLibrary.register_selection_changed"></a>

#### register\_selection\_changed

```python
@classmethod
def register_selection_changed(cls, widget: WdpProjectToolWidget) -> None
```

X.register_selection_changed(widget) -> None
Register Selection Changed

Args:
    widget (WdpProjectToolWidget):

<a id="unreal.ProjectToolLibrary.import_project_ids"></a>

#### import\_project\_ids

```python
@classmethod
def import_project_ids(cls) -> None
```

X.import_project_ids() -> None
Import Project Ids

<a id="unreal.ProjectToolLibrary.get_project_entity_id_by_name"></a>

#### get\_project\_entity\_id\_by\_name

```python
@classmethod
def get_project_entity_id_by_name(cls, actor: Actor) -> Optional[int]
```

X.get_project_entity_id_by_name(actor) -> int32 or None
Get Project Entity Id by Name

Args:
    actor (Actor): 

Returns:
    int32 or None: 

    out_id (int32):

<a id="unreal.ProjectToolLibrary.get_node_id_by_instance_info"></a>

#### get\_node\_id\_by\_instance\_info

```python
@classmethod
def get_node_id_by_instance_info(cls, actor: Actor, comp_name: Name,
                                 instance_index: int) -> Optional[int]
```

X.get_node_id_by_instance_info(actor, comp_name, instance_index) -> int32 or None
Get Node Id by Instance Info

Args:
    actor (Actor): 
    comp_name (Name): 
    instance_index (int32): 

Returns:
    int32 or None: 

    out_node_id (int32):

<a id="unreal.ProjectToolLibrary.export_project_ids"></a>

#### export\_project\_ids

```python
@classmethod
def export_project_ids(cls) -> None
```

X.export_project_ids() -> None
Export Project Ids

<a id="unreal.ProjectToolLibrary.alloc_node_id_for_selected_ism_actors"></a>

#### alloc\_node\_id\_for\_selected\_ism\_actors

```python
@classmethod
def alloc_node_id_for_selected_ism_actors(cls) -> None
```

X.alloc_node_id_for_selected_ism_actors() -> None
Alloc Node Id for Selected ISMActors

<a id="unreal.ProjectToolLibrary.alloc_id_for_selected_actors"></a>

#### alloc\_id\_for\_selected\_actors

```python
@classmethod
def alloc_id_for_selected_actors(cls) -> None
```

X.alloc_id_for_selected_actors() -> None
Alloc Id for Selected Actors

<a id="unreal.WdpProjectToolWidget"></a>