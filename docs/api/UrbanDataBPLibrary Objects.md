## UrbanDataBPLibrary Objects

```python
class UrbanDataBPLibrary(BlueprintFunctionLibrary)
```

Urban Data BPLibrary

**C++ Source:**

- **Plugin**: AesBuilderCommon
- **Module**: UrbanDataboard
- **File**: UrbanDataBPLibrary.h

<a id="unreal.UrbanDataBPLibrary.get_used_foliage_types"></a>

#### get\_used\_foliage\_types

```python
@classmethod
def get_used_foliage_types(cls,
                           actor: InstancedFoliageActor) -> Array[FoliageType]
```

X.get_used_foliage_types(actor) -> Array[FoliageType]
Returns all the different types of UFoliageType assets that a particular AInstancedFoliageActor uses.
This function exists because we want to retrieve all instances of all foliage types on an actor, but we
can't return nested containers from UFUNCTIONs, so users of this API should call this, and then GetInstanceTransforms.

Args:
    actor (InstancedFoliageActor): 

Returns:
    Array[FoliageType]:

<a id="unreal.UrbanDataBPLibrary.get_source"></a>

#### get\_source

```python
@classmethod
def get_source(cls, foliage_type: FoliageType) -> Object
```

X.get_source(foliage_type) -> Object
Returns the source asset for a UFoliageType.
It can be a UStaticMesh in case we're dealing with a UFoliageType_InstancedStaticMesh, but it can be other types of objects.

Args:
    foliage_type (FoliageType): 

Returns:
    Object:

<a id="unreal.UrbanDataBPLibrary.get_instance_transforms"></a>

#### get\_instance\_transforms

```python
@classmethod
def get_instance_transforms(cls,
                            actor: InstancedFoliageActor,
                            foliage_type: FoliageType,
                            instances_level: Level = None) -> Array[Transform]
```

X.get_instance_transforms(actor, foliage_type, instances_level=None) -> Array[Transform]
Returns the transforms of all instances of a particular UFoliageType on a given level. If no level is provided all instances will be returned.
Use GetUsedFoliageTypes() to retrieve all foliage types managed by a particular actor.

Args:
    actor (InstancedFoliageActor): 
    foliage_type (FoliageType): 
    instances_level (Level): 

Returns:
    Array[Transform]:

<a id="unreal.UrbanDataBPLibrary.generated_project_eid"></a>

#### generated\_project\_eid

```python
@classmethod
def generated_project_eid(cls) -> str
```

X.generated_project_eid() -> str
Generated Project EID

Returns:
    str:

<a id="unreal.UrbanDataBPLibrary.fixup_referencers"></a>

#### fixup\_referencers

```python
@classmethod
def fixup_referencers(cls, asset_datas: Array[AssetData]) -> None
```

X.fixup_referencers(asset_datas) -> None
Fixup Referencers

Args:
    asset_datas (Array[AssetData]):

<a id="unreal.UrbanBuildTemplateMeshComponent"></a>