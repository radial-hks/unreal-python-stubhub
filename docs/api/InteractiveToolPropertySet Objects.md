## InteractiveToolPropertySet Objects

```python
class InteractiveToolPropertySet(Object)
```

A UInteractiveTool contains a set of UObjects that contain "properties" of the Tool, ie
the configuration flags, parameters, etc that control the Tool. Currently any UObject
can be added as a property set, however there is no automatic mechanism for those child
UObjects to notify the Tool when a property changes.

If you make your property set UObjects subclasses of UInteractiveToolPropertySet, then
when the Tool Properties are changed *in the Editor*, the parent Tool will be automatically notified.
You can override UInteractiveTool::OnPropertyModified() to act on these notifications

**C++ Source:**

- **Module**: InteractiveToolsFramework
- **File**: InteractiveTool.h

<a id="unreal.BakeMultiTexture2DProperties"></a>