## LowEntryLatentActionStruct Objects

```python
class LowEntryLatentActionStruct(Object)
```

Low Entry Latent Action Struct

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLatentActionStruct.h

<a id="unreal.LowEntryLatentActionStruct.wait_till_done"></a>

#### wait\_till\_done

```python
def wait_till_done(world_context_object: Object,
                   latent_info: LatentActionInfo) -> InstancedStruct
```

x.wait_till_done(world_context_object, latent_info) -> InstancedStruct
Waits till the latent action is done.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 

Returns:
    InstancedStruct: 

    result (InstancedStruct):

<a id="unreal.LowEntryLatentActionStruct.is_done"></a>

#### is\_done

```python
def is_done() -> bool
```

x.is_done() -> bool
Returns true if the latent action is done.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionStruct.get_result"></a>

#### get\_result

```python
def get_result() -> InstancedStruct
```

x.get_result() -> InstancedStruct
Returns the result.

Returns:
    InstancedStruct: 

    result (InstancedStruct):

<a id="unreal.LowEntryLatentActionStruct.done"></a>

#### done

```python
def done(result: InstancedStruct) -> None
```

x.done(result) -> None
Causes the latent action to be done.

Args:
    result (InstancedStruct):

<a id="unreal.LowEntryLong"></a>