## MockDataMeshTrackerComponent_OnMockDataMeshTrackerUpdated Objects

```python
class MockDataMeshTrackerComponent_OnMockDataMeshTrackerUpdated(
        MulticastDelegateBase)
```

Delegate used by OnMeshUpdated().

Args:
    index (int32): The index of the mesh section in the ProceduralMeshComponent that was updated.
    vertices (Array[Vector]): List of all vertices in the updated mesh section.
    triangles (Array[int32]): List of all triangles in the updated mesh section.
    normals (Array[Vector]): List of the normals of all triangles in the updated mesh section.
    confidence (Array[float]): List of the confidence values per vertex in the updated mesh section. This can be used to determine if the user needs to scan more.

**C++ Source:**

- **Module**: MRMesh
- **File**: MockDataMeshTrackerComponent.h

<a id="unreal.MockDataMeshTrackerComponent_OnMockDataMeshTrackerUpdated.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnPropertyValueChanged"></a>