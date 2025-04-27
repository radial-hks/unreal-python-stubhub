## PCGClusterSettings Objects

```python
class PCGClusterSettings(PCGSettings)
```

Given a desired number of clusters (categories), find the best fit cluster for each point by distance, using one of various clustering algorithms.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGClusterElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``algorithm`` (PCGClusterAlgorithm):  [Read-Write] Mathematical algorithm for selecting clusters.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``cluster_attribute`` (Name):  [Read-Write] Cluster IDs will be written to this attribute on the output.
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``max_iterations`` (int32):  [Read-Write] A limit on the number of iterations to run on each algorithm, if it doesn't otherwise converge. A higher number can offer more accuracy at the cost of processing time.
- ``num_clusters`` (int32):  [Read-Write] Number of clusters (segments) to group the points into. Each point will be assigned a cluster at the end.
- ``output_final_centroids`` (bool):  [Read-Write] Output the final location of the centroids or gaussians.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``tolerance`` (double):  [Read-Write] For EM, the maximum allowed difference between the last two iterations' "Log Likelihood"--which converges from positive infinity to 0 in relation to point-to-cluster probabilities.
  It is exponential, so raising this number can offer faster iteration if exact precision isn't needed.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGClusterSettings.algorithm"></a>

#### algorithm

```python
@property
def algorithm() -> PCGClusterAlgorithm
```

(PCGClusterAlgorithm):  [Read-Write] Mathematical algorithm for selecting clusters.

<a id="unreal.PCGClusterSettings.algorithm"></a>

#### algorithm

```python
@algorithm.setter
def algorithm(value: PCGClusterAlgorithm) -> None
```

<a id="unreal.PCGClusterSettings.num_clusters"></a>

#### num_clusters

```python
@property
def num_clusters() -> int
```

(int32):  [Read-Write] Number of clusters (segments) to group the points into. Each point will be assigned a cluster at the end.

<a id="unreal.PCGClusterSettings.num_clusters"></a>

#### num_clusters

```python
@num_clusters.setter
def num_clusters(value: int) -> None
```

<a id="unreal.PCGClusterSettings.cluster_attribute"></a>

#### cluster_attribute

```python
@property
def cluster_attribute() -> Name
```

(Name):  [Read-Write] Cluster IDs will be written to this attribute on the output.

<a id="unreal.PCGClusterSettings.cluster_attribute"></a>

#### cluster_attribute

```python
@cluster_attribute.setter
def cluster_attribute(value: Name) -> None
```

<a id="unreal.PCGClusterSettings.max_iterations"></a>

#### max_iterations

```python
@property
def max_iterations() -> int
```

(int32):  [Read-Write] A limit on the number of iterations to run on each algorithm, if it doesn't otherwise converge. A higher number can offer more accuracy at the cost of processing time.

<a id="unreal.PCGClusterSettings.max_iterations"></a>

#### max_iterations

```python
@max_iterations.setter
def max_iterations(value: int) -> None
```

<a id="unreal.PCGClusterSettings.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(double):  [Read-Write] For EM, the maximum allowed difference between the last two iterations' "Log Likelihood"--which converges from positive infinity to 0 in relation to point-to-cluster probabilities.
It is exponential, so raising this number can offer faster iteration if exact precision isn't needed.

<a id="unreal.PCGClusterSettings.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.PCGClusterSettings.output_final_centroids"></a>

#### output_final_centroids

```python
@property
def output_final_centroids() -> bool
```

(bool):  [Read-Write] Output the final location of the centroids or gaussians.

<a id="unreal.PCGClusterSettings.output_final_centroids"></a>

#### output_final_centroids

```python
@output_final_centroids.setter
def output_final_centroids(value: bool) -> None
```

<a id="unreal.PCGCollapsePointsSettings"></a>