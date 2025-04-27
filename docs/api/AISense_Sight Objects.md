## AISense_Sight Objects

```python
class AISense_Sight(AISense)
```

AISense Sight

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Sight.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_register_all_pawns_as_sources`` (bool):  [Read-Write] If true all newly spawned pawns will get auto registered as source for this sense.
- ``high_importance_query_distance_threshold`` (float):  [Read-Write]
- ``max_async_traces_per_tick`` (int32):  [Read-Write] Maximum number of asynchronous traces that can be requested in a single update call
- ``max_query_importance`` (float):  [Read-Write]
- ``max_time_slice_per_tick`` (double):  [Read-Write]
- ``max_traces_per_tick`` (int32):  [Read-Write]
- ``min_queries_per_time_slice_check`` (int32):  [Read-Write]
- ``notify_type`` (AISenseNotifyType):  [Read-Write]
- ``pending_queries_budget_reduction_ratio`` (float):  [Read-Write] Defines the amount of async trace queries to prevent based on the number of pending queries at the start of an update.
  1 means that the async trace budget is slashed by the pending queries count
  0 means that the async trace budget is not impacted by the pending queries
- ``sight_limit_query_importance`` (float):  [Read-Write]
- ``use_asynchronous_trace_for_default_sight_queries`` (bool):  [Read-Write] Defines if we are allowed to use asynchronous trace queries when there is no IAISightTargetInterface for a Target
- ``wants_new_pawn_notification`` (bool):  [Read-Write] whether this sense is interested in getting notified about new Pawns being spawned
      this can be used for example for automated sense sources registration

<a id="unreal.AISense_Team"></a>