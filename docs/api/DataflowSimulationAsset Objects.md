## DataflowSimulationAsset Objects

```python
class DataflowSimulationAsset(StructBase)
```

Dataflow simulation asset (should be in the interface children)

**C++ Source:**

- **Module**: DataflowSimulation
- **File**: DataflowSimulationInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dataflow_asset`` (Dataflow):  [Read-Write] Simulation dataflow asset used to advance in time on Pt
- ``simulation_groups`` (Set[str]):  [Read-Write] Simulation groups used to filter within the simulation nodes

<a id="unreal.DataflowSimulationAsset.__init__"></a>

#### \_\_init\_\_

```python
def __init__(dataflow_asset: Dataflow = None,
             simulation_groups: Set[str] = []) -> None
```

<a id="unreal.DataflowSimulationAsset.dataflow_asset"></a>

#### dataflow\_asset

```python
@property
def dataflow_asset() -> Dataflow
```

(Dataflow):  [Read-Write] Simulation dataflow asset used to advance in time on Pt

<a id="unreal.DataflowSimulationAsset.dataflow_asset"></a>

#### dataflow\_asset

```python
@dataflow_asset.setter
def dataflow_asset(value: Dataflow) -> None
```

<a id="unreal.DataflowSimulationAsset.simulation_groups"></a>

#### simulation\_groups

```python
@property
def simulation_groups() -> Set[str]
```

(Set[str]):  [Read-Write] Simulation groups used to filter within the simulation nodes

<a id="unreal.DataflowSimulationAsset.simulation_groups"></a>

#### simulation\_groups

```python
@simulation_groups.setter
def simulation_groups(value: Set[str]) -> None
```

<a id="unreal.DataflowSimulationProperty"></a>