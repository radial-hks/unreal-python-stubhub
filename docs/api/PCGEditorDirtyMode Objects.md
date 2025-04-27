## PCGEditorDirtyMode Objects

```python
class PCGEditorDirtyMode(EnumBase)
```

EPCGEditor Dirty Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCommon.h

<a id="unreal.PCGEditorDirtyMode.NORMAL"></a>

#### NORMAL

0: Normal editing mode where generation changes (generation, cleanup) dirty the component and its resources.

<a id="unreal.PCGEditorDirtyMode.PREVIEW"></a>

#### PREVIEW

1: Editing mode where generation changes (generation, cleanup, resources) on the component will not trigger any dirty state, but will also not save any of the generated resources. Also represents the state after loading from the Load as Preview edit mode, where this will hold the last saved generation until a new generation is triggered.

<a id="unreal.PCGEditorDirtyMode.LOAD_AS_PREVIEW"></a>

#### LOAD_AS_PREVIEW

2: Acts as the normal editing mode until the next load of the component, at which state it acts as-if-transient, namely that any further generation changes will not dirty the component.

<a id="unreal.PCGChangeType"></a>