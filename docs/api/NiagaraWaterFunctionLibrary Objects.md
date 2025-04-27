## NiagaraWaterFunctionLibrary Objects

```python
class NiagaraWaterFunctionLibrary(BlueprintFunctionLibrary)
```

Niagara Water Function Library

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: NiagaraWaterFunctionLibrary.h

<a id="unreal.NiagaraWaterFunctionLibrary.set_water_body_component"></a>

#### set_water_body_component

```python
@classmethod
def set_water_body_component(cls, niagara_system: NiagaraComponent,
                             override_name: str,
                             water_body_component: WaterBodyComponent) -> None
```

X.set_water_body_component(niagara_system, override_name, water_body_component) -> None
Sets the water body component on the Niagra water data interface on a Niagara particle system

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    water_body_component (WaterBodyComponent):

<a id="unreal.NiagaraWaterFunctionLibrary.set_water_body"></a>

#### set_water_body

```python
@classmethod
def set_water_body(cls, niagara_system: NiagaraComponent, override_name: str,
                   water_body: WaterBody) -> None
```

X.set_water_body(niagara_system, override_name, water_body) -> None
Set Water Body
deprecated: Use SetWaterBodyComponent instead

Args:
    niagara_system (NiagaraComponent): 
    override_name (str): 
    water_body (WaterBody):

<a id="unreal.OceanCollisionComponent"></a>