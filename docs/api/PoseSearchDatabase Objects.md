## PoseSearchDatabase Objects

```python
class PoseSearchDatabase(DataAsset)
```

A data asset for indexing a collection of animation sequences.

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchDatabase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_extrapolation_time`` (FloatInterval):  [Read-Write] extrapolation of animation assets will be clamped by AnimationAssetTimeStart + AdditionalExtrapolationTime.Min, AnimationAssetTimeEnd + AdditionalExtrapolationTime.Max
- ``base_cost_bias`` (float):  [Read-Write] Base Cost added or removed to all poses from this database. It can be overridden by Anim Notify: Pose Search Modify Cost at the frame level of animation data.
  Negative values make it more likely to be picked, or stayed in, Positive values make it less likely to be picked or stay in.
- ``continuing_pose_cost_bias`` (float):  [Read-Write] Cost added to the continuing pose from this database. This allows users to apply a cost bias (positive or negative) to the continuing pose.
  This is useful to help the system stay in one animation segment longer, or shorter depending on how you set this bias.
  Negative values make it more likely to be picked, or stayed in, positive values make it less likely to be picked or stay in.
  Note: excluded from DDC hash, since used only at runtime in SearchContinuingPose
- ``exclude_from_database_parameters`` (FloatInterval):  [Read-Write] These settings allow users to trim the start and end of animations in the database to preserve start/end frames for blending, and prevent the system from selecting the very last frames before it blends out.
  valid animation frames will be AnimationAssetTimeStart + ExcludeFromDatabaseParameters.Min, AnimationAssetTimeEnd + ExcludeFromDatabaseParameters.Max
- ``kd_tree_max_leaf_size`` (int32):  [Read-Write]
- ``kd_tree_query_num_neighbors`` (int32):  [Read-Write]
  todo:: rename to KNNQueryNumNeighbors to be usable with the VPTree as well Out of a kdtree search, results will have only an approximate cost, so the database search will select the best “KDTree Query Num Neighbors” poses to perform the full cost analysis, and be able to elect the best pose. Memory & Performance Optimization! If KDTreeQueryNumNeighbors is 1 all the SearchIndexPrivate::Values will be stripped away, and the search will exclusively rely on the KDTree query result from the PCA space encoded values (SearchIndexPrivate::PCAValues).
- ``kd_tree_query_num_neighbors_with_duplicates`` (int32):  [Read-Write]
  todo:: rename to KNNQueryNumNeighborsWithDuplicates to be usable with the VPTree as well if PCAValuesPruningSimilarityThreshold > 0 the kdtree will remove duplicates, every result out of the KDTreeQueryNumNeighbors could potentially references multiple poses. KDTreeQueryNumNeighborsWithDuplicates is the upper bound number of poses the system will perform the full cost evaluation. if KDTreeQueryNumNeighborsWithDuplicates is zero then there's no upper bound
- ``looping_cost_bias`` (float):  [Read-Write] Cost added to all looping animation assets in this database. This allows users to make it more or less likely to pick the looping animation segments.
  Negative values make it more likely to be picked, or stayed in, Positive values make it less likely to be picked or stay in.
- ``normalization_set`` (PoseSearchNormalizationSet):  [Read-Write] This optional asset defines a list of databases you want to normalize together. Without it, it would be difficult to compare costs from separately normalized databases containing different types of animation,
  like only idles versus only runs animations, given that the range of movement would be dramatically different.
- ``number_of_principal_components`` (int32):  [Read-Write] Number of dimensions used to create the kdtree. More dimensions allows a better explanation of the variance of the dataset that usually translates in better search results, but will imply more memory usage and worse performances.
- ``pca_values_pruning_similarity_threshold`` (float):  [Read-Write] if two PCA values (multi dimensional point with the GetNumberOfPrincipalComponents cardinality) are closer than PCAValuesPruningSimilarityThreshold,
  only one will be saved into the database FSearchIndex (to save memory).
- ``pose_pruning_similarity_threshold`` (float):  [Read-Write] if two poses values (multi dimensional point with the schema cardinality) are closer than PosePruningSimilarityThreshold,
  only one will be saved into the database FSearchIndexBase (to save memory) and accessed by the two different pose indexes
- ``pose_search_mode`` (PoseSearchMode):  [Read-Write] This dictates how the database will perform the search.
- ``preview_mesh`` (SkeletalMesh):  [Read-Write] If null, the default preview mesh for the skeleton will be used. Otherwise, this will be used in preview scenes.
  todo:: Move this to be a setting in the Pose Search Database editor.
- ``schema`` (PoseSearchSchema):  [Read-Write] The Schema sets what channels this database will use to match against (bones, trajectory and what properties of those you’re interested in, such as position and velocity).
- ``tags`` (Array[Name]):  [Read-Write] Array of tags that can be used as metadata.

<a id="unreal.PoseSearchDatabase.schema"></a>

#### schema

```python
@property
def schema() -> PoseSearchSchema
```

(PoseSearchSchema):  [Read-Only] The Schema sets what channels this database will use to match against (bones, trajectory and what properties of those you’re interested in, such as position and velocity).

<a id="unreal.PoseSearchDatabase.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Only] Array of tags that can be used as metadata.

<a id="unreal.PoseSearchDatabase.normalization_set"></a>

#### normalization_set

```python
@property
def normalization_set() -> PoseSearchNormalizationSet
```

(PoseSearchNormalizationSet):  [Read-Only] This optional asset defines a list of databases you want to normalize together. Without it, it would be difficult to compare costs from separately normalized databases containing different types of animation,
like only idles versus only runs animations, given that the range of movement would be dramatically different.

<a id="unreal.PoseSearchDatabase.get_num_animation_assets"></a>

#### get_num_animation_assets

```python
def get_num_animation_assets() -> int
```

x.get_num_animation_assets() -> int32
Get Num Animation Assets

Returns:
    int32:

<a id="unreal.PoseSearchDatabase.get_animation_asset"></a>

#### get_animation_asset

```python
def get_animation_asset(index: int) -> Object
```

x.get_animation_asset(index) -> Object
Get Animation Asset

Args:
    index (int32): 

Returns:
    Object:

<a id="unreal.PoseSearchFeatureChannel"></a>