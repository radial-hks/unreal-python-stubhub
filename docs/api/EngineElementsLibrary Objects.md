## EngineElementsLibrary Objects

```python
class EngineElementsLibrary(BlueprintFunctionLibrary)
```

Engine Elements Library

**C++ Source:**

- **Module**: Engine
- **File**: EngineElementsLibrary.h

<a id="unreal.EngineElementsLibrary.k2_acquire_editor_sm_instance_element_handle"></a>

#### k2_acquire_editor_sm_instance_element_handle

```python
@classmethod
def k2_acquire_editor_sm_instance_element_handle(
        cls,
        ism_component: InstancedStaticMeshComponent,
        instance_index: int,
        allow_create: bool = True) -> ScriptTypedElementHandle
```

X.k2_acquire_editor_sm_instance_element_handle(ism_component, instance_index, allow_create=True) -> ScriptTypedElementHandle
K2 Acquire Editor SMInstance Element Handle

Args:
    ism_component (InstancedStaticMeshComponent): 
    instance_index (int32): 
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.EngineElementsLibrary.k2_acquire_editor_object_element_handle"></a>

#### k2_acquire_editor_object_element_handle

```python
@classmethod
def k2_acquire_editor_object_element_handle(
        cls,
        object: Object,
        allow_create: bool = True) -> ScriptTypedElementHandle
```

X.k2_acquire_editor_object_element_handle(object, allow_create=True) -> ScriptTypedElementHandle
K2 Acquire Editor Object Element Handle

Args:
    object (Object): 
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.EngineElementsLibrary.k2_acquire_editor_component_element_handle"></a>

#### k2_acquire_editor_component_element_handle

```python
@classmethod
def k2_acquire_editor_component_element_handle(
        cls,
        component: ActorComponent,
        allow_create: bool = True) -> ScriptTypedElementHandle
```

X.k2_acquire_editor_component_element_handle(component, allow_create=True) -> ScriptTypedElementHandle
K2 Acquire Editor Component Element Handle

Args:
    component (ActorComponent): 
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.EngineElementsLibrary.k2_acquire_editor_actor_element_handle"></a>

#### k2_acquire_editor_actor_element_handle

```python
@classmethod
def k2_acquire_editor_actor_element_handle(
        cls,
        actor: Actor,
        allow_create: bool = True) -> ScriptTypedElementHandle
```

X.k2_acquire_editor_actor_element_handle(actor, allow_create=True) -> ScriptTypedElementHandle
K2 Acquire Editor Actor Element Handle

Args:
    actor (Actor): 
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementCommonActions"></a>