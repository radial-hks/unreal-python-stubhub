## LowEntryLatentActionNone Objects

```python
class LowEntryLatentActionNone(Object)
```

Low Entry Latent Action None

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: LowEntryLatentActionNone.h

<a id="unreal.LowEntryLatentActionNone.wait_till_done"></a>

#### wait\_till\_done

```python
def wait_till_done(world_context_object: Object,
                   latent_info: LatentActionInfo) -> None
```

x.wait_till_done(world_context_object, latent_info) -> None
Waits till the latent action is done.

Args:
    world_context_object (Object): 
    latent_info (LatentActionInfo):

<a id="unreal.LowEntryLatentActionNone.is_done"></a>

#### is\_done

```python
def is_done() -> bool
```

x.is_done() -> bool
Returns true if the latent action is done.

Returns:
    bool:

<a id="unreal.LowEntryLatentActionNone.done"></a>

#### done

```python
def done() -> None
```

x.done() -> None
Causes the latent action to be done.

<a id="unreal.LowEntryLatentActionObject"></a>