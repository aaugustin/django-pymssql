from unittest import expectedFailure

try:
    from django.utils.module_loading import import_string   # Django >= 1.7
except ImportError:
    from django.utils.module_loading import import_by_path as import_string


def mark_as_expected_failure(*test_names):
    for test_name in test_names:
        test_case_name, _, method_name = test_name.rpartition('.')
        test_case = import_string(test_case_name)
        method = getattr(test_case, method_name)
        method = expectedFailure(method)
        setattr(test_case, method_name, method)


failing_tests = [

    # Some tests are known to fail with django-mssql.
    'aggregation.tests.BaseAggregateTestCase.test_dates_with_aggregation',
    'aggregation_regress.tests.AggregationTests.test_more_more_more',
    'inspectdb.tests.InspectDBTestCase.test_number_field_types',

    # pymssql doesn't handle binary data correctly.
    'backends.tests.LastExecutedQueryTest.test_query_encoding',
    'model_fields.tests.BinaryFieldTests.test_set_and_retrieve',

    # pymssql doesn't check parameter counts.
    'backends.tests.ParameterHandlingTest.test_bad_parameter_count',

    # MSSQL throws an arithmetic overflow error.
    'expressions_regress.tests.ExpressionOperatorTests.test_righthand_power',

    # TODO -- figure out why this test fails.
    'timezones.tests.NewDatabaseTests.test_raw_sql',

    # The migrations and schema tests also fail massively at this time.
]


mark_as_expected_failure(*failing_tests)
