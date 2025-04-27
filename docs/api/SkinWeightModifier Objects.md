## SkinWeightModifier Objects

```python
class SkinWeightModifier(Object)
```

API used to modify skin weights on a Skeletal Mesh asset.

To use:
1. Instantiate an instance of USkinWeightModifier
2. Call "SetSkeletalMesh(MyMeshAsset)", passing in the skeletal mesh you want to edit weights on
3. Use Get/Set weights functions, and Normalize/Prune to edit the weights as desired
4. When ready to commit to the asset, call CommitWeightsToSkeletalMesh() and save the asset if desired

This API can be used from C++, Blueprint or Python. Here is a sample usage of the API in Python:

import unreal

# create a weight modifier for a given skeletal mesh
skel_mesh = unreal.EditorAssetLibrary().load_asset("/Game/Characters/Wolf/Meshes/SK_Wolf")
weight_modifier = unreal.SkinWeightModifier()
weight_modifier.set_skeletal_mesh(skel_mesh)

# get weight of vertex 1234
vertex_weights = weight_modifier.get_vertex_weights(1234)
print(vertex_weights)

# remove neck2 as an influence on this vertex
vertex_weights.pop("neck2")
weight_modifier.set_vertex_weights(vertex_weights, True)
print(vertex_weights)

# commit change to the skeletal mesh
weight_modifier.commit_weights_to_skeletal_mesh()

OUTPUT:
{"head": 0.6, "neck1": 0.3, "neck2": 0.1}
{"head": 0.6, "neck1": 0.3}

In Python, the per-vertex weights are stored as a dictionary mapping Bone Names to float weight values.

The "SetVertexWeights()" function expects the same data structure. You can add/remove/edit influences as needed.
The SetVertexWeights() function does not normalize the weights. So you can make multiple modifications
and call NormalizeVertexWeights() or NormalizeAllWeights() as desired.

The PruneVertexWeights() and EnforceMaxInfluences() functions can be used to trim small influences
and clamp the total number of influences per vertex as needed.

Note that it is not required to normalize the weights by calling any of the normalize functions. Or manually before
calling SetVertexWeights(). Committing the weights to the skeletal mesh will always enforce normalization.

Though it may be useful to normalize while editing.

**C++ Source:**

- **Plugin**: MeshModelingToolsetExp
- **Module**: SkeletalMeshModifiers
- **File**: SkinWeightModifier.h

<a id="unreal.SkinWeightModifier.set_vertex_weights"></a>

#### set_vertex_weights

```python
def set_vertex_weights(vertex_id: int,
                       weights: Map[Name, float],
                       replace_all: bool = False) -> bool
```

x.set_vertex_weights(vertex_id, weights, replace_all=False) -> bool
Set bone weights for a single vertex. The weights are stored as supplied and not normalized until
either "CommitWeightsToSkeletalMesh()" or "NormalizeVertexWeights()" is called.

Args:
    vertex_id (int32): the index of the vertex
    weights (Map[Name, float]): a map of Bone-Name to Weight for all bones that influence the specified vertex, ie {"Head": 0.6, "Neck": 0.4}
    replace_all (bool): if true, all weights on this vertex will be replaced with the input weights. Default is false.

Returns:
    bool:

<a id="unreal.SkinWeightModifier.set_skeletal_mesh"></a>

#### set_skeletal_mesh

```python
def set_skeletal_mesh(mesh: SkeletalMesh) -> bool
```

x.set_skeletal_mesh(mesh) -> bool
Call this first to load the weights for a skeletal mesh for fast editing.

Args:
    mesh (SkeletalMesh): The skeletal mesh asset to load for weight editing

Returns:
    bool: bool - true if the mesh weights were successfully loaded.

<a id="unreal.SkinWeightModifier.prune_vertex_weights"></a>

#### prune_vertex_weights

```python
def prune_vertex_weights(vertex_id: int, weight_threshold: float) -> bool
```

x.prune_vertex_weights(vertex_id, weight_threshold) -> bool
Remove all weights below the given threshold value, on the given vertex.
Influences that are pruned will no longer receive weight from normalization.

