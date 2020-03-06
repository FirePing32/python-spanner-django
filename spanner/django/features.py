# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db.backends.base.features import BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    can_introspect_big_integer_field = False
    can_introspect_duration_field = False
    # https://cloud.google.com/spanner/quotas#query_limits
    max_query_params = 950
    supports_foreign_keys = False
    supports_ignore_conflicts = False
    supports_partial_indexes = False
    supports_regex_backreferencing = False
    supports_timezones = False
    supports_transactions = False
    supports_column_check_constraints = False
    supports_table_check_constraints = False
    uses_savepoints = False

    # Django tests that aren't supported by Spanner.
    skip_tests = (
        # No foreign key constraints in Spanner.
        'fixtures_regress.tests.TestFixtures.test_loaddata_raises_error_when_fixture_has_invalid_foreign_key',
        # No Django transaction management in Spanner.
        'basic.tests.SelectOnSaveTests.test_select_on_save_lying_update',
        # spanner.django monkey patches AutoField to have a default value.
        'basic.tests.ModelTest.test_hash',
        'm2m_through_regress.tests.ToFieldThroughTests.test_m2m_relations_unusable_on_null_pk_obj',
        'many_to_many.tests.ManyToManyTests.test_add',
        'many_to_one.tests.ManyToOneTests.test_fk_assignment_and_related_object_cache',
        'many_to_one.tests.ManyToOneTests.test_relation_unsaved',
        'model_fields.test_durationfield.TestSerialization.test_dumping',
        'model_fields.test_uuid.TestSerialization.test_dumping',
        'model_fields.test_booleanfield.ValidationTest.test_nullbooleanfield_blank',
        'one_to_one.tests.OneToOneTests.test_get_reverse_on_unsaved_object',
        'one_to_one.tests.OneToOneTests.test_set_reverse_on_unsaved_object',
        'one_to_one.tests.OneToOneTests.test_unsaved_object',
        'queries.test_bulk_update.BulkUpdateNoteTests.test_unsaved_models',
        'timezones.tests.LegacyDatabaseTests.test_cursor_execute_accepts_naive_datetime',
        'timezones.tests.NewDatabaseTests.test_cursor_execute_accepts_naive_datetime',
        # Tests that assume a serial pk.
        'admin_filters.tests.ListFiltersTests.test_booleanfieldlistfilter_nullbooleanfield',
        'admin_filters.tests.ListFiltersTests.test_booleanfieldlistfilter_tuple',
        'admin_filters.tests.ListFiltersTests.test_booleanfieldlistfilter',
        'admin_filters.tests.ListFiltersTests.test_datefieldlistfilter_with_time_zone_support',
        'admin_filters.tests.ListFiltersTests.test_datefieldlistfilter',
        'admin_filters.tests.ListFiltersTests.test_fieldlistfilter_underscorelookup_tuple',
        'admin_filters.tests.ListFiltersTests.test_fk_with_to_field',
        'admin_filters.tests.ListFiltersTests.test_listfilter_genericrelation',
        'admin_filters.tests.ListFiltersTests.test_lookup_with_non_string_value_underscored',
        'admin_filters.tests.ListFiltersTests.test_lookup_with_non_string_value',
        'admin_filters.tests.ListFiltersTests.test_relatedfieldlistfilter_manytomany',
        'admin_filters.tests.ListFiltersTests.test_simplelistfilter',
        'admin_inlines.tests.TestInline.test_inline_hidden_field_no_column',
        'admin_views.tests.AdminViewPermissionsTest.test_history_view',
        'aggregation.test_filter_argument.FilteredAggregateTests.test_plain_annotate',
        'aggregation.tests.AggregateTestCase.test_annotate_basic',
        'aggregation.tests.AggregateTestCase.test_annotation',
        'aggregation.tests.AggregateTestCase.test_filtering',
        'aggregation_regress.tests.AggregationTests.test_more_more',
        'aggregation_regress.tests.AggregationTests.test_more_more_more',
        'aggregation_regress.tests.AggregationTests.test_ticket_11293',
        'defer_regress.tests.DeferRegressionTest.test_ticket_23270',
        'distinct_on_fields.tests.DistinctOnTests.test_basic_distinct_on',
        'generic_relations_regress.tests.GenericRelationTests.test_annotate',
        'get_earliest_or_latest.tests.TestFirstLast',
        'known_related_objects.tests.ExistingRelatedInstancesTests.test_reverse_one_to_one_multi_prefetch_related',
        'known_related_objects.tests.ExistingRelatedInstancesTests.test_reverse_one_to_one_multi_select_related',
        'lookup.tests.LookupTests.test_get_next_previous_by',
        'lookup.tests.LookupTests.test_values_list',
        'migrations.test_operations.OperationTests.test_alter_order_with_respect_to',
        'model_fields.tests.GetChoicesOrderingTests.test_get_choices_reverse_related_field',
        'model_formsets_regress.tests.FormfieldShouldDeleteFormTests.test_custom_delete',
        'multiple_database.tests.RouterTestCase.test_generic_key_cross_database_protection',
        'ordering.tests.OrderingTests.test_default_ordering_by_f_expression',
        'ordering.tests.OrderingTests.test_order_by_fk_attname',
        'ordering.tests.OrderingTests.test_order_by_override',
        'ordering.tests.OrderingTests.test_order_by_pk',
        'queries.test_bulk_update.BulkUpdateNoteTests.test_multiple_fields',
        'queries.test_bulk_update.BulkUpdateTests.test_inherited_fields',
        'queries.tests.Queries1Tests.test_ticket9411',
        'queries.tests.Queries4Tests.test_ticket15316_exclude_true',
        'queries.tests.Queries5Tests.test_ticket7256',
        'queries.tests.SubqueryTests.test_related_sliced_subquery',
        'queries.tests.Ticket14056Tests.test_ticket_14056',
        'queries.tests.RelatedLookupTypeTests.test_values_queryset_lookup',
        'raw_query.tests.RawQueryTests.test_annotations',
        'raw_query.tests.RawQueryTests.test_get_item',
        'select_related.tests.SelectRelatedTests.test_field_traversal',
        'syndication_tests.tests.SyndicationFeedTest.test_rss2_feed',
        'syndication_tests.tests.SyndicationFeedTest.test_latest_post_date',
        'syndication_tests.tests.SyndicationFeedTest.test_rss091_feed',
        'syndication_tests.tests.SyndicationFeedTest.test_template_feed',
        # can't use QuerySet.dates() on DateTimeField:
        # https://github.com/orijtech/spanner-orm/issues/182
        'dates.tests.DatesTests.test_dates_trunc_datetime_fields',
        # datetimes retrieved from the database with the wrong hour when
        # USE_TZ = True: https://github.com/orijtech/spanner-orm/issues/193
        'datetimes.tests.DateTimesTests.test_21432',
        'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_trunc_timezone_applied_before_truncation',  # noqa
        # Unable to infer type for parameter:
        # https://github.com/orijtech/spanner-orm/issues/185
        'timezones.tests.LegacyDatabaseTests.test_cursor_execute_returns_naive_datetime',
        'timezones.tests.NewDatabaseTests.test_cursor_execute_returns_naive_datetime',
        # extract() with timezone not working as expected:
        # https://github.com/orijtech/spanner-orm/issues/191
        'timezones.tests.NewDatabaseTests.test_query_datetimes',
        # To be investigated: https://github.com/orijtech/spanner-orm/issues/135
        'admin_changelist.tests.ChangeListTests.test_multiuser_edit',
        # Implement DatabaseOperations.datetime_cast_date_sql():
        # https://github.com/orijtech/spanner-orm/issues/170
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_date_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_date_none',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_time_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_time_none',
        'model_fields.test_datetimefield.DateTimeFieldTests.test_lookup_date_with_use_tz',
        'model_fields.test_datetimefield.DateTimeFieldTests.test_lookup_date_without_use_tz',
        # Implement DatabaseOperations.time_trunc_sql():
        # https://github.com/orijtech/spanner-orm/issues/262
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_hour_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_minute_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_none',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_trunc_second_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_trunc_func_with_timezone',
        # Spanner's EXTRACT() 'week' differs from Django:
        # https://github.com/orijtech/spanner-orm/issues/263
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_week_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_week_func_boundaries',
        'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_func_with_timezone',
        'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_week_func',
        'db_functions.datetime.test_extract_trunc.DateFunctionWithTimeZoneTests.test_extract_week_func_boundaries',
        # using NULL with + crashes: https://github.com/orijtech/spanner-orm/issues/201
        'annotations.tests.NonAggregateAnnotationTestCase.test_combined_annotation_commutative',
        # Spanner loses DecimalField precision due to conversion to float:
        # https://github.com/orijtech/spanner-orm/pull/133#pullrequestreview-328482925
        'aggregation.tests.AggregateTestCase.test_decimal_max_digits_has_no_effect',
        'aggregation.tests.AggregateTestCase.test_related_aggregate',
        'db_functions.comparison.test_cast.CastTests.test_cast_to_decimal_field',
        'model_fields.test_decimalfield.DecimalFieldTests.test_fetch_from_db_without_float_rounding',
        'model_fields.test_decimalfield.DecimalFieldTests.test_roundtrip_with_trailing_zeros',
        # No UNIQUE constraints in Spanner.
        'model_fields.test_filefield.FileFieldTests.test_unique_when_same_filename',
        'one_to_one.tests.OneToOneTests.test_multiple_o2o',
        # No CHECK constraints in Spanner.
        'model_fields.test_integerfield.PositiveIntegerFieldTests.test_negative_values',
        # No matching signature for function REGEXP_CONTAINS for argument
        # types: INT64, INT64: https://github.com/orijtech/spanner-orm/issues/177
        'lookup.tests.LookupTests.test_lookup_int_as_str',
        # 'DatabaseWrapper' object has no attribute 'pattern_ops'
        # https://github.com/orijtech/spanner-orm/issues/178
        'expressions.tests.BasicExpressionsTests.test_ticket_16731_startswith_lookup',
        'expressions.tests.ExpressionsTests.test_insensitive_patterns_escape',
        'expressions.tests.ExpressionsTests.test_patterns_escape',
        'lookup.tests.LookupTests.test_pattern_lookups_with_substr',
        # Spanner doesn't supoprt the variance the standard deviation database
        # functions:
        'aggregation.test_filter_argument.FilteredAggregateTests.test_filtered_numerical_aggregates',
        'aggregation_regress.tests.AggregationTests.test_stddev',
        # SELECT list expression references <column> which is neither grouped
        # nor aggregated: https://github.com/orijtech/spanner-orm/issues/245
        'aggregation_regress.tests.AggregationTests.test_annotated_conditional_aggregate',
        'aggregation_regress.tests.AggregationTests.test_annotation_with_value',
        # Cloud Spanner's docs: "The rows that are returned by LIMIT and OFFSET
        # is unspecified unless these operators are used after ORDER BY."
        'aggregation_regress.tests.AggregationTests.test_sliced_conditional_aggregate',
        'queries.tests.QuerySetBitwiseOperationTests.test_or_with_both_slice',
        'queries.tests.QuerySetBitwiseOperationTests.test_or_with_both_slice_and_ordering',
        'queries.tests.QuerySetBitwiseOperationTests.test_or_with_lhs_slice',
        'queries.tests.QuerySetBitwiseOperationTests.test_or_with_rhs_slice',
        'queries.tests.SubqueryTests.test_slice_subquery_and_query',
        # Cloud Spanner limit: "Number of functions exceeds the maximum
        # allowed limit of 1000."
        'queries.test_bulk_update.BulkUpdateTests.test_large_batch',
        # QuerySet.extra() with select literal percent doesn't work:
        # https://github.com/orijtech/spanner-orm/issues/252
        'queries.tests.Queries5Tests.test_extra_select_literal_percent_s',
        # Spanner doesn't support random ordering.
        'ordering.tests.OrderingTests.test_random_ordering',
        # No matching signature for function MOD for argument types: FLOAT64,
        # FLOAT64. Supported signatures: MOD(INT64, INT64)
        'db_functions.math.test_mod.ModTests.test_decimal',
        'db_functions.math.test_mod.ModTests.test_float',
        # The Chr and Ord database functions are not implemented:
        # https://github.com/orijtech/spanner-orm/issues/243
        'db_functions.text.test_chr.ChrTests.test_basic',
        'db_functions.text.test_chr.ChrTests.test_non_ascii',
        'db_functions.text.test_chr.ChrTests.test_transform',
        'db_functions.text.test_ord.OrdTests.test_basic',
        'db_functions.text.test_ord.OrdTests.test_transform',
        # Spanner's CAST function returns null if any of its arguments are
        # null: https://github.com/orijtech/spanner-orm/issues/242
        'db_functions.text.test_concat.ConcatTests.test_basic',
        'db_functions.text.test_concat.ConcatTests.test_many',
        # implement SchemaEditor.quote_value():
        # https://github.com/orijtech/spanner-orm/issues/227
        'indexes.tests.PartialIndexConditionIgnoredTests.test_condition_ignored',
        # Cast from Python date or datetime crashes:
        # https://github.com/orijtech/spanner-orm/issues/257
        'db_functions.comparison.test_cast.CastTests.test_cast_from_python_to_date',
        'db_functions.comparison.test_cast.CastTests.test_cast_from_python_to_datetime',
        # Greatest/Least Coalesce workaround crashes:
        # https://github.com/orijtech/spanner-orm/issues/259
        'db_functions.comparison.test_greatest.GreatestTests.test_coalesce_workaround',
        'db_functions.comparison.test_least.LeastTests.test_coalesce_workaround',
        # Cast to CharField with max_length doesn't work:
        # https://github.com/orijtech/spanner-orm/issues/258
        'db_functions.comparison.test_cast.CastTests.test_cast_to_char_field_with_max_length',
        # casting DateField to DateTimeField adds an unexpected hour:
        # https://github.com/orijtech/spanner-orm/issues/260
        'db_functions.comparison.test_cast.CastTests.test_cast_from_db_date_to_datetime',
        # Did not expect to issue a SQL statement:
        # https://github.com/orijtech/spanner-orm/issues/266
        'validation.test_unique.PerformUniqueChecksTest.test_primary_key_unique_check_not_performed_when_adding_and_pk_not_specified',  # noqa
        'validation.test_unique.PerformUniqueChecksTest.test_primary_key_unique_check_not_performed_when_not_adding',
        # Database queries are issued to 'default' but shouldn't be:
        # https://github.com/orijtech/spanner-orm/issues/267
        'validation.test_custom_messages.CustomMessagesTests.test_custom_null_message',
        'validation.test_custom_messages.CustomMessagesTests.test_custom_simple_validator_message',
        'validation.test_validators.TestModelsWithValidators.test_custom_validator_passes_for_correct_value',
        'validation.test_validators.TestModelsWithValidators.test_custom_validator_raises_error_for_incorrect_value',
        'validation.test_validators.TestModelsWithValidators.test_field_validators_can_be_any_iterable',
        # Invalid table names aren't supported:
        # https://github.com/orijtech/spanner-orm/issues/268
        'backends',
        # Cloud Spanner supports Unicode as the native encoding yet Django
        # doesn't expect the backend to support it, so skip this test.
        'auth_tests.test_basic.BasicTestCase.test_unicode_username',
        # Obscure error with auth_tests:
        # https://github.com/orijtech/spanner-orm/issues/271
        'auth_tests.test_admin_multidb.MultiDatabaseTests.test_add_view',
        # We can't run GIS tests on a non-GIS database.
        'gis_tests',
        # Tests that by-pass using spanner.django and generate
        # invalid DDL: https://github.com/orijtech/django-spanner/issues/298
        'cache.tests.CreateCacheTableForDBCacheTests',
        'cache.tests.DBCacheTests',
        'cache.tests.DBCacheWithTimeZoneTests',
        # A rollback failed and should be investigated:
        # https://github.com/orijtech/django-spanner/issues/299
        'test_utils.tests.TestBadSetUpTestData.test_failure_in_setUpTestData_should_rollback_transaction',
        # The default object being compared against apparently shouldn't have an assigned id.
        # https://github.com/orijtech/django-spanner/issues/300
        'str.tests.SimpleTests.test_defaults',
    )
