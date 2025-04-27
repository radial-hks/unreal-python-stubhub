## MovieGraphCollectionModifier Objects

```python
class MovieGraphCollectionModifier(Object)
```

Base class for providing actor modification functionality via collections.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

<a id="unreal.MovieGraphCollectionModifier.set_collections"></a>

#### set_collections

```python
def set_collections(collections: Array[MovieGraphCollection]) -> None
```

x.set_collections(collections) -> None
Overwrites the existing collections with the provided array of collections.

Args:
    collections (Array[MovieGraphCollection]):

<a id="unreal.MovieGraphCollectionModifier.get_collections"></a>

#### get_collections

```python
def get_collections() -> Array[MovieGraphCollection]
```

x.get_collections() -> Array[MovieGraphCollection]
Get Collections

Returns:
    Array[MovieGraphCollection]:

<a id="unreal.MovieGraphCollectionModifier.add_collection"></a>

#### add_collection

```python
def add_collection(collection: MovieGraphCollection) -> None
```

x.add_collection(collection) -> None
Adds a collection to the existing set of collections in this modifier.

Args:
    collection (MovieGraphCollection):

<a id="unreal.MoviePipelineCollectionModifier"></a>