## PoseSearchMode Objects

```python
class PoseSearchMode(EnumBase)
```

namespace UE::PoseSearch

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchDatabase.h

<a id="unreal.PoseSearchMode.BRUTE_FORCE"></a>

#### BRUTE_FORCE

0: Database searches will be evaluated extensively. the system will evaluate all the indexed poses to search for the best one.

<a id="unreal.PoseSearchMode.PCAKD_TREE"></a>

#### PCAKD_TREE

1: Optimized search mode: the database projects the poses into a PCA space using only the most significant "NumberOfPrincipalComponents" dimensions, and construct a kdtree to facilitate the search.

<a id="unreal.PoseSearchMode.VP_TREE"></a>

#### VP_TREE

2: Optimized search mode using a vantage point tree
Experimental, this feature might be removed without warning, not for production use

<a id="unreal.InputQueryPose"></a>