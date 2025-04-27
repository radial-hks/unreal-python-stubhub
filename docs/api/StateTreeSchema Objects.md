## StateTreeSchema Objects

```python
class StateTreeSchema(Object)
```

Schema describing which inputs, evaluators, and tasks a StateTree can contain.
Each StateTree asset saves the schema class name in asset data tags, which can be
used to limit which StatTree assets can be selected per use case, i.e.:

    UPROPERTY(EditDefaultsOnly, Category = AI, meta=(RequiredAssetDataTags="Schema=StateTreeSchema_SupaDupa"))
    UStateTree* StateTree;

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeSchema.h

<a id="unreal.AvaTransitionTreeSchema"></a>