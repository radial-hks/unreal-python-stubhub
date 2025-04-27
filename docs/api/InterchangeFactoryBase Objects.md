## InterchangeFactoryBase Objects

```python
class InterchangeFactoryBase(Object)
```

Asset factory implementation:

The first three steps use the Interchange factory node to import or reimport the UObject:

1. BeginImportAsset_GameThread - Create the asset UObject. You can also import source data (retrieve payloads) and set up properties on the game thread.
2. ImportAsset_Async - Import source data (retrieve payloads) and set up properties asynchronously on any thread.
3. EndImportAsset_GameThread - Anything you need to do on the game thread to finalize the import source data and set up properties. For example, conflict resolution that needs UI.

The last three steps can modify the created UObject

4. SetupObject_GameThread - Do any UObject setup required before the build, the UObject dependencies should exist and have all the source data and properties imported.
5. BuildObject_GameThread - Build the asset if it can be built.
6. FinalizeObject_GameThread - Do any final UObject setup after the build. Note that the build of an asset can be asynchronous and this function will be call after the async build is done.

Scene factory implementation:

1. ImportSceneObject_GameThread - Create an actor in a level.

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeFactoryBase.h

<a id="unreal.InterchangeFactoryBase.get_factory_class"></a>

#### get_factory_class

```python
def get_factory_class() -> Class
```

x.get_factory_class() -> type(Class)
Return the UClass this factory can create.

Returns:
    type(Class):

<a id="unreal.InterchangeSourceData"></a>