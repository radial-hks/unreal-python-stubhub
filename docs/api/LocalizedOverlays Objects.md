## LocalizedOverlays Objects

```python
class LocalizedOverlays(Overlays)
```

Implements an asset that contains a set of Basic Overlays that will be displayed in accordance with
the current locale, or a default set if an appropriate locale is not found

**C++ Source:**

- **Module**: Overlay
- **File**: LocalizedOverlays.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] The import data used to make this overlays asset
- ``default_overlays`` (BasicOverlays):  [Read-Write] The overlays to use if no overlays are found for the current culture
- ``locale_to_overlays_map`` (Map[str, BasicOverlays]):  [Read-Write] Maps a set of cultures to specific BasicOverlays assets.
  Cultures are comprised of three hyphen-separated parts:
               A two-letter ISO 639-1 language code (e.g., "zh")
               An optional four-letter ISO 15924 script code (e.g., "Hans")
               An optional two-letter ISO 3166-1 country code  (e.g., "CN")

<a id="unreal.BasicOverlaysFactory"></a>