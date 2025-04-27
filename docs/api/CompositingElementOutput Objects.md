## CompositingElementOutput Objects

```python
class CompositingElementOutput(CompositingElementPass)
```

Compositing Element Output

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementPasses.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingElementOutput.relay_output"></a>

#### relay_output

```python
def relay_output(final_result: Texture,
                 post_process_proxy: ComposurePostProcessingPassProxy) -> None
```

x.relay_output(final_result, post_process_proxy) -> None
Relay Output

Args:
    final_result (Texture): 
    post_process_proxy (ComposurePostProcessingPassProxy):

<a id="unreal.ColorConverterOutputPass"></a>