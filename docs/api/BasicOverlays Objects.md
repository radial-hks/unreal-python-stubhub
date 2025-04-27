## BasicOverlays Objects

```python
class BasicOverlays(Overlays)
```

Implements an asset that contains a set of overlay data (which includes timing, text, and position) to be displayed for any
given source (including, but not limited to, audio, dialog, and movies)

**C++ Source:**

- **Module**: Overlay
- **File**: BasicOverlays.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] The import data used to make this overlays asset
- ``overlays`` (Array[OverlayItem]):  [Read-Write] The overlay data held by this asset. Contains info on timing, position, and the subtitle to display

<a id="unreal.LocalizedOverlays"></a>