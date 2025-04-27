## AnimBoneCompressionSettings Objects

```python
class AnimBoneCompressionSettings(Object)
```

* This object is used to wrap a bone compression codec. It allows a clean integration in the editor by avoiding the need
* to create asset types and factory wrappers for every codec.

**C++ Source:**

- **Module**: Engine
- **File**: AnimBoneCompressionSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``codecs`` (Array[AnimBoneCompressionCodec]):  [Read-Write] A list of animation bone compression codecs to try. Empty entries are ignored but the array cannot be empty.
- ``error_threshold`` (float):  [Read-Write] When compressing, the best codec below this error threshold will be used.
- ``force_below_threshold`` (bool):  [Read-Write] Any codec (even one that increases the size) with a lower error will be used until it falls below the threshold.

<a id="unreal.AssetMappingTable"></a>