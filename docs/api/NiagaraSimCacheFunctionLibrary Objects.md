## NiagaraSimCacheFunctionLibrary Objects

```python
class NiagaraSimCacheFunctionLibrary(BlueprintFunctionLibrary)
```

Niagara Sim Cache Function Library

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSimCacheFunctionLibrary.h

<a id="unreal.NiagaraSimCacheFunctionLibrary.create_niagara_sim_cache"></a>

#### create_niagara_sim_cache

```python
@classmethod
def create_niagara_sim_cache(cls,
                             world_context_object: Object) -> NiagaraSimCache
```

X.create_niagara_sim_cache(world_context_object) -> NiagaraSimCache
Captures the simulation cache object that can be captured into using the various API calls.

Args:
    world_context_object (Object): 

Returns:
    NiagaraSimCache:

<a id="unreal.NiagaraSimCacheFunctionLibrary.capture_niagara_sim_cache_immediate"></a>

#### capture_niagara_sim_cache_immediate

```python
@classmethod
def capture_niagara_sim_cache_immediate(
        cls,
        sim_cache: NiagaraSimCache,
        create_parameters: NiagaraSimCacheCreateParameters,
        niagara_component: NiagaraComponent,
        advance_simulation: bool = False,
        advance_delta_time: float = 0.016660) -> Optional[NiagaraSimCache]
```

X.capture_niagara_sim_cache_immediate(sim_cache, create_parameters, niagara_component, advance_simulation=False, advance_delta_time=0.016660) -> NiagaraSimCache or None
Captures the simulations current frame data into the SimCache.
This happens immediately so you may need to be careful with tick order of the component you are capturing from.
The return can be invalid if the component can not be captured for some reason (i.e. not active).
When AdvanceSimulation is true we will manually advance the simulation one frame using the provided AdvanceDeltaTime before capturing.

Args:
    sim_cache (NiagaraSimCache): 
    create_parameters (NiagaraSimCacheCreateParameters): 
    niagara_component (NiagaraComponent): 
    advance_simulation (bool): 
    advance_delta_time (float): 

Returns:
    NiagaraSimCache or None: 

    out_sim_cache (NiagaraSimCache):

<a id="unreal.NiagaraSpriteRendererProperties"></a>