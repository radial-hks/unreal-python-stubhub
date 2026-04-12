## LowEntryLatentActionString Objects

```python
class LowEntryLatentActionString(Object)
```

Low Entry Latent Action String

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLatentActionString.h

<a id="unreal.LowEntryLatentActionString.wait_till_done"></a>

#### wait\_till\_done

```python
def wait_till_done(world_context_object: Object,
                   latent_info: LatentActionInfo) -> str
```

x.wait_till_done(world_context_object, latent_info) -> str
Waits till the latent action is done.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo): 

Returns:
    str: 

    result (str):

<a id="unreal.LowEntryLatentActionString.is_done"></a>

#### is\_done

```python
def is_done() -> bool
```

x.is_done() -> bool
Returns true if the latent action is done.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionString.get_result"></a>

#### get\_result

```python
def get_result() -> str
```

x.get_result() -> str
Returns the result.

Returns:
    str: 

    result (str):

<a id="unreal.LowEntryLatentActionString.done"></a>

#### done

```python
def done(result: str) -> None
```

x.done(result) -> None
Causes the latent action to be done.

Args:
    result (str):

<a id="unreal.LowEntryLatentActionStruct"></a>