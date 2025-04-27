## DataflowSimulationActor Objects

```python
class DataflowSimulationActor(Interface)
```

Dataflow Simulation Actor

**C++ Source:**

- **Module**: DataflowSimulation
- **File**: DataflowSimulationManager.h

<a id="unreal.DataflowSimulationActor.pre_dataflow_simulation_tick"></a>

#### pre_dataflow_simulation_tick

```python
def pre_dataflow_simulation_tick(simulation_time: float,
                                 delta_time: float) -> None
```

x.pre_dataflow_simulation_tick(simulation_time, delta_time) -> None
Pre simulation callback function that can be implemented in C++ or Blueprint.

Args:
    simulation_time (float): 
    delta_time (float):

<a id="unreal.DataflowSimulationActor.post_dataflow_simulation_tick"></a>

#### post_dataflow_simulation_tick

```python
def post_dataflow_simulation_tick(simulation_time: float,
                                  delta_time: float) -> None
```

x.post_dataflow_simulation_tick(simulation_time, delta_time) -> None
Post simulation callback function that can be implemented in C++ or Blueprint.

Args:
    simulation_time (float): 
    delta_time (float):

<a id="unreal.ChaosDebugDrawComponent"></a>