## NiagaraParticleCallbackHandler Objects

```python
class NiagaraParticleCallbackHandler(Interface)
```

Niagara Particle Callback Handler

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceExport.h

<a id="unreal.NiagaraParticleCallbackHandler.receive_particle_data"></a>

#### receive_particle_data

```python
def receive_particle_data(data: Array[BasicParticleData],
                          niagara_system: NiagaraSystem,
                          simulation_position_offset: Vector) -> None
```

x.receive_particle_data(data, niagara_system, simulation_position_offset) -> None
This function is called once per tick with the gathered particle data. It will not be called if there is no particle data to call it with.

Args:
    data (Array[BasicParticleData]): 
    niagara_system (NiagaraSystem): 
    simulation_position_offset (Vector):

<a id="unreal.NiagaraDataInterfaceGrid2D"></a>