Args:
    vertex_id (int32): the index of the vertex to prune weights on
    weight_threshold (float): vertex weights below this value will be removed.

Returns:
    bool: true if influences were removed, false otherwise

<a id="unreal.SkinWeightModifier.prune_all_weights"></a>

#### prune_all_weights

```python
def prune_all_weights(weight_threshold: float) -> bool
```

x.prune_all_weights(weight_threshold) -> bool
Remove all weights below the given threshold value, on all vertices.

Args:
    weight_threshold (float): vertex weights below this value will be removed.

Returns:
    bool: true if influences were removed, false otherwise

<a id="unreal.SkinWeightModifier.normalize_vertex_weights"></a>

#### normalize_vertex_weights

```python
def normalize_vertex_weights(vertex_id: int) -> bool
```

x.normalize_vertex_weights(vertex_id) -> bool
Normalize weights on the specified vertex.

Args:
    vertex_id (int32): the index of the vertex to normalize weights on

Returns:
    bool: true if normalization was performed, false otherwise

<a id="unreal.SkinWeightModifier.normalize_all_weights"></a>

#### normalize_all_weights

```python
def normalize_all_weights() -> bool
```

x.normalize_all_weights() -> bool
Normalize weights on all vertices in the mesh.

Returns:
    bool: true if normalization was performed, false otherwise

<a id="unreal.SkinWeightModifier.get_vertex_weights"></a>

#### get_vertex_weights

```python
def get_vertex_weights(vertex_id: int) -> Map[Name, float]
```

x.get_vertex_weights(vertex_id) -> Map[Name, float]
Get all bone weights for a single vertex.

Args:
    vertex_id (int32): the index of the vertex

Returns:
    Map[Name, float]: a map of Bone Name to weight values for all bones that influence the specified vertex.

<a id="unreal.SkinWeightModifier.get_skeletal_mesh"></a>

#### get_skeletal_mesh

```python
def get_skeletal_mesh() -> SkeletalMesh
```

x.get_skeletal_mesh() -> SkeletalMesh
Get a reference to the skeletal mesh that was loaded

Returns:
    SkeletalMesh: USkeletalMesh* - the mesh that was loaded, or null

<a id="unreal.SkinWeightModifier.get_num_vertices"></a>

#### get_num_vertices

```python
def get_num_vertices() -> int
```

x.get_num_vertices() -> int32
Get the total number of vertices in the skeletal mesh.

Returns:
    int32: int, number of vertices

<a id="unreal.SkinWeightModifier.get_all_bone_names"></a>

#### get_all_bone_names

```python
def get_all_bone_names() -> Array[Name]
```

x.get_all_bone_names() -> Array[Name]
Get an array of all bone names in the skeletal mesh.

Returns:
    Array[Name]: array of bone names

<a id="unreal.SkinWeightModifier.enforce_max_influences"></a>

#### enforce_max_influences

```python
def enforce_max_influences(max_influences: int = -1) -> bool
```

x.enforce_max_influences(max_influences=-1) -> bool
Strips out smallest influences to ensure each vertex does not have weight on more influences than MaxInfluences.
Influences with the smallest weight are culled first.

Args:
    max_influences (int32): The maximum number of influences to allow for each vertex in the mesh. If -1 is passed, will use the project-wide MaxInfluences amount.

Returns:
    bool: true if influences were removed, false otherwise

<a id="unreal.SkinWeightModifier.commit_weights_to_skeletal_mesh"></a>

#### commit_weights_to_skeletal_mesh

```python
def commit_weights_to_skeletal_mesh() -> bool
```

x.commit_weights_to_skeletal_mesh() -> bool
Actually applies the weight modifications to the skeletal mesh. This action creates an undo transaction.
The skeletal mesh asset will be dirtied, but it is up to the user to save the asset if required.

Returns:
    bool: true if weights were applied to a skeletal mesh, false otherwise

<a id="unreal.PropertyAnimatorCoreBase"></a>