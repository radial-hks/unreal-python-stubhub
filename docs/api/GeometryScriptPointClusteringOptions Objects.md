## GeometryScriptPointClusteringOptions Objects

```python
class GeometryScriptPointClusteringOptions(StructBase)
```

Geometry Script Point Clustering Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PointSetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial_cluster_centers`` (Array[Vector]):  [Read-Write] If not empty, will be used instead of Target Num Clusters. Specifies the initial cluster centers to use.
- ``initialize_method`` (GeometryScriptInitKMeansMethod):  [Read-Write] Method to initialize the cluster centers, if Initial Cluster Centers is empty
- ``max_iterations`` (int32):  [Read-Write] Maximum iterations to run the clustering process. Will stop earlier if/when clustering converges.
- ``random_seed`` (int32):  [Read-Write] Random Seed used to initialize clustering, if the Random cluster initialization is chosen
- ``target_num_clusters`` (int32):  [Read-Write] Number of clusters requested, if Initial Cluster Centers is empty. Actual clusters generated may be smaller, e.g. if there are fewer points

<a id="unreal.GeometryScriptPointClusteringOptions.__init__"></a>

#### __init__

```python
def __init__(
        initial_cluster_centers: Array[Vector] = [],
        target_num_clusters: int = 0,
        initialize_method:
    GeometryScriptInitKMeansMethod = GeometryScriptInitKMeansMethod.RANDOM,
        random_seed: int = 0,
        max_iterations: int = 0) -> None
```

<a id="unreal.GeometryScriptPointClusteringOptions.initial_cluster_centers"></a>

#### initial_cluster_centers

```python
@property
def initial_cluster_centers() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] If not empty, will be used instead of Target Num Clusters. Specifies the initial cluster centers to use.

<a id="unreal.GeometryScriptPointClusteringOptions.initial_cluster_centers"></a>

#### initial_cluster_centers

```python
@initial_cluster_centers.setter
def initial_cluster_centers(value: Array[Vector]) -> None
```

<a id="unreal.GeometryScriptPointClusteringOptions.target_num_clusters"></a>

#### target_num_clusters

```python
@property
def target_num_clusters() -> int
```

(int32):  [Read-Write] Number of clusters requested, if Initial Cluster Centers is empty. Actual clusters generated may be smaller, e.g. if there are fewer points

<a id="unreal.GeometryScriptPointClusteringOptions.target_num_clusters"></a>

#### target_num_clusters

```python
@target_num_clusters.setter
def target_num_clusters(value: int) -> None
```

<a id="unreal.GeometryScriptPointClusteringOptions.initialize_method"></a>

#### initialize_method

```python
@property
def initialize_method() -> GeometryScriptInitKMeansMethod
```

(GeometryScriptInitKMeansMethod):  [Read-Write] Method to initialize the cluster centers, if Initial Cluster Centers is empty

<a id="unreal.GeometryScriptPointClusteringOptions.initialize_method"></a>

#### initialize_method

```python
@initialize_method.setter
def initialize_method(value: GeometryScriptInitKMeansMethod) -> None
```

<a id="unreal.GeometryScriptPointClusteringOptions.random_seed"></a>

#### random_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Write] Random Seed used to initialize clustering, if the Random cluster initialization is chosen

<a id="unreal.GeometryScriptPointClusteringOptions.random_seed"></a>

#### random_seed

```python
@random_seed.setter
def random_seed(value: int) -> None
```

<a id="unreal.GeometryScriptPointClusteringOptions.max_iterations"></a>

#### max_iterations

```python
@property
def max_iterations() -> int
```

(int32):  [Read-Write] Maximum iterations to run the clustering process. Will stop earlier if/when clustering converges.

<a id="unreal.GeometryScriptPointClusteringOptions.max_iterations"></a>

#### max_iterations

```python
@max_iterations.setter
def max_iterations(value: int) -> None
```

<a id="unreal.GeometryScriptPointPriorityOptions"></a>