## NiagaraPreviewAxis Objects

```python
class NiagaraPreviewAxis(Object)
```

Base class for all preview axis types.
NiagaraPreviewGrid uses these to control how many systems to spawn in each axis and how each system varies on that axis.
C++ Examples are show below. You can also create these as Blueprint classes as show in the Plugin content folder.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraPreviewGrid.h

<a id="unreal.NiagaraPreviewAxis.num"></a>

#### num

```python
def num() -> int
```

x.num() -> int32
Returns the number of previews for this axis.

Returns:
    int32:

<a id="unreal.NiagaraPreviewAxis.apply_to_preview"></a>

#### apply_to_preview

```python
def apply_to_preview(preview_component: NiagaraComponent, preview_index: int,
                     is_x_axis: bool) -> str
```

x.apply_to_preview(preview_component, preview_index, is_x_axis) -> str
Applies this axis for the preview at PreviewIndex on this axis.

Args:
    preview_component (NiagaraComponent): 
    preview_index (int32): 
    is_x_axis (bool): 

Returns:
    str: 

    out_label_text (str):

<a id="unreal.NiagaraPreviewAxis_InterpParamBase"></a>